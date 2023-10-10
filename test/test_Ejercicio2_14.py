from src.Ejercicio2_14 import cantidadPayasos,cantidadMuñecas,pesoTotal

def test_cantidadPayasos():
    assert cantidadPayasos(20) == 2240

def test_cantidadMuñecas():
    assert cantidadMuñecas(30) == 2250

def test_pesoTotal():
    assert pesoTotal(20,30) == 4490