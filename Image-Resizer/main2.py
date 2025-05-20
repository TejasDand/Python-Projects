# Code given by Google AI
import cv2

image = cv2.imread(r'C:\Users\tejas\VS CODE\Python Projects\Image-Resizer\verse.png')

height, width, channels = image.shape
new_width = int(input("Enter new width: "))
new_height = int(input("Enter new height: "))

resized_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_LINEAR)

# cv2.imshow('Resized Image', resized_image)

cv2.imwrite('resized_image2.png', resized_image)
print("Resized image saved as 'resized_image2.png'")

cv2.waitKey(0)