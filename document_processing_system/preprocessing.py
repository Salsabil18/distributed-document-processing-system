image = load_image()

processed = preprocess(image)

regions = detect_regions(processed)

texts = []

for region in regions:
    texts.append(extract_text(region))

merge_text(texts)
