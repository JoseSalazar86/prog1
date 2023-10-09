def precioIva(importe,iva):
    return importe * (iva /100)+ importe


if __name__ == "__main__":
    # Leer datos
    importe = int(input("Introduce el importe del articulo: "))
    iva = int(input("introduce el iva: "))

    # Procesar datos
    precioFinal = precioIva(importe,iva)


    # mostrar resultados
    print("El precio del producto con iva es:",str(precioFinal))