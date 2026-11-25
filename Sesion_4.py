##sesion 4
## consultar cadenas de texto

producto = "monitor"
print(producto [0]) #m
print(producto [1]) #o
print(producto [2]) #n
print(producto [3]) #i
print(producto [4]) #t
print(producto [5]) #o
print(producto [6]) #r



##f strings construir mensajes con varibles
print(f"el producto es: {producto}") #el producto es: monitor

#posiciones positivas y negativas

print(producto[6]) #r
print(producto[-1]) #o
print(producto[0]) #m

#extraer partes de la cadena de texto

print(producto[0:3]) #mon
print(producto[3:6]) #it
print(producto[2:]) #mon

#longitud de la cadena de texto

producto = "memoria ram 16gb"
longitud = len(producto)
print(f"la longitud de la cadena de texto es: {longitud}")


