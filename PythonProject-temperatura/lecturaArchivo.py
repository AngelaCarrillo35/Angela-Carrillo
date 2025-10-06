def leer_archivo_linea_por_linea(nombre_archivo):
    try:
        with open(nombre_archivo, 'r',) as archivo:
            print(f"Contenido de '{nombre_archivo}' de Angela Carrillo:")
            for linea in archivo:
                print(linea.strip())
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no existe.")
    except IOError:
        print(f"Error: No se pudo abrir el archivo '{nombre_archivo}'.")

# Ruta completa del archivo
ruta_archivo = r'my_notes.txt'

# Llamada a la función
leer_archivo_linea_por_linea(ruta_archivo)
