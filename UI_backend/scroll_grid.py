import pygame
import Items
from UI_backend import item_icon



class Scroll_Grid():
    def __init__(self,pc):
        self.__item_list = Items.load_all_items()
        self.__buttons = []
        self.__font = pygame.font.Font(None, 36)
        self.__pc = pc

        for item in self.__item_list.values():
            b = item_icon.div(item, (50, 50))
            self.__buttons.append(b)


        self.__inner = False                # inside shop
        self.__outer = False                # hover shop
        self.__inner_idx = 0             # shop selected index
        self.__cols = 5
        self.__mode = "none"
        self.__inv_buttons = []
        self.__inv_idx = 0
        self.__inventory = False
        self.__item = False
        self.__shop = False
        

    def draw(self,screen):
        for idx, btn in enumerate(self.__buttons):                              # listing items in shop
            row = idx // self.__cols
            col = idx % self.__cols

            x = 50 + col * (100 + 20)
            y = 50 + row * (100 + 20)

            btn.move((x, y)) 

        inventory = self.__pc.get_loaded_inventory()
        self.__inv_buttons = []

        for item in inventory:
            b= item_icon.div(item, (50,50))
            self.__inv_buttons.append(b)

        for idx, btn in enumerate(self.__inv_buttons):
            row = idx // self.__cols
            col = idx % self.__cols

            x = 740 + col * (100 + 20)
            y = 430 + row * (100 + 20)

            btn.move((x,y))

        border = pygame.Rect((26,26), (1388, 736))                              # large border around whole shop
        pygame.draw.rect(screen, (240,240,240), border, 2)      
        shape = pygame.Surface((1384, 732), pygame.SRCALPHA)                    # inner shading of whole shop

        if self.__outer:
            shape.fill((114,110,115, 150))                                      # shades shop if hovered
        else:
            shape.fill((114,110,115,0))                                         # transparent shop otherwise
        screen.blit(shape,(28,28))  


        if self.__shop:
            shape = pygame.Surface((500,500), pygame.SRCALPHA)
            shape.fill((240,240,240, 20))
            screen.blit(shape,(28,28))
        
        elif self.__inventory:
            shape = pygame.Surface((500,500), pygame.SRCALPHA)
            shape.fill((240,240,240, 20))
            screen.blit(shape,(720,410))

        elif self.__item:
            shape = pygame.Surface((500,500), pygame.SRCALPHA)
            shape.fill((240,240,240, 20))
            screen.blit(shape,(28,28))


        pygame.draw.line(screen, (240,240,240), (720,26), (720, 760),3)         # center line
        pygame.draw.line(screen, (240,240,240), (720,406), (1412, 406), 3)      # item display from inventory
        pygame.draw.line(screen, (240,240,240), (1067,26), (1067, 406),3)       # item display from item info

        for b in self.__buttons:                                                # shop list buttons
            if self.__mode == "shop":
                self.__buttons[self.__inner_idx].selected(True)
            else:
                b.selected(False)
            b.draw(screen)  

        for b in self.__inv_buttons:                                            # Inventory buttons
            if self.__mode == "inventory":
                self.__inv_buttons[self.__inv_idx].selected(True)
            else:
                b.selected(False)
            b.draw(screen)

        if self.__inner:                                                        # hovered item
            if self.__mode == "shop":
                i = self.buttons[self.__inner_idx].item 
                self.item_display(i, screen)
            elif self.__mode == "inventory":
                i = self.__inv_buttons[self.__inv_idx].item 
                self.item_display(i, screen)

    def item_display(self, i, screen):  
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
        if event.key == pygame.K_ESCAPE:
            if self.__mode == "none":
                self.__outer = False
                self.__inner = False
                self.__inner_idx = 0
                for b in self.__buttons:
                    b.selected(False)
                return "back"

            elif self.__mode == "shop":
                self.__mode = "none"
                self.__inner_idx = 0
                for b in self.__buttons:
                    b.selected(False)

            elif self.__mode == "inventory":
                self.__mode = "none"
                self.__inv_idx = 0
                for b in self.__inv_buttons:
                    b.selected(False)

            elif self.__mode == "item":
                self.__mode = "none"    

        elif self.__mode == "shop":
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
        
        elif self.__mode == "inventory":
            ps = self.__inv_idx
            total = len(self.__inv_buttons)
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

            self.__inv_buttons[ps].selected(False)

            # Clamp to valid index
            value = row * cols + col
            if value >= total:
                value = total - 1  # prevent out-of-range index

            self.__inv_idx = value
            self.__inv_buttons[value].selected(True)

        else:
            if event.key == pygame.K_RETURN:
                if self.__shop:
                    self.__mode = "shop"
                elif self.__inventory:
                    self.__mode = "inventory"
                elif self.__item:
                    self.__mode = "item"
                

            elif event.key == pygame.K_LEFT:
                if self.__inventory:
                    self.__inventory = False
                    self.__shop = True
                
            elif event.key == pygame.K_RIGHT:
                if self.__shop:
                    self.__inventory = True
                    self.__shop = False
        


# shop and inventory, we can only go into item if from the store or inventory by hitting enter






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
    @property
    def shop(self):
        return self.__shop

    
    @inner.setter
    def inner(self,value):
        self.__inner = value
    @outer.setter
    def outer(self,value):
        self.__outer = value
    @inner_idx.setter
    def inner_idx(self,value):
        self.__inner_idx = value
    @shop.setter
    def shop(self,value):
        self.__shop = value