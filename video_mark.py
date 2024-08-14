import numpy as np
import cv2
import matplotlib.image
from moviepy.editor import *

## Setting the path of raw and output videos
raw_video_path = 'E:/Research/Data/HelioViewer/20210117/20210117-0100-0600-aia171.mp4'
out_video_path = 'C:/Users/rzhuo/Desktop/marked.mp4'

# Initializing video settings
# Reading video
cap = cv2.VideoCapture(raw_video_path)
# Setting the writing format
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# Getting frames rate
fps_video = cap.get(cv2.CAP_PROP_FPS)
print('frame_rate: ', fps_video)
# Getting video width
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print('frame_width: ', frame_width)
# Getting video height
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print('frame_height: ', frame_height)

## Setting the appearance of regions
# Setting region size
reg_width = 5
reg_height = 100
reg_num = int(3)
# Setting vertex location (left-up- and right-down-vertex)
x_lt_up = [780, 800, 820]
y_lt_up = [460, 475, 490]
x_rt_dw = np.zeros(shape=(reg_num, 1))
y_rt_dw = np.zeros(shape=(reg_num, 1))
for i_reg in range(reg_num):
    x_rt_dw[i_reg] = x_lt_up[i_reg] + reg_width
    y_rt_dw[i_reg] = y_lt_up[i_reg] + reg_height
# Setting mark color
color_list = [(0, 0, 255), (0, 255, 0), (255, 0, 0), (255, 255, 0), (255, 0, 255), (0, 255, 255)]

## Marking video
videoWriter = cv2.VideoWriter(out_video_path, fourcc, fps_video, (frame_width, frame_height))
# Iterating by frame
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        # Marking rectangles
        for i_reg in range(reg_num):
            cv2.rectangle(frame, (int(x_lt_up[i_reg]), int(y_lt_up[i_reg])), (int(x_rt_dw[i_reg]), int(y_rt_dw[i_reg])), color_list[i_reg], 2)
        # Writing video
        videoWriter.write(frame)
    else:
        videoWriter.release()
        break
