import pygame

window = pygame.display.set_mode((800, 600), pygame.RESIZABLE)

running = True
pygame.init()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    window.fill((0, 200, 190))
    pygame.display.flip()
