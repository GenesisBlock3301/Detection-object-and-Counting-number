import argparse
import imutils
import cv2
from imutils.perspective import four_point_transform
from imutils import contours
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="path to input image")
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
cv2.imshow('Orginal image',image)
cv2.waitKey(0)

ANSWER_KEY  = {0:1,1:4,2:0,3:3,4:1}
# image = np.array(image)
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray,(5,5),0)
cv2.imshow('blur',blurred)
cv2.waitKey(0)

edged = cv2.Canny(blurred,threshold1=75,threshold2=200)
cv2.imshow('edge',edged)
cv2.waitKey(0)
#use contiurs

conts = cv2.findContours(edged.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(conts)
docCnt = None

print(conts)
if len(conts) > 0:
    conts = sorted(conts,key=cv2.contourArea,reverse=True)
    for c in conts:
        peri = cv2.arcLength(c,True)
        approx = cv2.approxPolyDP(c,0.02*peri,True)

        if len(approx) == 4:
            docCnt = approx
            break
