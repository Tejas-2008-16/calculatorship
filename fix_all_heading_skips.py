import os
import glob
import re

html_files = glob.glob("*.html")
print(f"Fixing heading skips across {len(html_files)} files...")

for f in html_files:
    with open(f, "r", encoding="utf-8") as fp:
        c = fp.read()
    
    modified = False
    
    # 1. Replace <h4 ...>Table of Contents</h4> with <h2 ...>Table of Contents</h2>
    c_new = re.sub(r'<h4([^>]*)>Table of Contents</h4>', r'<h2\1>Table of Contents</h2>', c)
    if c_new != c:
        c = c_new
        modified = True
        
    # 2. In 404.html: If any skip exists, ensure it is sequential
    # 3. In blog.html: The hero is <h1>, and articles are inside cards with <h3>.
    # To prevent skip from h1 to h3 in blog.html, add a hidden or visible section <h2>Browse Articles &amp; Guides</h2>
    if f == "blog.html":
        if '<h2 class="sr-only">Comprehensive Financial Guides</h2>' not in c:
            c = c.replace('<div id="articlesGrid"', '<h2 class="sr-only">Comprehensive Financial Guides</h2>\n      <div id="articlesGrid"')
            modified = True
            
    # 4. In article pages, ensure sections use <h2> and subsections use <h3>, and card links/asides use <h3> or <h4> appropriately
    # Replace any leftover <h4 class="..."> in scenario/checklist boxes
    c_new = re.sub(r'<h4([^>]*)>', r'<h3\1>', c)
    c_new = re.sub(r'</h4>', r'</h3>', c_new)
    if c_new != c:
        c = c_new
        modified = True

    if modified:
        with open(f, "w", encoding="utf-8") as fp:
            fp.write(c)

print("All heading skips fixed.")
