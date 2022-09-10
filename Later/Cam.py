import numpy as np
import cv2

#lab
cap = cv2.VideoCapture("/home/ailab/OUTPUT.mp4")

while(True):

    ret, frame = cap.read()
    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
