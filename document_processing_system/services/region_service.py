import cv2
import os

from models.region import Region


class RegionService:

    def detect_regions(
        self,
        original_image,
        processed_image
    ):

        contours, _ = cv2.findContours(
            processed_image,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

        os.makedirs(
            "output/regions",
            exist_ok=True
        )

        regions = []

        counter = 1

        for contour in contours:

            x, y, w, h = cv2.boundingRect(contour)

            if w > 60 and h > 20:

                roi = original_image[
                    y:y+h,
                    x:x+w
                ]

                image_path = (
                    f"output/regions/region_{counter}.png"
                )

                cv2.imwrite(
                    image_path,
                    roi
                )

                region = Region(

                    image_path=image_path,

                    x=x,

                    y=y,

                    width=w,

                    height=h

                )

                regions.append(region)

                counter += 1

        return regions
