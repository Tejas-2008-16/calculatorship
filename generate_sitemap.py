import os
import glob
from datetime import datetime

DOMAIN = "https://calculatorship.in"
TODAY = "2026-08-23"

# Categorization and priorities for XML sitemap
CALCULATOR_SLUGS = {
    "index.html", "lumpsum.html", "step-up.html", "goal.html",
    "ppf-calculator.html", "swp-calculator.html", "emi-calculator.html",
    "fd-calculator.html", "budget-planner.html", "income-tax-calculator.html"
}

CORE_PAGES = {
    "blog.html": (0.8, "weekly"),
    "about.html": (0.5, "monthly"),
    "contact.html": (0.5, "monthly"),
    "disclaimer.html": (0.3, "monthly"),
    "terms.html": (0.3, "monthly"),
    "privacy.html": (0.3, "monthly"),
    "cookies.html": (0.3, "monthly"),
}

# Collect all HTML files
all_html = set(glob.glob("*.html"))
all_html.discard("404.html")

calculators = sorted([f for f in all_html if f in CALCULATOR_SLUGS])
# Make index.html first in calculators list
if "index.html" in calculators:
    calculators.remove("index.html")
    calculators = ["index.html"] + calculators

static_core = sorted([f for f in all_html if f in CORE_PAGES and f != "blog.html"])
blog_page = ["blog.html"] if "blog.html" in all_html else []

articles = sorted([f for f in all_html if f not in CALCULATOR_SLUGS and f not in CORE_PAGES])

print(f"Total Calculators: {len(calculators)}")
print(f"Total Articles/Guides: {len(articles)}")
print(f"Total Static/Core Pages: {len(static_core) + len(blog_page)}")
total_count = len(calculators) + len(articles) + len(static_core) + len(blog_page)
print(f"Total URLs in new sitemap.xml: {total_count}")

xml_lines = [
    '<?xml version="1.0" encoding="UTF-8"?>',
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
]

# 1. Calculators (Priority: 0.9, changefreq: weekly)
for calc in calculators:
    p = "1.0" if calc == "index.html" else "0.9"
    xml_lines.append(f'  <url>')
    xml_lines.append(f'    <loc>{DOMAIN}/{calc}</loc>')
    xml_lines.append(f'    <lastmod>{TODAY}</lastmod>')
    xml_lines.append(f'    <changefreq>weekly</changefreq>')
    xml_lines.append(f'    <priority>{p}</priority>')
    xml_lines.append(f'  </url>')

# 2. Blog Hub
for b in blog_page:
    xml_lines.append(f'  <url>')
    xml_lines.append(f'    <loc>{DOMAIN}/{b}</loc>')
    xml_lines.append(f'    <lastmod>{TODAY}</lastmod>')
    xml_lines.append(f'    <changefreq>weekly</changefreq>')
    xml_lines.append(f'    <priority>0.8</priority>')
    xml_lines.append(f'  </url>')

# 3. All Educational Articles / Guides (Priority: 0.8, changefreq: monthly)
for art in articles:
    xml_lines.append(f'  <url>')
    xml_lines.append(f'    <loc>{DOMAIN}/{art}</loc>')
    xml_lines.append(f'    <lastmod>{TODAY}</lastmod>')
    xml_lines.append(f'    <changefreq>monthly</changefreq>')
    xml_lines.append(f'    <priority>0.8</priority>')
    xml_lines.append(f'  </url>')

# 4. Core & Legal Pages (Priority: 0.3 - 0.5, changefreq: monthly)
for core in static_core:
    p, freq = CORE_PAGES.get(core, (0.5, "monthly"))
    xml_lines.append(f'  <url>')
    xml_lines.append(f'    <loc>{DOMAIN}/{core}</loc>')
    xml_lines.append(f'    <lastmod>{TODAY}</lastmod>')
    xml_lines.append(f'    <changefreq>{freq}</changefreq>')
    xml_lines.append(f'    <priority>{p}</priority>')
    xml_lines.append(f'  </url>')

xml_lines.append('</urlset>')

sitemap_content = '\n'.join(xml_lines) + '\n'

with open('sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(sitemap_content)

print("Successfully generated sitemap.xml!")
