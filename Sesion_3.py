##sesion 3 
##TIPOS DE DATOS

##ENTEROS (INT)

edad = 25
cantidad = 2
temperatura = -50


#flotantes (float)

precio = 10.5
pi = 3.1416
peso = 25.3
print(edad, cantidad, temperatura, precio, pi, peso)


## booleanos (bool)
requiere_incripcion = True
esta_lluvioso = False
print(requiere_incripcion, esta_lluvioso)

# tipe() nos permite conocer el tipo de dato de una variable
print(type(edad))
print(type(precio))
print(type(requiere_incripcion))
print(type(pi))
print(type(peso))

producto = input("Ingrese el nombre del producto: ")
cantidad = int(input("Ingrese la cantidad vendida: "))
precio = float(input("Ingrese el precio unitario: "))

total = cantidad * precio
print("producto: ", producto)
print("total: ", total)
