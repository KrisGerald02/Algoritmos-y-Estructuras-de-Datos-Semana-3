class Factura:
    def __init__(self):
        self._productos = []
        self._descuento = 0.0

    def agregar_producto(self, nombre, cantidad, precio):
        if cantidad <= 0 or precio < 0:
            raise ValueError("La cantidad debe ser mayor que 0 y el precio no puede ser negativo.")
        self._productos.append({
            'nombre': nombre,
            'cantidad': cantidad,
            'precio': precio
        })

    def establecer_descuento(self, descuento):
        if descuento < 0:
            raise ValueError("El descuento no puede ser negativo.")
        self._descuento = descuento

    def calcular_total(self):
        total = sum(producto['cantidad'] * producto['precio'] for producto in self._productos)
        total_con_descuento = total - self._descuento
        return total_con_descuento if total_con_descuento > 0 else 0.0

    def generar_reporte(self):
        reporte = "Reporte de factura:\n"
        for producto in self._productos:
            reporte += f"Producto: {producto['nombre']}, Cantidad: {producto['cantidad']}, Precio: {producto['precio']:.2f}\n"
        reporte += f"Descuento: {self._descuento:.2f}\n"
        reporte += f"Total a pagar: {self.calcular_total():.2f}\n"
        return reporte

    def validar_integridad(self):
        if not self._productos:
            raise ValueError("No hay productos en la factura.")
        for producto in self._productos:
            if producto['cantidad'] <= 0 or producto['precio'] < 0:
                raise ValueError(f"Producto {producto['nombre']} tiene cantidad o precio invalido.")


if __name__ == "__main__":
    factura = Factura()
    factura.agregar_producto("Producto A", 2, 50.0)
    factura.agregar_producto("Producto B", 1, 30.0)
    factura.establecer_descuento(10.0)

    try:
        factura.validar_integridad()
        print(factura.generar_reporte())
    except ValueError as e:
        print(f"Error: {e}")
 
