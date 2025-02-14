import cv2
image = cv2.imread("/Users/samathagandla/Pictures/Photos Library.photoslibrary/resources/derivatives/A/A140F02F-FD7F-485E-A6CB-550917ED9102_1_105_c.jpeg")
greyimage = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.namedWindow("Anyasree Gandla",cv2.WINDOW_NORMAL)
cv2.imshow("Anyasree Gandla",greyimage)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(image.shape)
