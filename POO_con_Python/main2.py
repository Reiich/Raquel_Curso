'''
Created on 27 mar. 2020

@author: Raquel
'''
'''
Lecciones básicas. Aqií crearemos un CONSTRUCTOR DE LA CLASE Y DAREMOS UN PARAMETRO A UN METODO
PARA QUE CAMBIE SU ESTADE DE EN MARCHA  A PARADO (CON DOS COCHES DISTINTOS)
'''

class Coche(): 
    #LAS propiedades ahora las metermos en un CONSTRUCTOR.
    #Ya que es así como se hacen las cosas ¿como se define el estado inicial que tiene una clase?
    # con el constructor __init__ o inicial.
    # init, sería el estado de partida
    def __init__(self):   #es lo mismo que hacer un método. PEro que especifica el valor inicial del objeto de esa clase
        
        self.largoChasis=250
        self.anchoChasis=120
        self.ruedas=4
        self.enmarcha=False #for defecto los coches estarán detenidos
    

    def arrancar(self,arrancamos):  
        self.enmarcha = arrancamos #la variable enmarcha va a valer lo que le llegue al método
                                    # por el constructor arrancamos
        
        # y además, una vez, reciba su valor. Se comprueba si está o no en marcha
        if(self.enmarcha):     #la comprobación que hace python es si la propiedad es TRUE
            return "El coche está en marcha"
        else: 
            return "El coche está parado"
    
    def estado(self):
        print("El coche tiene ", self.ruedas, " ruedas. Y un largo de ", self.largoChasis)
    
miCoche = Coche()   
print("Las ruedas del coche son ", miCoche.ruedas)  #compuebo alguna de las propiedades así
print("EL coche tiene de largo ", miCoche.largoChasis) 
print(miCoche.arrancar(True))
miCoche.estado()
    
    
print("''''''''''''''A continuación creamos el segundo objeto ''''''''''''")

miCoche2=Coche()
print("Las ruedas del coche son ", miCoche2.ruedas)  #compuebo alguna de las propiedades así
print("EL coche tiene de largo ", miCoche2.largoChasis) 
print(miCoche.arrancar(False))
miCoche2.estado()




