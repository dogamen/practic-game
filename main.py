import pygame

pygame.init()
screen = pygame.display.set_mode((600, 300)) #, flags = pygame.NOFRAME убрать рамку
pygame.display.set_caption('game') # название

running = True
while running: # бесконечный цикл для воспроизведения окна

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

