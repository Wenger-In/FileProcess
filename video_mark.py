import numpy as np
import cv2
import matplotlib.image
from moviepy.editor import *

video = "E:/Research/Data/HelioViewer/20210117/20210117-0100-0600-aia171.mp4"
result_video = "C:/Users/rzhuo/Desktop/marked.mp4"
# 读取视频
cap = cv2.VideoCapture(video)
# 获取视频帧率
fps_video = cap.get(cv2.CAP_PROP_FPS)
# 设置写入视频的编码格式
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
# 获取视频宽度
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print('frame_width: ', frame_width)
# 获取视频高度
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print('frame_height: ', frame_height)
videoWriter = cv2.VideoWriter(result_video, fourcc, fps_video, (frame_width, frame_height))
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        # select region
        reg_width = 5
        reg_height = 100
        reg_num = int(3)
        left_x_up = [780, 800, 820]
        left_y_up = [460, 475, 490]
        right_x_down = np.zeros(shape=(reg_num, 1))
        right_y_down = np.zeros(shape=(reg_num, 1))
        for i_reg in range(reg_num):
            right_x_down[i_reg] = left_x_up[i_reg] + reg_width
            right_y_down[i_reg] = left_y_up[i_reg] + reg_height
        # mark the region
        color_list = [(0, 0, 255), (0, 255, 0), (255, 0, 0), (255, 255, 0), (255, 0, 255), (0, 255, 255)]
        for i_reg in range(reg_num):
            cv2.rectangle(frame, (int(left_x_up[i_reg]), int(left_y_up[i_reg])), (int(right_x_down[i_reg]), int(right_y_down[i_reg])), color_list[i_reg], 2)
        # # determine the position of each region
        # word_x1 = left_x1_up - 20
        # word_y1 = left_y1_up - 10
        # word_x2 = left_x2_up - 20
        # word_y2 = left_y2_up - 10
        # word_x3 = left_x3_up - 20
        # word_y3 = left_y3_up - 10
        # # mark label of the region
        # cv2.putText(frame, 'reg1', (word_x1, word_y1), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 1)
        # cv2.putText(frame, 'reg2', (word_x2, word_y2), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 1)
        # cv2.putText(frame, 'reg3', (word_x3, word_y3), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 1)
        # write video
        videoWriter.write(frame)
    else:
        videoWriter.release()
        break
