# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 18:15:03 2016

@author: jeroen
"""

import numpy
import cv2

cap = cv2.VideoCapture(0)
print "Frame default resolution: (" + str(cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)) + ";"
cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 1024)

#dummy read because first frame seems buggy
ret, frame = cap.read()
xs=frame.shape[0]
ys=frame.shape[1]

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    frame=cv2.resize(frame, (ys*2,xs*2))    
    
    
    # Our operations on the frame come here
    try:
        OldGray
    except  NameError:
        #OldGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        OldGray=frame
    #Gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    Gray=frame
    fact=0.05
    cv2.addWeighted( Gray, fact, OldGray, 1-fact, 0.0, OldGray,dtype=16);    

    # Display the resulting frame

    cv2.imshow('frame',OldGray)
    key=cv2.waitKey(1)
    if key & 0xFF == ord('r'):
        OldGray=Gray
        print "Reset"
        print frame.shape
        print frame.dtype
    if key & 0xFF == ord('q'):
        break
    
    
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
print "Done"