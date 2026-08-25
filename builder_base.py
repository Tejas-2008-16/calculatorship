import os
import json
import re

SITE_DIR = r"c:\Users\ravin\OneDrive\Desktop\50 websites\1.1"

AUTHOR_BIO_HTML = """        <div class="author-bio-card">
          <div class="author-bio-header">
            <div class="author-avatar">T</div>
            <div>
              <h3 class="author-name">Tejas</h3>
              <p class="author-title">Finance Researcher &amp; Editor, Calculatorship</p>
            </div>
          </div>
          <p class="author-desc">Tejas researches SEBI guidelines, AMFI data, AMC reports, and RBI circulars to write plain-English financial guides for Indian retail investors. All content is for educational purposes and does not constitute SEBI-registered investment advice.</p>
        </div>"""

def generate_faq_html(faqs):
    html_items = []
    for q, a in faqs:
        html_items.append(f"""          <details class="faq-item" style="background:var(--bg-elevated); border:1px solid var(--border-soft); border-radius:var(--radius-md); padding:16px 20px; margin-bottom:12px;">
            <summary style="font-weight:700; cursor:pointer; font-size:1.02rem; color:var(--text-primary);">{q}</summary>
            <p style="margin-top:12px; color:var(--text-secondary); line-height:1.65; margin-bottom:0;">{a}</p>
          </details>""")
    return "\n".join(html_items)

def generate_schema_json(slug, title, desc, pub_date, mod_date, faqs):
    url = f"https://calculatorship.in/{slug}"
    faq_entities = []
    for q, a in faqs:
        # clean HTML tags from schema answer
        clean_a = re.sub(r'<[^>]+>', '', a)
        clean_q = re.sub(r'<[^>]+>', '', q)
        faq_entities.append({
            "@type": "Question",
            "name": clean_q,
            "acceptedAnswer": {
                "@type": "Answer",
                "text": clean_a
            }
        })
    
    schema = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Article",
                "headline": title,
                "description": desc,
                "image": "https://calculatorship.in/og-image.png",
                "datePublished": f"{pub_date}T08:00:00+05:30",
                "dateModified": f"{mod_date}T12:00:00+05:30",
                "author": {
                    "@type": "Person",
                    "name": "Tejas",
                    "url": "https://calculatorship.in/about.html"
                },
                "publisher": {
                    "@type": "Organization",
                    "name": "Calculatorship",
                    "logo": {
                        "@type": "ImageObject",
                        "url": "https://calculatorship.in/logo-light.svg"
                    }
                },
                "mainEntityOfPage": url
            },
            {
                "@type": "FAQPage",
                "mainEntity": faq_entities
            }
        ]
    }
    return json.dumps(schema, indent=2, ensure_ascii=False)

print("Base builder components ready.")
