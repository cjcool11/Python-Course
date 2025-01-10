import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

WHITE = (255, 255, 255)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Player and Enemies")

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()

    def update(self):
        pass

player = Sprite(WHITE, 50, 50)  
player.rect.x = SCREEN_WIDTH // 2
player.rect.y = SCREEN_HEIGHT // 2

enemies = pygame.sprite.Group()
for _ in range(3):
    enemy = Sprite(WHITE, 50, 50)
    enemy.rect.x = random.randint(0, SCREEN_WIDTH - 50)
    enemy.rect.y = random.randint(0, SCREEN_HEIGHT - 50)
    enemies.add(enemy)

all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(*enemies)

score = 0

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.rect.x -= 5
    if keys[pygame.K_RIGHT]:
        player.rect.x += 5
    if keys[pygame.K_UP]:
        player.rect.y -= 5
    if keys[pygame.K_DOWN]:
        player.rect.y += 5

    collided_enemies = pygame.sprite.spritecollide(player, enemies, True)
    score += len(collided_enemies)

    screen.fill((0, 0, 0))

    all_sprites.draw(screen)

    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", 1, WHITE)
    screen.blit(text, (5, 5))

    pygame.display.flip()

    clock.tick(30)

pygame.quit()
