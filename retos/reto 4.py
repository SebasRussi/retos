def potencia(base, exp):
    if exp == 0:
        resultado = 1
        return resultado
    else:
        resultado = base * potencia(base, exp - 1)
        return resultado

print(potencia(3,3))