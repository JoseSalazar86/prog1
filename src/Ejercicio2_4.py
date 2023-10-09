def celciusFarenheint(celcius:int):
    return (celcius * 9/5) + 32

if __name__ == "__main__":

    #Leer datos
    celcius = int(input("Introduce los grados celcius"))

    #Procesar datos
    farenheit = celciusFarenheint(celcius)

    #Imprimir datos
    print("hay:",farenheit,"ºF")
    