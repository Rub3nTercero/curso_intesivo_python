# Autor: Rubén Tercero - 10/03/2025

import pytest
from empleado import Empleado

@pytest.fixture
def empleado():
    empleado = Empleado("ruben", "tercero", 24000)
    return empleado

def test_dar_aumento_predeterminado(empleado):
    empleado.dar_aumento()
    assert empleado.salario == 29000
    
def test_dar_aumento_personalizado(empleado):
    empleado.dar_aumento(10000)
    assert empleado.salario == 34000