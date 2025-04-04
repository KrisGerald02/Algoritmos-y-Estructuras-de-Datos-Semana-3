import models.clases as c
import controllers.dao_controller as dao

def menu():
    producto_dao = dao.ProductoDao()
    while True:
        print("\n--- Menu ---")
        print("1. Agregar Producto")
        print("2. Buscar Producto")
        print("3. Actualizar Producto")
        print("4. Eliminar Producto")
        print("5. Mostrar Inventario")
        print("6. Salir")
        
        opcion = input("Seleccione una opcion: ")
        
        if opcion == "1":
            codigo = input("Ingrese codigo del producto: ")
            nombre = input("Ingrese nombre del producto: ")
            precio = float(input("Ingrese precio del producto: "))
            cantidad_stock = int(input("Ingrese cantidad en stock: "))
            producto = c.Producto(codigo, nombre, precio, cantidad_stock)
            producto_dao.agregar_producto(producto)
        
        elif opcion == "2":
            codigo = input("Ingrese el codigo del producto a buscar: ")
            producto = producto_dao.buscar_producto(codigo)
            if producto:
                print(f"Producto encontrado: {producto}")
            else:
                print("Producto no encontrado.")
        
        elif opcion == "3":
            codigo = input("Ingrese el codigo del producto a actualizar: ")
            nombre = input("Nuevo nombre (dejar vacio para no cambiar): ") or None
            precio = input("Nuevo precio (dejar vacio para no cambiar): ")
            precio = float(precio) if precio else None
            cantidad_stock = input("Nueva cantidad en stock (dejar vacio para no cambiar): ")
            cantidad_stock = int(cantidad_stock) if cantidad_stock else None
            producto_dao.actualizar_producto(codigo, nombre, precio, cantidad_stock)
        
        elif opcion == "4":
            codigo = input("Ingrese el codigo del producto a eliminar: ")
            producto_dao.eliminar_producto(codigo)
        
        elif opcion == "5":
            producto_dao.mostrar_inventario()
        
        elif opcion == "6":
            print("Saliendo")
            break
        
        else:
            print("opcion invalida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
