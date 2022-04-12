class circuit:
    
    def __init__(self,nom,distance):
        self.__nom=nom
        self.__distance=distance
        
    @property
    def nom(self):
        return self.__nom
    @property
    def distance(self):
        return self.__distance
    @distance.getter
    def distance(self,value):
        self.__distance=value
        
    def __str__(self):
        return f"Circuit - {self.nom} - {self.distance} "        
    
    def __repr__(self):
        return f"Circuit - {self.nom} - {self.distance} "