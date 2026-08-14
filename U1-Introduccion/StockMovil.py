class Producto:
    def __init__(self, marca: str, modelo: str, precio: float, cantidad: int, imei: str = "", proveedor: str = ""):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.cantidad = cantidad
        self.imei = imei
        self.proveedor = proveedor
    
    def vender(self, cantidad: int) -> bool:
        if cantidad <= self.cantidad:
            self.cantidad -= cantidad
            return True
        return False
    
    def reabastecer(self, cantidad: int) -> None:
        self.cantidad += cantidad
    
    @property
    def disponible(self) -> bool:
        return self.cantidad > 0
    
    def __str__(self) -> str:
        return f"{self.marca} {self.modelo} - ${self.precio:.2f} - Stock: {self.cantidad}"


# Sistema Stock Móvil con POO adaptado al ejemplo[cite: 1]
inventario = []

def agregar_celular():
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))
    imei = input("IMEI (opcional): ")
    proveedor = input("Proveedor (opcional): ")
    
    celular = Producto(marca=marca, modelo=modelo, precio=precio, cantidad=cantidad, imei=imei, proveedor=proveedor)
    inventario.append(celular)
    print("Celular agregado.\n")

def mostrar_inventario():
    if not inventario:
        print("Inventario vacío.\n")
        return
    for i, c in enumerate(inventario):
        print(f"{i+1}. {c}")
    print()

def vender_celular():
    mostrar_inventario()
    if not inventario:
        return
    idx = int(input("Número del celular a vender: ")) - 1
    if 0 <= idx < len(inventario):
        cantidad_a_vender = int(input("Cantidad a vender: "))
        if inventario[idx].vender(cantidad_a_vender):
            print("Venta realizada.\n")
        else:
            print("Sin stock suficiente.\n")
    else:
        print("Selección inválida.\n")

def stock_bajo(limite=3):
    print(f"Celulares con stock menor o igual a {limite}:")
    filtrados = [c for c in inventario if c.cantidad <= limite]
    if not filtrados:
        print("No hay productos con stock bajo.\n")
        return
    for c in filtrados:
        print(f"- {c}")
    print()

def menu():
    while True:
        print("1. Agregar celular")
        print("2. Mostrar inventario")
        print("3. Vender celular")
        print("4. Ver stock bajo")
        print("5. Salir")
        opcion = input("Elige una opción: ")
        if opcion == "1":
            agregar_celular()
        elif opcion == "2":
            mostrar_inventario()
        elif opcion == "3":
            vender_celular()
        elif opcion == "4":
            stock_bajo()
        elif opcion == "5":
            break
        else:
            print("Opción inválida.\n")

if __name__ == "__main__":
    menu()
    
    #ricardo jose Acuna espinoza
    #jose Angel Vorja
    #justin geobani Scott oporta
    