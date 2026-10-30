# Practica 4 - Parte 3: Explorar Documentacion de Redes

## 1. Respuestas Teoricas

### Que tipo de problema podrias resolver consultando la documentacion de GNS3
Problemas como cuando el programa no quiere encender, cuando los routers virtuales no conectan entre ellos, cuando la maquina virtual da error de memoria o cuando no sabes como meter una nueva imagen de Cisco a la topologia

### Que diferencia existe entre la documentacion de una herramienta y el repositorio de una biblioteca
La documentacion de la herramienta te enseña a usar el programa visual para armar tus redes con botones y cables, mientras que el repositorio de la biblioteca es una pagina llena de codigos de Python que sirven para meterte a esos equipos programando

### Que informacion revisarias antes de utilizar una biblioteca de automatizacion
Revisaria si funciona con la version de Python que tengo instalada, si es compatible con la marca de routers que estamos usando en la escuela y si los creadores todavia la actualizan para que no tenga fallas

### Por que es importante comprobar que plataformas y funciones admite una biblioteca
Porque cada marca de router usa comandos muy diferentes, si la biblioteca no acepta routers de Cisco el codigo va a fallar a la primera y no va a conectar a nada

### Como podrian utilizarse estos recursos en las siguientes practicas
Nos van a servir como una guia de ejemplos para saber como poner las contraseñas, los usuarios y los comandos de configuracion en nuestros scripts de Python para que controlen la red solos

---

## 2. Registro de Recursos de Redes

### Recurso 1
* **Nombre del recurso:** Documentacion oficial de GNS3
* **URL:** https://gns3.com
* **Tema que aborda:** Como instalar el simulador, armar las redes y arreglar errores comunes de conexion
* **Tipo de informacion que ofrece:** Manuales sencillos con fotos y pasos para seguir
* **Utilidad para el proyecto integrador:** Nos ayuda a que la maqueta de la red funcione bien y no de errores al conectarla con Python
* **Ejemplo de una situacion en la que lo consultaria:** Si un router de la red se traba o no quiere encender dentro del mapa

### Recurso 2
* **Nombre del recurso:** Repositorio de Netmiko en GitHub
* **URL:** https://github.com
* **Tema que aborda:** Codigos de ejemplo para conectar Python con routers y switches por SSH
* **Tipo de informacion que ofrece:** Ejemplos de codigos listos para copiar, pegar y cambiar tus datos
* **Utilidad para el proyecto integrador:** Es la base para programar el script que va a entrar a los routers y sacar la informacion que nos piden
* **Ejemplo de una situacion en la que lo consultaria:** Cuando no sepamos que linea de codigo poner para mandar un comando de configuracion a los equipos

### Recurso 3
* **Nombre del recurso:** Cisco Developer Network
* **URL:** https://cisco.com
* **Tema que aborda:** Guias basicas sobre como automatizar y programar equipos de la marca Cisco
* **Tipo de informacion que ofrece:** Tutoriales de redes, laboratorios de prueba y ejemplos de comandos sencillos
* **Utilidad para el proyecto integrador:** Nos da ideas claras de como se manejan los equipos de red usando codigos sencillos
* **Ejemplo de una situacion en la que lo consultaria:** Si ocupamos ver la lista de comandos basicos que Python le puede pedir al router de Cisco
