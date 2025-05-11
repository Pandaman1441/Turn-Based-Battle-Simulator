import pygame
import Items
from UI_backend import item_icon



class Scroll_Grid():
    def __init__(self):
        self.__item_list = Items.load_all_items()
        self.__buttons = []
        self.__font = pygame.font.Font(None, 36)


        for item in self.__item_list.values():
            b = item_icon.div(item, (50, 50))
            self.__buttons.append(b)


        self.__inner = False                # inside shop list
        self.__outer = False                # hover shop list
        self.__inner_idx = 0                # shop selected index
        self.__cols = 5
        

    def draw(self,screen):
        for idx, btn in enumerate(self.__buttons):
            row = idx // self.__cols
            col = idx % self.__cols

            x = 50 + col * (100 + 20)
            y = 50 + row * (100 + 20)

            btn.move((x, y)) 

        border = pygame.Rect((26,26), (1388, 736))
        pygame.draw.rect(screen, (240,240,240), border, 2)
        pygame.draw.line(screen, (240,240,240), (720,26), (720, 760),3)
        shape = pygame.Surface((1384, 732), pygame.SRCALPHA)

        if self.__outer:
            shape.fill((114,110,115, 150))    
        else:
            shape.fill((114,110,115,0))
        screen.blit(shape,(28,28))

        for b in self.__buttons:
            if self.__inner:
                self.__buttons[self.__inner_idx].selected(True)
            
            b.draw(screen)  

        if self.__inner:                                        # hovered item
            i = self.buttons[self.__inner_idx].item
            text = self.__font.render(i.name, 1, (255,255,255))
            screen.blit(text, (730, 120))
            if i.build:
                h = self.get_build_path(i.name,self.__item_list)
                y = 160
                for line in h:
                    line_surf = self.__font.render(line, 1, (220, 220, 220))
                    screen.blit(line_surf, (730, y))
                    y += 25
                

    def handle_event(self, event):
        ps = self.__inner_idx
        total = len(self.__buttons)
        cols = self.__cols
        rows = (total + cols - 1) // cols

        row = ps // cols
        col = ps % cols

        if event.key == pygame.K_RIGHT:
            col = (col + 1) % cols
        elif event.key == pygame.K_LEFT:
            col = (col - 1 + cols) % cols
        elif event.key == pygame.K_DOWN:
            row = (row + 1) % rows
        elif event.key == pygame.K_UP:
            row = (row - 1 + rows) % rows

        self.__buttons[ps].selected(False)

        # Clamp to valid index
        value = row * cols + col
        if value >= total:
            value = total - 1  # prevent out-of-range index

        self.__inner_idx = value
        self.__buttons[value].selected(True)


    def get_build_path(self, item_name, shop_items, depth=0):
        lines = []
        item = shop_items[item_name]
        indent = "  " * depth
        lines.append(f"{indent}- {item.name}")

        if item.build:
            for sub_name in item.build:
                if sub_name in shop_items:
                    lines.extend(self.get_build_path(sub_name, shop_items, depth + 1))
                else:
                    lines.append(f"{indent}  - [Missing Item: {sub_name}]")
        return lines
    





    @property
    def inner(self):
        return self.__inner
    @property
    def outer(self):
        return self.__outer
    @property
    def inner_idx(self):
        return self.__inner_idx
    @property
    def buttons(self):
        return self.__buttons
    
    
    @inner.setter
    def inner(self,value):
        self.__inner = value
    @outer.setter
    def outer(self,value):
        self.__outer = value
    @inner_idx.setter
    def inner_idx(self,value):
        self.__inner_idx = value