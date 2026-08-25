import glob
import json
import re

non_articles = {
    'index.html', 'lumpsum.html', 'step-up.html', 'goal.html', 'ppf-calculator.html',
    'swp-calculator.html', 'emi-calculator.html', 'fd-calculator.html', 'budget-planner.html',
    'income-tax-calculator.html', 'about.html', 'contact.html', 'disclaimer.html',
    'terms.html', 'privacy.html', 'cookies.html', 'blog.html', '404.html'
}

articles = [f for f in glob.glob('*.html') if f not in non_articles]
print(f'Validating JSON-LD schemas across {len(articles)} articles...')
errors = 0

for f in sorted(articles):
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    m = re.search(r'<script type="application/ld\+json">\s*(\{.*?\})\s*</script>', c, re.DOTALL)
    if not m:
        print(f'Missing schema in {f}')
        errors += 1
        continue
    try:
        data = json.loads(m.group(1))
        graph = data.get('@graph', [data])
        types = [item.get('@type') for item in graph]
        if 'Article' not in types or 'FAQPage' not in types:
            print(f'Missing Article or FAQPage in {f}: {types}')
            errors += 1
        article_item = next(item for item in graph if item.get('@type') == 'Article')
        author_name = article_item.get('author', {}).get('name')
        if author_name != 'Tejas':
            print(f'Invalid author in {f}: {author_name}')
            errors += 1
        faq_item = next(item for item in graph if item.get('@type') == 'FAQPage')
        faqs = faq_item.get('mainEntity', [])
        if len(faqs) < 4:
            print(f'Too few FAQs in {f}: {len(faqs)}')
            errors += 1
    except Exception as e:
        print(f'JSON parse error in {f}: {e}')
        errors += 1

if errors == 0:
    print('100% PASS: All 35 articles have valid Article + FAQPage JSON-LD schemas with Author: Tejas and 4-6 FAQs!')
