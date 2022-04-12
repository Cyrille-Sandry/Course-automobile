



class concurent:
    
    def __init__(self, nom, numero, voiture):
        self.__nom=nom
        self.__numero=numero
        self.__voiture=voiture
        self.__temps=list()
        self.__vitesse=[]
        
    @property
    def nom(self):
        return self.__nom  
    
    
    @property
    def numero(self):
        return self.__numero
    
    @property
    def voiture(self,value):
        self.__voiture=value
    
     
    @property
    def vitesses(self):
        return tuple(self.__vitesse)
     
     
        
    @property
    def temps_total(self):
        return sum(self.__temps) 
    
     
        