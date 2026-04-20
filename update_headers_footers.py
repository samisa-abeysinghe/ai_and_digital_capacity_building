import os
import re

ROOT_DIR = "/Users/samisa/Idasara/git/ai_and_digital_capacity_building"
EXCEPTION = "assets/job-aids/core-03-safety-print.html"

FILES_AND_LEVELS = [
    ("content/en/digitruck/index.html", 3),
    ("content/en/digitruck/personas/*.html", 4),
    ("content/en/digitruck/modules/core/*.html", 5),
    ("content/en/digitruck/modules/tot/*.html", 5),
    ("content/en/digitruck/schedules/*.html", 4),
    ("content/en/digitruck/schedules/daily/*.html", 5),
]

def get_relative_path(level):
    return "../" * level

LANG_SELECTOR = """            <div class="lang-selector">
                <a href="#" class="active">English</a>
                <a href="#">සිංහල</a>
                <a href="#">தமிழ்</a>
            </div>"""

TRUST_TAGLINE = '            <p class="trust-tagline">Build Trust. Verify Before Trust. Verify Everything.</p>'

def update_file(file_path, level):
    if EXCEPTION in file_path:
        return

    with open(file_path, 'r') as f:
        content = f.read()

    rel_path = get_relative_path(level)

    # 1. Update Header: Logo Link and Lang Selector
    # Logo Link
    logo_regex = r'(<div class="logo">.*?<a href=").*?(".*?>AI & Digital Capacity Building</a>)'
    new_logo_href = rf'\1{rel_path}index.html\2'
    content = re.sub(logo_regex, new_logo_href, content, flags=re.DOTALL)

    # Lang Selector
    if '<div class="lang-selector">' not in content:
        nav_regex = r'(</div\s*>\s*</nav\s*>)'
        content = re.sub(nav_regex, rf'            <div class="lang-selector">\n                <a href="#" class="active">English</a>\n                <a href="#">සිංහල</a>\n                <a href="#">தமிழ்</a>\n            </div>\n\1', content, count=1)
    else:
        # Standardize existing lang-selector if needed (optional but good)
        pass

    # 2. Update Footer: Trust Tagline and License Link
    # Trust Tagline
    if 'class="trust-tagline"' not in content:
        footer_content_regex = r'(<div class="container footer-content">)'
        content = re.sub(footer_content_regex, rf'\1\n{TRUST_TAGLINE}', content)

    # Copyright & License
    license_regex = r'(<p>&copy; 2000-2026 Samisa Abeysinghe)(.*?)(</p>)'
    new_license_line = rf'\1. Licensed under <a href="{rel_path}LICENSE">CC BY-SA 4.0</a>\3'
    
    # Check if already has license
    if 'Licensed under' not in content:
        content = re.sub(license_regex, new_license_line, content)
    else:
        # Update existing license path
        license_path_regex = r'(<a href=").*?(LICENSE">CC BY-SA 4.0</a>)'
        content = re.sub(license_path_regex, rf'\1{rel_path}\2', content)

    with open(file_path, 'w') as f:
        f.write(content)

import glob

for pattern, level in FILES_AND_LEVELS:
    full_pattern = os.path.join(ROOT_DIR, pattern)
    for file_path in glob.glob(full_pattern):
        print(f"Updating {file_path} at level {level}")
        update_file(file_path, level)
