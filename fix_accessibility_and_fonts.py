import os
import glob
import re

html_files = glob.glob("*.html")
print(f"Auditing and upgrading {len(html_files)} HTML files for PageSpeed / Search Console...")

# 1. Update font links to include display=swap & preconnect optimization
font_link_target = 'family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@700;800&display=swap'

for f in html_files:
    with open(f, "r", encoding="utf-8") as fp:
        c = fp.read()
    
    modified = False

    # Fix unlabelled number inputs by adding aria-label based on preceding label or field ID
    def replace_num_input(match):
        full_tag = match.group(0)
        if "aria-label" in full_tag or "aria-labelledby" in full_tag:
            return full_tag
        
        # Check if ID exists
        id_m = re.search(r'id=["\']([^"\']+)["\']', full_tag)
        if not id_m:
            return full_tag
        
        inp_id = id_m.group(1)
        # Create a readable label from id
        label_text = inp_id.replace("-num", "").replace("-", " ").title()
        if "sip" in inp_id.lower():
            label_text = label_text.replace("Sip", "SIP")
        if "ppf" in inp_id.lower():
            label_text = label_text.replace("Ppf", "PPF")
        if "fd" in inp_id.lower():
            label_text = label_text.replace("Fd", "FD")
        if "emi" in inp_id.lower():
            label_text = label_text.replace("Emi", "EMI")
        if "swp" in inp_id.lower():
            label_text = label_text.replace("Swp", "SWP")
        if "80c" in inp_id.lower():
            label_text = label_text.replace("80C", "80C")
            
        # Add aria-label
        new_tag = full_tag[:-1] + f' aria-label="{label_text} Input">'
        return new_tag

    c_new = re.sub(r'<input[^>]*type=["\']number["\'][^>]*>', replace_num_input, c)
    if c_new != c:
        c = c_new
        modified = True

    # Also check range inputs if missing aria-label
    def replace_range_input(match):
        full_tag = match.group(0)
        if "aria-label" in full_tag or "aria-labelledby" in full_tag:
            return full_tag
        
        id_m = re.search(r'id=["\']([^"\']+)["\']', full_tag)
        if not id_m:
            return full_tag
        
        inp_id = id_m.group(1)
        label_text = inp_id.replace("-", " ").title() + " Slider"
        if "sip" in inp_id.lower():
            label_text = label_text.replace("Sip", "SIP")
        if "ppf" in inp_id.lower():
            label_text = label_text.replace("Ppf", "PPF")
        if "fd" in inp_id.lower():
            label_text = label_text.replace("Fd", "FD")
        if "emi" in inp_id.lower():
            label_text = label_text.replace("Emi", "EMI")
        if "swp" in inp_id.lower():
            label_text = label_text.replace("Swp", "SWP")
        if "80c" in inp_id.lower():
            label_text = label_text.replace("80C", "80C")
            
        new_tag = full_tag[:-1] + f' aria-label="{label_text}">'
        return new_tag

    c_new = re.sub(r'<input[^>]*type=["\']range["\'][^>]*>', replace_range_input, c)
    if c_new != c:
        c = c_new
        modified = True

    # Ensure font stylesheet has font-display=swap and is loaded cleanly
    if "fonts.googleapis.com" in c and "&display=swap" not in c:
        c = c.replace("&display=swap", "") # clean if partial
        c = re.sub(r'family=Inter:[^\"\'&]+(&family=JetBrains\+Mono:[^\"\'&]+)?', r'family=Inter:wght@400;500;600;700;800\1&display=swap', c)
        modified = True

    # Ensure AdSense script and tags have proper containment & layout-shift prevention
    if modified:
        with open(f, "w", encoding="utf-8") as fp:
            fp.write(c)

print("HTML input labeling and font swap upgrades complete.")
