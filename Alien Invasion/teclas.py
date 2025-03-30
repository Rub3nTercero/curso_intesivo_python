import pygame
import sys

class Imprimir_Teclas:
    
    def __init__(self):
        """Inicializa el juego y crea recursos"""
        pygame.init()
        self.clock = pygame.time.Clock()
        
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        
        self.fuente = pygame.font.Font(None, 74)
        self.text_color = (0,0,0)
        self.texto = self.fuente.render("", True, self.text_color)
        
        self.bg_color = (255, 255, 255)
        
    def run_game(self):
        while True:
            self._check_events()
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
        if event.key == pygame.K_RIGHT:
            text = f"Estas pulsando la tecla derecha."
            self.texto = self.fuente.render(text, True, self.text_color)
        elif event.key == pygame.K_LEFT:
            text = f"Estas pulsando la tecla izquierda."
            self.texto = self.fuente.render(text, True, self.text_color)
        elif event.key == pygame.K_UP:
            text = f"Estas pulsando la tecla de arriba."
            self.texto = self.fuente.render(text, True, self.text_color)
        elif event.key == pygame.K_DOWN:
            text = f"Estas pulsando la tecla de abajo."
            self.texto = self.fuente.render(text, True, self.text_color)
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
            
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            text = ""
            self.texto = self.fuente.render(text, True, self.text_color)
        elif event.key == pygame.K_LEFT:
            text = ""
            self.texto = self.fuente.render(text, True, self.text_color)
        elif event.key == pygame.K_UP:
            text = ""
            self.texto = self.fuente.render(text, True, self.text_color)
        elif event.key == pygame.K_DOWN:
            text = ""
            self.texto = self.fuente.render(text, True, self.text_color)
            
    def _update_screen(self):
        self.screen.fill(self.bg_color)
        texto_rect = self.texto.get_rect()
        texto_rect.center = self.screen.get_rect().center
        self.screen.blit(self.texto, texto_rect)
        pygame.display.flip()
        
if __name__ == '__main__':
    teclas = Imprimir_Teclas()
    teclas.run_game()