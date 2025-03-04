# Autor: Rubén Tercero - 04/03/2025

class Car:
    """Una simple intento de representar un coche."""

    def __init__(self, make, model, year):
        """Inicializa los atributos para describir un coche."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Devuelve un nombre descriptivo correctamente formateado."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Imprime una frase mostrando el kilometraje del vehículo."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Establece la lectura del cuentakilómetros a un valor dado.
        Rechaza el cambio si se intenta reducir el kilometraje.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Incrementa la lectura del cuentakilómetros para el valor dado."""
        self.odometer_reading += miles


class Battery:
    """Un simple intento de modelar una batería para un coche eléctrico."""

    def __init__(self, battery_size=40):
        """Inicializa los atributos de la batería."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Imprime una frase que describe el tamaño de la batería."""
        print(f"Esta pila tiene {self.battery_size}-kWh de batería.")
        
    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles on a full charge.")
        
    def upgrade_battery(self):
        if self.battery_size != 65:
            self.battery_size = 65

class ElectricCar(Car):
    """Representa aspectos de un coche propios de los vehículos eléctricos."""

    def __init__(self, make, model, year):
        """
        Inicializa los atributos de la clase base.
        Luego inicializa los atributos específicos de un coche eléctrico.
        """
        super().__init__(make, model, year)
        self.battery = Battery()

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()
my_leaf.battery.upgrade_battery()
my_leaf.battery.get_range()
