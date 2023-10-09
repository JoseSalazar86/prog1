def contarLetras(nombre :str):
    numeroLetras = len(nombre)
    nombreMay = nombre.upper()
    totalLetras = f"{nombreMay} tiene {numeroLetras} letras."

    return totalLetras

if __name__ == "__main__":

    nombre = input("Introduce tu nombre: ")

    contadorLetras = contarLetras(nombre)

    print(contadorLetras)
