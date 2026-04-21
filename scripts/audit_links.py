import os
import re

def audit_file(filepath, root_dir):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    links = re.findall(r'href="(.*?)"', content)
    broken_links = []
    
    for link in links:
        if link == "#" or link.startswith("http") or link.startswith("mailto"):
            continue
        
        # Correctly join relative link with current file directory
        file_dir = os.path.dirname(filepath)
        target_path = os.path.abspath(os.path.join(file_dir, link))
        
        if not os.path.exists(target_path):
            broken_links.append(link)

    return broken_links

root = "/Users/samisa/Idasara/git/ai_and_digital_capacity_building"
results = {}

for dirpath, dirs, filenames in os.walk(root):
    if ".git" in dirpath: continue
    for f in filenames:
        if f.endswith(".html"):
            fpath = os.path.join(dirpath, f)
            broken = audit_file(fpath, root)
            if broken:
                results[os.path.relpath(fpath, root)] = broken

if not results:
    print("No broken links found!")
else:
    for path, broken in results.items():
        print(f"File: {path}")
        print(f"  - Broken links: {broken}")
