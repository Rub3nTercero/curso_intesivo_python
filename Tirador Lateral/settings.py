class Settings:
    """Una clase para guardar toda la configuración de Alien Invasion."""
    
    def __init__(self):
        """Inicializa la configuración del juego."""
        # Configuración de la pantalla
        self.screen_width = 1200
        self.screen_height = 720
        self.bg_color = (173, 216, 230)
        
        # Configuración de la nave.
        self.ship_speed = 2.5
        
        # Configuración de las balas.
        self.bullet_speed = 3.5
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        