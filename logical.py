temperatur = int(input("Was ist heute das wetter"))

if (temperatur >=0 and temperatur <=30):
    print("Die Temperatur ist gut")
    print("Geh draussen")
elif(temperatur <0 or temperatur > 30):
    print("Die Temperatur ist schlecht heute")
    print("Bleib Hause")
