




class Node():
    def __init__(self, item, depth, zone):
        self.__children = []
        self.__item = item            
        self.__depth = depth
        self.__type = zone
        self.__status = False

    
    
    @property
    def children(self):
        return self.__children
    
    @property
    def item(self):
        return self.__item
    
    @property
    def type(self):
        return self.__type
    
    @property
    def status(self):
        return self.__status
    
    
    def add_child(self, node):
        self.__children.append(node)

    