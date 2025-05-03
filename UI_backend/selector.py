


import pygame

class Selector:
    def __init__(self, options, position):
        self.__options = options
        self.__x, self.__y = position
        self.__current_index = 0
        self.__font = pygame.font.Font(None, 36)
        self.__selected = False


    def draw(self,screen):
        # Draw left arrow
        pygame.draw.polygon(screen, (200, 200, 200), [(self.__x + 25, self.__y - 25), (self.__x, self.__y), (self.__x + 25, self.__y + 25)])

        # Draw right arrow
        pygame.draw.polygon(screen, (200, 200, 200), [(self.__x + 225, self.__y - 25), (self.__x + 250, self.__y), (self.__x + 225, self.__y + 25)])

        # Draw current item text
        text = self.__font.render(self.__options[self.__current_index], 1, (255, 255, 255))
        text_rect = text.get_rect(center=(self.__x + 125, self.__y))
        screen.blit(text, text_rect)



    def handle_event(self,event):
        if event.key == pygame.K_LEFT:
            self.__current_index = (self.__current_index - 1) % len(self.__options)
        elif event.key == pygame.K_RIGHT:
            self.__current_index = (self.__current_index + 1) % len(self.__options)


    def selected(self, value):
        self.__selected = value

    def get_choice(self):
        return self.__current_index
    
    def get_selected(self):
        return self.__selected