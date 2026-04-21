import os
import re

root_dir = "/Users/samisa/Idasara/git/ai_and_digital_capacity_building"

def get_rel_path_to_root(depth):
    if depth <= 0:
        return ""
    return "../" * depth

def fix_lang_selector(content, parts, current_lang):
    lang_selector_match = re.search(r'<div class="lang-selector">.*?</div>', content, re.DOTALL)
    if not lang_selector_match:
        return content
    
    old_selector = lang_selector_match.group(0)
    
    en_link = "#"
    si_link = "#"
    ta_link = "#"
    
    depth = len(parts) - 1
    
    if parts[0] == 'content' and len(parts) >= 4:
        # content/[lang]/digitruck/...
        subpath = os.path.join(*parts[3:])
        steps_to_content = depth - 1
        
        if current_lang == 'en': en_link = "../" * depth + "index.html"
        else: en_link = "../" * steps_to_content + "en/digitruck/" + subpath
        
        if current_lang == 'si': si_link = "../" * depth + "index_si.html"
        else: si_link = "../" * steps_to_content + "si/digitruck/" + subpath
        
        if current_lang == 'ta': ta_link = "../" * depth + "index_ta.html"
        else: ta_link = "../" * steps_to_content + "ta/digitruck/" + subpath
        
    elif parts[0] == 'governance':
        if len(parts) == 2: # governance/standards.html (en)
            if current_lang == 'en': en_link = "../index.html"
            else: en_link = "standards.html"
            si_link = "si/standards.html"
            ta_link = "ta/standards.html"
        else: # governance/[si|ta]/standards.html
            en_link = "../standards.html"
            if current_lang == 'si': si_link = "../../index_si.html"
            else: si_link = "../si/standards.html"
            if current_lang == 'ta': ta_link = "../../index_ta.html"
            else: ta_link = "../ta/standards.html"
            
    elif len(parts) == 1: # root files
        if current_lang == 'en': en_link = "index.html"
        else: en_link = "index.html"
        if current_lang == 'si': si_link = "index_si.html"
        else: si_link = "index_si.html"
        if current_lang == 'ta': ta_link = "index_ta.html"
        else: ta_link = "index_ta.html"

    active_en = ' class="active"' if current_lang == 'en' else ''
    active_si = ' class="active"' if current_lang == 'si' else ''
    active_ta = ' class="active"' if current_lang == 'ta' else ''

    new_selector = f'''<div class="lang-selector">
                <a href="{en_link}"{active_en}>English</a>
                <a href="{si_link}"{active_si}>සිංහල</a>
                <a href="{ta_link}"{active_ta}>தமிழ்</a>
            </div>'''
    
    return content.replace(old_selector, new_selector)

def fix_breadcrumbs(content, parts):
    if 'digitruck' in parts and parts[0] == 'content':
        idx = parts.index('digitruck')
        steps_up = len(parts) - 1 - idx
        if steps_up > 0:
            dt_index_link = "../" * steps_up + "index.html"
            
            # Match <p class="breadcrumb">...</p>
            # But avoid matching if it's already linked
            def breadcrumb_repl(match):
                text = match.group(1)
                if 'DigiTruck' in text and '<a' not in text:
                    # Replace first occurrence of DigiTruck with linked version
                    new_text = text.replace('DigiTruck', f'<a href="{dt_index_link}">DigiTruck</a>', 1)
                    return f'<p class="breadcrumb">{new_text}</p>'
                return match.group(0)

            content = re.sub(r'<p class="breadcrumb">(.*?)</p>', breadcrumb_repl, content)
    return content

def process_file(file_path):
    rel_path = os.path.relpath(file_path, root_dir)
    parts = rel_path.split(os.sep)
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Determine language
    current_lang = 'en'
    if parts[0] == 'content' and len(parts) > 1:
        current_lang = parts[1]
    elif parts[0] == 'governance' and len(parts) > 2:
        current_lang = parts[1]
    elif rel_path == 'index_si.html':
        current_lang = 'si'
    elif rel_path == 'index_ta.html':
        current_lang = 'ta'
        
    content = fix_lang_selector(content, parts, current_lang)
    content = fix_breadcrumbs(content, parts)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    html_files = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".html"):
                html_files.append(os.path.join(root, file))
                
    for file_path in html_files:
        process_file(file_path)
    print(f"Processed {len(html_files)} files.")

if __name__ == "__main__":
    main()
