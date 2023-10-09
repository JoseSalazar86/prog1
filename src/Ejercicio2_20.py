def telefono(numeroTelefono):
    separador = numeroTelefono.split('-')
    sinPrefijoExtension = separador[1]
    return sinPrefijoExtension

if __name__ == "__main__":
    numeroTelefono = input("Introduce el numero de telefono con el prefijo y extension ejemplo +34-123456789-12: ")

    mostrarTelefono = telefono(numeroTelefono)

    print(f"El numero de telefono sin el prefijo y sin extension es: {mostrarTelefono}")
