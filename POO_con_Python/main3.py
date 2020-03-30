'''
Lecciones básicas. Aquí  MODIFICAMOS LAS PROPIEDAD DE UN OBJETO.
SE PUEDE MODIFICAR LA PROPIEDAD QUE VIENE DADA  POR UNA CLASE.

también veremos la ENCAPSULACIÓN. Para proteger una propiedad y no pueda así
modificarse "fuera" de la clase. SI NO QUIERO QUE pueda variarse,porque queremos ser
que las propiedades sean rígidas.
Sí será accesible desde dentro de la propia clase (modificando en __ini__)
Cómo? poniendo __ruedas (es decir, dos guines bajos a la propiedad)
así ese dato queda protegido y no podrá ser modificado.
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
        self.enmarcha = arrancamos 
        
        if(self.enmarcha):
            return "El coche está en marcha"
        else: 
            return "El coche está parado"
    
    def estado(self):
        print("El coche tiene ", self.__ruedas, " ruedas. Y un largo de ", self.__largoChasis)
            #recuerda que al traer el dafo que almacena la propiedad, también debe llevar esos dos guiones
miCoche = Coche()   
print(miCoche.arrancar(True))

miCoche.ruedas=2  #simplemente SE MODIFICA,asignado un nuevo valor a esa propiedad
miCoche.estado()
    
    
print("''''''''''''''A continuación creamos el segundo objeto ''''''''''''")

miCoche2=Coche()
print(miCoche.arrancar(False))
miCoche2.estado()




