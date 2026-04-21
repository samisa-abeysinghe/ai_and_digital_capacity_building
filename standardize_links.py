import os
import re

def process_file(filepath, root_dir):
    rel_path = os.path.relpath(filepath, root_dir)
    parts = rel_path.split(os.sep)
    depth = len(parts) - 1
    
    lang = "en"
    if "content/si" in rel_path or "governance/si" in rel_path or "index_si.html" in rel_path:
        lang = "si"
    elif "content/ta" in rel_path or "governance/ta" in rel_path or "index_ta.html" in rel_path:
        lang = "ta"

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return

    # 1. Update Lang Selector
    si_path = rel_path.replace("content/en", "content/si").replace("content/ta", "content/si").replace("governance/ta", "governance/si").replace("index.html", "index_si.html").replace("index_ta.html", "index_si.html")
    ta_path = rel_path.replace("content/en", "content/ta").replace("content/si", "content/ta").replace("governance/si", "governance/ta").replace("index.html", "index_ta.html").replace("index_si.html", "index_ta.html")
    en_path = rel_path.replace("content/si", "content/en").replace("content/ta", "content/en").replace("governance/si", "governance").replace("governance/ta", "governance").replace("index_si.html", "index.html").replace("index_ta.html", "index.html")

    def to_rel(target_rel_from_root, current_depth):
        return ("../" * current_depth) + target_rel_from_root

    en_link = to_rel(en_path, depth)
    si_link = to_rel(si_path, depth)
    ta_link = to_rel(ta_path, depth)

    if depth == 0:
        en_link = "index.html"
        si_link = "index_si.html"
        ta_link = "index_ta.html"

    active_en = ' class="active"' if lang == "en" else ""
    active_si = ' class="active"' if lang == "si" else ""
    active_ta = ' class="active"' if lang == "ta" else ""

    new_selector = f'''<div class="lang-selector">
                <a href="{en_link}"{active_en}>English</a>
                <a href="{si_link}"{active_si}>සිංහල</a>
                <a href="{ta_link}"{active_ta}>தமிழ்</a>
            </div>'''
    
    content = re.sub(r'<div class="lang-selector">.*?</div>', new_selector, content, flags=re.DOTALL)

    # 2. Update Breadcrumbs
    if depth >= 2:
        idx_depth = depth - 2
        digitruck_idx = ("../" * idx_depth) + "index.html"
        content = re.sub(r'<p class="breadcrumb">DigiTruck (.*?)<\/p>', 
                        f'<p class="breadcrumb"><a href="{digitruck_idx}">DigiTruck</a> \\1</p>', 
                        content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

root = "/Users/samisa/Idasara/git/ai_and_digital_capacity_building"
for dirpath, dirs, filenames in os.walk(root):
    if ".git" in dirpath: continue
    for f in filenames:
        if f.endswith(".html"):
            process_file(os.path.join(dirpath, f), root)
