import os
import csv
from datetime import datetime

class Cliente:
    def __init__(self, nombre, apellido, año, dni, telefono, domicilio, mail):
        self.nombre = nombre
        self.apellido = apellido
        self.año = año
        self.dni = dni
        self.telefono = telefono
        self.domicilio = domicilio
        self.mail = mail
        self.compras = []
    
    def es_nuevo(self):
        return len(self.compras) == 0
    
lista_clientes = []

def guardad_datos_clientes():
    ahora = datetime.now()
    anio = ahora.strftime("%Y")
    mes = ahora.strftime("%m")
    
    if not os.path.exists(anio):
        os.makedirs(anio)

    ruta = os.path.join(anio, f"clientes_{mes}.csv")

    with open(ruta, mode="w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(['Nombre', 'Apellido', 'Año', 'DNI', 'Telefono', 'Domicilio', 'Mail'])
        for c in lista_clientes:
            escritor.writerow([c.nombre, c.apellido, c.año, c.dni, c.telefono, c.domicilio, c.mail])
    print(f"💾 Guardado en {ruta}")

def cargar_datos_clientes():
    ahora = datetime.now()
    anio = ahora.strftime("%Y")
    mes = ahora.strftime("%m")
    ruta = os.path.join(anio, f"clientes_{mes}.csv")

    if not os.path.exists(ruta):
        return
    
    with open(ruta, mode='r', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            c = Cliente(fila['Nombre'], fila['Apellido'], fila['Año'], 
                        fila['DNI'], fila['Telefono'], fila['Domicilio'], fila['Mail'])
            lista_clientes.append(c)
    print(f"📂 Se cargaron {len(lista_clientes)} clientes del mes actual.")

def registrar_cliente(nombre, apellido, año, dni, telefono, domicilio, mail):
    for c in lista_clientes:
        if str(c.dni) == str(dni):
            print(f"\n❌ Error: El Dni {dni} ya pertenece al cliente {c.nombre} {c.apellido}.")
            return False
        
    nuevo = Cliente(nombre, apellido, año, dni, telefono, domicilio, mail)
    lista_clientes.append(nuevo)
    print(f"✅ Cliente {nombre} registrado con éxito.")
    return True

def buscar_por_apellido(apellido_buscado):
    resultado = []
    for c in lista_clientes:
        if c.apellido.lower() == apellido_buscado.lower():
            resultado.append(c)
    return resultado
