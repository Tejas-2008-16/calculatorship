import glob
import re

html_files = glob.glob('*.html')
print(f'Checking {len(html_files)} files...')

for f in html_files:
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    
    # 1. Check images without width or height
    imgs = re.findall(r'<img[^>]+>', c)
    for img in imgs:
        if 'width=' not in img or 'height=' not in img:
            print(f'[IMG missing dimensions] {f}: {img}')
            
    # 2. Check unlabelled inputs
    inputs = re.findall(r'<input[^>]+>', c)
    for inp in inputs:
        if 'aria-label' not in inp and 'aria-labelledby' not in inp:
            m = re.search(r'id=["\']([^"\']+)["\']', inp)
            if m:
                i_id = m.group(1)
                if not re.search(r'<label[^>]+for=["\']' + re.escape(i_id) + r'["\']', c):
                    print(f'[INPUT missing label] {f}: {inp}')
            else:
                print(f'[INPUT missing id & label] {f}: {inp}')
