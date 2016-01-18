# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 20:13:00 2016

@author: jeroen
"""

import numpy
import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 1024)

#dummy read because first frame seems buggy
ret, frame = cap.read()
xs=frame.shape[0]
ys=frame.shape[1]

PicsList=[]
NumberPics=100
for i in range(NumberPics):
    # Capture frame-by-frame
    ret, frame = cap.read()
    PicsList.append(numpy.float32(frame[450:600,450:600])/255)

    # Display the resulting frame
print "images Read"

xs=PicsList[-1].shape[0]
ys=PicsList[-1].shape[1]

cv2.imshow('frame',PicsList[-1])
f=4
while(True):
    key=cv2.waitKey(1)
    if key & 0xFF == ord('p'):
        sp=cv2.resize(PicsList[-1], (ys*f,xs*f),interpolation=cv2.INTER_LANCZOS4)    
        cv2.imshow('frame',sp)
    if key & 0xFF == ord('s'):
        sp=PicsList[0]
        for p in PicsList[1:-1]:
            sp=sp+p
        sp=sp/len(PicsList)
        sp=cv2.resize(sp, (ys*f,xs*f),interpolation=cv2.INTER_LANCZOS4)    
        cv2.imshow('frame',sp)
    if key & 0xFF == ord('o'):
        sp=cv2.resize(PicsList[0], (ys*f,xs*f))    
        for p in PicsList[1:-1]:
            sp=sp+cv2.resize(p, (ys*f,xs*f))    
        sp=sp/len(PicsList)
        #sp=cv2.resize(sp, (ys*f,xs*f))    
        cv2.imshow('frame',sp)
    if key & 0xFF == ord('q'):
        break
    
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
print "Done"