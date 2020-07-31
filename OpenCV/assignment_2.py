import numpy as np
import cv2
from matplotlib import pyplot as plt

img_original =cv2.imread("umic.png",1)
img = cv2.resize(img_original, (400, 400), interpolation = cv2.INTER_NEAREST) 

cv2.imshow('originally',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

def translation(img,x,y):
    rows,cols = img.shape[0], img.shape[1]
    M = np.float32([[1,0,x],[0,1,y]])
    dst = cv2.warpAffine(img,M,(cols,rows))
    return dst
def rotation(img, theta):
    rows,cols = img.shape[0], img.shape[1]
    M = cv2.getRotationMatrix2D((cols/2,rows/2),theta,1)
    dst = cv2.warpAffine(img,M,(cols,rows))
    img2= dst[int(cols*0.25):int(cols*0.75), int(rows*0.25):int(rows*0.75)]
    img2 = cv2.resize(img2, (200, 200), interpolation = cv2.INTER_NEAREST) 
    return img2
   

def blurr(img):
    blur = cv2.blur(img,(8,8))
    return blur

j=0
for i in range(2):
    for t in range(5): 
        Titles =["translationed","translationed","translationed","translationed","rotated","rotated","rotated" ,"rotated", "blurred",  "blurred"] 
        images =[translation(img, np.random.randint(50), np.random.randint(50)),translation(img, np.random.randint(50), np.random.randint(50)),translation(img, np.random.randint(50), np.random.randint(50)),translation(img, np.random.randint(50), np.random.randint(50)), rotation(img_original, 90*np.random.randint(1,5)),rotation(img_original, 90*np.random.randint(1,5)),rotation(img_original, 90*np.random.randint(1,5)),rotation(img_original, 90*np.random.randint(1,5)), blurr(img),blurr(img)] 
        plt.subplot2grid((2, 5), (i,t)) 
        plt.title(Titles[j]), plt.xticks([]), plt.yticks([])
        plt.imshow(images[j])
        j+=1 
        
        
plt.show() 

