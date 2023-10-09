def  invertirFrase(frase):
    fraseInvertida =""
    for caracter in frase:
        fraseInvertida = caracter + fraseInvertida
    return fraseInvertida

def invertidaFrase(frase):
    return frase[::-1]

def invertFrase(frase):
    palabras = frase.split()
    fraseInvertida = ""

    for palabra in palabras:
        fraseInvertida = palabra + " " + fraseInvertida
    
    fraseInvertida = fraseInvertida.strip()
    
    return fraseInvertida
  
if __name__ == "__main__":
    frase = input("introduce una frase: ")


    fraseInvertida = invertirFrase(frase)
    fraseInverti = invertidaFrase(frase)
    fraseInvert = invertFrase(frase)

    print(f"La frase invertida es: {fraseInvertida}")
    print(f"La frase invertida es: {fraseInverti}")
    print(f"La frase invertida es: {fraseInvert}")