# QR Code Generator with Centered Logo

This project provides Python scripts to generate **high-resolution QR codes** — for arbitrary data/URLs or for Wi-Fi network credentials — with an **optional centered logo**. The output is optimized for **printing (600 DPI)** and can be customized (size, border, logo scale, etc.). Every generated file name gets a `YYYYMMDD-HHMMSS` timestamp suffix so repeated runs never overwrite previous outputs.

---

## 📦 Requirements

Install the required dependencies before running the Python script:

```
python.exe -m pip install --upgrade pip
pip install Pillow qrcode
```

## ▶️ Usage: generateQRcode.py

1. (Optional) Place your logo file (PNG recommended, supports transparency) in the same folder as the script.
   Example: NEMM-logo.png
2. Run the script:

   ```
   python generateQRcode.py
   ```
3. The script will generate a QR code image (default: QRcode.png, saved as QRcode_<timestamp>.png)

- Resolution: 3860 × 3860 pixels
- DPI: 600 (print ready)
- Border: Reduced for compact look
- Logo: Centered with white square background (badge) — omit `logo_path` (or pass `""`) to generate a plain QR code with no logo

## ⚙️ Script Parameters: generateQRcode.py

Inside generateQRcode.py, you can adjust:

- data → The URL or text to encode in the QR code
- logo_path → Path to your logo image (optional — leave empty/omit for no logo)
- out_path → File name for the output QR code (default: QRcode.png); a timestamp is automatically inserted after the "QRcode" keyword
- qr_px → Output image resolution in pixels (default: 3860 for ultra-high resolution)
- border → QR border thickness (default: 1)
- logo_scale → Logo size relative to QR width (default: 0.22)
- badge_padding → White padding around the logo inside the square badge
- dpi → Output DPI (default: 600 for print)

## 📂 Example

```
if __name__ == "__main__":
    generate_qr_with_logo(
        data="https://bio.site/nemmjosh",
        logo_path="NEMM-logo.png",
        out_path="QRcode.png",
        qr_px=3860,
        dpi=600
    )
```
This saves a file like `QRcode_20261007-230226.png` — a high-res QR code with your logo in the center, ready for both digital use and professional printing.

## 🖼 Output: generateQRcode.py

- Format: PNG
- Filename: `<out_path>` with a `YYYYMMDD-HHMMSS` timestamp inserted after the "QRcode" keyword
- Resolution: 3860 x 3860 px
- DPI: 600
- Logo: Centered with a white square badge (optional)
- Border: Reduced for cleaner design

---

## ▶️ Usage: generateWiFiQRcode.py

Generates a QR code that, when scanned, connects the device directly to a Wi-Fi network — with an optional centered logo/symbol, same as `generateQRcode.py`.

1. (Optional) Place your logo/Wi-Fi symbol image in the same folder as the script.
2. Run the script:

   ```
   python generateWiFiQRcode.py
   ```
3. The script will generate a Wi-Fi QR code image (default: WiFi-QRcode.png, saved as WiFi-QRcode-<timestamp>.png)

## ⚙️ Script Parameters: generateWiFiQRcode.py

Inside generateWiFiQRcode.py, you can adjust:

- ssid → Wi-Fi network name
- password → Wi-Fi password
- auth_type → Authentication type: "WPA", "WEP", or "nopass" (default: "WPA")
- hidden → True if the network is hidden (default: False)
- filename → File name for the output QR code (default: WiFi-QRcode.png); a timestamp is automatically inserted after the "QRcode" keyword
- resolution → Output image resolution in pixels (default: 3860)
- border → QR border thickness (default: 1)
- logo_path → Path to a logo/symbol image to center on the QR code (optional — leave empty/omit for no logo)
- logo_scale → Logo size relative to QR width (default: 0.22)
- badge_padding → White padding around the logo inside the square badge

## 📂 Example

```
if __name__ == "__main__":
    create_wifi_qr(
        ssid="MyNetwork",
        password="MyPassword",
        resolution=3860,
        border=1,
        logo_path="wifi_logo.png"
    )
```
This saves a file like `WiFi-QRcode-20261007-233200.png`.

## 🖼 Output: generateWiFiQRcode.py

- Format: PNG
- Filename: `<filename>` with a `YYYYMMDD-HHMMSS` timestamp inserted after the "QRcode" keyword
- Resolution: configurable (default 3860 x 3860 px)
- Logo: Centered with a white square badge (optional)

## ✅ Tips

- Use a high-contrast logo for best scan reliability
- Keep logo size ≤ 25% of QR width
- If placing on colored backgrounds, consider generating a transparent background version

## 📜 License

Free to use and modify for personal or organizational projects.