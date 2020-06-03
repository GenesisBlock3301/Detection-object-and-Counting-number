import numpy as np
import cv2

font = cv2.FONT_HERSHEY_COMPLEX
img2 = cv2.imread('image3.jpg',cv2.IMREAD_COLOR)
# cv2.imshow('orginal image',img2)
# cv2.waitKey(0)

img = cv2.imread('image3.jpg',cv2.IMREAD_GRAYSCALE)
# cv2.imshow('Grayscale',img)
# cv2.waitKey(0)

thresh = cv2.threshold(img,110,255,cv2.THRESH_BINARY)[1]
cv2.imshow('thresh hold',img)
cv2.waitKey(0)

cnts = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0]
m = 0
for c in cnts:
    peri = cv2.arcLength(c,True)
    approx = cv2.approxPolyDP(c,0.009*peri,True)
    cv2.drawContours(img2,[approx],-1,(0,0,255),5)
    # print(approx,m)
    # print(peri*0.09)
    n = approx.ravel()
    print(n)
    i = 0
    for j in n:
        if (i%2 == 0):
            x = n[i]
            y = n[i+1]
            string = str(x)+" "+str(y)
            if (i == 0):
                cv2.putText(img2,"Arrow tips",(x,y),font,0.5,(255,0,0))
            else:
                cv2.putText(img2, string, (x, y), font, 0.5, (0, 255, 0))
        i+=1
    cv2.imshow('image2',img2)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
    # m+=1
    # if m == 3:
    #     break