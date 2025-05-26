import pygame
import Items
from UI_backend import item_icon
import math
from UI_backend import node


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
        self.__cols = 5                     # 5 by 6 
        self.__mode = "none"
        self.__inv_buttons = []
        self.__inv_idx = 0
        self.__inventory = False
        self.__item = False
        self.__shop = False
        self.__prev = "none"
        self.__item_tree = {}
        self.__tree_idx = (0,0)                 # tuple
        self.__selected_node = None
        self.__visible_offset = 0

    def draw(self,screen):
        total = len(self.__buttons)
        self.__visible_offset = max(0, min(self.__visible_offset, max(0, total - 30)))
        visible_items = self.__buttons[self.__visible_offset : self.__visible_offset + 30]

        for v_idx, btn in enumerate(visible_items):                              # listing items in shop
            actual_idx = self.__visible_offset + v_idx
            row = actual_idx // self.__cols
            col = actual_idx % self.__cols

            y = 50 + (row - (self.__visible_offset // self.__cols)) * (100 + 20)
            x = 50 + col * (100 + 20)

            btn.move((x,y))


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



        scroll_bar = pygame.Rect(700, 50, 10, 600)                              # vertical bar
        scroll_height = int(600 * (30 / len(self.__buttons)))                   # visible vs total
        scroll_pos = int((600 - scroll_height) * (self.__visible_offset / (len(self.__buttons) - 30)))
        pygame.draw.rect(screen, (180, 180, 180), scroll_bar)
        pygame.draw.rect(screen, (240, 240, 240), (700, 50 + scroll_pos, 10, scroll_height))

        border = pygame.Rect((26,26), (1388, 736))                              # large border around whole shop
        pygame.draw.rect(screen, (240,240,240), border, 2)      
        shape = pygame.Surface((1384, 732), pygame.SRCALPHA)                    # inner shading of whole shop

        if self.__outer:
            shape.fill((114,110,115, 150))                                      # shades shop if hovered
        else:
            shape.fill((114,110,115,0))                                         # transparent shop otherwise
        screen.blit(shape,(28,28))  


        if self.__shop:
            shape = pygame.Surface((694,732), pygame.SRCALPHA)
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

        pc_gold = self.__font.render(str(self.__pc.gold), 1, (255,255,255))
        screen.blit(pc_gold, (750,730))


        for b in visible_items:                                                # shop list buttons
            if self.__mode == "shop":
                if self.__visible_offset <= self.__inner_idx < self.__visible_offset + 30:
                    self.__buttons[self.__inner_idx].selected(True) 
            else:
                b.selected(False)
            b.draw(screen)  

        if self.__inv_buttons:
            for b in self.__inv_buttons:                                            # Inventory buttons
                if self.__mode == "inventory":
                    self.__inv_buttons[self.__inv_idx].selected(True)
                else:
                    b.selected(False)
                b.draw(screen)

        

        if self.__inner:                                                        # hovered item
            if self.__mode == "shop":
                i = self.__buttons[self.__inner_idx].item 
                self.item_display(i, screen)
                self.build_tree(screen,i.name, 850,30)
                if self.__item_tree:
                        for b in self.__item_tree.values():
                            b.item.draw(screen)
            elif self.__mode == "inventory":
                if self.__inv_buttons:
                    i = self.__inv_buttons[self.__inv_idx].item 
                    self.item_display(i, screen)
                    self.build_tree(screen,i.name, 850,30)
                    if self.__item_tree:
                        for b in self.__item_tree.values():
                            b.item.draw(screen)
            elif self.__mode == "item":
                if self.__prev == "shop":
                    i = self.__buttons[self.__inner_idx].item
                    self.item_display(i, screen)
                    self.build_tree(screen,i.name, 850,30)
                    if self.__item_tree:
                        for b in self.__item_tree.values():
                            b.item.draw(screen)
                elif self.__prev == "inventory":
                    i = self.__inv_buttons[self.__inv_idx].item 
                    self.item_display(i, screen)
                    self.build_tree(screen,i.name, 850,30)
                    if self.__item_tree:
                        for b in self.__item_tree.values():
                            b.item.draw(screen)
            


        
                    
        if self.__mode == "item":                                       # make the tree then display the hovered item
            self.__selected_node = self.__item_tree[self.__tree_idx]
            self.__selected_node.item.selected(True)
            if self.__item_tree:
                for b in self.__item_tree.values():
                    b.item.draw(screen)

        

        # for x,i in self.__item_tree.items():
        #     print(f"{x} === {i.item.item.name}")



        
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
                self.__mode = self.__prev
                self.__tree_idx = (0,0)    
# --------------------------------------------------------------------------------
        elif self.__mode == "shop":
            ps = self.__inner_idx
            total = len(self.__buttons)
            cols = self.__cols
            rows = (total + cols - 1) // cols

            row = ps // cols
            col = ps % cols

            if event.key == pygame.K_RIGHT:
                col += 1
                if row == rows - 1:
                    last_row_count = total % cols if total % cols != 0 else cols
                    if col >= last_row_count:
                        col = 0
                else:
                    if col >= cols:
                        col = 0

            elif event.key == pygame.K_LEFT:
                col -= 1
                if col < 0:
                    if row == rows - 1:
                        last_row_count = total % cols if total % cols != 0 else cols
                        col = last_row_count - 1
                    else:
                        col = cols - 1

            elif event.key == pygame.K_DOWN:
                row += 1
                if row * cols + col >= total:
                    row = 0

            elif event.key == pygame.K_UP:
                row -= 1
                if row < 0:
                    row = rows - 1


            if row == rows - 1:
                last_row_count = total % cols if total % cols != 0 else cols
                if col >= last_row_count:
                    col = last_row_count - 1

            next_idx = row * cols + col
            if next_idx >= total:
                next_idx = total - 1

            wrapped = abs(next_idx - ps) > self.__cols

            if wrapped:
                # Big jump
                self.__visible_offset = min(max((next_idx // self.__cols) * self.__cols, 0), total - 30)
            else:
                # Small jump
                if next_idx >= self.__visible_offset + 30:
                    self.__visible_offset = min(self.__visible_offset + self.__cols, total - 30)
                elif next_idx < self.__visible_offset:
                    self.__visible_offset = max(self.__visible_offset - self.__cols, 0)


            self.__buttons[ps].selected(False)
            self.__inner_idx = next_idx
            self.__visible_offset = max(0, min(self.__visible_offset, max(0, total - 30)))
            self.__buttons[next_idx].selected(True)

            if event.key == pygame.K_RETURN:
                self.__prev = "shop"
                self.__mode = "item"
                # self.buy_item(self.buttons[self.__inner_idx].item)  

# --------------------------------------------------------------------------------
        elif self.__mode == "inventory":
            if self.__inv_buttons:
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

                if event.key == pygame.K_RETURN:
                    self.__prev = "inventory"
                    self.__mode = "item"

                    # self.sell_item(self.__inv_buttons[self.__inv_idx].item)

# --------------------------------------------------------------------------------
        elif self.__mode == "item":
            x,y = self.__tree_idx
            prev_key = (x,y)
            new_key = (x,y)
            attempt = None

            if event.key == pygame.K_RIGHT:
                attempt = (x+1,y)
            elif event.key == pygame.K_LEFT:
                attempt = (x-1,y)
            elif event.key == pygame.K_DOWN:
                if self.__selected_node.children:
                    attempt = self.__selected_node.children[0].position
            elif event.key == pygame.K_UP:
                if self.__selected_node.parent:
                    attempt = self.__selected_node.parent.position
            
            if attempt in self.__item_tree:
                new_key = attempt

            self.__item_tree[prev_key].item.selected(False)
            self.__item_tree[new_key].item.selected(True)
            
            self.__selected_node = self.__item_tree[new_key]
            self.__tree_idx = self.__selected_node.position

            if event.key == pygame.K_RETURN:
                if self.__prev == "shop":
                    self.buy_item(self.__item_tree[self.__tree_idx].item.item)


# --------------------------------------------------------------------------------
        else:
            if event.key == pygame.K_RETURN:
                if self.__shop:
                    self.__mode = "shop"
                elif self.__inventory:
                    self.__mode = "inventory"
                

            elif event.key == pygame.K_LEFT:
                if self.__inventory:
                    self.__inventory = False
                    self.__shop = True
                
            elif event.key == pygame.K_RIGHT:
                if self.__shop:
                    self.__inventory = True
                    self.__shop = False
        


# shop and inventory, we can only go into item if from the store or inventory by hitting enter







    def item_display(self, i, screen):  
        x = 1080
        y = 80
        name = self.__font.render(i.name, 1, (255,255,255))                     # item name
        screen.blit(name, (1080, 50))

        cost = self.__font.render(str(i.cost), 1, (255,255,255))                # item cost
        cost_rect = cost.get_rect()
        cost_rect.topright = (1400, 50)                                         # right aligned
        screen.blit(cost, cost_rect)
        
        for stat in i.stats:                                                    # item stat values
            att = self.__font.render(str(stat), 1, (255,255,255))
            y += 40
            screen.blit(att, (x+70,y))

            value = self.__font.render(str(i.stats[stat]), 1, (255,255,255))
            screen.blit(value, (x,y))

        desc = self.__font.render(i.description, 1, (255,255,255))              # item lore thing
        screen.blit(desc, (1080, 300))

        # if i.build:
                
     
    def build_tree(self, screen, item_name, x, y, parent=None, depth=0, max_width=300, pos=0):  
        if depth == 0:
            self.__item_tree = {}
        i = self.__item_list[item_name]
# dictionary keying a div to a tuple of (x, depth)
# x is a var we pass through the recursion and increment in the for i, sub_name loop below
        
        b = item_icon.div(i, (x,y))
        key = (pos, depth)
        n = node.Node(key,b,parent)
        if parent:
            parent.add_child(n)
        self.__item_tree[key] = n

        if not self.__item_list[item_name].build:
            return
        else:
            num = len(i.build)
            spacing = max_width // max(1,num)
            start_x = x - ((num -1) * spacing //2)
            child_y = y +135
            pos = pos
            for i, sub_name in enumerate(i.build):
                child_x = start_x + i * spacing

                pygame.draw.line(screen,(200,200,200), (x+40, y + 90), (x+40, y+110),2)                     # |
                pygame.draw.line(screen,(200,200,200), (x+40, y + 110), (child_x+40, y+110),2)              # -
                pygame.draw.line(screen,(200,200,200), (child_x+40, y + 110), (child_x+40, child_y),2)      # |

                self.build_tree(screen,sub_name, child_x,child_y, n, depth +1, spacing,pos)
                pos += 1



    def buy_item(self, i):
        if i.cost > self.__pc.gold:
            print("not enough gold")
        else:
            if self.__pc.add_item(i.name):
                self.__pc.take_gold(i.cost)
            else:
                print("not enough inventory space")

    def sell_item(self, i):
        value = math.ceil(i.cost * .65)
        if self.__inv_buttons:
            self.__inv_idx = 0
        else:
            self.__inv_idx = None
        self.__pc.add_gold(value)
        self.__pc.remove_item(i.name)
        




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