import math
import pygame
import random

screen_width = 800
screen_height = 500
player_start_x = 370
player_start_y = 380
enemy_start_y_min = 50
enemy_start_y_max = 150
enemy_speed_x = 0.5
enemy_speed_y = 5
bullet_speed_y = 0.5
collision_distance = 27

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))

background = pygame.image.load("backgroundforpython2.png")
pygame.display.set_caption("Space Invader")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

playerImg = pygame.image.load("Player.png")
player_X = player_start_x
player_Y = player_start_y
player_X_change = 0

enemyImg = []
enemy_X = []
enemy_Y = []
enemy_X_change = []
enemy_Y_change = []
num_of_enemies = 6
for _i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("Enemy.png"))
    enemy_X.append(random.randint(0, screen_width - 64))
    enemy_Y.append(random.randint(enemy_start_y_min, enemy_start_y_max))
    enemy_X_change.append(enemy_speed_x)
    enemy_Y_change.append(enemy_speed_y)

bulletImg = pygame.image.load("Bullet.png")
bullet_X = 0
bullet_Y = player_start_y
bullet_X_change = 0
bullet_Y_change = bullet_speed_y
bullet_state = "ready"

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
text_X = 10
text_Y = 10

over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER!!!", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

def iscollision(enemy_X, enemy_Y, bullet_X, bullet_Y):
    distance = math.sqrt((enemy_X - bullet_X)**2 + (enemy_Y - bullet_Y)**2)
    return distance < collision_distance

running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_X_change = -0.5
            if event.key == pygame.K_RIGHT:
                player_X_change = 0.5
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bullet_X = player_X
                fire_bullet(bullet_X, bullet_Y)
        if event.type == pygame.KEYUP and event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
            player_X_change = 0

    player_X += player_X_change
    player_X = max(0, min(player_X, screen_width - 64))

    for i in range(num_of_enemies):
        if enemy_Y[i] > 340:
            for j in range(num_of_enemies):
                enemy_Y[j] = 2000
            game_over_text()
            break

        enemy_X[i] += enemy_X_change[i]
        if enemy_X[i] <= 0 or enemy_X[i] >= screen_width - 64:
            enemy_X_change[i] *= -1
            enemy_Y[i] += enemy_Y_change[i]

        if iscollision(enemy_X[i], enemy_Y[i], bullet_X, bullet_Y):
            bullet_Y = player_start_y
            bullet_state = "ready"
            score_value += 1
            enemy_X[i] = random.randint(0, screen_width - 64)
            enemy_Y[i] = random.randint(enemy_start_y_min, enemy_start_y_max)

        enemy(enemy_X[i], enemy_Y[i], i)

    if bullet_Y <= 0:
        bullet_Y = player_start_y
        bullet_state = "ready"
    elif bullet_state == "fire":
        fire_bullet(bullet_X, bullet_Y)
        bullet_Y -= bullet_Y_change

    player(player_X, player_Y)
    show_score(text_X, text_Y)
    pygame.display.update()