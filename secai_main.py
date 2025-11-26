import pygame

pygame.init()
screen = pygame.display.set_mode((480, 320))
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 255, 0), (100, 80, 200, 120))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
