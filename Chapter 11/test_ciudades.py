from ciudad_funciones import ciudad_pais

def test_ciudad_pais():
    resultado = ciudad_pais("santiago", "chile")
    assert resultado == "Santiago, Chile"
    
def test_ciudad_pais_habitantes():
    resultado = ciudad_pais("santiago", "chile", 5000000)
    assert resultado == "Santiago, Chile - habitantes=5000000"