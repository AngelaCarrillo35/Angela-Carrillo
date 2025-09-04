matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def mostrar_matriz(mat):
    for fila in mat:
        print(fila)
    print()


def ordenar_fila(matriz, fila_index):
    n = len(matriz[fila_index])
    for i in range(n):
        for j in range(0, n - i - 1):
            if matriz[fila_index][j] > matriz[fila_index][j + 1]:
                # Intercambio
                matriz[fila_index][j], matriz[fila_index][j + 1] = matriz[fila_index][j + 1], matriz[fila_index][j]


print("Matriz original:")
mostrar_matriz(matriz)

# Ordenar una fila específica (ejemplo: la segunda fila, índice 1)
fila_a_ordenar = int(input("Ingrese el número a buscar: "))
ordenar_fila(matriz, fila_a_ordenar)

print(f"Matriz con la fila {fila_a_ordenar} ordenada en forma ascendente:")
mostrar_matriz(matriz)
