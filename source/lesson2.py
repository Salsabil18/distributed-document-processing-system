###### Crop & Resize image ######
import cv2

image = cv2.imread("document.jpg")

cropped = image[100:500, 100:500] # Crop the image from y=100 to y=500 and x=100 to x=500 

cv2.imshow("Crop", cropped)

######
resized = cv2.resize(image, (800,600))

cv2.imshow("Resize", resized)

cv2.waitKey(0)
cv2.destroyAllWindows()
