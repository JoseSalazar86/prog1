def vocalIntroducida(frase,vocal):
    vocalMayuscula = frase.replace(vocal,vocal.upper())

    return vocalMayuscula




if __name__ == "__main__":

    frase = input("Introduce una frase: ")

    vocal = input("introduce una vocal: ")

    vocalMayuscula = vocalIntroducida(frase,vocal)

    print(f"La frase con la vocal en mayusculas: {vocalMayuscula}")