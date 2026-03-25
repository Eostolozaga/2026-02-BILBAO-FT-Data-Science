from funciones import preparar_entorno, organizar_archivos

def ejecutar():
    print("--- INICIANDO ORGANIZADOR DE ARCHIVOS ---")
    
    # 1. Crear carpetas
    preparar_entorno()
    
    # 2. Mover archivos
    total = organizar_archivos()
    
    if total > 0:
        print(f"\n ¡Listo! Se han organizado {total} archivos.")
    else:
        print("\nLa carpeta ya estaba organizada.")

if __name__ == "__main__":
    ejecutar()
