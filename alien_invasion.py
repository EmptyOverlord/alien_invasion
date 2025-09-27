import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Класс для управления ресурсами и поведением игры"""

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()  # создаем экземпляр класса Settings

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        self.ship = Ship(self)

        pygame.display.set_caption("👽Alien Invasion👽🚀")

    def run_game(self):
        """Запускает основной цикл игры"""
        while True:
            # Отслеживание событий клавиатуры и мыши
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # При каждом проходе цикла перерисовывается экран
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # Отображение последнего прорисованного экрана
            pygame.display.flip()
            self.clock.tick(60)


if __name__ == '__main__':
    # Создание экземпляра и запуск игры.
    ai = AlienInvasion()
    ai.run_game()
