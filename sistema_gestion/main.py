from clientes import (
    cargar_datos_clientes,
    guardad_datos_clientes,
    buscar_por_apellido,
    registrar_cliente,
)
from stock import (
    cargar_stock,
    guardar_stock,
    lista_productos,
    registrar_producto,
)
from ventas import mostrar_productos_venta, registrar_venta

print("Iniciando sistema...")
cargar_datos_clientes()
cargar_stock()

while True:
    print("\n===== MENU =====")
    print("1. Registrar Cliente")
    print("2. Buscar Cliente")
    print("3. Ver Stock")
    print("4. Cargar Productos")
    print("5. Vender Producto")
    print("0. Salir")

    opcion = input("Seleccione una Opción: ").strip()

    if opcion == "1":
        print("\n--- Registro de Nuevo Cliente ---")
        nombre = input("Nombre/s: ")
        apellido = input("Apellido/s: ")
        dni = input("DNI: ")
        año = input("Fecha de Nacimiento: ")
        telefono = input("Número de teléfono: ")
        mail = input("Mail: ")
        domicilio = input("Domicilio: ")

        registrar_cliente(nombre, apellido, año, dni, telefono, domicilio, mail)

    elif opcion == "2":
        print("\n--- Buscar Cliente ---")
        apellido_buscado = input("Ingrese el apellido a buscar: ")
        encontrados = buscar_por_apellido(apellido_buscado)

        if not encontrados:
            print("No se encontró nadie con ese apellido.")
        else:
            print(f"\nSe encontraron {len(encontrados)} clientes:")
            for c in encontrados:
                print("-" * 20)
                print(f"Nombre: {c.nombre} {c.apellido}")
                print(f"DNI: {c.dni}")
                print(f"Mail: {c.mail}")

    elif opcion == "3":
        print("\n" + "*" * 10 + " STOCK DE PRODUCTOS " + "*" * 10)
        if len(lista_productos) == 0:
            print("El stock está vacío. Cargue productos en la opción 4.")
        else:
            for p in lista_productos:
                estado = "DISPONIBLE" if p.hay_stock() else "AGOTADO"
                print(f"Producto: {p.nombre} | Precio: $ {p.precio} | Cantidad: {p.cantidad} [{estado}]")
            print("*" * 30)

    elif opcion == "4":
        print("\n--- Cargar Nuevo Producto ---")
        n = input("Nombre: ").strip()
        try:
            p = float(input("Precio: ").replace(",", "."))
            c = int(input("Cantidad: "))
        except ValueError:
            print("❌ Ingresá un precio y una cantidad válidos.")
            continue

        registrar_producto(n, p, c)
        print(f"✔ Datos Guardados: {n} añadido al stock.")

    elif opcion == "5":
        print("\n--- Registrar venta ---")
        if mostrar_productos_venta():
            seleccion = input("Elegí número o nombre del producto: ").strip()
            if seleccion.isdigit():
                indice = int(seleccion) - 1
                if 0 <= indice < len(lista_productos):
                    nombre_p = lista_productos[indice].nombre
                else:
                    print("❌ Número de producto fuera de rango.")
                    continue
            else:
                nombre_p = seleccion

            try:
                cant = int(input("Cantidad a vender: "))
            except ValueError:
                print("❌ La cantidad debe ser un número entero.")
                continue

            registrar_venta(nombre_p, cant)

    elif opcion == "0":
        print("Guardando datos...")
        guardad_datos_clientes()
        guardar_stock()
        print("Saliendo del Sistema.")
        break

    else:
        print("Opción no válida, intente de nuevo.")