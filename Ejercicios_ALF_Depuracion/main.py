'''
Created on 25 mar. 2020

@author: Raquel
'''
# Ejercicio 1
# Corregir los errores sintácticos del siguiente programa:

contrasena = input('Introduce la contraseña: ')

if contrasena in ['sesamo']:
  print('Pasa')
else:
  print('No pasa')
  
# Ejercicio 2
# Detectar y corregir los errores del siguiente programa que aplica el iva a una factura:


def aplica_iva(base, iva = 21):
    base = base + base * iva/100
    return base 

base = float(input('Introduce la base imponible de la factura: '))
print(aplica_iva(base))

# Ejercicio 3
# Detectar y corregir los errores del siguiente programa que calcula el producto escalar de dos vectores:
u = [1, 2, 3]
v = [4, 5, 6]

def producto_escalar(u, v):
    for i in range(len(u)):
        u[i] *= v[i]
    return sum(u)

print(producto_escalar(u, v))


# Ejercicio 4
# Detectar y corregir los errores del siguiente programa que devuelve 
# y elimina el teléfono de un listín telefónico a través del nombre del usuario:

listin = {'Juan':123456789, 'Pedro':987654321}

def elimina(listin, usuario):
    return listin.pop(usuario) #pop hace que devuelva el valor asociado al key
                                #y lo elimina

print(elimina(listin, 'Pedro'))
print(listin) #cumpruebo que se ha borrado


Ejercicio 5
Detectar y corregir los errores del siguiente programa que multiplica dos matrices:

a = ((1, 2, 3),
     (3, 2, 1))
b = ((1, 2),
     (3, 4),
     (5, 6))

def producto(a, b):
    producto = []
    for i in range(len(a)):
        fila = [] 
        for j in range(len(b[0])):
            suma = 0
            for k in range(len(a[0])):
                suma += a[i][k] * b[k][j]
            fila.append(suma)
        producto.append(tuple(fila))
    return tuple(producto)

print(producto(a, b))