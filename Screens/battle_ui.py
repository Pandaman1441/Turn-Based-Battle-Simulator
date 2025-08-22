from UI_backend import button, character_info
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

        # self.__p_info = []
        # for i in self.__party:
        #     c = character_info.Character_Info(i, 'ally', (20, 576))
        #     self.__p_info.append(c)

        # self.__e_info = []
        # for i in self.__e_party:
        #     c = character_info.Character_Info(i, 'enemy', (1330, 76))

        self.__test_p = character_info.Character_Info(self.__party[0], 'ally', (20,576))
        self.__test_e = character_info.Character_Info(self.__e_party[0], 'enemy', (1350,20))
    
    

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


        self.__test_p.draw(screen)
        
        self.__test_e.draw(screen)


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
