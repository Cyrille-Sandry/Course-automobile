
import random

class Voiture:
    
    def __init__(self, modele,marque,vitesse_min,vitesse_max):
        if vitesse_min> vitesse_max:
           raise ValueError()
        self.__modele=modele
        self.__marque=marque
        self.__vitesse_min=vitesse_min
        self.__vitesse_max=vitesse_max
    @property
    def  modele(self):
         return self.__modele 
    @property
    def  marque(self):
         return self.__marque 
    @property
    def  vitesse_min(self):
         print("Vitesse minimum récupérée")
         return self.__vitesse_min 
        
    @vitesse_min.setter
    def vitesse_min(self,value):
        print("Vitesse minimum changée")
        if value <=self.__vitesse_max:
            self.__vitesse_min=value
    
    @property
    def  vitesse_max(self):
         print("Vitesse maximum récupérée")
         return self.__vitesse_max 
        
    @vitesse_min.setter
    def vitesse_min(self,value):
        print("Vitesse maximum changée")
        if value > self.__vitesse_min:
            self.__vitesse_max=value    
        
        
    def obtenir_vitesse(self):
        return random.randint(self.__vitesse_min,self.__vitesse_max)    
        
        
        
        
