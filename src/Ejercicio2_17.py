def repetirNombre(nombre:str,numero:int):
    contador =""
    for i in  range(numero):
        contador += nombre
    return contador


if __name__ == "__main__":
    nombre = input("introduce tu nombre: ")

    numero = int(input("Introduce cuantas veces quieres que se repita: "))

    nombre = repetirNombre(nombre,numero)
    print(f"Te llamas {nombre}")