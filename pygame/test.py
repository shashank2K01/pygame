import pygame
pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("just like life")
is_blue = True
run = True
x = 30
y = 30
clock = pygame.time.Clock()
surface = pygame.Surface((100 ,200), pygame.SRCALPHA)
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                is_blue = not is_blue
    screen.fill((255, 255, 255))
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y -= 3
    if pressed[pygame.K_DOWN]:y += 3
    if pressed[pygame.K_RIGHT]: x += 3
    if pressed[pygame.K_LEFT]: x -= 3

    if is_blue:
        color= (0,128,255)
    else:
        color = (255,100,0)
    pygame.draw.rect(screen,color,pygame.Rect(x,y,60,60))
    clock.tick(60)


    pygame.display.flip()