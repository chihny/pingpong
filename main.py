from pygame import *
from random import randint
 
 
WIDHT = 600
HEIGHT = 500
FPS = 60
WIN_SCORE = 10
RESTART_TIME = 1000
 
 
BACKGROUND_COLOR = (randint(0, 255), randint(0, 255), randint(0, 255))
WHITE = (255, 255, 255)
RED = (150, 0, 0)
GREEN = (0, 150, 0)
 
window = display.set_mode((WIDHT, HEIGHT))
display.set_caption("Ping-Pong Yoy")
clock = time.Clock()
 
class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y, w, h):
        super().__init__()
        self.image = transform.scale(image.load(img), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
 
class Player(GameSprite):
    def __init__(self, up, down, img, x, y, w, h, speed):
        super().__init__(img, x, y, w, h)
        self.speed = speed
        self.up = up
        self.down = down
 
    def update(self):
        keys = key.get_pressed()
        if keys[self.up] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[self.down] and self.rect.y < HEIGHT - self.rect.height:
            self.rect.y += self.speed
 
racket1 = Player(K_w, K_s, "racket.png", 30, 200, 50, 150, 4)
racket2 = Player(K_UP, K_DOWN, "racket.png", 520, 200, 50, 150, 4)            
 
 
run = True
finish = False
 
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
 
    if not finish:
        window.fill(BACKGROUND_COLOR)
 
        racket1.reset()
        racket2.reset()
 
        racket1.update()
        racket2.update()
 
 
    display.update()
    clock.tick(FPS)