from UI_backend import button
import pygame
import battle_manager
import generate_enemies


class b_UI:
    def __init__(self, party):
        self.__width = 200
        self.__height = 100
        self.__party = party
        # self.__manager = battle_manager.Battle_Manager(party, enemies)
        self.__enemies = generate_enemies.Goblin()
        self.__font = pygame.font.Font(None, 36)      # 24 pixel height

        self.attack = button.Button("Attack",  (30,660), self.__width, self.__height)
        self.skill = button.Button("Skill", (240, 660), self.__width, self.__height)
        self.inventory = button.Button("Inventory", (450, 660), self.__width, self.__height)
        self.defend = button.Button("Defend", (30, 770), self.__width, self.__height)
        self.status = button.Button("Status", (240, 770), self.__width, self.__height)
        self.end_turn = button.Button("End Turn", (450, 770), self.__width, self.__height)

        self.__buttons = [self.attack, self.skill, self.inventory,
                          self.defend, self.status, self.end_turn]
        self.__selected_idx = 0
        self.__buttons[self.__selected_idx].selected(True)
        self.__turn = 0
    

    def draw(self, screen):
        x = pygame.image.load("Assests/background.jpg")
        bg = pygame.Surface.convert(x)
        screen.blit(bg,(0,0))

        self.attack.draw(screen)
        self.defend.draw(screen)
        self.inventory.draw(screen)
        self.skill.draw(screen)
        self.status.draw(screen)
        self.end_turn.draw(screen)

        ########################### party borders and info

        party_border = pygame.Rect((20, 650), (1400, 230))
        pygame.draw.rect(screen, (240,240,240), party_border, 2)
        party_icon_b = pygame.Rect((20, 576), (70,70))
        pygame.draw.rect(screen, (240,240,240), party_icon_b, 2)

        party_x = pygame.image.load(self.__party[0].icon)
        party_icon = pygame.Surface.convert_alpha(party_x)
        party_icon_rect = party_icon.get_rect(center = party_icon_b.center)
        screen.blit(party_icon, party_icon_rect)
        
        health_values = f'HP: {self.__party[0].get_stat("hp")["max"]} / {self.__party[0].get_stat("hp")["current"]}'  
        health = self.__font.render(health_values, 1, (255,255,255))
        screen.blit(health, (102,581))

        r_values = f'resource: {self.__party[0].get_stat("resource")["max"]} / {self.__party[0].get_stat("resource")["current"]}'  
        resource = self.__font.render(r_values, 1, (255,255,255))
        screen.blit(resource, (102,617))

        hp_bar = pygame.Rect((92,576), (300, 34))
        pygame.draw.rect(screen, (240,240,240), hp_bar, 2)

        r_bar = pygame.Rect((92,612), (300, 34))
        pygame.draw.rect(screen, (240,240,240), r_bar, 2)

        ########################

        # e_border = pygame.Rect((20, 250), (1400, 230))
        # pygame.draw.rect(screen, (240,240,240), e_border, 2)
        e_icon_b = pygame.Rect((1330, 76), (70,70))
        pygame.draw.rect(screen, (40,40,40), e_icon_b, 2)

        e_x = pygame.image.load(self.__enemies.icon)
        e_icon = pygame.Surface.convert_alpha(e_x)
        e_icon_rect = e_icon.get_rect(center = e_icon_b.center)
        screen.blit(e_icon, e_icon_rect)
        
        e_health_values = f'{self.__enemies.get_stat("hp")["current"]} / {self.__enemies.get_stat("hp")["max"]} :HP'
        aligned_text = f'{e_health_values:>}'  
        e_health = self.__font.render(aligned_text, 1, (55,55,55))
        e_health_rect = e_health.get_rect(topright=(1390,156))
        screen.blit(e_health, e_health_rect)

        e_hp_bar = pygame.Rect((1100,148), (300, 34))
        pygame.draw.rect(screen, (40,40,40), e_hp_bar, 2)
        ########################


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
