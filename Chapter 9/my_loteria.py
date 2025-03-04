from loteria import Loteria

loteria = Loteria()
loteria.empezar_loteria()
# loteria.comprobar_numero('0B330')
intentos = loteria.probabilidad_loteria()
print(f"Número de intentos hasta ganar la lotería: {intentos}")