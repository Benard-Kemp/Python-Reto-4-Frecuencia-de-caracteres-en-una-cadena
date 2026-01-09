import pytest
from reto_04_frecuencia_caracteres import frecuencia_caracteres


def test_texto_normal():
    assert frecuencia_caracteres("hola") == {
        "h": 1,
        "o": 1,
        "l": 1,
        "a": 1,
    }


def test_texto_con_espacios():
    assert frecuencia_caracteres("hola hola")[" "] == 1


def test_cadena_vacia():
    assert frecuencia_caracteres("") == {}


def test_none_devuelve_diccionario_vacio():
    assert frecuencia_caracteres(None) == {}


def test_tipo_incorrecto_lanza_typeerror():
    with pytest.raises(TypeError):
        frecuencia_caracteres(123)
