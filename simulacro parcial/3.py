def misma_diagonal(matriz, fila=0, columna=0, digito=None):
    # Verificar si hemos alcanzado el final de la diagonal
    if fila == len(matriz) or columna == len(matriz[0]):
        return True

    # Si es la primera iteración, obtenemos el dígito inicial de la diagonal
    if digito is None:
        digito = matriz[fila][columna] % 10

    # Verificar si el dígito actual es diferente al dígito inicial
    if matriz[fila][columna] % 10 != digito:
        return False

    # Llamada recursiva para el siguiente elemento en la diagonal
    return misma_diagonal(matriz, fila + 1, columna + 1, digito)


# Ejemplo de uso
matriz_ejemplo = [
    [0, 2, 3, 5],
    [4, 0, 6, 3],
    [7, 8, 6, 9],
    [1, 8, 4, 0]
]

resultado = misma_diagonal(matriz_ejemplo)
if resultado:
    print("La diagonal tiene los mismos dígitos.")
else:
    print("La diagonal no tiene los mismos dígitos.")
