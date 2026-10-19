# Práctica 3 - Primer programa de Python para representar información de dispositivos

dispositivos = [
    {
        "nombre": "R1",
        "tipo": "Router",
        "ip": "10.1.1.1",
        "estado": "Activo",
        "fabricante": "Cisco",
        "sistema": "Cisco IOSv 15.9(3)M6",
        "protocolo": "OSPF",
        "funcion": "Enrutamiento"
    },
    {
        "nombre": "R2",
        "tipo": "Router",
        "ip": "10.1.1.2",
        "estado": "Activo",
        "fabricante": "Cisco",
        "sistema": "Cisco IOSv 15.9(3)M6",
        "protocolo": "OSPF",
        "funcion": "Enrutamiento"
    },
    {
        "nombre": "S1",
        "tipo": "Switch",
        "ip": "10.1.1.3",
        "estado": "Activo",
        "fabricante": "Cisco",
        "sistema": "Cisco IOSvL2 15.2",
        "protocolo": "N/A",
        "funcion": "Conectividad"
    }
]


def mostrar_dispositivo(dispositivo):
    """Muestra toda la información de un dispositivo."""
    print("Nombre:", dispositivo["nombre"])
    print("Tipo:", dispositivo["tipo"])
    print("IP:", dispositivo["ip"])
    print("Estado:", dispositivo["estado"])
    print("Fabricante:", dispositivo["fabricante"])
    print("Sistema:", dispositivo["sistema"])
    print("Protocolo:", dispositivo["protocolo"])
    print("Función:", dispositivo["funcion"])


def buscar_dispositivo(lista, nombre_buscado):
    """Busca un dispositivo por su nombre (sin distinguir mayúsculas)."""
    for dispositivo in lista:
        if dispositivo["nombre"].lower() == nombre_buscado.lower():
            return dispositivo
    return None



for dispositivo in dispositivos:
    mostrar_dispositivo(dispositivo)

    if dispositivo["estado"] == "Activo":
        print("El dispositivo está disponible.")
    else:
        print("El dispositivo requiere atención.")

    print("--------------------")


entrada = input("Ingrese el nombre del dispositivo: ")
dispositivo_encontrado = buscar_dispositivo(dispositivos, entrada)

if dispositivo_encontrado:
    print("Dispositivo encontrado:")
    mostrar_dispositivo(dispositivo_encontrado)
else:
    print("Dispositivo no encontrado.")