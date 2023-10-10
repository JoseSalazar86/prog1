from src.Ejercicio2_15 import cuentaAhorro

def test_cuentaAhorro():

    assert cuentaAhorro(100.0) == 104.0
    assert cuentaAhorro(104.0) == 108.16
    assert cuentaAhorro(108.16) == 112.49

