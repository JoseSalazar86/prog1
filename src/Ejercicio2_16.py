def barrasPan(panNoDia:int):
    porcentaje = 0.6
    panDelDia = 3.49
    descuento = panDelDia * porcentaje
    costeFinal = (panDelDia - descuento) * panNoDia
    return panDelDia, descuento, costeFinal

if __name__ == "__main__":

    #Leemos los datos
    panNoDia = int(input("Introduce las barras de pan que no son frescas: "))

    #Procesamos los datos
    panDelDia ,costeFinal,descuento = barrasPan(panNoDia)

    #Imprimimos los datos

    print(f"El precio de la barra de pan es {panDelDia}€,\nEl descuento por no ser fresca o del dia es {descuento:.2f}€,\nEl precio final de todas las barras no fresca es {costeFinal:.2f}€")