
def cuentaAhorro(cantidad:float,):
    cantidad *= 1.04
    return round(cantidad,2)

if __name__ == "__main__":

    # Leemos datos
    cantidad = float(input("Introduce una cantidad: "))

    # Procesamos datos y Imprimimos los datos
    
    print(f"El deposito es de cantidad: ",cantidad)
    print(f"Cantidad de ahorros después de 1 año: {cuentaAhorro(cantidad)}")
    cantidad=cuentaAhorro(cantidad)
    print(f"Cantidad de ahorros después de 2 año: {cuentaAhorro(cantidad)}")
    cantidad=cuentaAhorro(cantidad)
    print(f"Cantidad de ahorros después de 3 año: {cuentaAhorro(cantidad)}")
