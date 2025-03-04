# Autor: Rubén Tercero - 04/03/2025

from dados import Dado

dado_6 = Dado()
dado_10 = Dado(10)
dado_20 = Dado(20)

tiradas_6 = []
tiradas_10 = []
tiradas_20 = []

for tiradas in range(10):
    tiradas_6.append(dado_6.tirar_dado())
    tiradas_10.append(dado_10.tirar_dado())
    tiradas_20.append(dado_20.tirar_dado())
    
print(tiradas_6)
print(tiradas_10)
print(tiradas_20)

