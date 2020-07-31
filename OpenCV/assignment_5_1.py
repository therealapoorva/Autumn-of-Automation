
import cv2 
import numpy as np 

def ball(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    gray_blurred = cv2.blur(gray, (3, 3)) 
    detected_circles = cv2.HoughCircles(gray_blurred,  
                    cv2.HOUGH_GRADIENT, 1, 600, param1 = 50, 
                param2 = 30, minRadius = 5, maxRadius = 35) 
    if detected_circles is not None: 
        detected_circles = np.uint16(np.around(detected_circles)) 
        for (a,b,r) in detected_circles[0, :]: 
            #a, b, r = pt[0], pt[1], pt[2] 
            cv2.circle(img, (a, b), r, (0, 255, 0), 2) 
            cv2.circle(img, (a, b), 2, (0, 0, 255), 3) 
            cv2.imshow("Detected Circle", img) 

cap= cv2.VideoCapture('messi.mp4');
while(True):
    ret, frame = cap.read()
    ball(frame)
    if cv2.waitKey(1) & 0xFF== 27:
        break
cap.release()
cv2.destroyAllWindows()