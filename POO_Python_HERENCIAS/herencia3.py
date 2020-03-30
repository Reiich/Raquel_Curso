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



class VELelectricos():  #clase independiente que no hereda de vehiculos. SuperClase
    def __init__(self):
        self.autonomia=100
        
    def cargarEnergia(self):
        self.cargando=True

################


# creamos una clase que herede de dos SUPERCLASES. Vehículos y VELelectrico


class BicicletaElectrica(Vehiculos, VELelectricos):
    #de esta manera, hereda automaticamente los métodos y propiedades de AMBAS
    pass 




#comprobaciones con la clase bicicletaElectrica
#¿qué constructor? está heredando?
# pues hereda el __init__ o constructor, de la primera Class o superclase puesta al crear 
#la class bicicletaElectrica. En este caso Vehiculos, pero podría ser la otra sin problema.
miBici=BicicletaElectrica("orbea", "HC33")










