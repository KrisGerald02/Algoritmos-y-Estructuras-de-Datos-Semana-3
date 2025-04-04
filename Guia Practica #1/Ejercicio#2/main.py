
from modulo_ordenamiento import bubble_sort

def main():
    numeros = [34, 12, 5, 66, 1, 89, 3]
    print("Lista original:", numeros)
    
    lista_ordenada = bubble_sort(numeros.copy())
    print("Lista ordenada:", lista_ordenada)

main()
    
