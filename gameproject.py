import hellopenguin

hellopenguin.init()

screen = hellopenguin.display.set_mode((800, 600))
hellopenguin.display.set_caption('Pygame Window')

running = True
while running:
    for event in hellopenguin.event.get():
        if event.type == hellopenguin.QUIT:
            running = False
    
    hellopenguin.display.flip()

hellopenguin.quit()
