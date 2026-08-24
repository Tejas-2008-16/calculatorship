import re

with open('sitemap.xml', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace all <lastmod>...</lastmod> with <lastmod>2026-08-24</lastmod>
updated_content = re.sub(r'<lastmod>[^<]+</lastmod>', '<lastmod>2026-08-24</lastmod>', content)

# Also ensure homepage has root URL https://calculatorship.in/ with daily frequency and priority 1.0 if not already present
homepage_root_block = '''  <url>
    <loc>https://calculatorship.in/</loc>
    <lastmod>2026-08-24</lastmod>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://calculatorship.in/index.html</loc>
    <lastmod>2026-08-24</lastmod>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
  </url>'''

# Replace index.html block at top with both root and index.html
index_pattern = re.compile(r'  <url>\s*<loc>https://calculatorship\.in/index\.html</loc>\s*<lastmod>[^<]+</lastmod>\s*<changefreq>[^<]+</changefreq>\s*<priority>[^<]+</priority>\s*</url>')
if index_pattern.search(updated_content):
    updated_content = index_pattern.sub(homepage_root_block, updated_content)

with open('sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(updated_content)

print('sitemap.xml updated with 2026-08-24 for all URLs!')
