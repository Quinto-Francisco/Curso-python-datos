# ####  sesion 2 ###
# comentario 1
# comentario 2

print("hello word")

print ("bienvenido al programa de bienvenida")

### preguntar al usuario su Nombre
Nombre = input("por favor, Ingrese su nombre: ")
print(f"¡Hola, {Nombre}! Bienvenido al programa de bienvenida.")

#### concatenar el nombre con un mensaje de bienvenida
nombre = input("Por favor, ingrese su nombre: ")
mensaje_bienvenida = f"¡Hola, {nombre}! Bienvenido al programa de bienvenida."
print(mensaje_bienvenida)

# Variables
edad = input("Por favor, ingrese su edad: ")
print("su edad es: ", edad)

# Expreciones y combinar valores
edad = int(edad)
edad = edad / 2
print("su edad dividida entre 2 es: ", edad)  


## registrar venta

producto = input("Ingrese el nombre del producto: ")
cantidad = input("Ingrese la cantidad vendida: ")  
precio = input("Ingrese el precio del producto: ")
datos = f"Producto: {producto}, Cantidad: {cantidad}, Precio: {precio}"
print("Datos de la venta:", datos)
total = int(cantidad) * float(precio)
print("El total de la venta es: ", total)
