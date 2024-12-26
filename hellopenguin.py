import hellopenguin

hellopenguin.init()

surface = hellopenguin.display.setmode(500,500)
caption = hellopenguin.display.set_caption("adding background and main image...")

backgroundimage = hellopenguin.image.load("background.png")
penguinimage = hellopenguin.image.load("hello penguin.png")
penguinrect = penguinimage.get_rect(500 // 2,(500 // 20-30))

text = hellopenguin.font.Font(None, 36).render("hello world", True,hellopenguin.Color("Black"))
textrect = text.get_rect(center = (500 // 2,500 // 2+ 110))

def gameloop():
    clock = hellopenguin.time.Clock()
    running = True
    while running:
        for event in hellopenguin.event.get:
            if event.type == hellopenguin.QUIT:
                running = False
        
        surface.blit(backgroundimage, (0, 0))
        surface.blit(penguinimage,penguinrect)
        surface.blit(text,textrect)

        hellopenguin.display.flip()
        clock.tick(30)
    hellopenguin.quit()

if __name__ == "__main__":
    gameloop()

