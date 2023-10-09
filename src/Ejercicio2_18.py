def nombreCompleto(nombre:str):
    nombreMin = nombre.lower()
    nombreMay = nombre.upper()
    separarNombre = nombre.split()
    # Crear una versión del nombre con la primera letra de cada palabra en mayúscula
    nombrePriMayus = ' '.join([palabra.capitalize() for palabra in separarNombre])
    return nombreMin, nombreMay, nombrePriMayus

if __name__ == "__main__":

    nombre = input("Introduce tu nomrbe: ")

    resultado = nombreCompleto(nombre)


    print(f"Nombre completo en minúsculas: {resultado[0]}")
    print(f"Nombre completo en mayúsculas: {resultado[1]}")
    print(f"Nombre completo con la primera letra en mayúscula: {resultado[3]}")