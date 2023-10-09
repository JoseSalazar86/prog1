def sumaBucle(numero):
    suma = 0
    for i in range(1, numero + 1):
        if(numero < 0):
            print("No puedes introducir numeros negativos")
        else:
            suma += i
            print("La suma desde 1 hasta :",numero,"es:",suma) 
    return suma


if __name__ == "__main__":
    numero = int(input("Introduce un numero: "))

    suma = sumaBucle(numero)

    print("la suma de los numeros es:",suma)