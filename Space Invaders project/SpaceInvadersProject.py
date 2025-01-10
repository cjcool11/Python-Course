#Teacher, if you are here i have to tell you that the project is in the "spaceinvadershomework" folder...
import math
import pygame
import random

screen_width = 800
screen_height = 500
player_start_x = 370
player_start_y = 380
enemy_start_y_min = 50
enemy_start_y_max = 150
enemy_speed_x = 4
enemy_speed_y = 40
bullet_speed_y = 10
collision_distance = 27

pygame.init()

screen = pygame.display.set_mode((screen_width,screen_height))

background = pygame.image.load("backgroundforpython2.png")
pygame.display.set_caption("Space Invader")
icon = pygame.image.load("Ufo.png")
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
    enemy_X.append(random.randint(0,screen_width - 64))
    enemy_Y.append(random.randint(enemy_start_y_min,enemy_start_y_max))
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
    score = font.render("Score : " + str(score_value), True, (255,255,255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER!!!", True, (255,255,255))
    screen.blit(over_text, (200,250))

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))
    

