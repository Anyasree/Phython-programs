import cv2
import numpy as np

def apply_color_filter(image, filter_type):
    filtered_image = image.copy()
    if filter_type == "red_tint":
        filtered_image[:, :, 1] = 0
        filtered_image[:, :, 0] = 0

    elif filter_type == "blue_tint":
        filtered_image[:, :, 1] = 0
        filtered_image[:, :, 2] = 0

    elif filter_type == "green_tint":
        filtered_image[:, :, 0] = 0
        filtered_image[:, :, 2] = 0

    return filtered_image

image = cv2.imread("/Users/samathagandla/Pictures/Photos Library.photoslibrary/resources/derivatives/A/A140F02F-FD7F-485E-A6CB-550917ED9102_1_105_c.jpeg")

if image is None:
    print("ERROR:Image not found!")

else:
    filter_type = "original"

    print("Press the following keys to apply filter:")
    print("r - Red Tint")
    print("b - Blue Tint")
    print("g - Green Tint")
    print("q - Quit")
    while True:
        filtered_image = apply_color_filter(image, filter_type)
        cv2.imshow("Filtered Image", filtered_image)
        key = cv2.waitKey(0) & 0xFF

        if key == ord('r'):
            filter_type = "red_tint"

        elif key == ord('b'):
            filter_type = "blue_tint"

        elif key == ord('g'):
            filter_type = "green_tint"

        elif key == ord('q'):
            cv2.destroyAllWindows()
            print("Exiting...")
            break
        
        else:
            
            print("Invalid key!!! Please use 'r', 'b', 'g', 'q' ")

cv2.destroyAllWindows()