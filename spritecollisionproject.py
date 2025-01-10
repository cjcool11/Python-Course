import pygame
import random

pygame.init()

screen_width, screen_height = 500, 400

movement_speed = 2.5
font_size = 72

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sprite Color Change")

background_image = pygame.transform.scale(pygame.image.load("backgroundforpython2.png"), (screen_width, screen_height))

Font = pygame.font.SysFont("Times New Roman", font_size)

CHANGE_COLOR = pygame.USEREVENT + 1

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
    
    def move(self, x_change, y_change):
        self.rect.x = max(min(self.rect.x + x_change, screen_width - self.rect.width), 0)
        self.rect.y = max(min(self.rect.y + y_change, screen_height - self.rect.height), 0)
    
    def change_color(self, color):
        self.image.fill(color)

all_sprites = pygame.sprite.Group()

sprite1 = Sprite(pygame.Color("blue"), 20, 30)
sprite1.rect.x, sprite1.rect.y = random.randint(0, screen_width - sprite1.rect.width), random.randint(0, screen_height - sprite1.rect.height)
all_sprites.add(sprite1)

sprite2 = Sprite(pygame.Color("red"), 20, 30)
sprite2.rect.x, sprite2.rect.y = random.randint(0, screen_width - sprite2.rect.width), random.randint(0, screen_height - sprite2.rect.height)
all_sprites.add(sprite2)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_c:
            pygame.event.post(pygame.event.Event(CHANGE_COLOR))
        elif event.type == CHANGE_COLOR:
            new_color1 = pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            new_color2 = pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            sprite1.change_color(new_color1)
            sprite2.change_color(new_color2)
    
    keys = pygame.key.get_pressed()
    x_change = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * movement_speed
    y_change = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * movement_speed
    sprite1.move(x_change, y_change)

    screen.blit(background_image, (0, 0))
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
