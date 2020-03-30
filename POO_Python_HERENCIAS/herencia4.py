'''
Funcion super() y Funcion isinstance()


'''

'''
Herencia SImple y múltiple

creo la clase que no hereda de ninguna otra, uqe es VELelectrico()
y otra de BicicletaElectrica


de esta manera, la BicicletaElectrica OBTENDRÁ HERENCIA MULTIPLE
ES DECIR, obtiene valores de vehiculo y también de VELelectrico
porque comparte propiedades de ambos.

herencia multiple. LO acepta Python, pero NO TODOS los lenguajes de programación
acepta la her.multiple porque puede acabar siendo todo muy complejo.

'''


#superclase

class Vehiculos():
    def __init__(self, marca,modelo):
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



class VELelectricos(Vehiculos):  #clase independiente que no hereda de vehiculos. SuperClase
    def __init__(self, marca, modelo):  #vehíuclo ELectrico tmb va a pedirme marca y modelo
        
        super().__init__(marca, modelo)
        
        self.autonomia=100
        
    def cargarEnergia(self):
        self.cargando=True

################


# creamos una clase que herede de dos SUPERCLASES. Vehículos y VELelectrico


class BicicletaElectrica(VELelectricos, Vehiculos ): #de esta manera, recoge __init__ de la que está más a la izq.
    pass 



#miBici=BicicletaElectrica("orbea", "HC33")

# si BicicletaElectrica, recoge los constructores __init__ de VELelectricos
#y yo le doy la marca y el modelo. Da error. ¿por qué? porque los VELeelectricos sólo
# reciben un parámetro, que es la autonomía. 


#¿cómo puedo hacerle para que mi bicicletaELectrica reciba entonces, una marca y modelo?



