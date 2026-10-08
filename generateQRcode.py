import re
from datetime import datetime
from PIL import Image, ImageDraw
import qrcode
from qrcode.constants import ERROR_CORRECT_H

def generate_qr_with_logo(
    data: str,
    logo_path: str = "",
    out_path: str = "QRcode.png",
    qr_px: int = 3860,       # Resolution of final QR (px x px)
    border: int = 1,         # Quiet zone around QR (smaller = thinner border)
    logo_scale: float = 0.22,# Logo size relative to QR
    badge_padding: int = 20, # White margin around logo
    dpi: int = 600           # Dots per inch for print
):
    """
    Generate a high-resolution QR code with a centered logo (300 DPI ready).
    """

    # Step 1: Generate QR code with high error correction
    qr = qrcode.QRCode(
        version=None,
        error_correction=ERROR_CORRECT_H,  # ~30% recovery
        box_size=10,
        border=border,
    )
    qr.add_data(data)
    qr.make(fit=True)

    qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGBA")
    qr_img = qr_img.resize((qr_px, qr_px), Image.Resampling.NEAREST)

    # Step 2: Load and resize logo (only if a logo_path was provided)
    if logo_path:
        logo = Image.open(logo_path).convert("RGBA")
        target_logo_w = int(qr_px * logo_scale)
        logo_ratio = logo.height / logo.width
        logo_w = target_logo_w
        logo_h = int(target_logo_w * logo_ratio)
        logo = logo.resize((logo_w, logo_h), Image.Resampling.LANCZOS)

        # Step 3: Create square white badge behind logo
        badge_w = logo_w + 2 * badge_padding
        badge_h = logo_h + 2 * badge_padding
        badge = Image.new("RGBA", (badge_w, badge_h), (255, 255, 255, 255))

        # Paste logo onto badge
        badge_center = ((badge_w - logo_w) // 2, (badge_h - logo_h) // 2)
        badge.paste(logo, badge_center, logo)

        # Step 4: Paste badge+logo at QR center
        qr_center = ((qr_px - badge_w) // 2, (qr_px - badge_h) // 2)
        qr_img.paste(badge, qr_center, badge)

    # Append timestamp (YYYYMMDD-HHMMSS) suffix to the "qrcode" keyword in out_path
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    out_path = re.sub(r"(?i)QRcode", lambda m: f"{m.group(0)}-{timestamp}", out_path, count=1)

    # Save result with 600 DPI
    qr_img.save(out_path, dpi=(dpi, dpi), optimize=True)
    print(f"QR code saved to {out_path} at {dpi} DPI")


if __name__ == "__main__":
    # Your logo and URL
    generate_qr_with_logo(
        data="https://drive.google.com/file/d/1_8icyeylx2pCCtbAnTKyjnq-yEyGWrje/view",
        logo_path="NEMM-logo.png",   # <-- replace with your logo file path
        out_path="QRcode.png",
        qr_px=3860,                     # high resolution
        dpi=600                         # print-ready DPI
    )