import cv2

def preprocess(image):

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    _, threshold = cv2.threshold(
        gray,
        0,
        255,
        cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
    )

    kernel = cv2.getStructuringElement(
        cv2.MORPH_RECT,
        (25,5)
    )

    dilated = cv2.dilate(
        threshold,
        kernel,
        iterations=1
    )

    return dilated
