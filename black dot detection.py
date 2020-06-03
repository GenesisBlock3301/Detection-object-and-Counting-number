import cv2
import imutils

img = cv2.imread('black-dot1.jpg',0)
cv2.imshow('orginal imge gray',img)
cv2.waitKey(0)

thresh = cv2.threshold(img,100,255,cv2.THRESH_BINARY_INV)[1]
cv2.imshow('thresh hold',thresh)
cv2.waitKey(0)
cnts = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
conts = imutils.grab_contours(cnts)
o = cv2.drawContours(img,conts,-1,(255,0,0),1)
print(len(conts))
cv2.imshow('Detected',o)
cv2.waitKey(0)