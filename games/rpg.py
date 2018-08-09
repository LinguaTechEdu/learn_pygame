import pygame
from pygame.locals import *
from pygame.compat import geterror

GAME_ON = True
clock = pygame.time.Clock()


def load_image(name, colorkey=None):
    """Return a tuple with the image and it's area (size)."""
    try:
        image = pygame.image.load(name)
    except pygame.error:
        print ('Cannot load image:', name)
        raise SystemExit(str(geterror()))

    image = image.convert()
    image = pygame.transform.scale(image, (40, 60))
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()


class Player(pygame.sprite.Sprite):
    IDLE_IMAGE = 'images/Player/idle/1.png'
    IMAGE_PATH = 'images/Player/idle/'
    IMAGE_WALK_PATH = 'images/Player/Run/'
    IMAGES = ['1.png', '2.png', '3.png', '4.png']
    WALK_IMAGES = [IMAGE_PATH + image for image in IMAGES]

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image(self.IDLE_IMAGE, -1)
        self.pos = None
        self.speed_x = 0
        self.speed_y = 0

    def move_left(self):
        self.rect.x += 2

    def move_right(self):
        self.rect.x -= 2

    def jump(self):
        self.rect.y += 3
        self.rect.y -= 3

    # def walk(self):
    #     for p in self.WALK_IMAGES:


pygame.init()

screen = pygame.display.set_mode((400, 300))
background = pygame.Surface(screen.get_size())
background.fill((0, 0, 100))
player = Player()
player.pos = (100, 100,)
sprites = pygame.sprite.RenderPlain((player,))
keys = [False, False]

while GAME_ON:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME_ON = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            GAME_ON = False
        if event.type == pygame.KEYDOWN:
            if event.key == K_a:
                keys[0] = True
            elif event.key == K_d:
                keys[1] = True
        if event.type == pygame.KEYUP:
            if event.key == K_a:
                keys[0] = False
            elif event.key == K_d:
                keys[1] = False

    if keys[0]:
        player.move_right()
    elif keys[1]:
        player.move_left()

    sprites.update()

    screen.blit(background, (0, 0))
    sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)

