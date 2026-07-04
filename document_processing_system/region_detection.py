import cv2
import os

def detect_regions(original_image, processed_image):

    contours, _ = cv2.findContours(
        processed_image,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    os.makedirs("output/regions", exist_ok=True)

    regions=[]

    counter=1

    for contour in contours:

        x,y,w,h=cv2.boundingRect(contour)

        if w>60 and h>20:

            roi=original_image[y:y+h,x:x+w]

            filename=f"output/regions/region_{counter}.png"

            cv2.imwrite(filename,roi)

            regions.append(filename)

            counter+=1

    return regions
