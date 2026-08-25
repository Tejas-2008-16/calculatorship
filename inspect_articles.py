import glob
import os
import re

non_articles = {
    'index.html', 'lumpsum.html', 'step-up.html', 'goal.html', 'ppf-calculator.html',
    'swp-calculator.html', 'emi-calculator.html', 'fd-calculator.html', 'budget-planner.html',
    'income-tax-calculator.html', 'about.html', 'contact.html', 'disclaimer.html',
    'terms.html', 'privacy.html', 'cookies.html', 'blog.html', '404.html'
}

html_files = [f for f in glob.glob('*.html') if f not in non_articles]
print(f"Total Article HTML files: {len(html_files)}")
for f in sorted(html_files):
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    has_filler = "Understanding the fundamental mechanics of" in c
    has_bio = "author-bio-card" in c
    faq_count = len(re.findall(r'<details\s+class=["\']faq-item["\']', c))
    pub_m = re.search(r'"datePublished":\s*"([^"]+)"', c)
    pub_date = pub_m.group(1)[:10] if pub_m else "N/A"
    author_m = re.findall(r'"author":\s*\{[^}]*"name":\s*"([^"]+)"', c)
    author_name = author_m[0] if author_m else "N/A"
    print(f"{f:44} | FAQs: {faq_count} | Filler: {str(has_filler):5} | Bio: {str(has_bio):5} | Pub: {pub_date} | Auth: {author_name}")
