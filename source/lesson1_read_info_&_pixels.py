import cv2

image = cv2.imread("document.jpg") # read the image

print(type(image)) # print the type of the image object

# print the information of the image   
print("Height:", image.shape[0])
print("Width:", image.shape[1])
print("Channels:", image.shape[2])

image[0,0] = [0, 0, 255] # Change the first pixel at (0,0) to red color  

cv2.imwrite("modified.jpg", image) # save the modified image (the first pixel has been successfully changed to red color )

