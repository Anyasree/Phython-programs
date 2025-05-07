import cv2
import numpy as np

def apply_filter(image, filter_type):
    filtered_image = image.copy()

    if filter_type == "sobel":
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        sobelx = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize = 3)
        sobely = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize = 3)
        combined_sobel = cv2.bitwise_or(sobelx.astype('uint8'), sobely.astype('uint8'))

        filtered_image = cv2.cvtColor(combined_sobel, cv2.COLOR_GRAY2BGR)
    elif filter_type == "canny":
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray_image, 100, 200)
        filtered_image = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

    return filtered_image

image = cv2.imread("/Users/samathagandla/Pictures/Photos Library.photoslibrary/resources/derivatives/A/A140F02F-FD7F-485E-A6CB-550917ED9102_1_105_c.jpeg")

if image is None:
    print("ERROR: Image not Found!!!")

else:
    filter_type = "original"

    print("Press the following keys to apply filters")
    print("s - Sobel Edge Detection")
    print("c - Canny Edge Detection")
    print("q - Quit")

    while True:
        filtered_image = apply_filter(image, filter_type)
        cv2.imshow("Filtered Image", filtered_image)
        key = cv2.waitKey(0) & 0xFF

        if key == ord('s'):
            filter_type = "sobel"
        elif key == ord('c'):
            filter_type = "canny"
        elif key == ord('q'):
            print("Exiting...")
            break
        else:
            print("Invalid key! Please use 's', 'c', or 'q'.")

cv2.destroyAllWindows()