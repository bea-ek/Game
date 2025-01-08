import os
import sys

import pygame

def load_image(name):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Board:
    # создание поля
    def __init__(self):
        self.width = 5 # Кол-во клеток в ширину
        self.height = 7 # в высоту
        self.board = [[0] * self.width for _ in range(self.height)]
        #Значения положения поля по умолчанию
        self.left = 0
        self.top = 0
        #размер клетки
        self.cell_size = 120
        self.grass = load_image('grass.jpg')
        self.grass = pygame.transform.scale(self.grass, (self.cell_size, self.cell_size))
    # настройка положения поля
    def set_view(self, left, top):
        self.left = left
        self.top = top

    # отрисовка
    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                screen.blit(self.grass,(
                    x * self.cell_size + self.left, y * self.cell_size + self.top))


def main():
    pygame.init()
    size = 600, 840
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Инициализация игры')
    board = Board()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()