import cv2
import numpy as np
import time
import os
import HandTrackingModule as htm

Wcam, Hcam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, Wcam)
cap.set(4, Hcam)

