import sys 
import pygame

class AlienInvasio:
    """класс для управления ресурсами и поведением игры"""

    def __init__(self):
        pygame.init()
        self.colck = pygame.time.Clock()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("👽Alien Invasion👽🚀")
        self.bg_color = (230, 230, 230) # ! поменять на список чтобы можно было менять цвет фона прямо в игре или при событии

    
    def run_game(self):
        """запускает основной цикл игры"""
        while True:
            # Оьслеживание событий клава-Мишь
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    sys.exit()
            #при каждом проходе цыкла перерислвывается экран
            self.screen.fill(self.bg_color)
            # отоброжение последнего прорисовоного экрана 
            pygame.display.flip()
            self.colck.tick(60)

if __name__ == '__main__':
    #создание экземпляра и запуск игры.
    ai = AlienInvasio()
    ai.run_game()