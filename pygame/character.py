import pygame
pygame.init()
win = pygame.display.set_mode((500,480))
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')
pygame.display.set_caption("character")

clock =  pygame.time.Clock()
x = 50
y=400
width = 40
height = 60
vel = 5
run = True
jump =False
left = False
right= False
walkcount = 0
jumpcount =10


def redrawgamewindow():
    global walkcount

    win.blit(bg,(0,0))
    if walkcount +1 >= 27:
        walkcount = 0
    if left:
        win.blit(walkLeft[walkcount//3],(x,y))
        walkcount +=1
    elif right:
        win.blit(walkRight[walkcount//3],(x,y))
        walkcount+=1
    else:
        win.blit(char, (x,y))
    pygame.display.update()
    win.fill((0))

jumpcount = 10
while run:
    #pygame.time.delay(100)
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and  x > vel:
        x -= vel
        left = True
        right = False

    elif keys[pygame.K_RIGHT] and x < 500 - width - vel:
        right = True
        left = False
        x += vel
    else:
        right = left = False
        walkcount = 0
    if not jump:
        #if keys[pygame.K_UP] and y >30: y -= 15
        #if keys[pygame.K_DOWN] and y< 470: y += 15
        if keys[pygame.K_SPACE]:
            jump = True
            right = left = False
            walkcount = 0
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
    redrawgamewindow()

pygame.quit()
