class WGS84Coord:
    def __init__(self, long=0, lati=0):
        self._longtitude = long
        self._latitude = lati
        
    def getlongitude(self):
        return self._longtitude
    
    def setlongitude(self, value):
        if -180 <= value <= 180:
            self._longtitude = value
        else:
            raise ValueError("Fehler code1: Longitude muss zwischen -180 und 180 liegen.")

    longitude = property(getlongitude, setlongitude)  

    def getlatitude(self):
        return self._latitude
    
    def setlatitude(self, value):
        if -90 <= value <= 90:
            self._latitude = value
        else:
            raise ValueError("Fehler code2: Latitude muss zwischen -90 und 90 liegen.")  

    latitude = property(getlatitude, setlatitude)  


k = WGS84Coord(700, 2)
print(k.longitude, k.latitude)
k.longitude = 15
k.latitude = 40 
print(k.longitude, k.latitude)
