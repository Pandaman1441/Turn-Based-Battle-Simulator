from UI_backend import button
import pygame
import battle_manager
import generate_enemies

import combat
# need an object that can track a battle instance, has enemies, party, tracks turns.
        # this class communicates with the 'battle_tracker' 
        # 'battle_tracker' does all the bts stuff while this class takes the results and displays them

class b_UI:
    def __init__(self, party):
        self.__width = 200
        self.__height = 100
        self.__party = party
        e1 = generate_enemies.Goblin()
        e2 = generate_enemies.Goblin()
        self.__e_party = []
        self.__e_party.append(e1)
        self.__e_party.append(e2)
        self.__manager = battle_manager.Battle_Manager(party, self.__e_party)
        self.__font = pygame.font.Font(None, 36)      # 24 pixel height
        self.__log_font = pygame.font.Font(None, 24)
        
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
        self.__turn = self.__manager.turn
        self.__round = self.__manager.round
        self.__log = ""
        self.__targeting = "none"

    
    

    def draw(self, screen):
        x = pygame.image.load("Assets/background.jpg")
        bg = pygame.Surface.convert(x)
        screen.blit(bg,(0,0))

        self.attack.draw(screen)
        self.defend.draw(screen)
        self.inventory.draw(screen)
        self.skill.draw(screen)
        self.status.draw(screen)
        self.end_turn.draw(screen)
        party_border = pygame.Rect((20, 650), (1400, 230))
        pygame.draw.rect(screen, (240,240,240), party_border, 2)

        ########################### party borders and info

        # (x,y) (width, hight)

        # convert the icon and health bars into an object so we can do selection and stuff
        # it takes a position and have attributes to show the resource bars and move slightly
        
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

        e_x = pygame.image.load(self.__e_party[0].icon)
        e_icon = pygame.Surface.convert_alpha(e_x)
        e_icon_rect = e_icon.get_rect(center = e_icon_b.center)
        screen.blit(e_icon, e_icon_rect)
        
        e_health_values = f'{self.__e_party[0].get_stat("hp")["current"]} / {self.__e_party[0].get_stat("hp")["max"]} :HP'
        aligned_text = f'{e_health_values:>}'  
        e_health = self.__font.render(aligned_text, 1, (55,55,55))
        e_health_rect = e_health.get_rect(topright=(1390,156))
        screen.blit(e_health, e_health_rect)

        e_hp_bar = pygame.Rect((1100,148), (300, 34))
        pygame.draw.rect(screen, (40,40,40), e_hp_bar, 2)
        ########################

        log = self.__log_font.render(self.__log, 1, (255,255,255))
        screen.blit(log, (660, 700))


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
            if self.__targeting == 'enemy':
                current = self.__manager.current_turn()
                current.basic_attack(self.__manager.enemies[0])
                self.__manager.next_turn()
            elif self.__targeting == 'ally':
                pass
            if self.attack.get_selected():
                self.__targeting = 'enemy'
                
            else:
                return "menu"
        self.__buttons[ps].selected(False)
        
        value = (row * 3) + col
        self.__selected_idx = value
        self.__buttons[value].selected(True)

        if not self.__manager.fighting():
            return "menu"
