import pygame
import pymunk
import pymunk.pygame_util

import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Test Pymunk - Fisica")
clock = pygame.time.Clock()

space = pymunk.Space()
space.gravity = (0, 900)
draw_options = pymunk.pygame_util.DrawOptions(screen)

floor = pymunk.Segment(space.static_body, (0,580), (800,580), 5)
floor.elasticity = 0.8
floor.friction = 0.5
space.add(floor)

mass = 1
radius = 20
m = pymunk.moment_for_circle(mass, 0, radius)
body = pymunk.Body(mass, m)
body.position = (400,100)

shape = pymunk.Circle(body, radius)
shape.elasticity = 0.9
shape.friction = 0.5
space.add(body, shape)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((30, 30, 50))

    space.debug_draw(draw_options)

    space.step(1/60)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()