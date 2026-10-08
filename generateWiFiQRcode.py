import re
from datetime import datetime
import qrcode
from PIL import Image

def create_wifi_qr(ssid, password, auth_type="WPA", hidden=False, filename="WiFi-QRcode.png", resolution=3860, border=1,
                    logo_path="", logo_scale=0.22, badge_padding=20):
    """
    Generate a custom high-resolution Wi-Fi QR Code with reduced border.

    Parameters:
        ssid (str): Wi-Fi SSID (network name)
        password (str): Wi-Fi password
        auth_type (str): Authentication type - "WPA", "WEP", or "nopass"
        hidden (bool): True if the network is hidden
        filename (str): Output filename for the QR code image
        resolution (int): Final resolution (square) in pixels
        border (int): Border size around the QR code
        logo_path (str): Path to a logo/symbol image to center on the QR code (optional)
        logo_scale (float): Logo size relative to the QR code
        badge_padding (int): White margin around the logo
    """
    # Wi-Fi QR Code format
    wifi_config = f"WIFI:T:{auth_type};S:{ssid};P:{password};H:{'true' if hidden else 'false'};;"

    # Generate QR code with reduced border
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=border,
    )
    qr.add_data(wifi_config)
    qr.make(fit=True)

    # Create QR image
    img = qr.make_image(fill_color="black", back_color="white").convert("RGBA")

    # Resize to desired resolution (e.g., 3860x3860)
    img = img.resize((resolution, resolution), Image.Resampling.NEAREST)

    # Load and center a logo/symbol on the QR code (only if a logo_path was provided)
    if logo_path:
        logo = Image.open(logo_path).convert("RGBA")
        target_logo_w = int(resolution * logo_scale)
        logo_ratio = logo.height / logo.width
        logo_w = target_logo_w
        logo_h = int(target_logo_w * logo_ratio)
        logo = logo.resize((logo_w, logo_h), Image.Resampling.LANCZOS)

        # Create square white badge behind logo
        badge_w = logo_w + 2 * badge_padding
        badge_h = logo_h + 2 * badge_padding
        badge = Image.new("RGBA", (badge_w, badge_h), (255, 255, 255, 255))

        # Paste logo onto badge
        badge_center = ((badge_w - logo_w) // 2, (badge_h - logo_h) // 2)
        badge.paste(logo, badge_center, logo)

        # Paste badge+logo at QR center
        qr_center = ((resolution - badge_w) // 2, (resolution - badge_h) // 2)
        img.paste(badge, qr_center, badge)

    img = img.convert("RGB")

    # Append timestamp (YYYYMMDD-HHMMSS) suffix to the "QRcode" keyword in filename
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = re.sub(r"(?i)QRcode", lambda m: f"{m.group(0)}-{timestamp}", filename, count=1)

    # Save image
    img.save(filename, dpi=(300, 300))
    print(f"Wi-Fi QR Code saved as {filename} with {resolution}x{resolution}px resolution")

# Example usage
if __name__ == "__main__":
    create_wifi_qr("ABCD", "ABCD", resolution=3860, border=1)
