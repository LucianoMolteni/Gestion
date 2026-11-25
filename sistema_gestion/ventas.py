import csv
import os
from datetime import datetime
from stock import lista_productos


def mostrar_productos_venta():
    if not lista_productos:
        print("No hay productos cargados en el stock.")
        return False

    print("\n--- Productos disponibles ---")
    for i, p in enumerate(lista_productos, start=1):
        print(f"{i}. {p.nombre} | Precio: ${p.precio} | Stock: {p.cantidad}")
    return True


def buscar_producto(nombre_buscado):
    for p in lista_productos:
        if p.nombre.lower() == nombre_buscado.lower():
            return p
    return None


def guardar_venta_csv(producto, cantidad_vendida, total):
    ahora = datetime.now()
    anio = ahora.strftime("%Y")
    mes = ahora.strftime("%m")
    fecha_hora = ahora.strftime("%Y-%m-%d %H:%M:%S")

    if not os.path.exists(anio):
        os.makedirs(anio)

    ruta = os.path.join(anio, f"ventas_{mes}.csv")
    archivo_nuevo = not os.path.exists(ruta)

    with open(ruta, mode="a", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        if archivo_nuevo:
            escritor.writerow(["Fecha", "Producto", "Cantidad", "Precio_Unitario", "Total"])
        escritor.writerow([fecha_hora, producto.nombre, cantidad_vendida, producto.precio, total])

    return ruta


def registrar_venta(nombre_producto, cantidad_vendida):
    if cantidad_vendida <= 0:
        print("❌ La cantidad a vender debe ser mayor a 0.")
        return False

    producto = buscar_producto(nombre_producto)
    if producto is None:
        print(f"❌ No existe el producto '{nombre_producto}' en el stock.")
        return False

    if not producto.actualizar_stock(cantidad_vendida):
        print(f"❌ Stock insuficiente de '{producto.nombre}'. Disponible: {producto.cantidad}")
        return False

    total = cantidad_vendida * producto.precio
    ruta = guardar_venta_csv(producto, cantidad_vendida, total)
    print(f"✅ Venta registrada: {cantidad_vendida} x {producto.nombre} = ${total:.2f} (guardado en {ruta})")
    print(f"📦 Stock restante de {producto.nombre}: {producto.cantidad}")
    return True