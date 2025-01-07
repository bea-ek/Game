import pygame


# class Rules:

class Board:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 800))
        pygame.display.set_caption("Crazy Road)))")
        background = pygame.image.load('field.png').convert()
        running = True
        while running:
            for event in pygame.event.get():
                self.screen.blit(background, (0, 0))
                pygame.display.update()
                if event.type == pygame.QUIT:
                    running = False
        pygame.display.flip()
        pygame.quit()


if __name__ == '__main__':
    board = Board()
    # board.run()
