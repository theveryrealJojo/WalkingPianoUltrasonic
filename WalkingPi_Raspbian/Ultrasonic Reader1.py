from gpiozero import DistanceSensor #Hier wird die Unterbibliothek für den US-Sensor importiert, um die Funktionen zur Distanzmessung verfügbar zu machen
import audio #Hier wird die Audiodatei ähnlich wie eine Bibliothek importiert
from time import sleep
thresholdValue = float(input("Input a threshold value here to determine the 'width' of the piano keys in centimeters: "))
ultrasonic1 = DistanceSensor(trigger=4, echo=17)*100 #Hier werden Echo und Trigger Ports für den ersten US-Sensor festgelegt
# Hier Alternative zur Port-Abfrage: echo=int(input("Input the Echo-1 Port here: ")), trigger=int(input("Input the Trigger-1 Port here: "))

def tone1read():
    while True: #Einfache Schleife, um den Algorithmus permanent laufen zu lassen, solange das Gerät an ist
        while thresholdValue * 15 >= ultrasonic1.distance >= 1: #Aktiviert den Tonausgabe-Algorithmus nur, wenn sich das Objekt innerhalb des Tastaturbereichs befindet
            uQnotrounded = ultrasonic1.distance/thresholdValue #Legt einen ungefähren Wert für die Tonausgabe fest
            uQrounded = int(uQnotrounded) #Rundet den ungefähren Wert auf einen ganzzahligen Wert ab, der später den Ton aus dem Array wählt
            audio.playSound(uQrounded) #Führt die Funktion der Tonausgabe mit dem ganzzahligen Wert als Tonzuordnung aus
            sleep(0.5)

tone1read() #Hier werden die Funktionen zum Starten des Pianos ausgeführt
