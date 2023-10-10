from src.Ejercicio2_1 import saludos

def test_saludos():
    nombre1 = "Paquito"
    nombre2 = "Jose"
    assert saludos(nombre1) == "Hola, Paquito"
    assert saludos(nombre2) == "Hola, Jose"
