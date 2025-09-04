matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# print("Matriz fija:")
# for fila in matriz:
#     print(fila)
#
# print("\nSolo dos filas de la matriz:")
# print(matriz[0][0])
# print(matriz[0][1])
# print(matriz[0][2])
#
# print("\nUsando for (dos primeras filas):")
# for i in range(3):
#     print(matriz[i])
print(len(matriz))

def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return f"Valor {valor} encontrado en posición [{i}][{j}]"
    return f"Valor {valor} no encontrado en la matriz"

print("Matriz:")
for fila in matriz:
    print(fila)

numero = int(input("Ingrese el número a buscar: "))
resultado = buscar_valor(matriz, numero)
print(resultado)