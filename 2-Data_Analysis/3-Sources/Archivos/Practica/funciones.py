import os
import shutil
from variables import RUTA_BASE, DOC_TYPES, IMG_TYPES, SOFTWARE_TYPES, CATEGORIAS

def preparar_entorno():
    """Crea las carpetas de destino si no existen."""
    for carpeta in CATEGORIAS:
        ruta_completa = os.path.join(RUTA_BASE, carpeta)
        if not os.path.exists(ruta_completa):
            os.makedirs(ruta_completa)

def clasificar_archivo(nombre_archivo):
    """Devuelve el nombre de la carpeta destino según la extensión."""
    nombre_low = nombre_archivo.lower()
    
    if nombre_low.endswith(IMG_TYPES):
        return "Imagenes"
    elif nombre_low.endswith(DOC_TYPES):
        return "Documentos"
    elif nombre_low.endswith(SOFTWARE_TYPES):
        return "Software"
    return "Otros"

def organizar_archivos():
    """Mueve los archivos de la ruta base a sus carpetas correspondientes."""
    archivos_movidos = 0
    
    for item in os.listdir(RUTA_BASE):
        ruta_origen = os.path.join(RUTA_BASE, item)
        
        # Solo procesamos archivos, ignoramos las carpetas de destino
        if os.path.isfile(ruta_origen):
            destino = clasificar_archivo(item)
            ruta_destino = os.path.join(RUTA_BASE, destino, item)
            
            try:
                shutil.move(ruta_origen, ruta_destino)
                archivos_movidos += 1
                print(f"Movido: {item} -> {destino}")
            except Exception as e:
                print(f"Error moviendo {item}: {e}")
                
    return archivos_movidos