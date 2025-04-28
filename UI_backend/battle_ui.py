from UI_backend import button
import pygame



class b_UI:
    def __init__(self):
        self.__width = 200
        self.__height = 100
        # self.__buttons = []
        self.attack = button.Button("Attack",  (30,660), self.__width, self.__height)
        self.defend = button.Button("Defend", (240, 660), self.__width, self.__height)
        self.inventory = button.Button("Inventory", (450, 660), self.__width, self.__height)
        self.skill = button.Button("Skill", (30, 770), self.__width, self.__height)
        self.status = button.Button("Status", (240, 770), self.__width, self.__height)
        self.wait = button.Button("Wait", (450, 770), self.__width, self.__height)
    
    def draw(self, screen):
        self.attack.draw(screen)
        self.defend.draw(screen)
        self.inventory.draw(screen)
        self.skill.draw(screen)
        self.status.draw(screen)
        self.wait.draw(screen)

        border = pygame.Rect((20, 650), (1400, 230))
        pygame.draw.rect(screen, (240,240,240), border, 2)