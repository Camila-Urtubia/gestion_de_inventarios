inventario = {}
productos = []
ciclo = 0
vuelta = 10



def agregar_producto():
  print()
  nombre = input("Ingrese el nombre del producto: ")
  cant = int(input("Ingrese la cantidad del producto: "))
  precio = int(input("Ingrese el precio del producto: "))
  print()

  inventario = {
      "ID": vuelta,
      "Nombre del Producto": nombre,
      "Cantidad": cant,
      "Precio": precio
  }

  productos.append(inventario)
  print(f"Producto {nombre} agregado con éxito!")

def listar_inventario():
  for i in productos:
    print("_______________________")
    for clave, valor in i.items():
      print(f"{clave}: {valor}")

#def buscar_producto():
#  nom = str(input("Nombre: "))
#  for i in productos:
#    for clave in i.items():
#      print(clave)

#def archivo():
#  with open ("inventario.csv", mode ="a", newline = "") as lista_csv:
#    lista_csv.write()

#def leer():
# with open ("inventario.csv", mode ="r", newline = "") as lista_csv:
#    lista_csv.read()

while True:
  print("Seleccione la aciión que desea realizar: ")
  print("1. Agregar productos")
  print("2. Listar Inventario.")
  print("3. Salir")
  op = int(input())

  if op == 1:
    agregar_producto()
    ciclo += 10
  if op == 2:
    listar_inventario()
  if op == 3:
    break