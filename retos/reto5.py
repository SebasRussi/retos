lista = [1, 2, 3]

def sumalista(lista):
    if lista == []:
        suma = 0
    else:
        suma = lista[0] + sumalista(lista[1:])
    return suma

print(sumalista(lista))

