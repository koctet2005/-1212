import os
import pygame
import random

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert()
    return image




pygame.init()
size = width, height = 500, 400
screen = pygame.display.set_mode(size)
screen.fill(pygame.Color('White'))
running = True
all_sprites = pygame.sprite.Group()
sprite = pygame.sprite.Sprite()

class Bomb(pygame.sprite.Sprite):
    image = load_image("bomb.png")
    image.set_colorkey((0, 0, 0))
    image_boom = load_image("boom.png")
    image_boom.set_colorkey((0, 0, 0))

    def __init__(self, group):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite. Это очень важно !!!
        super().__init__(group)
        self.image = Bomb.image
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(width)
        self.rect.y = random.randrange(height)

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            self.image = self.image_boom

for _ in range(50):
    Bomb(all_sprites)

    
while running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    all_sprites.draw(screen)
    all_sprites.update(event)
    pygame.display.flip()


pygame.quit()