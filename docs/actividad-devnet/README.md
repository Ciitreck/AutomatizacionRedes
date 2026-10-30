# Actividad 4.2: Exploración de Cisco DevNet y las certificaciones de automatización de Cisco

| Campo | Detalle |
|-------|---------|
| **Asignatura** | Automatización de Infraestructura Digital I |
| **Profesor** | Victor Alejandro Galvan Guerra |
| **Grupo** | 3IRI3V |
| **Fecha** | 29 de octubre de 2026 |
| **Equipo** | José Emilio Montes Villarreal, Carlos Martín Cobos Hernández y Erik Osiel Camarillo Espinoza |

## Propósito

Investigar los recursos que ofrece Cisco DevNet y reconocer las certificaciones de Cisco relacionadas con el desarrollo de software, las API y la automatización de redes. Desde el 3 de febrero de 2026 la ruta DevNet se llama **Cisco Automation** (CCNA, CCNP y CCIE Automation), por lo que se consultaron las páginas oficiales vigentes.

El reporte completo está en [`reporte.pdf`](reporte.pdf).

## Estructura de la carpeta

```
docs/
└── actividad-devnet/
    ├── README.md        ← este archivo
    ├── reporte.pdf      ← reporte de investigación
    └── evidencias/
        ├── 01-devnet-inicio.png
        ├── 02-devnet-acerca.png
        ├── 03-devnet-documentacion.png
        ├── 04-devnet-labs.png
        ├── 05-devnet-sandbox.png
        ├── 06-devnet-code-exchange.png
        ├── 07-certificaciones-automation.png
        ├── 08-ccna-automation.png
        ├── 09-ccnp-automation.png
        ├── 10-ccie-automation.png
        └── 11-anuncio-cisco-automation.png
```

## Resumen

| Certificación | Nivel | Exámenes |
|---------------|-------|----------|
| CCNA Automation (antes DevNet Associate) | Associate | 200-901 CCNAAUTO |
| CCNP Automation (antes DevNet Professional) | Professional | 350-901 AUTOCOR + 300-435 ENAUTO o 300-635 DCNAUTO |
| CCIE Automation (antes DevNet Expert) | Expert | 350-901 AUTOCOR + examen práctico de 8 horas |

## Relación con el proyecto integrador

- Practicar SSH, RESTCONF y NETCONF en el Sandbox **Catalyst 8000 Always On** antes de tocar R1 y R2 en GNS3.
- Aprender NETCONF, RESTCONF y YANG con los **Learning Labs**.
- Probar peticiones de la API de IOS XE en Postman antes de pasarlas a Python.
- Revisar ejemplos de **Code Exchange** (Netmiko, Nornir) para ampliar [`src/dispositivos.py`](../../src/dispositivos.py).

## Enlaces oficiales consultados

- [Cisco DevNet](https://developer.cisco.com/)
- [About Cisco DevNet](https://developer.cisco.com/about/)
- [Cisco Automation certifications](https://www.cisco.com/site/us/en/learn/training-certifications/certifications/automation/index.html)
- [Certificaciones y exámenes de Cisco](https://www.cisco.com/site/us/en/learn/training-certifications/exams/index.html)
- [Anuncio de la evolución de las certificaciones Cisco](https://blogs.cisco.com/learning/par-merat-announces-learn-with-cisco)
