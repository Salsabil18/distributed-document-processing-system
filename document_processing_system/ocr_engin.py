import cv2
import pytesseract

def extract_text(image_path):

    image=cv2.imread(image_path)

    text=pytesseract.image_to_string(
        image,
        lang="ara"
    )

    return text
