



class Node():
    def __init__(self, pos, item, parent=None):
        self.__parent = parent
        self.__children = []
        self.__item = item              # item_icon.div
        self.__position = pos


    @property
    def parent(self):
        return self.__parent
    
    @property
    def children(self):
        return self.__children
    
    @property
    def item(self):
        return self.__item
    
    @property
    def position(self):
        return self.__position
    
    def add_child(self, node):
        self.__children.append(node)