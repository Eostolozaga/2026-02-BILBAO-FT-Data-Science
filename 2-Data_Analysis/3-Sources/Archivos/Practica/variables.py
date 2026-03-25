import os

# Ruta de la carpeta a organizar (por defecto Descargas)
RUTA_BASE = os.path.expanduser("~/Downloads")

# Extensiones de archivos
DOC_TYPES = ('.doc', '.docx', '.txt', '.pdf', '.xls', '.ppt', '.xlsx', '.pptx')
IMG_TYPES = ('.jpg', '.jpeg', '.png', '.svg', '.gif')
SOFTWARE_TYPES = ('.exe', '.py', '.ipynb')

# Carpetas de destino
CATEGORIAS = ["Imagenes", "Documentos", "Software", "Otros"]