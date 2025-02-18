import RPi.GPIO as GPIO
import time
import audio
GPIO.setmode(GPIO.BOARD)

TRIG = 23
ECHO = 24

pulse_end = 0.0
pulse_start = 0.0
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

thresholdv = int(input("Hier Breite der Tasten in cm angeben, um Schwellenwert zu bestimmen"))
GPIO.output(TRIG, False)
print("Kalibriert...")
time.sleep(2)

try:
    while True:
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO) == 0:
            pulse_start = time.time()

        while GPIO.input(ECHO) == 1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start

        distance = pulse_duration * 17150 #Centimeter, die Schall in der Sekunde zurücklegt durch 2 geteilt, da hin und zurück



        if thresholdv*15 >= distance >= 0:
            print(distance)
            audioquot = distance/thresholdv
            audiov = int(audioquot)
            if audiov < 14 or audiov > 1:
                print("Außerhalb der Tastatur! Bitte erneut starten und gültigen Schwellwert angeben!")

            else:
                audio(audiov)

        else:
            print("Außer Reichweite!")

        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()