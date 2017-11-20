import pygame

pygame.init()
screen = pygame.display.set_mode((400, 400))
rect = pygame.Rect(180, 180, 20, 20)
clock = pygame.time.Clock()
d=1
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            raise

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), rect)
    rect.move_ip(d, 0)
    if not screen.get_rect().contains(rect):
        d *= -1

    pos = pygame.mouse.get_pos()

    # print the 'absolute' mouse position (relative to the screen)
    print ('absoulte:', pos)

    # print the mouse position relative to rect
    print('to rect:', pos[0] - rect.x, pos[1] - rect.y)

    clock.tick(100)
    pygame.display.flip()