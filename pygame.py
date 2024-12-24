import pygame

pygame.init()

surface = pygame.display.setmode(500,500)
caption = pygame.display.set_caption("adding background and main image...")

backgroundimage = pygame.image.load("background.png")
penguinimage = pygame.image.load("hello penguin.png")
penguinrect = penguinimage.get_rect(500 // 2,(500 // 20-30))

text = pygame.font.Font(None, 36).render("hello world", True,pygame.Color("Black"))
textrect = text.get_rect(center = (500 // 2,500 // 2+ 110))

def gameloop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get:
            if event.type == pygame.QUIT:
                running = False
        
        surface.blit(backgroundimage, (0, 0))
        surface.blit(penguinimage,penguinrect)
        surface.blit(text,textrect)

        pygame.display.flip()
        clock.tick(30)
    pygame.quit()

if __name__ == "__main__":
    gameloop()

