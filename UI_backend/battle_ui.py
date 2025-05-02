from UI_backend import button
import pygame



class b_UI:
    def __init__(self):
        self.__width = 200
        self.__height = 100
       

        self.attack = button.Button("Attack",  (30,660), self.__width, self.__height)
        self.skill = button.Button("Skill", (240, 660), self.__width, self.__height)
        self.inventory = button.Button("Inventory", (450, 660), self.__width, self.__height)
        self.defend = button.Button("Defend", (30, 770), self.__width, self.__height)
        self.status = button.Button("Status", (240, 770), self.__width, self.__height)
        self.wait = button.Button("Wait", (450, 770), self.__width, self.__height)

        self.__buttons = [self.attack, self.skill, self.inventory,
                          self.defend, self.status, self.wait]
        self.__selected_idx = 0
        self.__buttons[self.__selected_idx].selected(True)
    
    def draw(self, screen):
        self.attack.draw(screen)
        self.defend.draw(screen)
        self.inventory.draw(screen)
        self.skill.draw(screen)
        self.status.draw(screen)
        self.wait.draw(screen)

        border = pygame.Rect((20, 650), (1400, 230))
        pygame.draw.rect(screen, (240,240,240), border, 2)
        x = pygame.image.load("Assests/64x64/tile014.png")
        
        icon_b = pygame.Rect((20, 576), (70,70))
        icon = pygame.Surface.convert_alpha(x)
        icon_rect = icon.get_rect(center = icon_b.center)
        screen.blit(icon, icon_rect)
        pygame.draw.rect(screen, (240,240,240), icon_b, 2)


    def handle_event(self, event):
        ps = self.__selected_idx
        row = ps // 3
        col = ps % 3
        if event.key == pygame.K_RIGHT:
            col = (col + 1) % 3
        elif event.key == pygame.K_LEFT:
            col = (col - 1) % 3
        elif event.key == pygame.K_DOWN:
            row = (row + 1) % 2
        elif event.key == pygame.K_UP:
            row = (row - 1) % 2
        elif event.key == pygame.K_RETURN:
            return "menu"
        self.__buttons[ps].selected(False)
        
        value = (row * 3) + col
        self.__selected_idx = value
        self.__buttons[value].selected(True)
