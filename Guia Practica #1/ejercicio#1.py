from functools import reduce

class Venta:
    def __init__(self, precio, fecha, nombre_producto):
        self.precio = precio
        self.fecha = fecha
        self.nombre_producto = nombre_producto
    
    def __str__(self):
        return f"| Producto: {self.nombre_producto:<20} | Precio: {self.precio:<8} | Fecha: {self.fecha} |"


class VentaDao:
    def __init__(self):
        self.ventas = []
    
    def agregar_venta(self):
        print("\n--- Agregar nueva venta ---")
        precio = int(input("Ingrese el precio de la venta: "))
        fecha = input("Ingrese la fecha de la venta (dd/mm/aaaa): ")
        nombre_producto = input("Ingrese el nombre del producto vendido: ")
        self.ventas.append(Venta(precio, fecha, nombre_producto))
        print("Venta registrada correctamente.\n")
    
    def mostrar_ventas(self):
        print("\n=== Lista de Ventas ===")
        if not self.ventas:
            print("No hay ventas registradas.\n")
            return
        for venta in self.ventas:
            print(venta)
        print(f"Total de ventas: {len(self.ventas)}\n")
    
    def calcular_promedio(self):
        if not self.ventas:
            return 0
        return sum(map(lambda x: x.precio, self.ventas)) / len(self.ventas)
    
    def filtrar_por_precio(self):
        print("\n--- Filtrar por Precio ---")
        opcion = int(input("Filtrar por precios mayores o menores (0: mayores / 1: menores): "))
        precio = int(input("Ingrese el precio de referencia: "))
        if opcion == 0:
            return filter(lambda x: x.precio > precio, self.ventas)
        elif opcion == 1:
            return filter(lambda x: x.precio < precio, self.ventas)
        else:
            print("Opcion no valida.\n")
            return []
    
    def filtrar_por_fecha(self):
        print("\n--- Filtrar por Fecha ---")
        fecha = input("Ingrese la fecha (dd/mm/aaaa): ")
        return filter(lambda x: x.fecha == fecha, self.ventas)
    
    def calcular_suma_total(self):
        return sum(venta.precio for venta in self.ventas)


def main():
    dao = VentaDao()
    while True:
        print("\n======= MENU DE OPCIONES =======")
        print("1. Agregar venta")
        print("2. Mostrar ventas")
        print("3. Filtrar ventas")
        print("4. Mostrar promedio de ventas")
        print("5. Mostrar la suma total de las ventas")
        print("6. Salir")
        print("================================")
        
        try:
            opcion = int(input("Ingrese una opcion: "))
        except ValueError:
            print("Ingrese un numero valido.\n")
            continue
        
        if opcion == 1:
            dao.agregar_venta()
        elif opcion == 2:
            dao.mostrar_ventas()
        elif opcion == 3:
            print("\n--- Opciones de Filtro ---")
            print("1. Filtrar por precio")
            print("2. Filtrar por fecha")
            try:
                sub_opcion = int(input("Ingrese una opcion: "))
                if sub_opcion == 1:
                    resultados = list(dao.filtrar_por_precio())
                elif sub_opcion == 2:
                    resultados = list(dao.filtrar_por_fecha())
                else: 
                    print("Opcion no valida.\n")
                    continue
                
                if resultados:
                    print("\n--- Resultados del filtro ---")
                    for venta in resultados:
                        print(venta)
                    print()
                else:
                    print("No se encontraron coincidencias.\n")

            except ValueError:
                print("Ingrese una opcion valida.\n")
        elif opcion == 4:
            promedio = dao.calcular_promedio()
            print(f"\nPromedio de ventas: {promedio:.2f}\n")
        elif opcion == 5:
            suma = dao.calcular_suma_total()
            print(f"\nSuma total de ventas: {suma}\n")
        elif opcion == 6:
            print("Saliendo del programa. Hasta luego.")
            break
        else:
            print("Opcion no valida.\n")

main()
