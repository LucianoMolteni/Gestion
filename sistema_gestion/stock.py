import csv
import os


class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = float(precio)
        self.cantidad = int(cantidad)

    def hay_stock(self):
        return self.cantidad > 0

    def actualizar_stock(self, cantidad_vendida):
        if self.cantidad >= cantidad_vendida:
            self.cantidad -= cantidad_vendida
            return True
        return False


lista_productos = []
RUTA_STOCK = "stock_actual.csv"


def registrar_producto(nombre, precio, cantidad):
    nuevo_p = Producto(nombre, precio, cantidad)
    lista_productos.append(nuevo_p)


def guardar_stock():
    with open(RUTA_STOCK, mode="w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["Nombre", "Precio", "Cantidad"])
        for p in lista_productos:
            escritor.writerow([p.nombre, p.precio, p.cantidad])
    print(f"💾 Stock guardado en {RUTA_STOCK}")


def cargar_stock():
    lista_productos.clear()
    if not os.path.exists(RUTA_STOCK):
        return

    with open(RUTA_STOCK, mode="r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            p = Producto(fila["Nombre"], fila["Precio"], fila["Cantidad"])
            lista_productos.append(p)
    print(f"📦 Se cargaron {len(lista_productos)} productos del stock.")