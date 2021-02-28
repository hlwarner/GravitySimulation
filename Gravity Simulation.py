# https://www.youtube.com/watch?v=YrNpkuVIFdg&t=814s

# PyMunk library - 2D physics engine.
# PyGame library - graphical interface creator.
# sys library    - way of managing python runtime environment

import pygame, sys, pymunk

def create_apple(space):
    body = pymunk.Body(1, 100, body_type=pymunk.Body.DYNAMIC)
    body.position = (400,0)
    shape = pymunk.Circle(body,80)
    space.add(body, shape)
    return shape

def draw_apples(apples):
    for apple in apples:
        pos_x = int(apple.body.position.x)
        pos_y = int(apple.body.position.y)
        pygame.draw.circle(screen, (0,0,0), apple.body.position, 80)

pygame.init()                                       # initiating game
screen = pygame.display.set_mode((800, 800))        # creating display space
clock = pygame.time.Clock()                         # creating game clock
space = pymunk.Space()
space.gravity = (0, 500)
apples = []
apples.append(create_apple(space))                  #


while True:                                         # game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((200, 220, 220))                        # background color
    draw_apples(apples)                                 # calling draw_apples function with apples list param.
    space.step(1/50)                                    # physics loop
    pygame.display.update()                             # rendering frame
    clock.tick(120)                                     # 120 fps limit

