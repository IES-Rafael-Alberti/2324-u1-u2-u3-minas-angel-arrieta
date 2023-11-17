from src.buscaminas import jugar, dibujar_tablero, cubrir_tablero, control_coordenada
from src.buscaminas import comprobar_celda, marcar_celda, revelar_celda, cubrir_minas
from src.buscaminas import input_posicion_usable, crear_tablero, verificacion_victoria
import pytest


@pytest.mark.parametrize(
    "inMensaje, outMensaje",
    [
        ("Entrada1", "Salida1"),
        ("Entrada2", "Salida2")
    ]
)
def test_function(inMensaje, outMensaje):
    assert function(inMensaje) == outMensaje


@pytest.mark.parametrize(
    "inMensaje, outMensaje",
    [
        ("Entrada1", "Salida1"),
        ("Entrada2", "Salida2")
    ]
)
def test_function(inMensaje, outMensaje):
    assert function(inMensaje) == outMensaje


@pytest.mark.parametrize(
    "inMensaje, outMensaje",
    [
        ("Entrada1", "Salida1"),
        ("Entrada2", "Salida2")
    ]
)
def test_function(inMensaje, outMensaje):
    assert function(inMensaje) == outMensaje