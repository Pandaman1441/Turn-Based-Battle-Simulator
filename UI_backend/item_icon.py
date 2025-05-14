import pygame



class div:
    def __init__(self, i, position: tuple):
        self.__item = i
        self.__x, self.__y = position
        self.__width = 80
        self.__height = 90
        self.__font = pygame.font.Font(None, 26)
        self.__selected = False

    def draw(self, screen):
        border = pygame.Rect((self.__x - 4, self.__y - 4), (self.__width + 4*2, self.__height + 4*2))
        if self.__selected:
            shape = pygame.Surface((self.__width, self.__height), pygame.SRCALPHA)
            shape.fill((114,110,115,175))
            screen.blit(shape, (self.__x,self.__y))
            pygame.draw.rect(screen, (240,240,240), border, 2)

        else:
            shape = pygame.Surface((self.__width, self.__height), pygame.SRCALPHA)
            shape.fill((164,160,165,0))

        text = self.__font.render(self.__item.name, 1, (255,255,255))    
        val = border.centery - 20
        text_rect = text.get_rect(centerx=border.centerx,centery=val)             
        screen.blit(text,text_rect) 

        cost = self.__font.render(str(self.__item.cost), 1, (255,255,255))
        val = border.centery + 20
        cost_rect = cost.get_rect(centerx=border.centerx,centery=val)
        screen.blit(cost, cost_rect)


    def selected(self, value):
        self.__selected = value

    def get_selected(self):
        return self.__selected
    
    @property
    def item(self):
        return self.__item
    
    def move(self, position: tuple):
        self.__x, self.__y = position