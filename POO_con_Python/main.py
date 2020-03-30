'''
Lecciones básicas. Desde 0
'''
#las clases van en mayúscula
class Coche(): 
    #creamos las propiedades COMUNES a la clase Coche
    largoChasis=250
    anchoChasis=120
    ruedas=4
    enmarcha=False #for defecto los coches estarán detenidos
    
    # para establecer los comportamientos de un coche. Se crean FUNCIONES o métodos
    # también dentro de la clase. Un método es una función especial de una clase. 
    #En cambio las funciones, son globales,puede reutilizar.#
    # El Método es sólo propio de la clase en la que ha sido creado
    #como es propio de una clase. Siempre lleva el PARÁMETRO SELF
    # SELF, hace referencia al PROPIO OBJETO perteneciente a la clase
    
    
                #self se escribe por defecto pero no es un parámetro obligatorio .
    def arrancar(self):  
        self.enmarcha=True  #python obliga a especificar el SELF, con la nomenclatura del punto
    
    def estado(self):
        if(self.enmarcha):     #la comprobación que hace python es si la propiedad es TRUE
            return "El coche está en marcha"
        else:
            return "El coche está parado"
    
    
#¿cómo CREO UN OBJETO? pues lo instancio o ejemplarizo.
# una variable llamada miCoche, le indico que ese OBJETO va a pertenecer a la clase
# Coche(). Es decir, que de entrada ya le he dado unas caracteristicas.
 
miCoche = Coche()   
print(miCoche.ruedas)  #compuebo alguna de las propiedades así
print("EL coche tiene de largo ", miCoche.largoChasis) 

#arranco el coche y cambia el valor enmarcha a True
miCoche.arrancar()

#me devuelve el resultado de si el coche llegó a arrancar o no.
print(miCoche.estado())
    
    
print("''''''''''''''A continuación creamos el segundo objeto ''''''''''''")
