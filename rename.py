import os

def renombrar_archivos(directorio, prefijo):
    # Verificar si el directorio existe
    if not os.path.isdir(directorio):
        print(f"El directorio {directorio} no existe.")
        return

    # Inicializar el contador
    contador = 1

    # Iterar sobre cada archivo en el directorio
    for nombre_archivo in os.listdir(directorio):
        ruta_antigua = os.path.join(directorio, nombre_archivo)
        
        # Verificar si es un archivo
        if os.path.isfile(ruta_antigua):
            # Obtener la extensión del archivo
            extension = os.path.splitext(nombre_archivo)[1]
            # Crear el nuevo nombre con el formato especificado
            nuevo_nombre = f"{prefijo}_{contador}{extension}"
            ruta_nueva = os.path.join(directorio, nuevo_nombre)
            
            # Renombrar el archivo
            os.rename(ruta_antigua, ruta_nueva)
            print(f"{nombre_archivo} renombrado a {nuevo_nombre}")
            
            # Incrementar el contador
            contador += 1

# Ejemplo de uso
directorio = "D:/Me/Projects/juacar/img/juacar-2024"
prefijo = "juacar"
renombrar_archivos(directorio, prefijo)
