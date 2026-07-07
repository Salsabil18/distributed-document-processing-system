import easyocr

from ocr.base_engine import OCREngine


class EasyOCREngine(OCREngine):

    def __init__(self):

        self.reader = easyocr.Reader(
            ['ar', 'fr'],
            gpu=False
        )

    def extract_text(self, image_path):

        result = self.reader.readtext(
            image_path,
            detail=0
        )

        return "\n".join(result)
