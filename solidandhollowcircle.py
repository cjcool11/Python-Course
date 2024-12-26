import pygame

pygame.init()

screen = pygame.display.set_mode((500,500))

randomcolor = (24,60,98)

pygame.draw.circle(screen,randomcolor, (300,300), 50)
pygame.draw.circle(screen,randomcolor, (100,100), 50, 3)

pygame.display.update()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

if __name__ == "__main__":
    pygame.gameloop()


