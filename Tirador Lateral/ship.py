import pygame

class Ship:
    """Una clase para gestionar la nave."""
    def __init__(self, ai_game):
        """Inicializa la nave y configura su posición inicial."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        
        # Carga la imagen de la nave y obtiene su rect.
        self.image = pygame.image.load('Tirador Lateral\\images\\ship_lateral.bmp')
        self.rect = self.image.get_rect()
        
        # Coloca inicialmente cada nave nueva en el centro de la parte inferior de la pantalla.
        self.rect.midleft = self.screen_rect.midleft
        
        # Guarda un valor decimal para la posición horizontal exacta de la nave.
        self.y = float(self.rect.y)
        
        # Bandera de movimiento; empieza con una bandera que no se mueve.
        self.moving_up = False
        self.moving_down = False
        
    def update(self):
        """Actualiza la posición de la nave en función de la bandera de movimiento."""
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
            
        # Actualiza el objeto rect de self.x.
        self.rect.y = self.y
        
    def blitme(self):
        """Dibuja la naveen su ubicación actual."""
        self.screen.blit(self.image, self.rect)