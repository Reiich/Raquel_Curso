'''
sobrescritura de métodos
    una ver creada la clase superclase. Podemos MODIFICAR O AÑADIR
    NUEVAS PARTICULARIDADES A LA CLASE QUE ESTÁ HERENDANDO (la de segundo nivel)

Herencia SImple y múltiple

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


# Creamos clases con herencia. Otros vehiculos.

class Furgoneta(Vehiculos):

    def carga(self, cargar): # el valor cargar viene desde fuera como True o False
        self.cargado=cargar     #self.cargado obtendrá el valor dado desde fuera en el parámetro
        if(self.cargado):               #si es TRUE
            return "La furgoneta está cargada"
        else:                           #si es FALSE
            return "La furgoneta va vacía"



class Moto(Vehiculos):  #así es como se dice que Moto hereda de vehiculos
    caballito="" #creo una variable vacía. Que obtendrá un valor  al realizar el método caballito()


    def caballito(self): # creo un método propio de la clase moto, que no comparte con las demás
        self.caballito="Estoy circulanto sobre la rueda trasera! yipiyipiyeh!"

    def estado(self):  #tendremos que sobrescribir, el método Estado de la clase Padre, para que éste Estado, muestra si la moto hace o no el caballito
        # Porque no tiene sentido que demos la info. de caballito en la clase padre, ya que sólo las motos pueden hacerlo
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", self.enmarcha,
            "\nAcelera: ", self.acelera, "\nFrena: ", self.frena, "\nCaballito: ", self.caballito)


class Quad(Moto):  #creo una clase, que además hereda a su vez de una clase de nivel 2
    pass   #el estado que hereda realmente es el de Moto, y no la de veicuo, porque es la más inmediata o cercana



################
# lee en orden, hace abajo
 #1) creo el objeto mimoto y doy valores de marca y modelo
mimoto=Moto("macbor", "eightmile")

#2 Ejecuto el método caballito
mimoto.caballito()

#3. pido información sobre el estado
mimoto.estado()  # al tener su porpio estado, la clase Moto. Siempre la clase de segundo nivel, tiene prevalencia
#porque sobrescribe



#comprobaciones con la clase Furgoneta
miFurgoneta=Furgoneta("Renault", "kangoo")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))










