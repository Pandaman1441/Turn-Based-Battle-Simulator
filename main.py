from Classes import *
import pygame
import math
from Screens import title
import screen_manager



archetypes = ["artificer", "assassin", "barbarian", "bladeslinger", "cleric", "mercenary", "monk", "paladin", "ranger", "scholar", "sorceress", "thief" ]

pygame.init()
screen = pygame.display.set_mode((1440, 900))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
intro = True
running = True

first = title.Title()

pc = None

while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro = False
                running = False
            elif event.type == pygame.KEYDOWN:
                pc = first.handle_event(event)
                if pc:
                    intro = False
                    print(f"You have chosen: {pc.name}")
        first.draw(screen)
        pygame.display.flip()

manager = screen_manager.manager(pc)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            manager.handle_event(event)
                
    if not manager.get_status():
        running = False
    screen.fill("black")     
    manager.draw(screen)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()




