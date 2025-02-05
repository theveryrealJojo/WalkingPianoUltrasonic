from gpiozero import DistanceSensor #Hier wird die Unterbibliothek für den US-Sensor importiert, um die Funktionen zur Distanzmessung verfügbar zu machen
import audio #Hier wird die Audiodatei ähnlich wie eine Bibliothek importiert
from time import sleep
thresholdValue = float(input("Input a threshold value here to determine the 'width' of the piano keys in centimeters: "))
ultrasonic2 = DistanceSensor(trigger=27, echo=22)*100 #Hier werden Echo und Trigger Ports für den zweiten US-Sensor festgelegt


def tone2read():
    while True:
        while ultrasonic2.distance <= thresholdValue * 15 and ultrasonic2.distance >= 1: #Genau gleich wie oben
            uQnotrounded = -1*(ultrasonic2.distance/thresholdValue - 15) #Hier beginnt es, absteigend, mit einem Wert von etwa 14 statt 1, da der Sensor auf der anderen Seite des Pianos liegt
            uQrounded = int(uQnotrounded) #Genau gleich wie oben
            audio.playSound(uQrounded) #Genau gleich wie oben
            sleep(0.1)

tone2read()  #Hier werden die Funktionen zum Starten des Pianos ausgeführt