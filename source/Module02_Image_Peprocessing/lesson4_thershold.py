import cv2

image = cv2.imread("document.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # Convert the image to grayscale

_, threshold = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY) # Apply a binary threshold to the grayscale image

cv2.imshow("Threshold", threshold)

cv2.waitKey(0)
cv2.destroyAllWindows()
