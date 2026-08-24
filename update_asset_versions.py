import glob
import re

html_files = glob.glob("*.html")
count = 0
for f in html_files:
    with open(f, "r", encoding="utf-8") as fh:
        content = fh.read()
    
    new_content = re.sub(r'href=["\']style\.css(?:\?[^"\']*)?["\']', 'href="style.css?v=2.2"', content)
    new_content = re.sub(r'src=["\']theme\.js(?:\?[^"\']*)?["\']', 'src="theme.js?v=2.2"', new_content)
    
    if new_content != content:
        with open(f, "w", encoding="utf-8") as fh:
            fh.write(new_content)
        count += 1

print(f"Updated {count} HTML files with versioned asset URLs (v=2.2)")
