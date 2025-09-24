import sys 
import pygame

class AlienInvasio:
    """класс для управления ресурсами и поведением игры"""

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("👽Alien Invasion👽")
        while True:
             a=0
             a += 1
             pygame.display.set_caption(f"{a}👽Alien Invasion👽")

    
    def run_game(self):
        """запускает основной цикл игры"""
        while True:
            # Оьслеживание событий клава-Мишь
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # отоброжение последнего прорисовоного экрана 
            pygame.display.flip()

if __name__ == '__main__':
    #создание экземпляра и запуск игры.
    ai = AlienInvasio()
    ai.run_game()