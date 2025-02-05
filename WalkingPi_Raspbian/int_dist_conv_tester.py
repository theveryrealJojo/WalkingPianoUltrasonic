intFlt = float(input("Enter here the horizontal position of dMsr:"))
thresholdValue = float(input("Enter threshold value here (exp.: width of P-Keys in centimeters):"))

uQnotrounded = -1*(intFlt/thresholdValue - 15) #Hier beginnt es, absteigend, mit einem Wert von etwa 14 statt 1, da der Sensor auf der anderen Seite des Pianos liegt
uQrounded = int(uQnotrounded) #Genau gleich wie oben
print(uQrounded)
