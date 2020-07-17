import pygame
pygame.init()
win = pygame.display.set_mode((500,500))
pygame.display.set_caption("Red bouncing ball")
bg = pygame.image.load('bg.jpg')
x = y = 250
width = 250
height = 50
vel = 5
run = True
jump =False

jumpcount = 10
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and  x > 30: x -= 15
    if keys[pygame.K_RIGHT] and x < 470 : x += 15
    if not jump:
        if keys[pygame.K_UP] and y >30: y -= 15
        if keys[pygame.K_DOWN] and y< 470: y += 15
        if keys[pygame.K_SPACE]: jump = True
    else:
        if jumpcount >= -10:
            neg = 1
            if jumpcount < 0:
                neg = -1
            y -= int((jumpcount**2)*0.4*neg)
            jumpcount -= 1
        else:
            jump = False
            jumpcount = 10
    win.blit(bg, (0, 0))
    pygame.draw.circle(win, (255, 0, 0), (x, y), 60)
    pygame.display.update()
    win.fill((0))
pygame.quit()
