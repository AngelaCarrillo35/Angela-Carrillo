temperaturas = [
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

# Listas auxiliares
ciudades = ["Loja", "Macas", "Ambato"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
num_semanas = len(temperaturas[0][0])
# Mostrar datos organizados
for i, ciudad in enumerate(ciudades):
    print(f"\nCiudad: {ciudad}")
    for j, dia in enumerate(dias):
        print(f"  {dia}: ", end="")
        for k in range(num_semanas):  # recorrer semanas
            print(f"Semana {k+1}: {temperaturas[i][j][k]}°C ", end="| ")
        print()  # salto de línea después de cada día

