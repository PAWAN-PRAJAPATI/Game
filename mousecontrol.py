import pygame as py

py.init()

white = (255,255,255)

window = (400,400)
screen = py.display.set_mode(window)

clock = py.time.Clock()

done = False
while not done:
    for event in py.event.get():
        if event.type == py.QUIT:
            done = True
        elif event.type == py.MOUSEBUTTONDOWN:
            print(py.mouse.get_pos())
    screen.fill(white)
    py.display.flip()
    clock.tick(30)

py.quit()