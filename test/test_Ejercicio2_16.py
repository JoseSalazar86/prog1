from src.Ejercicio2_16 import barrasPan

def test_barraPan():

    panNoDia = 5
    panDelDia, costeFinal, descuento = barrasPan(panNoDia)
    assert(panDelDia, 3.49)  
    assert(descuento, 2.094)  
    assert(costeFinal, 15.68)  