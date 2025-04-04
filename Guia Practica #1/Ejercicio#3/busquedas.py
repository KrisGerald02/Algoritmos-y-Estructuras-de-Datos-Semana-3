def busqueda_lineal(lista, numero):
    for i in range(len(lista)):
        if lista[i] == numero:
            return f"Numero encontrado en la posicion {i} de la lista"
    return f"El numero {numero} no se encuentra en la lista"

def busqueda_binaria(lista, numero):
    if lista != sorted(lista):
        return "La lista debe estar ordenada"
    
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == numero:
            return f"El numero {numero} se encuentra en la posicion {medio} de la lista"
        elif lista[medio] < numero:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return f"El numero {numero} no se encuentra en la lista"
