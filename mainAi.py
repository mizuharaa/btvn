#Import Libraries
import cv2
import os
import numpy as np
import random
from matplotlib import pyplot as plt

capture = cv2.VideoCapture(0)

while True:
    img = capture.read()
    cv2.imshow("Facial Detection", img)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
    
