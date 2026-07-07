from utils import load_image

from preprocessing import preprocess

from region_detection import detect_regions

from ocr_engine import extract_text

from text_merger import save_text

from ocr.tesseract_engine import TesseractEngine

engine = TesseractEngine()

image = load_image("input/document.jpg")

processed = preprocess(image)

regions = detect_regions(image, processed)

texts = []

for region in regions:

    text = engine.extract_text(region)

    texts.append(text)

save_text(texts)

print("Pipeline Finished Successfully.")

from ocr.tesseract_engine import TesseractEngine

engine = TesseractEngine()
