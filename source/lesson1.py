import cv2

#read the image
image = cv2.imread("document.jpg")

print(type(image))
print(image.shape)
