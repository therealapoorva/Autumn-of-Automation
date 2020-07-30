import cv2
import numpy as np
from matplotlib import pyplot as plt

def conversion(img):
    kernel_s=np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    img2=cv2.filter2D(img,-1,kernel_s)
    img3= cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    inv = 255- img3
    img4= cv2.GaussianBlur(inv,ksize=(15,15),sigmaX=0, sigmaY=0)
    img= cv2.divide(img3, 255-img4, scale=226)
    return img

img = cv2.imread('lena.jpg')
edges= conversion(img)
plt.subplot(121),plt.imshow(cv2.imread('lena.jpg',1))
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Pencil sketch Image'), plt.xticks([]), plt.yticks([])
plt.show()

cap= cv2.VideoCapture(0);
while(True):
    ret, frame = cap.read()
    frame= conversion(frame)
    cv2.imshow('webcam display', frame)
    if cv2.waitKey(1) & 0xFF== 27:
        break

cap.release()
cv2.destroyAllWindows()
	