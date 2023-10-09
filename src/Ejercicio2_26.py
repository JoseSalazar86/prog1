def mostrarProductos(productos):
    
    listaProductos = productos.split(',')

    
    for producto in listaProductos:
        print(producto.strip())  

if __name__ == "__main__":
    
    productos = input("Introduce los productos de la cesta de compra, separados por comas: ")

    
    mostrarProductos(productos)
