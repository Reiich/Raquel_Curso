'''
esto será TEORIA para después usarlo con el archivo Herencia4

    super() : permite ir a esa parte de código de la clase padre y traerlo al lugar desde donde lo llamo

###### isinstance()

principio de sustitucion: es siempre un/una
     Un empleado, es siempre una persona. Antes que empleados somos personas.
     Pero una persona, no siempre es un empleado. (podría ser desempleado, o autónomo)
 
 isinstance() nos informa si un objeto es una instancia a una clase determinada
     será util cuando los programas sean complejos y no sepamos si un objeto pertenece a una clase o no
     
    devuelve True o False
 
'''

class Persona():
    
    def __init__(self, nombre, edad, Lugar_residencia):
       
        self.nombre=nombre
        self.edad=edad
        self.lugar_residencia=Lugar_residencia
        
    def descripcion(self):
        
        print("Nombre: ", self.nombre, "\nEdad: " , self.edad, "\nResidencia : " + self.lugar_residencia)
        
        
class Empleado(Persona):    # EMPLEADO VA A HEREDAD de PErsona, porque un empleado tb es persona
    
    def __init__(self, salario, antigüedad, nombre_empleado, edad_empleado, residencia_empleado):
        
        super().__init__(nombre_empleado, edad_empleado, residencia_empleado) # voy al INIT de la clase Padre y añado desde aquí, otros tres valores
        self.salario=salario
        self.antig=antigüedad
        
    def descripcion(self):
        
         super().descripcion() #al ponerr super, irá primero a la de la clase padre, ejecuta el print completo
         #y después imprime la línea propia del estado descripcion propipo de Empleado. Así te ahorras volver a escribir todo
         print("Salario : " , self.salario,"\nAntigüedad :", self.antig)
        
        
    #y además de los constructores de persona, tb tendrá salario y anttigüedad. 
    #es decir, no sobrescribe los constructorees de la clase persona, sino que añade
    # otros más. En total. El empleado tiene 5 constructores.
    # además, de también heredar los métodos que pudieran existir en la clase persona


##### comprobemos
#### creando un objeto

#antonio=Persona("Antonio", 55, "Sevilla")    
#antonio.descripcion()

#esto funciona

########################


#esto da error, porque no reconoce, nombre,ni edad,ni lugar de residencia
#porque empleado debería tener 5 parámetros

manuel=Empleado(1100, 8, "Manuel", 38, "Madrid")
manuel.descripcion()


#como se soluciona?
#creando dentro de la clase Empleado, en su constructor __init__ un 
# super()
# super() llama al metodo init de la clase padre


# probemos isinstance()
  
print(isinstance(manuel, Empleado)) #manuel es de la clase empleado?
print("Es manuel Persona?"isinstance(manuel, Persona))
# esto devuelve TRUE.


#si cambiamos que manuel, sea de la clase persona
manuel=Persona("Manuel", 38, "Madrid")
print("Es manuel empleado?" + isinstance(manuel, Empleado))
    #y le pregunto si es empleado, da FALSE. Porque que sea persona no quiere decir que sea empleado
        