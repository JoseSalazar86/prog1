def pesoImc(peso:int,altura:float):
    imc = round(peso / altura ** 2,2)
    return imc


if __name__ == "__main__":

    # Leemos datos
    peso = int(input("Introduce tu peso en kilos: "))
    altura = float(input("Introduce tu altura en metros: "))

    #Procesamos datos
    imc = pesoImc(peso,altura)

    #Imprimimos datos
    print("Tu IMC es de: ",imc)