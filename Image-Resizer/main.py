# Code given by Chatgpt
import cv2

# Load the image
image_path = r'C:\Users\tejas\VS CODE\Python Projects\Image-Resizer\verse.png'  # ✅ Update this path if needed
image = cv2.imread(image_path)

if image is None:
    print("Image not found or unable to load.")
else:
    print("Image loaded successfully!")

    # Get original dimensions
    original_height, original_width = image.shape[:2]
    print(f"Original Dimensions: {original_width} x {original_height}")

    # Get new dimensions from user
    new_width = int(input("Enter new width: "))
    new_height = int(input("Enter new height: "))

    # Resize the image
    resized_image = cv2.resize(image, (new_width, new_height))

    # Save resized image
    cv2.imwrite('resized_image.png', resized_image)
    print("Resized image saved as 'resized_image.png'")

    # Wait and close windows
    cv2.waitKey(0)