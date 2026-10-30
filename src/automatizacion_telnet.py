# Práctica 5 - Mi primer script en Python para la automatización de redes
#
# Se conecta por Telnet al router R1 de la topología "MiPrimerScript" (GNS3)
# y le aplica configuración: Loopback 0, Loopback 1 y OSPF en el área 0.
#
# Se ejecuta desde el Network Automation Container (NAC):
#     python3 automatizacion_telnet.py
#
# PLATAFORMA elige qué comandos se envían:
#   "frr"       -> R1 con FRRouting (lo que usamos, al no tener la imagen IOSv)
#   "cisco_ios" -> R1 con Cisco IOSv (el router que pide la guía)
#
# AVISO: Telnet no cifra nada. Úsalo solo en la topología aislada del
# laboratorio. Las contraseñas se piden al ejecutar; no se guardan aquí.

import getpass
import sys

try:
    import telnetlib
except ModuleNotFoundError:
    # telnetlib se quitó de Python a partir de la versión 3.13.
    print("Este Python (" + sys.version.split()[0] + ") ya no trae telnetlib.")
    print("Usa Python 3.12 o anterior (el NAC lo trae), o instala el reemplazo:")
    print("    pip install standard-telnetlib")
    sys.exit(1)

HOST = "192.168.122.70"  # IP de R1 (red de la NAT Cloud)
PLATAFORMA = "frr"

if PLATAFORMA == "frr":
    PIDE_USUARIO = b"login: "
    PROMPT = b"R1# "
    COMANDOS = [
        "configure terminal",
        # Loopback 0 (paso 22 de la guía)
        "interface lo0",
        "ip address 1.1.1.1/32",
        "exit",
        # Loopback 1 (paso 27)
        "interface lo1",
        "ip address 2.2.2.2/32",
        "exit",
        # OSPF (paso 27): 0.0.0.0/0 activa OSPF en todas las interfaces, área 0
        "router ospf",
        "network 0.0.0.0/0 area 0",
        "exit",
        "end",
        "write memory",
        # Verificación: la salida queda impresa al final como evidencia
        "terminal length 0",
        "show interface brief",
        "show running-config ospfd",
    ]
else:  # cisco_ios
    PIDE_USUARIO = b"Username: "
    PROMPT = b"#"
    COMANDOS = [
        "configure terminal",
        "interface loopback 0",
        "ip address 1.1.1.1 255.255.255.255",
        "exit",
        "interface loopback 1",
        "ip address 2.2.2.2 255.255.255.255",
        "exit",
        # En Cisco la segunda dirección es una wildcard:
        # 0.0.0.0 255.255.255.255 = todas las interfaces
        "router ospf 1",
        "network 0.0.0.0 255.255.255.255 area 0",
        "end",
        "write memory",
        "terminal length 0",
        "show ip interface brief",
        "show ip protocols",
    ]

user = input("Enter your Telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(PIDE_USUARIO)
tn.write(user.encode("ascii") + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode("ascii") + b"\n")

if PLATAFORMA == "cisco_ios":
    # IOS entra en modo usuario (R1>); hay que pasar a modo privilegiado.
    enable_password = getpass.getpass("Enable password: ")
    tn.read_until(b">", timeout=10)
    tn.write(b"enable\n")
    tn.write(enable_password.encode("ascii") + b"\n")

# Esperamos el prompt antes de mandar la configuración.
tn.read_until(PROMPT, timeout=10)

for comando in COMANDOS:
    tn.write(comando.encode("ascii") + b"\n")

tn.write(b"exit\n")

print(tn.read_all().decode("ascii", errors="replace"))
