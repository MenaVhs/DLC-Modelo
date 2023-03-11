# Tutorial seguido de DLC-live
from dlclive import DLCLive, Processor
import cv2 as cv
camera_id = 0
camera_resolution = (640, 480)
dlc_proc = Processor()
dlc_model_path = 'D:\DLC\CV-Mena-2023-02-26\exported-models\DLC_CV_resnet_50_iteration-0_shuffle-1'

# Connecting to a Webcam 
capture = cv.VideoCapture(camera_id)
def getFrame(): 
    # Lecture 
    while (capture.isOpened()):
        ret, frame = capture.read()
        if (ret == True): 
            cv.imshow('WebCam', frame)
            if(cv.waitKey(20) == ord('s')): # cambiar el valor de waitkey, mayor, más lento
                break

        return(frame)
    

capture.release()
cv.destroyAllWindows

config_path = 'D:\DLC\CV-Mena-2023-02-26\config.yaml'
dlc_proc = Processor()
dlc_live = DLCLive(dlc_model_path, processor=dlc_proc)

inferences = list()
frameDLC = getFrame()
cv.imwrite('savedImage.jpg', frameDLC)
capture.release()
dlc_live.process_frame(frameDLC)
dlc_live.init_inference(frameDLC)



# Código 2
# https://learnopencv.com/read-write-and-display-a-video-using-opencv-cpp-python/
# https://gist.github.com/dsalaj/b9143289784fbd7f741518301e6037ce
# https://medium.com/analytics-vidhya/how-to-convert-tensorflow-object-detection-csv-data-to-coco-json-format-d0693d5b2f75
