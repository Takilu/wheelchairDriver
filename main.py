import cv2
import numpy as np
from tensorflow.keras.models import load_model

#import WebcamModule as wM
#import MotorModule as mM
import cv2
from picamera2 import Picamera2

piCam = Picamera2()

piCam.preview_configuration.main.size=(640,480)
piCam.preview_configuration.format="RGB888"
piCam.preview_configuration.align()
piCam.configure("preview")
piCam.start()

#######################################
steeringSen = 0.70  # Steering Sensitivity
maxThrottle = 0.22  # Forward Speed %
#motor = mM.Motor(2, 3, 4, 17, 22, 27) # Pin Numbers


class Model:
    def __init__(self):
        self.mod = load_model('saved_model.h5')
######################################

    def preProcess(self, img):
        self.img = self.img[54:120, :, :]
        self.img = cv2.cvtColor(self.img, cv2.COLOR_RGB2YUV)
        self.img = cv2.GaussianBlur(self.img, (3, 3), 0)
        self.img = cv2.resize(self.img, (200, 66))
        self.img = self.img / 255
        return self.img


    def getImg(self, display=True, size=[480, 240]):
        while True:
            frame = piCam.capture_array()
            frame = cv2.resize(frame, (size[0], size[1]))
            if display:
                cv2.imshow('img', frame)
            return frame
            cv2.destroyAllWindows()


while True:
    model = Model()
    img = model.getImg(True, size=[240, 120])
    img = np.asarray(img)
    img = model.preProcess(img)
    img = np.array([img])
    steering = float(model.mod.predict(img))
    print(steering*steeringSen)
    motor.move(maxThrottle,-steering*steeringSen)
