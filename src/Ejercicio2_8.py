def dosVariables(numero:int,suma:int):
    suma += numero
    return suma


if __name__ == "__main__":
    # Inicializamos la variable suma a 0
    suma = 0

    # Leemos los datos
    
    numero = int(input("Introduce un primer numero: "))
    numero = int(input("Introduce un segundo numero: "))
    numero = int(input("Introduce un tercer numero: "))

    # Procesamos los datos
    suma = dosVariables(numero, suma)
    suma = dosVariables(numero, suma)
    suma = dosVariables(numero, suma)

    # Imprimimos los datos
    print("La suma de los numeros es:", suma)