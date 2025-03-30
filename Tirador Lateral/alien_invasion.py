import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet


class AlienInvasion:
    """Clase general para gestionar los recursos y el comportamiento del juego"""
    
    def __init__(self):
        """Inicializa el juego y crea recursos"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        
        """        
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        """
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        #self.calico = Calico_electronico(self)
        
        # Configura el color de fondo
        self.bg_color = self.settings.bg_color
        
    def run_game(self):
        """Inicia el bucle principal para el juego"""
        while True:
            self._check_events()
            self.ship.update()            
            self._update_bullets()
            self._update_screen()
            self.clock.tick(60)
            
    def _check_events(self):
        """Responde a pulsaciones de teclas y eventos de ratón."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                    
    def _check_keydown_events(self, event):
        """Responde a pulsaciones de teclas."""
        if event.key == pygame.K_UP:
            # Mueve la nave a la derecha.
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_ESCAPE:
            sys.exit() 
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
            
    def _check_keyup_events(self, event):
        """Responde a libreciones de teclas"""
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False
            
    def _fire_bullet(self):
        """Crea una nueva bala y la añade al grupo de balas."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self) 
            self.bullets.add(new_bullet)
        
    def _update_screen(self):
        """Actualiza las imágenes a la pantalla y cambia a la pantalla nueva."""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        #self.calico.blitme()
                
        pygame.display.flip()
        
    def _update_bullets(self):
        """Actualiza la posición de las balas y se deshace de las viejas."""
        self.bullets.update()
        
        # Se deshace de las balas que han desaparecido.
        for bullet in self.bullets.copy():
            if bullet.rect.right >= self.settings.screen_width:
                self.bullets.remove(bullet)
        # print(len(self.bullets))
    
if __name__ == '__main__':
    # Hace una instancia del juego y lo ejecuta
    ai = AlienInvasion()
    ai.run_game()