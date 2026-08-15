# Definición de la clase Producto que representará cada celular en el sistema
class Producto:
    # El método __init__ es el constructor que inicializa los datos de cada celular al crearlo
    def __init__(self, marca: str, modelo: str, precio: float, cantidad: int, imei: str = "", proveedor: str = ""):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.cantidad = cantidad
        self.imei = imei
        self.proveedor = proveedor
    
    # Método para registrar la venta de un producto, reduciendo su cantidad en el inventario
    def vender(self, cantidad: int) -> bool:
        # Verifica si hay suficientes equipos en stock antes de vender
        if cantidad <= self.cantidad:
            self.cantidad -= cantidad # Resta la cantidad vendida
            return True # Venta exitosa
        return False # Venta fallida por falta de stock
    
    # Método para aumentar la cantidad de productos en el inventario (reabastecer)
    def reabastecer(self, cantidad: int) -> None:
        self.cantidad += cantidad
    
    # @property permite usar esta función como si fuera una variable (ej. producto.disponible)
    @property
    def disponible(self) -> bool:
        # Retorna True (verdadero) si hay al menos 1 unidad, y False (falso) si es 0
        return self.cantidad > 0
    
    # __str__ define cómo se mostrará el objeto cuando se imprima en pantalla (ej. print(producto))
    def __str__(self) -> str:
        return f"{self.marca} {self.modelo} - ${self.precio:.2f} - Stock: {self.cantidad}"


# Sistema Stock Móvil con POO adaptado al ejemplo
# Lista global que funcionará como nuestra base de datos para guardar los celulares
inventario = []

# Función para registrar un nuevo celular en el sistema
def agregar_celular():
    # Solicitamos los datos del equipo al usuario
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))
    imei = input("IMEI (opcional): ")
    proveedor = input("Proveedor (opcional): ")
    
    # Creamos una nueva instancia (objeto) de la clase Producto con los datos ingresados
    celular = Producto(marca=marca, modelo=modelo, precio=precio, cantidad=cantidad, imei=imei, proveedor=proveedor)
    # Añadimos el nuevo celular a la lista del inventario
    inventario.append(celular)
    print("Celular agregado.\n")

# Función para listar todos los celulares registrados
def mostrar_inventario():
    # Validamos si la lista está vacía
    if not inventario:
        print("Inventario vacío.\n")
        return
    # Recorremos la lista y mostramos cada producto. 'enumerate' nos da el índice automático (i)
    for i, c in enumerate(inventario):
        print(f"{i+1}. {c}") # i+1 se usa para que la lista empiece en 1 y no en 0
    print()

# Función para gestionar la venta de un celular existente
def vender_celular():
    mostrar_inventario() # Mostramos las opciones disponibles al usuario
    if not inventario:
        return # Si no hay nada, salimos de la función
    
    # Pedimos el número del celular y restamos 1 porque las listas en Python empiezan en la posición 0
    idx = int(input("Número del celular a vender: ")) - 1
    
    # Verificamos que el número ingresado sea válido (que exista dentro de la lista)
    if 0 <= idx < len(inventario):
        cantidad_a_vender = int(input("Cantidad a vender: "))
        # Intentamos realizar la venta llamando al método 'vender' del objeto seleccionado
        if inventario[idx].vender(cantidad_a_vender):
            print("Venta realizada.\n")
        else:
            print("Sin stock suficiente.\n")
    else:
        print("Selección inválida.\n")

# Función para identificar qué productos están por agotarse
def stock_bajo(limite=3):
    print(f"Celulares con stock menor o igual a {limite}:")
    # Filtramos la lista creando una nueva solo con los celulares cuya cantidad sea menor o igual al límite
    filtrados = [c for c in inventario if c.cantidad <= limite]
    
    # Si la lista filtrada está vacía, significa que todo tiene buen stock
    if not filtrados:
        print("No hay productos con stock bajo.\n")
        return
    # Mostramos los productos que necesitan atención
    for c in filtrados:
        print(f"- {c}")
    print()

# Función principal que muestra el menú interactivo al usuario
def menu():
    # Bucle infinito para mantener el programa en ejecución hasta que se elija salir
    while True:
        print("1. Agregar celular")
        print("2. Mostrar inventario")
        print("3. Vender celular")
        print("4. Ver stock bajo")
        print("5. Salir")
        opcion = input("Elige una opción: ")
        
        # Evaluamos la opción elegida por el usuario y ejecutamos la función correspondiente
        if opcion == "1":
            agregar_celular()
        elif opcion == "2":
            mostrar_inventario()
        elif opcion == "3":
            vender_celular()
        elif opcion == "4":
            stock_bajo()
        elif opcion == "5":
            break # 'break' rompe el bucle infinito y cierra el programa
        else:
            print("Opción inválida.\n")

# Punto de entrada del script: asegura que el menú solo se ejecute si este archivo se corre directamente
if __name__ == "__main__":
    menu()
    
    #Ricardo Jose Acuna Espinoza
    #Jose Angel Borja Medrano
    #Justin Geovanny Scott Oporta
