import numpy as np
from tensorflow.keras.models import load_model

#import WebcamModule as wM
#import MotorModule as mM

#######################################
steeringSen = 0.70  # Steering Sensitivity
maxThrottle = 0.22  # Forward Speed %
#motor = mM.Motor(2, 3, 4, 17, 22, 27) # Pin Numbers
model = load_model('saved_model.h5')
print("model is loaded")

######################################

#model = load_model(('/home/pi/Desktop/model_test/model.h5'), custom_objects={'KerasLayer':hub.KerasLayer})

