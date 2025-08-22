# display icon, name, health, resource

import pygame


class Character_Info:
    def __init__(self, character, team, position: tuple):
        self.__character = character
        self.__x, self.__y = position
        self.__team = team
        self.__selected = False
        self.__font = pygame.font.Font(None, 36)

    def draw(self, screen):
        character_icon_b = pygame.Rect((self.__x, self.__y), (70,70))      #
        if self.__team == 'ally':
            pygame.draw.rect(screen, (240,240,240), character_icon_b, 2)
        else:
            pygame.draw.rect(screen, (40,40,40), character_icon_b, 2)

        img = pygame.image.load(self.__character.icon)
        character_icon = pygame.Surface.convert_alpha(img)
        character_icon_rect = character_icon.get_rect(center = character_icon_b.center)
        screen.blit(character_icon, character_icon_rect)

        if self.__team == 'ally':    
            health_values = f'HP: {self.__character.get_stat("hp")["max"]} / {self.__character.get_stat("hp")["current"]}'  
            health = self.__font.render(health_values, 1, (255,255,255))
            screen.blit(health, (self.__x + 82, self.__y + 5))                          #

            r_values = f'Resource: {self.__character.get_stat("resource")["max"]} / {self.__character.get_stat("resource")["current"]}'  
            resource = self.__font.render(r_values, 1, (255,255,255))
            screen.blit(resource, (self.__x + 82, self.__y + 41))                        #

            hp_bar = pygame.Rect((self.__x + 72, self.__y), (300, 34))               #
            pygame.draw.rect(screen, (240,240,240), hp_bar, 2)

            r_bar = pygame.Rect((self.__x + 72, self.__y + 36), (300, 34))                #
            pygame.draw.rect(screen, (240,240,240), r_bar, 2)

        else:
            e_health_values = f'{self.__character.get_stat("hp")["current"]} / {self.__character.get_stat("hp")["max"]} :HP'
            aligned_text = f'{e_health_values:>}'  
            e_health = self.__font.render(aligned_text, 1, (55,55,55))
            e_health_rect = e_health.get_rect(topright=(self.__x + 60, self.__y + 80))
            screen.blit(e_health, e_health_rect)

            e_resource_values = f'{self.__character.get_stat("resource")["current"]} / {self.__character.get_stat("resource")["max"]} :Resource'
            aligned_text = f'{e_resource_values:>}'  
            e_resource = self.__font.render(aligned_text, 1, (55,55,55))
            e_resource_rect = e_resource.get_rect(topright=(self.__x + 60, self.__y + 116))
            screen.blit(e_resource, e_resource_rect)

            e_hp_bar = pygame.Rect((self.__x - 230,self.__y + 72), (300, 34))
            pygame.draw.rect(screen, (40,40,40), e_hp_bar, 2)

            e_resource_bar = pygame.Rect((self.__x - 230, self.__y + 108), (300, 34))                #
            pygame.draw.rect(screen, (40,40,40), e_resource_bar, 2)

    def selected(self, value):
        self.__selected = value

    def get_selected(self):
        return self.__selected
    
    def move(self, position: tuple):
        self.__x, self.__y = position
        