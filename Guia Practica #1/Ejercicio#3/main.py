from busquedas import busqueda_lineal, busqueda_binaria

def main():
    lista = list(map(int, input("Ingrese los numeros separados por espacio: ").split()))
    numero = int(input("Ingrese el numero a buscar: "))

    print("\n--- Busqueda Lineal ---")
    print(busqueda_lineal(lista, numero))

    print("\n--- Busqueda Binaria ---")
    print(busqueda_binaria(lista, numero))

if __name__ == "__main__":
    main()
