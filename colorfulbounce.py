import pygame
import random

pygame.init()

sprite_color_change_event = pygame.USEREVENT + 1
background_color_change_event = pygame.USEREVENT + 2

green = pygame.Color("green")
red = pygame.Color("red")
blue = pygame.Color("blue")

cyan = pygame.Color("cyan")
dark_blue = pygame.Color("darkblue")
orange = pygame.Color("orange")
magenta = pygame.Color("magenta")

class Sprite1(pygame.sprite.Sprite):
    def __init__(self,color,height,width):
        super().__init__()
        self.image = pygame([width,height])
        self.image.fillcolor(color)
        self.rect = self.get_rect()
        self.velocity = [random.choice([-1,1]),random.choice([-1,1])]
    
    def update(self):
        self.rect.move_ip(self.velocity)
        boundary_hit = False
        if self.rect.left <= 0 or self.rect.right >= 500:
            self.velocit[0] = -self.velocity[0]
            boundary_hit = True
        if self.rect.top <= 0 or self.rect.bottom >= 400:
            self.velocity[1] = -self.velocity[1]
            boundary_hit = True

        if boundary_hit:
            pygame.event.post(pygame.event.Event(sprite_color_change_event))
            pygame.event.post(pygame.event.Event(background_color_change_event))
    def change_color(self):
        pygame.image.fill(random.choice([green,red,blue]))

    def change_background_color():
        global bg_color
        bg_color = random.choice([cyan,dark_blue,orange,magenta])

all_sprites_list = pygame.sprite.Group()
sp1 = Sprite1(green,20,30)
sp1.rect.x = random.randint(0,480)
sp1.rect.y = random.randint(0,370)
all_sprites_list.add(sp1)

screen = pygame.display.set_mode(())