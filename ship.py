import pygame

class Ship:
    """Класс для упровлением кораблем"""
    def __init__(self, ai_game):
        """Иницыализирует корабль и задает его начфльную позицию"""
        self.screen = ai_game.screen
        self.screen_rect =  ai_game.screen.get_rect()

        # загружает изоброжение коробля и получает прямоугольник
        self.imge = pygame.image.load('images/ship.bmp')
        self.rect = self.imge.get_rect

        #каждый новфй корабль появляется у нижнего края экрана 
        self.rect.midbottom = self.screen_rect.midbottom 
    def blitme(self):
        """рисует корабль в текушей позиции"""
        self.screen.blit(self.image,self.rect)

