import pygame

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Rectangle Sprites")

white = (255, 255, 255)
blue = (0, 0, 255)

rect_x = 100
rect_y = 100
rect_width = 50
rect_height = 50
rect_speed = 1

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        rect_x -= rect_speed
    if keys[pygame.K_RIGHT]:
        rect_x += rect_speed
    if keys[pygame.K_UP]:
        rect_y -= rect_speed
    if keys[pygame.K_DOWN]:
        rect_y += rect_speed

    screen.fill(white)
    
    pygame.draw.rect(screen, blue, [rect_x, rect_y, rect_width, rect_height])

    pygame.display.flip()

pygame.quit()
