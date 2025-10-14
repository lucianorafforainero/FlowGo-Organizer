"""
FlowGo Automation - Demo 1
Organizador automático de archivos (versión inicial)
Autor: Luciano Raffo Rainero
Descripción:
    Este programa va a escanear una carpeta y luego agrupar archivos por tipo.
    Por ahora, solo va a verificar que la ruta exista y mostrar un mensaje.
"""
import os
from pathlib import Path

def organizar_carpeta(ruta, simular=True, log_file="organizer_log.txt"):
    ruta = Path(ruta)
    log_path = Path(log_file)

    # Limpia o crea el log nuevo
    with open(log_path, "w", encoding="utf-8") as log:
        log.write(f"FlowGo Organizer Log\nFecha: {Path.cwd()}\n\n")

    def log_line(texto):
        print(texto)
        with open(log_path, "a", encoding="utf-8") as log:
            log.write(texto + "\n")

    if not ruta.exists():
        log_line("❌ La carpeta no existe.")
        return

    if not ruta.is_dir():
        log_line("⚠️ La ruta no es una carpeta.")
        return

    log_line(f"✅ Carpeta encontrada: {ruta}\n")
    log_line("🚀 Organizando archivos por tipo...\n")

    for elemento in ruta.iterdir():
        if elemento.is_file():
            extension = elemento.suffix.lower().strip(".")
            if extension == "":
                extension = "sin_extension"

            carpeta_destino = ruta / extension
            nueva_ruta = carpeta_destino / elemento.name

            if simular:
                log_line(f"🧪 [SIMULACIÓN] {elemento.name} → {carpeta_destino.name}/")
            else:
                carpeta_destino.mkdir(exist_ok=True)
                elemento.rename(nueva_ruta)
                log_line(f"🗂️  {elemento.name} → {carpeta_destino.name}/")

        elif elemento.is_dir():
            log_line(f"📁 (subcarpeta ignorada) {elemento.name}")

    if simular:
        log_line("\n✅ Simulación terminada.")
    else:
        log_line("\n✅ Organización completa.")



if __name__ == "__main__":
    carpeta = input("👉 Ingresá la ruta de la carpeta que querés organizar: ").strip()
    confirmar = input("¿Querés que realmente se muevan los archivos? (s/n): ").lower() == "s"
    organizar_carpeta(carpeta, simular=not confirmar)

