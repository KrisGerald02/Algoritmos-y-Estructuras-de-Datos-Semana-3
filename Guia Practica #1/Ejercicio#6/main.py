from models.clases import Factura

def main():
    factura = Factura()
    factura.agregar_producto("Producto A", 2, 50.0)
    factura.agregar_producto("Producto B", 1, 30.0)
    factura.establecer_descuento(10.0)

    try:
        factura.validar_integridad()
        print(factura.generar_reporte())
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
