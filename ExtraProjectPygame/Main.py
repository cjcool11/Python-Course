import pygame
import sys

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Maze Game")

wall_texture =pygame.image.load("C:/Users/aisha/OneDrive/Documents/Python Course/ExtraProjectPygame/wall_texture.png")
player_texture =player_texture = pygame.image.load("C:/Users/aisha/OneDrive/Documents/Python Course/ExtraProjectPygame/player_texture.png")
background_texture = pygame.image.load("background.png")

wall_texture = pygame.transform.scale(wall_texture, (40, 40))
player_texture = pygame.transform.scale(player_texture, (40, 40))

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
]

player_x, player_y = 1, 1

clock = pygame.time.Clock()

def draw_maze():
    screen.blit(background_texture, (0, 0))
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == 1:
                screen.blit(wall_texture, (col * 40, row * 40))
    screen.blit(player_texture, (player_x * 40, player_y * 40))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and maze[player_y - 1][player_x] == 0:
        player_y -= 1
    if keys[pygame.K_DOWN] and maze[player_y + 1][player_x] == 0:
        player_y += 1
    if keys[pygame.K_LEFT] and maze[player_y][player_x - 1] == 0:
        player_x -= 1
    if keys[pygame.K_RIGHT] and maze[player_y][player_x + 1] == 0:
        player_x += 1

    draw_maze()
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()