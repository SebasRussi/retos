def contar_digitos(numero):
  """
  Función recursiva sin cola que recibe un número y devuelve la cantidad de dígitos y si es par o impar.

  Parámetros:
    numero: El número entero a analizar.

  Retorno:
    (digitos, paridad): Tupla que contiene la cantidad de dígitos (int) y si el número es par o impar (bool).
  """

  if numero == 0:
    return (1, False)

  digitos, paridad = contar_digitos(numero // 10)

  return (digitos + 1, (numero % 2) == 0)


# Ejemplo de uso
numero = 124
digitos, paridad = contar_digitos(numero)

print(f"El número {numero} tiene {digitos} dígitos.")
print(f"El número {numero} es {'par' if paridad else 'impar'}.")