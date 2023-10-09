def cantidadPayasos(cantidad:int):
    peso = 112
    return peso*cantidad

def cantidadMuñecas(cantidad:int):
    peso = 75
    return peso * cantidad

def pesoTotal(cantidadPayaso:int,cantidadMuñeca:int):
    pesoPayaso = cantidadPayasos(cantidadPayaso)
    pesoMuñeca = cantidadMuñecas(cantidadMuñeca)
    return pesoPayaso + pesoMuñeca


if __name__ == "__main__":
    cantidadPayaso = int(input("Introduce la cantidad de payasos: "))
    cantidadMuñeca = int(input("Introduce la cantidad de muñecas: "))
    
    total = pesoTotal(cantidadPayaso, cantidadMuñeca)
    
    print(f"El peso total de {cantidadPayaso} payasos y {cantidadMuñeca} muñecas es {total} gramos.")