import sys, pygame
pygame.init()

size = width, height = 400, 300
speed = [1, 1]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("media/bouncy_ball.gif")
ballrect = ball.get_rect()
BOUNCE_BALL = True

while BOUNCE_BALL:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            BOUNCE_BALL = False

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    # The screen is constantly redrawn dozens of times each second
    # ...until the loop is stopped by the player quiting the game.
    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
