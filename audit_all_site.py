import glob
import re
import os

files = glob.glob('*.html')
print(f"Auditing {len(files)} active HTML files...")

emoji_pattern = re.compile(r'[\U00010000-\U0010ffff]|[\u2600-\u26ff]|[\u2700-\u27bf]|[\u2300-\u23ff]|[\u2b50-\u2b55]')

files_with_emojis = []
files_missing_adsense = []
files_missing_ga4 = []
files_missing_gsc = []
article_word_counts = {}

def count_words_in_article(html_content):
    m = re.search(r'<article class="article-main".*?>(.*?)</article>', html_content, flags=re.DOTALL)
    if not m:
        m = re.search(r'<main.*?>(.*?)</main>', html_content, flags=re.DOTALL)
    if not m:
        text = html_content
    else:
        text = m.group(1)
    text = re.sub(r'<script.*?>.*?</script>', ' ', text, flags=re.DOTALL)
    text = re.sub(r'<style.*?>.*?</style>', ' ', text, flags=re.DOTALL)
    text = re.sub(r'<[^>]+>', ' ', text)
    words = re.findall(r'\b[A-Za-z0-9\'-]+\b', text)
    return len(words)

non_articles = {
    'index.html', 'lumpsum.html', 'step-up.html', 'goal.html', 'ppf-calculator.html',
    'swp-calculator.html', 'emi-calculator.html', 'fd-calculator.html', 'budget-planner.html',
    'income-tax-calculator.html', 'about.html', 'contact.html', 'disclaimer.html',
    'terms.html', 'privacy.html', 'cookies.html', 'blog.html', '404.html'
}

for f in sorted(files):
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        content = fp.read()

    # Check emojis
    matches = emoji_pattern.findall(content)
    if matches:
        files_with_emojis.append(f)

    # Check AdSense
    if 'ca-pub-7598871729388798' not in content:
        files_missing_adsense.append(f)

    # Check GA4
    if 'G-0C93Q0VBQP' not in content:
        files_missing_ga4.append(f)

    # Check Search Console
    if 'wI-yq01MPBD-S1JZtupXa2CAdSvWceD5Kv0FvPJFDM8' not in content:
        files_missing_gsc.append(f)

    if f not in non_articles:
        wc = count_words_in_article(content)
        article_word_counts[f] = wc

print(f"\n================ AUDIT SUMMARY ================")
print(f"Total HTML files active: {len(files)}")
print(f"Files with emojis: {len(files_with_emojis)} {files_with_emojis}")
print(f"Files missing AdSense: {len(files_missing_adsense)} {files_missing_adsense}")
print(f"Files missing GA4: {len(files_missing_ga4)} {files_missing_ga4}")
print(f"Files missing Search Console verification: {len(files_missing_gsc)} {files_missing_gsc}")

print(f"\n================ ALL {len(article_word_counts)} ARTICLES WORD COUNTS (Target: 1,200 - 1,500+ words) ================")
under_1200 = []
for art, wc in sorted(article_word_counts.items()):
    status = "OK" if wc >= 1200 else "UNDER 1200"
    if wc < 1200:
        under_1200.append((art, wc))
    print(f"{art:45} : {wc:4} words [{status}]")

print(f"\nArticles below 1200 words: {len(under_1200)}")
if len(under_1200) == 0 and len(files_missing_adsense) == 0 and len(files_missing_ga4) == 0 and len(files_missing_gsc) == 0 and len(files_with_emojis) == 0:
    print("\nALL 28 ARTICLES AND ALL 46 WEBPAGES PASSED WITH 100% SUCCESS!")
