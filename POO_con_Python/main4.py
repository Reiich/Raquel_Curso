'''
Encapsular un método.
Qué utilidad tiene que pueda acceder desde la propia clase. 
pero no desde fuera? Para qué quisiera encapsular el método?

Vamos a realizar una función chequeo() que pueda comprobar
si el coche es apto para arranncar porque todo es correcto. Y permita arrancar.

¿pero qué sentido tendría comprobar o hacer chequeo() en un coche parado?
De este modo, y para eso. Lo encapsulamos. PAra que no pueda usarse un método desde
fuera si no siempre desde lo definido dentro de la clase, y sólo cuando se cumplen
las condiciones puestas. PARA ESO SIRVE ENCAPSULAR UN METODO

La forma es:  __chequeo()
'''



class Coche(): 

    def __init__(self):   
        self.__largoChasis=250
        self.__anchoChasis=120
        self.__ruedas=4  #propiedad ENCAPSULADA o PROTEGIDA 
        self.__enmarcha=False 
    
    # IMPORTANTE: la variable __enmarcha, aunque sea una propiedad dinámica que va cambiando
    #de valor, se puede proteger también para que no sea modificada desde fuera.
    #ya que, el valor si cambia o no, viene dado desde el método (arrancar) 
    #es decir, que está variando desde dentro de la CLASE, y no  desde fuera.
    
    

    def arrancar(self,arrancamos):  
        self.__enmarcha = arrancamos #el valor de entrada que le venga dado desde fuera, será el que tomará __enmarcha, que podrá ser TRUE o FALSE
        
        if(self.__enmarcha):        #si self __enmarcha es True (como no pone nada)
            chequeo=self.__chequeo()  #llama al método chequeo interno, que a suver devuelve el mensaje, que comprueba si todo es correcto          
                            #chequeo, es una variable,que va a devolver un valor, gracias al  RETURN. Una vez devuelto ese valor
        # ... realiza con el valor recibido las siguientes comprobaciones
        if(self.__enmarcha and chequeo):  #si es true y chequeo tb es true
            return "El coche está en marcha"
        
        elif(self.__enmarcha and chequeo==False):  #comprueba si el coche ha intentado arrancar, pero algo ha fallado en el chequeo. Y no se cumplent las condiciones de que todo sea correcto
            return "Algo ha ido mal en el chequeo, no puede arrancar"
                    
        else: 
            return "El coche está parado"
    
    def estado(self):
        print("El coche tiene ", self.__ruedas, " ruedas. Y un largo de ", self.__largoChasis)
            #recuerda que al traer el dafo que almacena la propiedad, también debe llevar esos dos guiones

    def __chequeo(self):
        print("---- Realizando chequeo interno ----")
        
        self.gasolina="ok"
        self.aceite="mal"
        self.puertas="cerradas"
        #como los parámetros anteriores los vario manualmente para comprobar...
        if self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas":
            return True
        else:
            return False
            





miCoche = Coche()   
print(miCoche.arrancar(True))
miCoche.estado()
    
    
print("''''''''''''''A continuación creamos el segundo objeto ''''''''''''")

miCoche2=Coche()
print(miCoche.arrancar(False))
miCoche2.estado()




