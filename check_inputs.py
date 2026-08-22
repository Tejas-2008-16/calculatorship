import os
import re

files = [f for f in os.listdir('.') if f.endswith('.html')]
missing_labels = []

for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()
    
    # Check all inputs
    inputs = re.findall(r'<input[^>]+>', content)
    for inp in inputs:
        inp_id = re.search(r'id=[\"\']([^\"\']+)[\"\']', inp)
        inp_type = re.search(r'type=[\"\']([^\"\']+)[\"\']', inp)
        t = inp_type.group(1) if inp_type else 'text'
        
        if t in ['number', 'range', 'text', 'email']:
            # Check if there is a matching label for="id" or aria-label
            has_aria = 'aria-label' in inp or 'aria-labelledby' in inp
            i_id = inp_id.group(1) if inp_id else None
            has_for_label = False
            if i_id:
                has_for_label = bool(re.search(rf'<label[^>]+for=[\"\']{re.escape(i_id)}[\"\']', content))
            
            if not has_aria and not has_for_label:
                missing_labels.append((f, inp))

print(f"Total unlabelled inputs found: {len(missing_labels)}")
for f, inp in missing_labels:
    print(f"{f}: {inp}")
