import cv2

image = cv2.imread("document.jpg")

cv2.rectangle(image,(50,50),(300,200),(0,255,0),3) # Draw a rectangle on the image with top-left corner at (50,50) and bottom-right corner at (300,200), with green color (0,255,0) and thickness of 3 pixels.

cv2.imshow("Rectangle", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
