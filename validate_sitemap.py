import re

sitemap = open('sitemap.xml','r',encoding='utf-8').read()
urls = re.findall(r'<loc>(.*?)</loc>', sitemap)
print('Total URLs in sitemap:', len(urls))

new_articles = [
    'income-tax-slabs-india-2026',
    'mutual-fund-categories-india',
    'debt-free-strategy-india',
    'home-loan-prepayment-vs-sip-strategy',
    'swp-for-retirement-income-guide',
    'ppf-rules-benefits-wealth-guide',
    'gold-vs-mutual-funds',
    'index-funds-vs-active-funds',
    'portfolio-rebalancing-guide-india',
    'inflation-impact-on-savings-india',
    'wedding-budget-planning',
    'child-education-planning',
    'sip-mistakes-to-avoid',
]
print()
missing = []
for art in new_articles:
    url = 'https://calculatorship.in/' + art + '.html'
    found = url in urls
    status = 'OK' if found else 'MISSING'
    print('  [' + status + '] ' + art + '.html')
    if not found:
        missing.append(url)

if missing:
    print('\nMISSING URLs:')
    for u in missing:
        print(' ', u)
else:
    print('\nAll checked URLs are in sitemap!')
