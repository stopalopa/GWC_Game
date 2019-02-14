import pygame

pygame.init()

screen_height = 480
screen_width = 500

win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('First Game')

walkRight = [pygame.image.load('png/R1.png'), pygame.image.load('png/R2.png'), pygame.image.load('png/R3.png'), pygame.image.load('png/R4.png'), pygame.image.load('png/R5.png'), pygame.image.load('png/R6.png'), pygame.image.load('png/R7.png'), pygame.image.load('png/R8.png'), pygame.image.load('png/R9.png')]
walkLeft = [pygame.image.load('png/L1.png'), pygame.image.load('png/L2.png'), pygame.image.load('png/L3.png'), pygame.image.load('png/L4.png'), pygame.image.load('png/L5.png'), pygame.image.load('png/L6.png'), pygame.image.load('png/L7.png'), pygame.image.load('png/L8.png'), pygame.image.load('png/L9.png')]
bg = pygame.image.load('Game/bg.jpg')
char = pygame.image.load('png/idle1.png')

clock = pygame.time.Clock()

pygame.mixer.music.load('got.mp3')
pygame.mixer.music.play(-1)


x = 50
y = 400
width = 64
height = 64
vel = 10
isJump = False
jumpCount = 10
fallCount = 6

#Need to keep track of which direction character is moving
left = False
right = False
walkCount = 0
win.blit(char, (x, y))

platform_x = 330
platform_y = 330
platform_width = 60
platform_height = 60


def redrawGameWindow():
    global walkCount
    win.blit(bg, (0, 0))
    if walkCount + 1 >= 9:
	walkCount = 0
    if left:
        win.blit(walkLeft[walkCount], (x, y))
	walkCount += 1
    elif right:
        win.blit(walkRight[walkCount], (x, y))
        walkCount += 1
    else:
        win.blit(char, (x, y))
    pygame.draw.rect(win, (0, 0, 0), (platform_x, platform_y, platform_width, platform_height))
    pygame.display.update()



run  = True
while run: 
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x >= vel:
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x <= screen_width - width - vel:
        x += vel
        right = True
        left = False
    else:
        right = False
        left = False
        walkCount = 0

    if not isJump:
        if keys[pygame.K_SPACE]:
            isJump = True
            right = False
            left = False
            walkCount = 0
        if y < 400 and (x > platform_x + platform_width - 34 or x+width < platform_x-49):
            if fallCount >= 3:
                y -= (fallCount ** 2) * -.6
            else:
                fallCount = 6

    else:
        if jumpCount >= -10:
	    neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * .7 * neg
            if y >= platform_y - height - 15 and x >= platform_x - 34 and x < platform_x + platform_width + width:
                y = platform_y - height - 15
                isJump = False
                jumpCount = 10
            else:
	        jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    redrawGameWindow()

pygame.quit()

