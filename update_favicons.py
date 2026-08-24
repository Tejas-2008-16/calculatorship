import glob
import os
import re

html_files = glob.glob('*.html')
print(f'Checking {len(html_files)} HTML files for favicon links...')

new_favicon_tags = '''  <link rel="icon" type="image/svg+xml" href="/favicon.svg">
  <link rel="icon" type="image/x-icon" href="/favicon.ico">
  <link rel="apple-touch-icon" sizes="180x180" href="/favicon.svg">
  <link rel="shortcut icon" href="/favicon.ico">'''

modified_count = 0
for filepath in sorted(html_files):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    lines = content.splitlines()
    new_lines = []
    inserted = False
    
    for line in lines:
        if ('rel="icon"' in line or 'rel="apple-touch-icon"' in line or 'rel="shortcut icon"' in line or
            "rel='icon'" in line or "rel='apple-touch-icon'" in line or "rel='shortcut icon'" in line):
            if not inserted:
                new_lines.append(new_favicon_tags)
                inserted = True
            continue
        new_lines.append(line)
        
    updated_content = '\n'.join(new_lines) + '\n'
    if updated_content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        modified_count += 1

print(f'Successfully updated favicon links in {modified_count} HTML files.')
