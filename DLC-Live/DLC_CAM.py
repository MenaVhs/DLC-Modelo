# Artículo: https://www.eneuro.org/content/7/3/ENEURO.0096-20.2020

import os
import cv2
import numpy as np
# import json
import pandas as pd
# import deeplabcut
import tensorflow as tf
from dlclive import DLCLive, Processor
from dlclive import benchmark_videos
from time import sleep


cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FPS, 60)
img_counter = 0
start_tick = cv2.getTickCount()

dlc_model_path = 'D:\DLC\CV-Mena-2023-02-26\exported-models\DLC_CV_resnet_50_iteration-0_shuffle-1'

if not (cam.isOpened()):
    print("Couldn't find camera")

def getFrame():
    frame_count = 0
    ret, frame = cam.read()
    scale_percent = 60
    width = int(frame.shape[1] * scale_percent / 100)
    height = int(frame.shape[0] * scale_percent / 100)
    dimentions = (width, height)

    # Resize frame
    # frame = cv2.resize(frame, dimentions, interpolation= cv2.INTER_AREA)

    # print(frame.shape)
    # original size: (480, 640, 3)
    # pruebas con: 300 x 533 -> 98 +- 5 aprox

    if ret:
        frame_count += 1
            
    # Get FPS
    fps = cv2.getTickFrequency() / (cv2.getTickCount() - start_tick)
    print("FPS: ", int(fps))

    if not ret:
        print("FAILED CAPTURE!")
        exit(0)
        
    return frame


dlc_proc = Processor()

# export_path = input("Enter exported model path:")
# #export_path = deeplabcut.export_model(path, iteration=None, shuffle=1, trainingsetindex=0, snapshotindex=None, TFGPUinference=True, overwrite=False, make_tar=True)
# print("file exists?", os.path.exists(export_path)) #make sure export_path exists
dlc_live = DLCLive(dlc_model_path, display=True, model_type='base', resize=0.75)


while(cam.isOpened()):
# Capture the video frame by frame
    frame = getFrame()  

# Display the resulting frame
    dlc_live.init_inference(frame)
    pose = dlc_live.get_pose(frame)
    print(pose)

    if (cv2.waitKey(20) & 0xFF == ord('s')):
        break


cam.release()
cv2.destroyAllWindows
