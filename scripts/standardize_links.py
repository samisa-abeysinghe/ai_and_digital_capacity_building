import os
import re

def process_file(filepath, root_dir):
    rel_file_path = os.path.relpath(filepath, root_dir)
    parts = rel_file_path.split(os.sep)
    depth = len(parts) - 1
    
    # 1. Detect language
    lang = "en"
    if "content/si" in rel_file_path or "governance/si" in rel_file_path or "index_si.html" in rel_file_path:
        lang = "si"
    elif "content/ta" in rel_file_path or "governance/ta" in rel_file_path or "index_ta.html" in rel_file_path:
        lang = "ta"

    root_indices = {"en": "index.html", "si": "index_si.html", "ta": "index_ta.html"}

    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # --- FIX HEADER LOGO & PORTAL LINK ---
    portal_link = ("../" * depth) + root_indices[lang]
    if depth == 0: portal_link = root_indices[lang]
    content = re.sub(r'<div class="logo">.*?<a href="[^"]*"', 
                    f'<div class="logo">\n                <img src="{"../"*depth}assets/img/ai-dl-sb-logo.jpg" alt="Logo" class="site-logo">\n                <a href="{portal_link}"', 
                    content, flags=re.DOTALL)

    # --- FIX LANG SELECTOR ---
    def get_lang_link(target_lang):
        if depth == 0: return root_indices[target_lang]
        new_rel_path = rel_file_path
        if lang == "en":
            if target_lang == "si": new_rel_path = new_rel_path.replace("content/en", "content/si").replace("governance/", "governance/si/")
            elif target_lang == "ta": new_rel_path = new_rel_path.replace("content/en", "content/ta").replace("governance/", "governance/ta/")
        elif lang == "si":
            if target_lang == "en": new_rel_path = new_rel_path.replace("content/si", "content/en").replace("governance/si/", "governance/")
            elif target_lang == "ta": new_rel_path = new_rel_path.replace("content/si", "content/ta").replace("governance/si/", "governance/ta/")
        elif lang == "ta":
            if target_lang == "en": new_rel_path = new_rel_path.replace("content/ta", "content/en").replace("governance/ta/", "governance/")
            elif target_lang == "si": new_rel_path = new_rel_path.replace("content/ta", "content/si").replace("governance/ta/", "governance/si/")
        return ("../" * depth) + new_rel_path

    en_link = get_lang_link("en")
    si_link = get_lang_link("si")
    ta_link = get_lang_link("ta")
    
    active_en = ' class="active"' if lang == "en" else ""
    active_si = ' class="active"' if lang == "si" else ""
    active_ta = ' class="active"' if lang == "ta" else ""

    new_selector = f'''<div class="lang-selector">
                <a href="{en_link}"{active_en}>English</a>
                <a href="{si_link}"{active_si}>සිංහල</a>
                <a href="{ta_link}"{active_ta}>தமிழ்</a>
            </div>'''
    content = re.sub(r'<div class="lang-selector">.*?</div>', new_selector, content, flags=re.DOTALL)

    # --- FIX BREADCRUMBS ---
    # content/en/digitruck/index.html is depth 3
    # content/en/digitruck/personas/women.html is depth 4
    # content/en/digitruck/schedules/daily/officials.html is depth 5
    if depth >= 3:
        # Link to content/[lang]/digitruck/index.html
        breadcrumb_idx = ("../" * (depth - 3)) + "index.html"
        content = re.sub(r'<p class="breadcrumb">.*?DigiTruck.*? >', 
                        f'<p class="breadcrumb"><a href="{breadcrumb_idx}">DigiTruck</a> >', 
                        content)

    # --- FIX ASSET PATHS ---
    root_prefix = "../" * depth if depth > 0 else ""
    content = re.sub(r'href="[^"]*assets/css/site\.css"', f'href="{root_prefix}assets/css/site.css"', content)
    content = re.sub(r'href="[^"]*assets/css/modules\.css"', f'href="{root_prefix}assets/css/modules.css"', content)
    content = re.sub(r'src="[^"]*assets/img/ai-dl-sb-logo\.jpg"', f'src="{root_prefix}assets/img/ai-dl-sb-logo.jpg"', content)
    content = re.sub(r'href="[^"]*assets/img/favicon\.ico"', f'href="{root_prefix}assets/img/favicon.ico"', content)
    content = re.sub(r'href="[^"]*license\.html"', f'href="{root_prefix}license.html"', content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

root = "/Users/samisa/Idasara/git/ai_and_digital_capacity_building"
for dirpath, dirs, filenames in os.walk(root):
    if ".git" in dirpath: continue
    for f in filenames:
        if f.endswith(".html"):
            process_file(os.path.join(dirpath, f), root)
