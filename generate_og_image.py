import os
from PIL import Image, ImageDraw, ImageFont

def generate_og_image():
    W, H = 1200, 630
    img = Image.new("RGBA", (W, H), (11, 19, 43, 255))
    draw = ImageDraw.Draw(img)

    # Gradient background
    for y in range(H):
        ratio = y / H
        r = int(11 + (15 - 11) * ratio)
        g = int(19 + (23 - 19) * ratio)
        b = int(43 + (42 - 43) * ratio)
        draw.line([(0, y), (W, y)], fill=(r, g, b, 255))

    # Ambient glowing compounding curves in background
    curve_points = [
        (60, 530), (180, 510), (320, 480), (460, 430),
        (600, 360), (760, 260), (920, 150), (1140, 60)
    ]
    
    # Outer glow
    for i in range(len(curve_points)-1):
        x1, y1 = curve_points[i]
        x2, y2 = curve_points[i+1]
        draw.line([(x1, y1), (x2, y2)], fill=(0, 230, 168, 40), width=24)
        draw.line([(x1, y1), (x2, y2)], fill=(0, 230, 168, 90), width=12)
        draw.line([(x1, y1), (x2, y2)], fill=(0, 230, 168, 220), width=5)

    for pt in curve_points:
        draw.ellipse([pt[0]-6, pt[1]-6, pt[0]+6, pt[1]+6], fill=(0, 230, 168, 255), outline=(255, 255, 255, 255), width=2)

    # Fonts
    try:
        font_brand = ImageFont.truetype("arialbd.ttf", 46)
        font_badge = ImageFont.truetype("arialbd.ttf", 16)
        font_h1 = ImageFont.truetype("arialbd.ttf", 44)
        font_sub = ImageFont.truetype("arial.ttf", 22)
        font_card_head = ImageFont.truetype("arialbd.ttf", 18)
        font_card_num = ImageFont.truetype("arialbd.ttf", 32)
        font_card_sub = ImageFont.truetype("arial.ttf", 15)
    except:
        font_brand = ImageFont.load_default()
        font_badge = font_brand
        font_h1 = font_brand
        font_sub = font_brand
        font_card_head = font_brand
        font_card_num = font_brand
        font_card_sub = font_brand

    # Main Left Glassmorphism Hero Panel
    draw.rounded_rectangle([60, 60, 740, 570], radius=24, fill=(28, 37, 65, 230), outline=(51, 65, 85, 255), width=2)

    # Logo Emblem
    draw.rounded_rectangle([95, 95, 145, 145], radius=14, fill=(11, 19, 43, 255), outline=(0, 230, 168, 255), width=2)
    draw.line([(105, 132), (117, 120), (127, 126), (137, 108)], fill=(0, 230, 168, 255), width=3)
    draw.ellipse([135, 106, 139, 110], fill=(255, 255, 255, 255))

    # Brand Title
    draw.text((160, 98), "Calculator", font=font_brand, fill=(255, 255, 255, 255))
    draw.text((388, 98), "ship", font=font_brand, fill=(0, 230, 168, 255))

    # Badge Pill: 10 Calculators & 28 Guides
    draw.rounded_rectangle([95, 175, 470, 215], radius=20, fill=(6, 78, 59, 240), outline=(0, 230, 168, 255), width=1)
    draw.text((115, 185), "10 PRO CALCULATORS  •  28 IN-DEPTH GUIDES", font=font_badge, fill=(167, 243, 208, 255))

    # Big Headline
    draw.text((95, 245), "Master Your Wealth\n& Tax Compounding", font=font_h1, fill=(248, 250, 252, 255), spacing=12)

    # Tools list
    draw.text((95, 375), "SIP • Lumpsum • PPF • SWP • Loan EMI • Tax Regimes", font=font_sub, fill=(148, 163, 184, 255))

    # Divider & Footer features
    draw.line([(95, 435), (705, 435)], fill=(51, 65, 85, 255), width=1)
    draw.text((95, 465), "100% Free & Independent Financial Mathematical Tools", font=font_sub, fill=(0, 230, 168, 255))
    draw.text((95, 510), "Built for Indian Investors, Salaried Professionals & Retirees", font=ImageFont.truetype("arial.ttf", 17) if hasattr(ImageFont, "truetype") else font_sub, fill=(148, 163, 184, 255))

    # Right Floating Card 1: PPF & Compounding
    draw.rounded_rectangle([770, 80, 1140, 235], radius=20, fill=(28, 37, 65, 240), outline=(51, 65, 85, 255), width=2)
    draw.text((800, 105), "100% TAX-FREE WEALTH", font=font_card_head, fill=(148, 163, 184, 255))
    draw.text((800, 140), "₹1.03 Crore (PPF)", font=font_card_num, fill=(0, 230, 168, 255))
    draw.text((800, 190), "Statutory EEE Triple Tax Exemption", font=font_card_sub, fill=(203, 213, 225, 255))

    # Right Floating Card 2: SWP Retirement Pension
    draw.rounded_rectangle([770, 260, 1140, 415], radius=20, fill=(28, 37, 65, 240), outline=(51, 65, 85, 255), width=2)
    draw.text((800, 285), "SWP MONTHLY PENSION", font=font_card_head, fill=(148, 163, 184, 255))
    draw.text((800, 320), "₹84.0 Lakh Payout", font=font_card_num, fill=(255, 255, 255, 255))
    draw.text((800, 370), "Plus ₹1.98 Cr Residual Portfolio", font=font_card_sub, fill=(148, 163, 184, 255))

    # Right Floating Card 3: Loan EMI Savings
    draw.rounded_rectangle([770, 440, 1140, 585], radius=20, fill=(28, 37, 65, 240), outline=(51, 65, 85, 255), width=2)
    draw.text((800, 465), "LOAN PREPAYMENT IMPACT", font=font_card_head, fill=(148, 163, 184, 255))
    draw.text((800, 500), "Save ₹18.4 Lakh", font=font_card_num, fill=(0, 230, 168, 255))
    draw.text((800, 545), "Cut 7+ Years from Mortgage Tenure", font=font_card_sub, fill=(203, 213, 225, 255))

    out_dir = r"c:\Users\ravin\OneDrive\Desktop\50 websites\1.1"
    png_path = os.path.join(out_dir, "og-image.png")
    webp_path = os.path.join(out_dir, "og-image.webp")

    img_rgb = img.convert("RGB")
    img_rgb.save(png_path, "PNG", quality=95)
    img_rgb.save(webp_path, "WEBP", quality=92)
    print(f"Generated Redesigned OG Images at {png_path} and {webp_path}")

if __name__ == "__main__":
    generate_og_image()
