import pygame



class Button:
    def __init__(self, text: str, position: tuple,   width: int=30, height: int=30):
        self.__text = text
        self.__x, self.__y = position
        # self.__callback = callback
        self.__width = width
        self.__height = height
        self.__font = pygame.font.Font(None, 36)
        print(position)
        print(self.__x)
        print(self.__y)

    def draw(self, screen):

        shape = pygame.Surface((self.__width, self.__height), pygame.SRCALPHA)
        shape.fill((164,160,165,230))
        screen.blit(shape, (self.__x,self.__y))

        border = pygame.Rect((self.__x - 4, self.__y - 4), (self.__width + 4*2, self.__height + 4*2))
        pygame.draw.rect(screen, (240,240,240), border, 2)
        text = self.__font.render(self.__text, 1, (255,255,255))    # create text
        text_rect = text.get_rect(center=border.center)             # we move the text rect to be centered in the shape
        screen.blit(text,text_rect)                                 # we are passing the top left of the rect, when we blit it only 
        