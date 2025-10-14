# FlowGo Organizer

**Autor:** Luciano Raffo  
**Proyecto:** FlowGo Automation — Demo 1  
**Versión:** 1.2

---

## Descripción

FlowGo Organizer es una herramienta de automatización desarrollada en Python que organiza automáticamente los archivos de una carpeta según su tipo (extensión).  
Permite ejecutar una **simulación previa (modo dry-run)** antes de mover archivos reales, y genera un **registro de actividad (log)** con cada acción.

Ideal para usuarios o empresas que necesitan mantener carpetas limpias y ordenadas de forma automática.

---

## Características

- Clasifica los archivos por extensión.  
- Crea subcarpetas automáticamente (`pdf`, `png`, `mp3`, etc.).  
- Modo **simulación** (no mueve nada).  
- Modo **confirmado** (mueve de verdad).  
- Registro completo en `organizer_log.txt`.  
- No borra ni sobrescribe archivos.  

---

## Uso

1. Ejecutar el script:

   ```bash
    python main.py

2. Ingresar la ruta de la carpeta que se desea organizar.

    por ejemplo: "C:/Users/usuario/Downloads"

3. Elegir:

    n → simulación (solo muestra lo que haría).

    s → mueve los archivos realmente.

## Ejemplo

"""
 Ingresá la ruta de la carpeta que querés organizar: C:\Users\lucia\Downloads
 ¿Querés mover los archivos de verdad? (s/n): n


Salida en consola:

  [SIMULACIÓN] informe.pdf → pdf/
  [SIMULACIÓN] musica.mp3 → mp3/
  (subcarpeta ignorada) carpeta_vieja
  Simulación terminada.

Estructura resultante

    Downloads/
    ├── pdf/
    │   └── informe.pdf
    ├── mp3/
    │   └── musica.mp3
    ├── png/
    │   └── foto.png
    └── sin_extension/
        └── nota
"""

## Requisitos

Python 3.8 o superior

No requiere librerías externas

## Licencia

Uso libre para demostraciones, estudios o desarrollo de automatizaciones personalizadas dentro de FlowGo Automation.

© 2025 — Luciano Raffo · FlowGo Automation