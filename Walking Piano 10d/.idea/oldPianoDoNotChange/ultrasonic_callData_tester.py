from gpiozero import DistanceSensor
from time import sleep
ultrasonicCD = DistanceSensor(trigger=23, echo=24)

def readUSCD():
    while True:
        print(ultrasonicCD.distance)
        sleep(0.1)

readUSCD()

# https://www.instructables.com/Distance-Sensing-With-Raspberry-Pi-and-HC-SR04/