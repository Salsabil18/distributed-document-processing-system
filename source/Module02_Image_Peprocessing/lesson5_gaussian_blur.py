import cv2

image = cv2.imread("document.jpg")

blur = cv2.GaussianBlur(image, (5,5), 0)

cv2.imshow("Blur", blur)

cv2.waitKey(0)

cv2.destroyAllWindows()
