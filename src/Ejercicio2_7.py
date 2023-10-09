def sumaNumero (numero1:int,numero2:int, numero3:int):
    return numero1 + numero2 + numero3


if __name__ == "__main__":
    
    # Leer datos
    numero1 = int(input("Introduce un numero: "))
    numero2 = int(input("Introduce un segundo numero# Imprimimos datos: "))
    numero3 = int(input("Introduce un tercer numero: "))

    # Procesar datos
    suma = sumaNumero(numero1,numero2,numero3)

    # Imprimimos datos

    print("La suma de los numero es: ",suma)