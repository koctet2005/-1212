import os
import pygame
import random
import time

def load_image(name, colorkey=None):
    fullname = os.path.join('dino', name)
    image = pygame.image.load(fullname).convert()
    return image


WHITE = (255, 255, 255)
clock =  pygame.time.Clock() 
clock.tick(50)
pygame.init()
size = width, height = 1000, 600
screen = pygame.display.set_mode(size)
screen.fill(pygame.Color('White'))
running = True
all_sprites = pygame.sprite.Group()
sprite = pygame.sprite.Sprite()
i = 0
y = 0
spi = []
spi2 = []
perv = 0
nogat = 0
timee = 0
f = open('text.txt', 'r')
l = [line.strip() for line in f]

class Dino(pygame.sprite.Sprite):
    global running
    i = 0
    y = 0
    image = load_image("ctoit.jpg")
    image_ctoit = load_image("ctoit.jpg")
    image_ctoit2 = load_image("ctoit2.jpg")
    image_ctoit3 = load_image("ctoit3.jpg")
    image_leg = load_image("leg.jpg")
    image_leg2 = load_image("leg2.jpg")
    

    def __init__(self, group):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite. Это очень важно !!!
        super().__init__(group)
        self.image = Dino.image
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 250
        self.y = 0
        self.ix = 6
        self.koln = 0
    def update(self, *arg):
        if game == 1:
            self.rect.x = 100
            self.rect.y = 250
            self.y = 0
            self.ix = 6
            self.koln = 0
        spi.append(self.rect) 
        if running:
            if (i) % 10 == 0 or (i) % 10 == 5:
                if self.y == 0:
                    self.rect.y = 250
                    if i % 3 == 0:
                        self.image = self.image_ctoit
                    elif i % 3 == 1:
                        self.image = self.image_ctoit3
                    else:
                        self.image = self.image_ctoit2
            
     #--прыжек       
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP] and self.y == 0:
                self.y = 1
                self.iz = 6
            
         #нагнулся-------------------------------   
            
            if keys[pygame.K_DOWN]:
                 self.rect.y = 284
                 self.y = 0
                 if (i) % 10 == 0 or (i) % 10 == 5:
                     if i % 2 == 0:
                        self.image = self.image_leg
                     elif i % 2 == 1:
                        self.image = self.image_leg2

            
      #------------------------------ сам прыжек
            if self.y == 1:
                self.rect.y -= self.iz
                self.iz -= 0.09
                if self.rect.y - self.iz > 250:
                    self.rect.y = 250
                    self.iz = 6
                    self.y = 0

            

#----------------------------------------------------------
t = time.time()
Dino(all_sprites)
class k(pygame.sprite.Sprite):
    global running
    i = 0
    y = 0
    image_kk = load_image("kaktyc.jpg")
    image_k1 = load_image("kaktyc.jpg")
    image_k2 = load_image("kaktyc2.jpg")
    image_k3 = load_image("kaktyc3.jpg")
    image_k4 = load_image("kaktyc4.jpg")
    image_let = load_image("let.jpg")
    image_let2 = load_image("let2.jpg")

    def __init__(self, group):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite. Это очень важно !!!
        super().__init__(group)
        self.image = k.image_k1
        self.rect = self.image.get_rect()
        self.rect.x = 1000
        self.rect.y = 280
        self.c = 2.5
        self.r = 0
      
    def update(self, *arg):
        if game == 1:
            self.rect.x = 1000
            self.rect.y = 280
            self.y = 0
            self.ix = 6
            self.koln = 0
            t = time.time()
        spi2.append(self.rect)
        if self.rect.colliderect(spi[len(spi) - 1]):
             running = False
             return running
        self.rect.x -= self.c
        
        if self.rect.x < -100:
            self.r = random.randint(0, 4)
            self.rect.x = 1000

            if self.r == 0:
                self.rect.y = 280
                self.image = self.image_k1
            if self.r == 1:
                self.rect.y = 280
                self.image = self.image_k2
            if self.r == 2:
                self.rect.y = 280
                self.image = self.image_k3
            if self.r == 3:
                self.rect.y = 280
                self.image = self.image_k4
            if self.r == 4:
                self.rect.y = random.randint(50, 280)
        
        if  i % 10 == 0 or 5:
            if self.r == 4:
                if i % 10 == 0:
                    self.image = self.image_let
                if i % 10 == 5:
                    self.image = self.image_let2            
        
       
    def d():
        font = pygame.font.Font(None, 50)
        text = font.render(str(tim), 1, (255, 255, 255))
        screen.blit(text, (500, 100))
        text1 = font.render(l[0], 1, (255, 255, 255))
        screen.blit(text1, (800, 100))
    
    
class rect(pygame.sprite.Sprite):
    image = load_image("kaktyc.jpg")
    def __init__(self, group):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite. Это очень важно !!!
        super().__init__(group)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 480

game = 0        
keys = pygame.key.get_pressed()
k(all_sprites)
WHITE = (255, 255, 255)
running1 = True

while running1:
    running = True
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                running1 = False
       
        i += 1

        all_sprites.draw(screen)
        all_sprites.update(event)
        t1 = time.time()
        if spi2[len(spi2) - 1].colliderect(spi[len(spi) - 1]):
            running = False
        pygame.draw.line(screen, WHITE, [0, 348],  [1000, 348],  5 )
        tim = (t1 - t) // 1
        tim = int((str(tim).split('.')[0]))
        k.d()
        if game == 1:
            game = 0
            i = 0
            t = time.time()
        time.sleep(0.01)
        pygame.display.flip()
        
        
    print('твой результат', end=' ')
    print(tim)
    print('лучший результат', end=' ')
    print(l[0])
    if int(tim * 10) > int(l[0]) * 10:
        f = open('text.txt', 'w')
        f.write(str(tim))
        f.close()
    game = 1
    
   

pygame.quit()

