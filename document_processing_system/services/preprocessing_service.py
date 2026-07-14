
import cv2

from config import KERNEL_SIZE


class PreprocessingService:

    def preprocess(self, image):

        gray = cv2.cvtColor(
            image,
            cv2.COLOR_BGR2GRAY
        )

        _, threshold = cv2.threshold(
            gray,
            0,
            255,
            cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
        )

        kernel = cv2.getStructuringElement(
            cv2.MORPH_RECT,
            KERNEL_SIZE
        )

        dilated = cv2.dilate(
            threshold,
            kernel,
            iterations=1
        )

        return dilated
