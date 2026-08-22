import os
import math
from PIL import Image, ImageDraw, ImageFont

def create_redesigned_og_image():
    W, H = 1200, 630
    
    # 1. Base Image - Clean Light Theme matching website #F3F7F5
    img = Image.new("RGBA", (W, H), (243, 247, 245, 255))

    # 2. Subtle luxury gradient background (from soft mint #F3F7F5 to clean white #FFFFFF)
    draw = ImageDraw.Draw(img)
    for y in range(H):
        ratio = y / H
        r = int(243 + (255 - 243) * (ratio * 0.6))
        g = int(247 + (255 - 247) * (ratio * 0.6))
        b = int(245 + (255 - 245) * (ratio * 0.6))
        draw.line([(0, y), (W, y)], fill=(r, g, b, 255))

    # 3. Soft decorative mesh / ambient glowing orbs behind cards
    glow_overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    glow_draw = ImageDraw.Draw(glow_overlay)
    
    # Top-right emerald radiant glow
    for rad in range(360, 0, -8):
        alpha = int(18 * (1 - rad / 360))
        glow_draw.ellipse([980 - rad, 200 - rad, 980 + rad, 200 + rad], fill=(0, 208, 156, alpha))
        
    # Soft accent glow bottom-left
    for rad in range(260, 0, -8):
        alpha = int(14 * (1 - rad / 260))
        glow_draw.ellipse([140 - rad, 520 - rad, 140 + rad, 520 + rad], fill=(167, 243, 208, alpha))
        
    img = Image.alpha_composite(img, glow_overlay)
    draw = ImageDraw.Draw(img)

    # 4. Subtle background geometric dot matrix matching fintech UI
    grid_color = (226, 232, 240, 160)
    for gx in range(40, W, 48):
        for gy in range(40, H, 48):
            draw.ellipse([gx-1, gy-1, gx+1, gy+1], fill=grid_color)

    # 5. Load Fonts
    font_folder = "C:/Windows/Fonts"
    try:
        font_logo = ImageFont.truetype(os.path.join(font_folder, "segoeuib.ttf"), 30)
        font_logo_sub = ImageFont.truetype(os.path.join(font_folder, "segoeuib.ttf"), 10)
        font_badge = ImageFont.truetype(os.path.join(font_folder, "segoeuib.ttf"), 13)
        font_h1 = ImageFont.truetype(os.path.join(font_folder, "segoeuib.ttf"), 40)
        font_h1_sub = ImageFont.truetype(os.path.join(font_folder, "segoeui.ttf"), 17)
        font_pill = ImageFont.truetype(os.path.join(font_folder, "segoeuib.ttf"), 13)
        font_card_head = ImageFont.truetype(os.path.join(font_folder, "segoeuib.ttf"), 15)
        font_card_val = ImageFont.truetype(os.path.join(font_folder, "segoeuib.ttf"), 28)
        font_card_sub = ImageFont.truetype(os.path.join(font_folder, "segoeui.ttf"), 13)
        font_micro = ImageFont.truetype(os.path.join(font_folder, "segoeui.ttf"), 12)
        font_micro_bold = ImageFont.truetype(os.path.join(font_folder, "segoeuib.ttf"), 12)
    except:
        font_logo = ImageFont.truetype("arialbd.ttf", 30)
        font_logo_sub = ImageFont.truetype("arialbd.ttf", 10)
        font_badge = ImageFont.truetype("arialbd.ttf", 13)
        font_h1 = ImageFont.truetype("arialbd.ttf", 40)
        font_h1_sub = ImageFont.truetype("arial.ttf", 17)
        font_pill = ImageFont.truetype("arialbd.ttf", 13)
        font_card_head = ImageFont.truetype("arialbd.ttf", 15)
        font_card_val = ImageFont.truetype("arialbd.ttf", 28)
        font_card_sub = ImageFont.truetype("arial.ttf", 13)
        font_micro = ImageFont.truetype("arial.ttf", 12)
        font_micro_bold = ImageFont.truetype("arialbd.ttf", 12)

    # 6. Top Navbar / Header Bar (Matching Website Header)
    draw.line([(0, 84), (W, 84)], fill=(226, 232, 240, 255), width=1)
    
    # Official Website Logo Icon (Exact shape from logo-light.svg)
    icon_x, icon_y = 50, 20
    # Gradient square background
    draw.rounded_rectangle([icon_x, icon_y, icon_x + 44, icon_y + 44], radius=12, fill=(0, 135, 90, 255))
    draw.rounded_rectangle([icon_x, icon_y, icon_x + 44, icon_y + 22], radius=12, fill=(0, 208, 156, 120))
    
    # 3 Rising bars inside logo
    draw.rounded_rectangle([icon_x + 9, icon_y + 26, icon_x + 16, icon_y + 36], radius=2, fill=(255, 255, 255, 220))
    draw.rounded_rectangle([icon_x + 19, icon_y + 19, icon_x + 26, icon_y + 36], radius=2, fill=(255, 255, 255, 240))
    draw.rounded_rectangle([icon_x + 29, icon_y + 10, icon_x + 36, icon_y + 36], radius=2, fill=(255, 255, 255, 255))

    # Brand Text: "Calculator" (#0F172A) + "ship" (#00D09C)
    draw.text((icon_x + 54, icon_y + 1), "Calculator", font=font_logo, fill=(15, 23, 42, 255))
    calc_len = draw.textlength("Calculator", font=font_logo)
    draw.text((icon_x + 54 + calc_len, icon_y + 1), "ship", font=font_logo, fill=(0, 208, 156, 255))
    
    # Brand Tagline
    draw.text((icon_x + 55, icon_y + 32), "SMART FINANCIAL TOOLS  •  CALCULATORSHIP.IN", font=font_logo_sub, fill=(100, 116, 139, 255))

    # Top Right Header Pills
    cats = ["SIP & Lumpsum", "PPF & Tax", "SWP Pension", "Loan EMI"]
    cx = 640
    for cat in cats:
        cat_w = draw.textlength(cat, font=font_pill) + 24
        draw.rounded_rectangle([cx, 24, cx + cat_w, 60], radius=18, fill=(255, 255, 255, 240), outline=(226, 232, 240, 255), width=1)
        draw.text((cx + 12, 32), cat, font=font_pill, fill=(51, 65, 85, 255))
        cx += cat_w + 12

    # 7. LEFT HERO SECTION (Value Proposition & Trust Signals)
    # Badge Pill (Emerald Soft theme)
    badge_x, badge_y = 50, 120
    draw.rounded_rectangle([badge_x, badge_y, badge_x + 380, badge_y + 34], radius=17, fill=(230, 248, 243, 255), outline=(167, 243, 208, 255), width=1)
    # Small emerald indicator dot
    draw.ellipse([badge_x + 14, badge_y + 12, badge_x + 22, badge_y + 20], fill=(0, 208, 156, 255))
    draw.text((badge_x + 28, badge_y + 8), "10 PRO CALCULATORS  •  28 IN-DEPTH GUIDES", font=font_badge, fill=(0, 135, 90, 255))

    # Main Bold Headline
    h1_y = 170
    draw.text((50, h1_y), "Master Your Wealth &", font=font_h1, fill=(15, 23, 42, 255))
    draw.text((50, h1_y + 48), "Tax Compounding", font=font_h1, fill=(0, 135, 90, 255))

    # Subheading paragraph
    draw.text((50, h1_y + 108), "Real-time math models, year-by-year schedules,", font=font_h1_sub, fill=(51, 65, 85, 255))
    draw.text((50, h1_y + 134), "and tax-optimised strategies for Indian investors.", font=font_h1_sub, fill=(100, 116, 139, 255))

    # Feature List with Clean Vector Checkmarks
    features = [
        "100% Free & Independent (No Login Required)",
        "Inflation-Adjusted & Post-Tax Real Growth",
        "Full Compounding Amortization Breakdown"
    ]
    feat_y = h1_y + 178
    for feat in features:
        # Checkmark bubble
        draw.ellipse([50, feat_y + 2, 70, feat_y + 22], fill=(230, 248, 243, 255), outline=(167, 243, 208, 255), width=1)
        draw.line([(56, feat_y + 12), (59, feat_y + 16), (65, feat_y + 8)], fill=(0, 135, 90, 255), width=2)
        draw.text((80, feat_y + 3), feat, font=font_micro_bold, fill=(15, 23, 42, 255))
        feat_y += 32

    # Bottom Trust Ribbon
    draw.line([(50, 560), (510, 560)], fill=(226, 232, 240, 255), width=1)
    draw.text((50, 574), "SIP • Lumpsum • Step-Up • PPF • SWP • Loan EMI • 15-15-15 Rule", font=font_micro, fill=(100, 116, 139, 255))

    # 8. RIGHT SIDE: UI PREVIEW SIMULATOR CARD (The Website Look & Feel)
    # White elevated container with shadow
    card_x, card_y, card_w, card_h = 540, 115, 610, 480
    
    # Shadow simulation
    for s in range(8, 0, -1):
        s_alpha = int(12 / s)
        draw.rounded_rectangle([card_x - s, card_y - s, card_x + card_w + s, card_y + card_h + s], radius=20 + s, fill=(15, 23, 42, s_alpha))
        
    # Main White Card
    draw.rounded_rectangle([card_x, card_y, card_x + card_w, card_y + card_h], radius=20, fill=(255, 255, 255, 255), outline=(226, 232, 240, 255), width=2)

    # Card Top Header Bar
    draw.rounded_rectangle([card_x, card_y, card_x + card_w, card_y + 54], radius=20, fill=(248, 250, 252, 255))
    draw.rectangle([card_x, card_y + 36, card_x + card_w, card_y + 54], fill=(248, 250, 252, 255))
    draw.line([(card_x, card_y + 54), (card_x + card_w, card_y + 54)], fill=(226, 232, 240, 255), width=1)

    # Window dots
    draw.ellipse([card_x + 18, card_y + 22, card_x + 28, card_y + 32], fill=(239, 68, 68, 255))
    draw.ellipse([card_x + 34, card_y + 22, card_x + 44, card_y + 32], fill=(245, 158, 11, 255))
    draw.ellipse([card_x + 50, card_y + 22, card_x + 60, card_y + 32], fill=(16, 185, 129, 255))

    draw.text((card_x + 76, card_y + 18), "SIP Compounding Simulation (Live Model)", font=font_card_head, fill=(15, 23, 42, 255))

    # Inner Content Grid: Left inputs simulator, Right Results donut
    # Left Input Rows
    in_x = card_x + 24
    in_y = card_y + 72
    
    inputs = [
        ("Monthly SIP Deposit", "₹25,000 / mo", 0.65),
        ("Expected Return Rate", "13.5% p.a.", 0.55),
        ("Investment Horizon", "15 Years", 0.40)
    ]
    
    for label, val, bar_fill in inputs:
        draw.text((in_x, in_y), label, font=font_micro, fill=(100, 116, 139, 255))
        draw.text((in_x + 175, in_y - 2), val, font=font_micro_bold, fill=(15, 23, 42, 255))
        
        # Slider Track
        draw.rounded_rectangle([in_x, in_y + 20, in_x + 245, in_y + 26], radius=3, fill=(226, 232, 240, 255))
        # Slider Active Fill (Emerald #00D09C)
        draw.rounded_rectangle([in_x, in_y + 20, in_x + int(245 * bar_fill), in_y + 26], radius=3, fill=(0, 208, 156, 255))
        # Slider Thumb
        thumb_x = in_x + int(245 * bar_fill)
        draw.ellipse([thumb_x - 6, in_y + 17, thumb_x + 6, in_y + 29], fill=(255, 255, 255, 255), outline=(0, 135, 90, 255), width=2)
        
        in_y += 52

    # Right Donut Ratio (Live SVG style Donut Chart)
    donut_cx, donut_cy = card_x + 440, card_y + 145
    donut_r = 46
    # Outer base circle (Capital invested in Slate #CBD5E1)
    draw.ellipse([donut_cx - donut_r, donut_cy - donut_r, donut_cx + donut_r, donut_cy + donut_r], outline=(203, 213, 225, 255), width=13)
    
    # Growth Segment in Emerald (#00D09C) arc
    draw.arc([donut_cx - donut_r, donut_cy - donut_r, donut_cx + donut_r, donut_cy + donut_r], start=270, end=130, fill=(0, 208, 156, 255), width=13)

    # Donut center text
    draw.text((donut_cx - 23, donut_cy - 13), "+187%", font=font_micro_bold, fill=(0, 135, 90, 255))
    draw.text((donut_cx - 18, donut_cy + 2), "GAIN", font=font_logo_sub, fill=(100, 116, 139, 255))

    # Mini Donut Legend
    draw.ellipse([donut_cx - 70, card_y + 215, donut_cx - 62, card_y + 223], fill=(0, 208, 156, 255))
    draw.text((donut_cx - 56, card_y + 212), "Growth: ₹85.6 L (65%)", font=font_micro, fill=(51, 65, 85, 255))

    draw.ellipse([donut_cx - 70, card_y + 233, donut_cx - 62, card_y + 241], fill=(203, 213, 225, 255))
    draw.text((donut_cx - 56, card_y + 230), "Invested: ₹45.0 L (35%)", font=font_micro, fill=(100, 116, 139, 255))

    # Divider inside card
    draw.line([(card_x + 20, card_y + 258), (card_x + card_w - 20, card_y + 258)], fill=(226, 232, 240, 255), width=1)

    # Results Summary Box (Green soft banner)
    res_box_y = card_y + 274
    draw.rounded_rectangle([card_x + 20, res_box_y, card_x + card_w - 20, res_box_y + 110], radius=16, fill=(230, 248, 243, 255), outline=(167, 243, 208, 255), width=2)

    draw.text((card_x + 36, res_box_y + 14), "TOTAL PROJECTED MATURITY VALUE", font=font_badge, fill=(0, 135, 90, 255))
    draw.text((card_x + 36, res_box_y + 40), "₹ 1,30,62,492", font=ImageFont.truetype(os.path.join(font_folder, "segoeuib.ttf"), 38) if os.path.exists(os.path.join(font_folder, "segoeuib.ttf")) else font_card_val, fill=(15, 23, 42, 255))
    draw.text((card_x + 395, res_box_y + 50), "(₹1.31 Crore)", font=font_card_head, fill=(0, 135, 90, 255))

    # Bottom Pill Badges in Card
    pill_w = (card_w - 60) // 3
    
    draw.rounded_rectangle([card_x + 20, card_y + 405, card_x + 20 + pill_w, card_y + 445], radius=10, fill=(248, 250, 252, 255), outline=(226, 232, 240, 255), width=1)
    draw.text((card_x + 34, card_y + 417), "Deposit: ₹45.0 L", font=font_micro_bold, fill=(51, 65, 85, 255))

    draw.rounded_rectangle([card_x + 30 + pill_w, card_y + 405, card_x + 30 + 2 * pill_w, card_y + 445], radius=10, fill=(248, 250, 252, 255), outline=(226, 232, 240, 255), width=1)
    draw.text((card_x + 44 + pill_w, card_y + 417), "Profit: +₹85.62 L", font=font_micro_bold, fill=(0, 135, 90, 255))

    draw.rounded_rectangle([card_x + 40 + 2 * pill_w, card_y + 405, card_x + card_w - 20, card_y + 445], radius=10, fill=(248, 250, 252, 255), outline=(226, 232, 240, 255), width=1)
    draw.text((card_x + 54 + 2 * pill_w, card_y + 417), "CAGR: 13.5%", font=font_micro_bold, fill=(15, 23, 42, 255))

    # 9. Save both PNG and WEBP high-resolution outputs
    out_dir = r"c:\Users\ravin\OneDrive\Desktop\50 websites\1.1"
    png_path = os.path.join(out_dir, "og-image.png")
    webp_path = os.path.join(out_dir, "og-image.webp")

    img_rgb = img.convert("RGB")
    img_rgb.save(png_path, "PNG", quality=95)
    img_rgb.save(webp_path, "WEBP", quality=92)
    print(f"Successfully generated light themed website-matched OG image at:\n{png_path}\n{webp_path}")

if __name__ == "__main__":
    create_redesigned_og_image()
