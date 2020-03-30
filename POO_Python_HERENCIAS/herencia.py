'''
herencia
    SE CREA UNA CLASE PADRE O SUPERCLASE, común a todas las clases 
    subordinadas. Así ahorraremos lineas de código.
    
    La superclase englobado todas las caracteristcas comunes al resto de objetos
    que se van a crear.
'''


#superclase

class Vehiculos():
    def __init__(self, marca,modelo):  #constructor con las propiedades originales
                            # obligatorio que desde fuera se le den dos parámetros. "marca", "modelo"
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False
        
        
    def arrancar(self):
        self.enmarcha=True
        
    def acelerar(self):        
        self.acelera= True
        
    def frenar(self):        
        self.frena=True
        
    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", self.enmarcha,
            "\nAcelera: ", self.acelera, "\nFrena: ", self.frena)
        
##### fin de la superclase ######


# Creamos clases con herencia. Otros vehiculos.

class Moto(Vehiculos):  #así es como se dice que Moto hereda de vehiculos
    pass

################

mimoto=Moto("macbor", "eightmile")

mimoto.estado()
        
#si creamos una objeto con las propiedades de  la clase Moto
# y después instanciamos que nos muestre su estado
#comprobaremos que muestra las de la Clase Vehiculo (__init__)
#y  que no hemos necesitado picar ningún código
#en la clase Moto. De eso se trata la herencia
        
        
        
        
        
        
        
        

