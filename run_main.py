import numpy as np
from MotorModule import Motor
from ultrasonic import Ultrasonic

from main import Model

if __name__ == '__main__':

    motor = Motor(23, 24, 25, 17, 27, 22)
    ultrasonic = Ultrasonic(26, 16)

    while True:
        """v= input()
        if v== "s":
            motor.stop()
            break"""
        try:
            steeringSen = 0.70  # Steering Sensitivity
            maxThrottle = 0.22
            model = Model()
            img = model.getImg(True, size=[240, 120])
            img = np.asarray(img)
            img = model.preProcess(img)
            img = np.array([img])
            steering = float(model.mod.predict(img))
            print(steering * steeringSen)
            motor.move(maxThrottle, -steering * steeringSen)
        except:
            try:
                joyVal = jsM.getJS()
                # print(joyVal)
                steering = joyVal['axis1']
                throttle = joyVal['o'] * maxThrottle
                # if joyVal['share'] == 1:
                #     if record == 0: print('Recording Started ...')
                #     record += 1
                #     sleep(0.300)

                motor.move(throttle, -steering)
                cv2.waitKey(1)
            except:
                if ultrasonic.distance() > 50:
                    motor.move(0.6)
                else:
                    motor.move(0.6, -0.6)
                print(ultrasonic.distance())
