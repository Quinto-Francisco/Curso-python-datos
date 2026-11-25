#sesion 5

# 1. Diccionarios de productos
producto1 = {"nombre": "Camiseta", "precio": 35000, "cantidad": 20, "categoria": "Ropa"}
producto2 = {"nombre": "Zapatos", "precio": 120000, "cantidad": 10, "categoria": "Calzado"}
producto3 = {"nombre": "Pantalón", "precio": 80000, "cantidad": 15, "categoria": "Ropa"}

# 2. Productos guardados en lista
inventario = [producto1, producto2, producto3]

# 3. Consultar el nombre de un producto
print("Nombre del primer producto:", inventario[0]["nombre"])

# 4. Modificar un precio y una cantidad
inventario[1]["precio"] = 110000
inventario[0]["cantidad"] = 25
print("Nuevo precio de", inventario[1]["nombre"], ":", inventario[1]["precio"])
print("Nueva cantidad de", inventario[0]["nombre"], ":", inventario[0]["cantidad"])

# 5. Conjunto de categorías únicas (el set elimina las repetidas)
categorias = set()
for producto in inventario:
    categorias.add(producto["categoria"])

print("Categorías únicas:", categorias)