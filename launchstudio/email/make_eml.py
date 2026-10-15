#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dung file .eml tu email HTML, de mo truc tiep trong Apple Mail.
Dung:  python3 make_eml.py launchstudio_email_nl.html
"""
import sys, io, re, os
from email.message import EmailMessage
from email.utils import formatdate, make_msgid

src = sys.argv[1] if len(sys.argv) > 1 else "launchstudio_email_nl.html"
html = io.open(src, encoding="utf-8").read()

m = re.search(r"<title>(.*?)</title>", html, re.S)
subject = re.sub(r"\s+", " ", m.group(1)).strip() if m else "LaunchStudio"

# fallback text/plain — bat buoc co, neu khong nhieu filter danh diem spam
text = re.sub(r"<(script|style|head)[^>]*>.*?</\1>", "", html, flags=re.S)
text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
text = re.sub(r"<[^>]+>", "\n", text)
import html as H
text = H.unescape(text)
text = "\n".join(l.strip() for l in text.split("\n") if l.strip())

msg = EmailMessage()
msg["Subject"] = subject
msg["From"] = "LaunchStudio <hallo@launchstudio.eu>"
msg["To"] = "test@example.com"
msg["Date"] = formatdate(localtime=True)
msg["Message-ID"] = make_msgid(domain="launchstudio.eu")
# header huy dang ky — Gmail/Yahoo yeu cau tu 2024
msg["List-Unsubscribe"] = "<https://launchstudio.eu/afmelden>, <mailto:afmelden@launchstudio.eu>"
msg["List-Unsubscribe-Post"] = "List-Unsubscribe=One-Click"
# Outlook mo .eml co header nay nhu DRAFT (co nut Send). Apple Mail KHONG nhan —
# voi Apple Mail dung open_draft.sh. Header nay vo hai o moi noi khac.
msg["X-Unsent"] = "1"

msg.set_content(text, subtype="plain", charset="utf-8")
msg.add_alternative(html, subtype="html", charset="utf-8")

out = os.path.splitext(src)[0] + ".eml"
io.open(out, "w", encoding="utf-8").write(msg.as_string())
print(f"{out}  ({round(os.path.getsize(out)/1024,1)} KB)")
print(f"Subject: {subject}")
