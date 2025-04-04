import models.clases as c
import controllers.dao_controller as dao
producto_dao = dao.ProductoDao()
producto1 = c.Producto("P001", "Laptop", 1200.99, 5)
producto2 = c.Producto("P002", "Mouse", 25.50, 10)
producto_dao.agregar_producto(producto1)
producto_dao.agregar_producto(producto2)
producto_dao.mostrar_inventario()
producto_dao.actualizar_producto("P001", precio=1100.99, cantidad_stock=7)
producto_buscado = producto_dao.buscar_producto("P001")
if producto_buscado:
    print(f"Producto encontrado: {producto_buscado}")

producto_dao.eliminar_producto("P002")
producto_dao.mostrar_inventario()
