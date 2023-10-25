import os
import cv2


def save_img():
    video_dir = 'C:/Users/rzhuo/Desktop/'
    image_dir = 'C:/Users/rzhuo/Desktop/lasco_c2/'
    vc = cv2.VideoCapture(video_dir + '210117_c2.mpg')
    c = 0
    rval = vc.isOpened()
    while rval:
        c = c + 1
        rval, frame = vc.read()
        if rval:
            cv2.imwrite(image_dir + str(c) + '.png', frame)
            cv2.waitKey(1)
        else:
            break
    vc.release()
    print('save_success')


save_img()
