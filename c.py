import os

directorio = 'D:/Me/Projects/juacar/img/juacar-2023/directora'  # Reemplaza con la ruta de tu directorio
prefijo = 'img'  # Puedes cambiar el prefijo según tus necesidades
extension = '.jpg'  # Puedes cambiar la extensión según tus necesidades

# Obtén la lista de archivos en el directorio
archivos = os.listdir(directorio)

# Ordena la lista de archivos
archivos.sort()

# Inicializa el contador
contador = 1

# Itera sobre cada archivo en el directorio
for archivo in archivos:
    # Construye el nuevo nombre del archivo con el formato deseado
    nuevo_nombre = f'{prefijo}_{contador:03d}{extension}'  # 3 dígitos de ancho, por ejemplo: archivo_001.txt
    
    # Ruta completa del archivo antiguo y nuevo
    ruta_antigua = os.path.join(directorio, archivo)
    ruta_nueva = os.path.join(directorio, nuevo_nombre)

    # Cambia el nombre del archivo
    os.rename(ruta_antigua, ruta_nueva)

    # Incrementa el contador para el próximo archivo
    contador += 1

print('Nombres de archivos cambiados con éxito.')
