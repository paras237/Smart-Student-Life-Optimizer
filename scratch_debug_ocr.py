import cv2
import pytesseract
import os
import re

# Configure tesseract path just like app.py does
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

image_files = [
    r"c:\Users\paras\OneDrive\Desktop\Project\dataset\uploads\WhatsApp_Image_2026-05-12_at_2.41.41_PM.jpeg",
    r"c:\Users\paras\OneDrive\Desktop\Project\dataset\uploads\WhatsApp_Image_2026-05-12_at_2.41.41_PM_1.jpeg",
    r"c:\Users\paras\OneDrive\Desktop\Project\dataset\uploads\WhatsApp_Image_2026-05-12_at_2.41.41_PM_2.jpeg"
]

for f in image_files:
    if not os.path.exists(f):
        print(f"FILE NOT FOUND: {f}")
        continue
        
    print(f"\n--- PROCESSING {os.path.basename(f)} ---")
    img = cv2.imread(f)
    if img is None:
        print("Failed to read img")
        continue
        
    h, w = img.shape[:2]
    scale = max(1.0, 1800.0 / w)
    img = cv2.resize(img, (int(w*scale), int(h*scale)), interpolation=cv2.INTER_CUBIC)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (1, 1), 0)
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    
    try:
        text = pytesseract.image_to_string(thresh, config='--oem 3 --psm 6')
        print("EXTRACTED RAW TEXT HEAD:")
        print("-" * 40)
        print(text)
        print("-" * 40)
    except Exception as e:
        print(f"OCR ERROR: {e}")
