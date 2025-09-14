temperaturas = [ #datos de temperatura que van a ser enviados como parametro a la función creada
    #Cada bloque representa una ciudad
    [  #Cada fila representa un  día de lunes a domingo
        [15, 16, 17],
        [17, 18, 19],
        [16, 15, 14],
        [18, 19, 20],
        [20, 21, 22],
        [19, 20, 21],
        [17, 18, 19]
    ],
    [
        [28, 29, 30],
        [30, 31, 32],
        [29, 28, 27],
        [32, 33, 34],
        [31, 30, 29],
        [30, 29, 28],
        [28, 27, 26]
    ],
    [
        [12, 13, 14],
        [14, 15, 16],
        [13, 12, 11],
        [15, 14, 13],
        [16, 17, 18],
        [15, 14, 13],
        [13, 12, 11]
    ]
]

ciudades = ["Loja", "Macas", "Ambato"] #parametro ciudades que será enviada a la función creada
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"] #parametro días que será enviada a la función creada
num_semanas = len(temperaturas[0][0]) #parametro num_semanas que será enviada a la función creada, de acuerdo a los datos de temperatura

def promedio_temperaturas_por_ciudad(temperaturas, ciudades, dias, num_semanas): #definición de la función promedio_temperaturas_por_ciudad con cuatro parámetros
    promedios = {} #valores de retorno

    for i, ciudad in enumerate(ciudades): #recorrido de cada ciudad ingresada en el parametro de la función
        suma_total = 0
        contador = 0
        for j in range(len(dias)):  # recorrido por día
            for k in range(num_semanas):  # recorrido por semana
                suma_total += temperaturas[i][j][k] #suma total de la temperaturas ingresadas
                contador += 1 #contador general para cálculo de promedio
        promedio = suma_total / contador #cálculo del promedio
        promedios[ciudad] = round(promedio, 2) #almacenar el promedio calculado por ciudad en el valor de retorno
    return promedios #valor retornado por ciudades

promedios = promedio_temperaturas_por_ciudad(temperaturas, ciudades, dias, num_semanas) #llamada a la función promedio_temperaturas_por_ciudad y almacenamiento en la variable promedios

for ciudad, promedio in promedios.items(): #recorrido para la impresión de los valores de la variable promedios
    print(f"Promedio de temperatura en {ciudad}: {promedio}°C")


