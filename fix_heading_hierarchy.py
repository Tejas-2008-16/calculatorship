import os
import glob
import re

html_files = glob.glob("*.html")
print(f"Normalizing heading hierarchy across {len(html_files)} files...")

for f in html_files:
    with open(f, "r", encoding="utf-8") as fp:
        c = fp.read()
    
    modified = False
    
    # 1. In info pages (about.html, contact.html, disclaimer.html, cookies.html, 404.html)
    # Change footer <h4> to <h3> if main content uses <h1> and <h2>
    # In all files, change footer column <h4>Calculators</h4> to <h3>Calculators</h3> for proper descending order
    c_new = re.sub(r'<div class="footer-col">\s*<h4>([^<]+)</h4>', r'<div class="footer-col">\n            <h3>\1</h3>', c)
    if c_new != c:
        c = c_new
        modified = True
        
    # Also change closing tag if any
    c_new = re.sub(r'<h3>([^<]+)</h4>', r'<h3>\1</h3>', c)
    if c_new != c:
        c = c_new
        modified = True

    # 2. In toc-box: change <h4>Table of Contents</h4> to <h2> or <h3>Table of Contents</h3>
    c_new = re.sub(r'<h4([^>]*)Table of Contents</h4>', r'<h2\1Table of Contents</h2>', c)
    if c_new != c:
        c = c_new
        modified = True

    # 3. In scenario-box: if following an <h2>, change <h4> to <h3>
    c_new = re.sub(r'<div class="scenario-box">\s*<h4>([^<]+)</h4>', r'<div class="scenario-box">\n            <h3>\1</h3>', c)
    if c_new != c:
        c = c_new
        modified = True

    # 4. In checklist-box: change <h4> to <h3>
    c_new = re.sub(r'<div class="checklist-box[^"]*">\s*<h4>([^<]+)</h4>', lambda m: m.group(0).replace('<h4>', '<h3>').replace('</h4>', '</h3>'), c)
    if c_new != c:
        c = c_new
        modified = True

    # 5. In blog.html: change hero <h1> then section headers...
    if modified:
        with open(f, "w", encoding="utf-8") as fp:
            fp.write(c)

print("Heading hierarchy normalization complete.")
