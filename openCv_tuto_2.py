import argparse
import imutils
import cv2


ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="path to input image")
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
cv2.imshow('Orginal image',image)
cv2.waitKey(0)

#convert to grayscale
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('grayscale image',gray)
cv2.waitKey(0)

########################
edgeed = cv2.Canny(gray,threshold1=30,threshold2=150)
cv2.imshow('edged',edgeed)
cv2.waitKey(0)

######################
thresh = cv2.threshold(gray,225,255,cv2.THRESH_BINARY_INV)[1]
cv2.imshow('threshold',thresh)
cv2.waitKey(0)
###############################

cnts = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
# cv2.imshow('counters',cnts)
cnts = imutils.grab_contours(cnts)
output = image.copy()
o = cv2.drawContours(output,cnts,-1,(240,0,159),3)
cv2.imshow('conturs',o)
cv2.waitKey(0)
"""For iteraviely use FOR loop"""
for c in cnts:
    cv2.drawContours(output,[c],-1,(240,0,159),3)
    cv2.imshow('output',output)
    cv2.waitKey(0)
text = f"i found {len(cnts)} objects"
cv2.putText(output,text,(10,25),cv2.FONT_HERSHEY_SIMPLEX,0.7,(240,0,159),2)
cv2.imshow('Contourse',output)
cv2.waitKey(0)