import cv2
import matplotlib.pyplot as plt
import numpy as np
image = cv2.imread("/Users/samathagandla/Pictures/Photos Library.photoslibrary/resources/derivatives/A/A140F02F-FD7F-485E-A6CB-550917ED9102_1_105_c.jpeg")
grayimage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
sobelx = cv2.Sobel(grayimage, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(grayimage, cv2.CV_64F, 0, 1, ksize=3)
combined_sobel = cv2.bitwise_or(sobelx.astype(np.uint8), sobely.astype(np.uint8))
#Canny Edge Detection
edges = cv2.Canny(image, 50, 150)
plt.imshow(edges, cmap ="gray")
plt.show()