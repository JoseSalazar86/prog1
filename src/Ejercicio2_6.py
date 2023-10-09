def calculaPrecio(precioFinal:int):
    precio = precioFinal / 1.10
    iva = precio * 0.10
    return precio,iva

def mensaje_precio_sin_iva(precio,iva):
    return print(f"Precio sin IVA: {precio}",f"\nIVA: {iva}")
if __name__ == "__main__":
    # Leer datos
    precioFinal= int(input("Introduce el precio final del articulo: "))

    
    # Procesar datos
    precio, iva = calculaPrecio(precioFinal)

    # Imprimimos datos
    mensaje_precio_sin_iva(precio,iva)