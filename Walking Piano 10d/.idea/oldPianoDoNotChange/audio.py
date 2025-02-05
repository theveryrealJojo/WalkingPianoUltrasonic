import pygame #Hier wird die PyGame Bibliothek importiert, um die Audiofunktionen verfügbar zu machen

path = "/home/User/Desktop/14SoundLib/"
soundFiles = [
"key01.wav",
"key02.wav",
"key03.wav",
"key04.wav",
"key05.wav",
"key06.wav",
"key07.wav",
"key08.wav",
"key09.wav",
"key10.wav",
"key11.wav",
"key12.wav",
"key13.wav",
"key14.wav"
]

pygame.mixer.init() #Audiowiedergabe wird eingeleitet

speakerV = float(input("Hier Wert für Lautstärke des Pianos zwischen 1.0 und 0.0 festlegen: ")) #Wert für Lautsprecherlautstärke wird festgelegt

pygame.mixer.music.set_volume(speakerV) #Lautsprecherlautstärkewert wird angewendet


def playSound(soundNr): #Methode zum Audio wiedergeben wird definiert - soundNr wird bei Anwendung durch Ultraschallsensoren angegeben

    
    pianoSound = pygame.mixer.music.load(path + soundFiles[soundNr-1]) #Hier wird der oben angegebene soundNr-Wert mit einer der 14 Audiodateien verknüpft und bei jedem Ausführen festgelegt
    pygame.mixer.music.play() #Audio wird abgespielt
    while pygame.mixer.music.get_busy() == True:
        continue #Lediglich eine Schleife, um das Geräusch des Pianos weiterlaufen zu lassen, bis es zu Ende ist





