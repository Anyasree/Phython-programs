import cv2
import matplotlib.pyplot as plt
image = cv2.imread("/Users/samathagandla/Pictures/Photos Library.photoslibrary/resources/derivatives/A/A140F02F-FD7F-485E-A6CB-550917ED9102_1_105_c.jpeg")
imagergb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
cv2.rectangle(imagergb,(10,10),(50,50),(0,0,255),(3))
cv2.circle(imagergb,(100,100),15,(0,255,0),-1)
plt.figure(figsize = (12,8))
plt.imshow(imagergb)
plt.title("Anotated image")
plt.axis("off")
plt.show()