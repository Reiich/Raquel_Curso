'''
POLIMORFISMO:

    un mismo objeto pueda cambiar de FORMA; es decir, pasar de ser 
    un coche a un camión.




'''

class Coche():
    
    def desplazamiento(self):
        print("Me desplazo utilizando cuatro ruedas")
        
class Moto():
    
    def desplazamiento(self):
        print("Me desplazo sobre dos ruedas")
    
class Camion():
    
    def desplazamiento(self):
        print("Me desplazo con seis ruedas")    

# creados tres clases distintas con el mismo método pero repsuestas distintas


############# como usar todos los objetos a la vez sin ir realizando un objeto para cada tipo de vehiculo
# creando una función que utlice el objeto que recibe por parámetro (vehiculo) para llamar al metodo Desplazamiento()

def desplazamientoVehiculo(vehiculo):   #va a usar la función desplazamientoVehiculo con cualquier
                                        #parámentro que venga desde fuera. ese parámetro será un objeto
    vehiculo.desplazamiento()


miCamion=Camion()
miCoche=Coche()
miMoto=Moto()
#llamo al método y le paso por parámetro el objeto mivehiculo. Que es de tipo camion

desplazamientoVehiculo(miCamion)

#de esta forma llama al Camion

desplazamientoVehiculo(miCoche)
desplazamientoVehiculo(miMoto)






    