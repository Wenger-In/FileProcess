import os
import cv2

def video2image(video_path, image_dir):
    '''
    This function splits a video into images. 
    INPUT
    video_path: the path of the video to be splited.
    image_dir:  the directory to save the splited images.
    '''
    # Reading video
    vc = cv2.VideoCapture(video_path)
    c = 0
    rval = vc.isOpened()
    
    # Iterating through frames
    while rval:
        # Spliting by frame
        c = c + 1
        rval, frame = vc.read()
        if rval:
            # Saving images
            cv2.imwrite(image_dir + str(c) + '.png', frame)
            cv2.waitKey(1)
        else:
            break
        
    # Releasing video
    vc.release()
    print('Converting into images is completed!')

video_path = 'C:/Users/rzhuo/Desktop/210117_c2.mpg'
image_dir = 'C:/Users/rzhuo/Desktop/lasco_c2/'

video2image(video_path, image_dir)
