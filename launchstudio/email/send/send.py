#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mail merge cho LaunchStudio — doc CSV, ca nhan hoa, gui tung email.

MAC DINH LA DRY RUN. Phai them --send moi gui that.

  python3 send.py --html ../launchstudio_email_nl.html --csv recipients.csv
  python3 send.py --html ../launchstudio_email_nl.html --csv recipients.csv --send

Token thay the trong HTML:
  {{name}}             ten day du
  {{first_name}}       ten dau
  {{email}}            email nguoi nhan
  {{unsubscribe_url}}  link huy dang ky rieng cho tung nguoi (co HMAC, khong gia mao duoc)
"""
import argparse, csv, hashlib, hmac, io, os, re, sys, time
from email.message import EmailMessage
from email.utils import formatdate, make_msgid
from urllib.parse import quote

SECRET = os.environ.get("UNSUB_SECRET", "")
UNSUB_BASE = os.environ.get("UNSUB_BASE", "https://launchstudio.eu/afmelden")

def unsub_url(email):
    if not SECRET:
        return f"{UNSUB_BASE}?e={quote(email)}"
    tok = hmac.new(SECRET.encode(), email.lower().encode(), hashlib.sha256).hexdigest()[:32]
    return f"{UNSUB_BASE}?e={quote(email)}&t={tok}"

def load_col(path, col="email"):
    if not os.path.exists(path): return set()
    with io.open(path, encoding="utf-8-sig", newline="") as f:
        return {r[col].strip().lower() for r in csv.DictReader(f) if r.get(col, "").strip()}

def render(tpl, row):
    name = row["name"].strip()
    out = tpl
    for k, v in (("{{name}}", name),
                 ("{{first_name}}", name.split()[0] if name else ""),
                 ("{{email}}", row["email"]),
                 ("{{unsubscribe_url}}", unsub_url(row["email"]))):
        out = out.replace(k, v)
    return out

def plain(html):
    t = re.sub(r"<(script|style|head)[^>]*>.*?</\1>", "", html, flags=re.S)
    t = re.sub(r"<!--.*?-->", "", t, flags=re.S)
    t = re.sub(r"<[^>]+>", "\n", t)
    import html as H
    return "\n".join(l.strip() for l in H.unescape(t).split("\n") if l.strip())

def build(row, html, subject, sender):
    body = render(html, row)
    m = EmailMessage()
    m["Subject"] = subject
    m["From"] = sender
    m["To"] = f'{row["name"]} <{row["email"]}>' if row["name"] else row["email"]
    m["Date"] = formatdate(localtime=True)
    m["Message-ID"] = make_msgid(domain=sender.split("@")[-1].rstrip(">"))
    u = unsub_url(row["email"])
    m["List-Unsubscribe"] = f"<{u}>"
    m["List-Unsubscribe-Post"] = "List-Unsubscribe=One-Click"
    m.set_content(plain(body), subtype="plain", charset="utf-8")
    m.add_alternative(body, subtype="html", charset="utf-8")
    return m

def send_smtp(msgs, host, port, user, pwd, delay, log):
    import smtplib
    with smtplib.SMTP(host, port) as s:
        s.starttls(); s.login(user, pwd)
        for i, (row, m) in enumerate(msgs, 1):
            s.send_message(m)
            log.write(row["email"].lower() + "\n"); log.flush()
            print(f"  [{i}/{len(msgs)}] -> {row['email']}")
            if i < len(msgs): time.sleep(delay)

def send_resend(msgs, key, delay, log):
    import json, urllib.request
    for i, (row, m) in enumerate(msgs, 1):
        htm = [p for p in m.walk() if p.get_content_type() == "text/html"][0]
        payload = {"from": m["From"], "to": [row["email"]], "subject": m["Subject"],
                   "html": htm.get_payload(decode=True).decode("utf-8"),
                   "headers": {"List-Unsubscribe": m["List-Unsubscribe"],
                               "List-Unsubscribe-Post": m["List-Unsubscribe-Post"]}}
        req = urllib.request.Request("https://api.resend.com/emails",
              data=json.dumps(payload).encode(),
              headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"})
        urllib.request.urlopen(req, timeout=20).read()
        log.write(row["email"].lower() + "\n"); log.flush()
        print(f"  [{i}/{len(msgs)}] -> {row['email']}")
        if i < len(msgs): time.sleep(delay)

def main():
    a = argparse.ArgumentParser()
    a.add_argument("--html", required=True)
    a.add_argument("--csv", required=True)
    a.add_argument("--subject", default=None, help="mac dinh: lay tu <title>")
    a.add_argument("--from", dest="sender", default="LaunchStudio <hallo@launchstudio.eu>")
    a.add_argument("--provider", choices=["resend", "smtp"], default="resend")
    a.add_argument("--delay", type=float, default=2.0, help="giay giua moi email")
    a.add_argument("--limit", type=int, default=0, help="chi gui N dau tien (0 = het)")
    a.add_argument("--send", action="store_true", help="GUI THAT. Khong co co nay = dry run")
    a.add_argument("--suppress", default="unsubscribed.csv")
    a.add_argument("--log", default="sent.log")
    o = a.parse_args()

    html = io.open(o.html, encoding="utf-8").read()
    subject = o.subject or (re.search(r"<title>(.*?)</title>", html, re.S).group(1).strip())

    # --- kiem tra truoc khi gui ---
    warn = []
    if "{{unsubscribe_url}}" not in html:
        warn.append("HTML khong co {{unsubscribe_url}} -> email KHONG co link huy dang ky "
                    "(Telecommunicatiewet 11.7). Them vao footer truoc khi gui that.")
    if "CAMPAIGN" in html:
        warn.append(f"Con {html.count('CAMPAIGN')} cho 'CAMPAIGN' chua thay trong utm.")
    if "*|" in html:
        warn.append("Con merge tag kieu Mailchimp (*|...|*) — script nay khong resolve chung.")
    if not SECRET:
        warn.append("Chua dat UNSUB_SECRET -> link huy dang ky khong co HMAC, co the bi gia mao.")

    with io.open(o.csv, encoding="utf-8-sig", newline="") as f:
        rows = [r for r in csv.DictReader(f) if r.get("email", "").strip()]
    supp = load_col(o.suppress)
    done = load_col(o.log, "email") if os.path.exists(o.log) else set()
    if os.path.exists(o.log):
        done = {l.strip().lower() for l in io.open(o.log, encoding="utf-8") if l.strip()}

    queue, skipped = [], []
    for r in rows:
        e = r["email"].strip().lower()
        if e in supp: skipped.append((r["email"], "da huy dang ky")); continue
        if e in done: skipped.append((r["email"], "da gui truoc do")); continue
        queue.append(r)
    if o.limit: queue = queue[:o.limit]

    print(f"\nSubject : {subject}")
    print(f"HTML    : {o.html} ({round(len(html)/1024,1)} KB)")
    print(f"Danh sach: {len(rows)} dong | gui: {len(queue)} | bo qua: {len(skipped)}")
    for e, why in skipped: print(f"    - {e} ({why})")
    if warn:
        print("\nCANH BAO:")
        for w in warn: print(f"  !! {w}")

    msgs = [(r, build(r, html, subject, o.sender)) for r in queue]

    if not o.send:
        print("\n--- DRY RUN. Them --send de gui that. ---")
        if msgs:
            r, m = msgs[0]
            print(f"\nVi du email dau tien ({r['email']}):")
            print(f"  To              : {m['To']}")
            print(f"  List-Unsubscribe: {m['List-Unsubscribe']}")
            b = [p for p in m.walk() if p.get_content_type()=='text/html'][0].get_payload(decode=True).decode()
            for tok in ("{{name}}","{{first_name}}","{{email}}","{{unsubscribe_url}}"):
                print(f"  {tok:22s} con sot: {b.count(tok)}")
        return

    if any("KHONG co link huy dang ky" in w for w in warn):
        print("\nDUNG: khong gui khi thieu link huy dang ky. Them {{unsubscribe_url}} vao HTML.")
        sys.exit(1)

    log = io.open(o.log, "a", encoding="utf-8")
    print(f"\nGUI THAT qua {o.provider}, {o.delay}s moi email...")
    if o.provider == "resend":
        key = os.environ.get("RESEND_API_KEY")
        if not key: sys.exit("Thieu RESEND_API_KEY")
        send_resend(msgs, key, o.delay, log)
    else:
        send_smtp(msgs, os.environ["SMTP_HOST"], int(os.environ.get("SMTP_PORT", 587)),
                  os.environ["SMTP_USER"], os.environ["SMTP_PASS"], o.delay, log)
    log.close()
    print(f"\nXong. Da ghi vao {o.log}.")

if __name__ == "__main__":
    main()
