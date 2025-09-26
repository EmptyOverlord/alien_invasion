import sys 
import pygame
from settings import Settings


class AlienInvasio:
    """класс для управления ресурсами и поведением игры"""

    def __init__(self):
        pygame.init()
        self.colck = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_heigt))

        pygame.display.set_caption("👽Alien Invasion👽🚀")


    def run_game(self):
        """запускает основной цикл игры"""
        while True:
            # Оьслеживание событий клава-Мишь
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    sys.exit()
            #при каждом проходе цыкла перерислвывается экран
            self.screen.fill(self.settings.bg_color)
            # отоброжение последнего прорисовоного экрана 
            pygame.display.flip()
            self.colck.tick(60)

if __name__ == '__main__':
    #создание экземпляра и запуск игры.
    ai = AlienInvasio()
    ai.run_game()