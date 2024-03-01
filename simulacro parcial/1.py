def contiene_digitos(string, indice=0):
    # Verificar si hemos alcanzado el final de la cadena
    if indice == len(string):
        return False
    digits = "0123456789"
    # Verificar si el carácter actual es un dígito
    if string[indice] in digits:
        return True

    # Llamada recursiva con el siguiente índice
    return contiene_digitos(string, indice + 1)


# Ejemplo de uso
assert(contiene_digitos("asdf1") == True)