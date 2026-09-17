#!/usr/bin/env python3
"""
Master Social Synchronizer for launchstudio/2026-extra/extra-11-lovable=bolt-replit/
Synchronizes all 60 articles into English and Dutch social posts using:
- Exact full founder names from the case studies
- Exact quantitative metrics and problem figures in the Hook
- Exact package costs, timelines, and measurable outcomes in the Result
- Exact matching base-article slugs for filenames and CTA URLs
- Cleans up any mismatched orphan files
"""

import os
import json
import importlib.util

BASE_DIR = os.path.abspath("launchstudio/2026-extra/extra-11-lovable=bolt-replit")
SYS_DIR = os.path.abspath("launchstudio/sys")

def load_cases():
    with open(os.path.join(SYS_DIR, "parsed_cases.json"), "r", encoding="utf-8") as f:
        return json.load(f)

def load_all_batches():
    all_data = {}
    batches = ['01_15', '16_30', '31_45', '46_60']
    for b in batches:
        path = os.path.join(SYS_DIR, f"generate_batch_{b}.py")
        spec = importlib.util.spec_from_file_location(f"mod_{b}", path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        for item in mod.DATA:
            num = item["num"]
            all_data[num] = item
    return all_data

def format_en(item, slug):
    en = item["en"]
    lines = [
        en["hook"],
        "",
        en["context"],
        "",
        "\n".join(f"❌ {p}" for p in en["problems"]),
        "",
        "\n".join(f"✅ {s}" for s in en["solutions"]),
        "",
        en["launchstudio"],
        "",
        en["result"],
        "",
        f"{en['cta']}: https://launchstudio.eu/en/blog/{slug}",
        "",
        " ".join(f"#{t}" for t in en["tags"]),
        ""
    ]
    return "\n".join(lines)

def format_nl(item, slug):
    nl = item["nl"]
    
    # Avoid duplicate "Waar het misgaat" lines
    if "Waar het" in nl["context"]:
        context_block = [nl["context"]]
    else:
        topic = nl.get("topic", "deze implementatie")
        context_block = [nl["context"], "", f"Waar het vaak misgaat bij {topic}:"]
        
    goal = nl.get("goal", "livegang")
    
    lines = [
        nl["hook"],
        "",
        *context_block,
        "",
        "\n".join(f"❌ {p}" for p in nl["problems"]),
        "",
        f"Wat u wél moet inrichten vóór {goal}:",
        "",
        "\n".join(f"✅ {s}" for s in nl["solutions"]),
        "",
        nl["launchstudio"],
        "",
        nl["result"],
        "",
        f"{nl['cta']}: https://launchstudio.eu/nl/blog/{slug}",
        "",
        " ".join(f"#{t}" for t in nl["tags"]),
        ""
    ]
    return "\n".join(lines)

def main():
    cases = load_cases()
    batch_data = load_all_batches()
    
    print(f"Loaded {len(cases)} case studies from parsed_cases.json")
    print(f"Loaded {len(batch_data)} items from batch scripts")
    
    # 1. Identify all valid base files and slugs
    base_files = {}
    for f in os.listdir(BASE_DIR):
        if f.endswith(".md") and not f.endswith("-social.md") and not f.endswith("-social-dutch.md"):
            num = f.split("-", 1)[0]
            slug = f.split("-", 1)[1][:-3]
            base_files[num] = (f, slug)
            
    assert len(base_files) == 60, f"Expected 60 base files, found {len(base_files)}"
    
    # 2. Write synchronized EN and NL social files matching exact base slugs
    written_en = set()
    written_nl = set()
    
    for num in sorted(base_files.keys(), key=lambda x: int(x)):
        _, slug = base_files[num]
        item = batch_data[num]
        
        # Write EN
        en_content = format_en(item, slug)
        en_filename = f"{num}-{slug}-social.md"
        en_path = os.path.join(BASE_DIR, en_filename)
        with open(en_path, "w", encoding="utf-8") as f:
            f.write(en_content)
        written_en.add(en_filename)
        
        # Write NL
        nl_content = format_nl(item, slug)
        nl_filename = f"{num}-{slug}-social-dutch.md"
        nl_path = os.path.join(BASE_DIR, nl_filename)
        with open(nl_path, "w", encoding="utf-8") as f:
            f.write(nl_content)
        written_nl.add(nl_filename)
        
    print(f"Successfully generated {len(written_en)} EN and {len(written_nl)} NL social posts.")
    
    # 3. Clean up any orphan social files (files that do not match current base slugs)
    orphan_deleted = 0
    for f in os.listdir(BASE_DIR):
        if f.endswith("-social.md") and f not in written_en:
            os.remove(os.path.join(BASE_DIR, f))
            print(f"Deleted orphan EN file: {f}")
            orphan_deleted += 1
        elif f.endswith("-social-dutch.md") and f not in written_nl:
            os.remove(os.path.join(BASE_DIR, f))
            print(f"Deleted orphan NL file: {f}")
            orphan_deleted += 1
            
    print(f"Cleaned up {orphan_deleted} orphan files.")
    
    # 4. Final verification of files in directory
    all_files = os.listdir(BASE_DIR)
    total_base = len([f for f in all_files if f.endswith(".md") and not f.endswith("-social.md") and not f.endswith("-social-dutch.md")])
    total_en = len([f for f in all_files if f.endswith("-social.md")])
    total_nl = len([f for f in all_files if f.endswith("-social-dutch.md")])
    total_md = len([f for f in all_files if f.endswith(".md")])
    
    print("--- Final Directory Stats ---")
    print(f"Base articles: {total_base}/60")
    print(f"EN social posts: {total_en}/60")
    print(f"NL social posts: {total_nl}/60")
    print(f"Total markdown files: {total_md}/180")
    assert total_base == 60 and total_en == 60 and total_nl == 60 and total_md == 180, "Directory count mismatch!"

if __name__ == "__main__":
    main()
