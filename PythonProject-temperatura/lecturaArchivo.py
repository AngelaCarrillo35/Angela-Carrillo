def leer_archivo_linea_por_linea(nombre_archivo): #Definicion de la función leer archivos
    try: #Control de excepciones
        with open(nombre_archivo, 'r',) as archivo: #apertura de archivo enviado en la función
            print(f"Contenido de '{nombre_archivo}' de Angela Carrillo:") #Imprime una etiqueta con mi nombre
            for linea in archivo: #repite la lectura linea por linea hasta completar el archivo
                print(linea.strip()) #impresión de la linea omitiendo salto de página
    except FileNotFoundError: #captura del error al no existir el archivo
        print(f"Error: El archivo '{nombre_archivo}' no existe.") #Impresión de leyenda del error
    except IOError: #Captura del error al no poder abrirlo
        print(f"Error: No se pudo abrir el archivo '{nombre_archivo}'.") #Impresión de leyenda del error

# Definición de la ruta completa del archivo
ruta_archivo = r'my_notes.txt' 

# Llamada a la función lectura de archivos
leer_archivo_linea_por_linea(ruta_archivo)
