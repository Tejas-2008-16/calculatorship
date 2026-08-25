import re
from collections import Counter

html = open('blog.html','r',encoding='utf-8').read()
cards = re.findall(r'class="calc-link-card article-card-item"', html)
print('Total article cards:', len(cards))
dates = re.findall(r'Published: ([^<]+)', html)
print('Date distribution:', Counter(dates))
print()
cats = re.findall(r'data-category="([^"]+)"', html)
cat_counts = Counter(cats)
print('data-category distribution:')
for c, n in cat_counts.most_common():
    print(f'  {c}: {n}')
print()
print('Has calc-main-container:', 'calc-main-container' in html)
print('Has articlesGrid:', 'articlesGrid' in html)
print('Has card-action links:', html.count('card-action'))
