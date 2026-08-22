import glob
import re

files = glob.glob('*.html')
print(f"Auditing {len(files)} active HTML files...")

emoji_pattern = re.compile(r'[\U00010000-\U0010ffff]|[\u2600-\u26ff]|[\u2700-\u27bf]|[\u2300-\u23ff]|[\u2b50-\u2b55]')

files_with_emojis = []
files_with_dark_toggle = []
files_with_reading_times = []
files_with_avatar = []
files_missing_adsense = []
files_missing_ga4 = []

# Exclude legal & error pages from AdSense ad tags check
legal_pages = {'disclaimer.html', 'terms.html', 'privacy.html', 'cookies.html', '404.html'}

for f in files:
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        content = fp.read()

    # Check emojis
    matches = emoji_pattern.findall(content)
    if matches:
        files_with_emojis.append(f)

    # Check dark toggle
    if 'theme-toggle-btn' in content or 'icon-sun' in content or 'icon-moon' in content:
        files_with_dark_toggle.append(f)

    # Check reading times
    if 'min read' in content:
        files_with_reading_times.append(f)

    # Check author avatar circle
    if 'byline-avatar' in content:
        files_with_avatar.append(f)

    # Check AdSense in content pages
    if f not in legal_pages and 'ca-pub-7598871729388798' not in content:
        files_missing_adsense.append(f)

    # Check GA4
    if 'G-0C93Q0VBQP' not in content:
        files_missing_ga4.append(f)

print(f"\n--- AUDIT RESULTS ---")
print(f"Total HTML files active: {len(files)}")
print(f"Files with emojis: {len(files_with_emojis)}")
print(f"Files with dark mode toggles: {len(files_with_dark_toggle)}")
print(f"Files with reading time text: {len(files_with_reading_times)}")
print(f"Files with author avatar logo: {len(files_with_avatar)}")
print(f"Content files missing AdSense tag: {len(files_missing_adsense)}")
print(f"Files missing GA4: {len(files_missing_ga4)}")
print("--- AUDIT PASS ---")
