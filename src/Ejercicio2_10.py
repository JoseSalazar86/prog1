def operacionAritmetica():
    operacion = round((3 + 2 / (2 * 5)) ** 2, 2)

    return "El resultado de la operacion aritmetica es: " +str(operacion)


if __name__=="__main__":
    print(operacionAritmetica())