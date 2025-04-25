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
        shape = pygame.Rect((self.__x,self.__y), (self.__width, self.__height))
        pygame.draw.rect(screen, (164,160,165), shape)      # draw rect on screen
        text = self.__font.render(self.__text, 1, (255,255,255))   # create text
        text_rect = text.get_rect(center=shape.center)      # we move the text rect to be centered in the shape
        screen.blit(text,text_rect)                         # we are passing the top left of the rect, when we blit it only 