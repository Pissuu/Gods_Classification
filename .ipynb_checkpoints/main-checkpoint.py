import cv2
import numpy as np
import argparse
import os
import csv
import time
from random import randint
# Opens the Video file
video_name='V_1.mp4'
cap = cv2.VideoCapture('videos/'+video_name)

#Find FPS
(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
if int(major_ver) < 3:
    fps = int(cap.get(cv2.cv.CV_CAP_PROP_FPS))
    print ("Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps))
else:
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))

i=0
j=0
final_fps=4
block=1
selected_frames=[]
while (len(selected_frames)<final_fps):
    r=randint(1,fps)
    if r not in selected_frames:
        selected_frames.append(r)
selected_frames.sort()

def update_frames(lb,ub):
    selected_frames=[]
    while (len(selected_frames) < final_fps):
        r = randint(lb, ub)
        if r not in selected_frames:
            selected_frames.append(r)
    selected_frames.sort()
    return selected_frames

v_name=video_name.split('.')
v=v_name[0]

while(cap.isOpened()):
    if j == final_fps:
        lb = fps * block
        ub = fps * (block + 1)
        selected_frames = update_frames(lb, ub)
        j = 0
        block += 1
    ret, frame = cap.read()
    if ret == False:
        break
    fname = v + '-frame' + str(i) + '.jpg'
    if i in selected_frames:
        cv2.imwrite('extracted_frames/' + fname, frame)
        j += 1
#        apply_yolo(fname, frame,writer)
        print(j, selected_frames)
    i += 1
    
cap.release()
cv2.destroyAllWindows()