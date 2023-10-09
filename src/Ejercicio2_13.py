def division(dividendo:int, divisor:int):
    cociente = dividendo // divisor
    resto = dividendo % divisor
    return (cociente,resto)

if __name__ == "__main__":
    dividendo = int(input("Introduce el dividendo de la division: "))
    divisor = int(input("Introduce el divisor de la division: "))

    resultado = division(divisor, dividendo)
    
    cociente, resto = resultado
    
    print(f"La división de {dividendo} y {divisor} da un cociente de {cociente} y un resto de {resto}")
