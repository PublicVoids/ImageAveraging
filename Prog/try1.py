# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 18:15:03 2016

@author: jeroen
"""

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    try:
        OldGray
    except  NameError:
        OldGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    Gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.addWeighted( Gray, 0.1, OldGray, 0.9, 0.0, OldGray);    

    # Display the resulting frame
    cv2.imshow('frame',OldGray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
print "Done"