from Convertor.entity.element import Element

class ElementList:
    def __init__(self):
        self.__elements = list()
    
    def add(self, element : Element):
        self.__elements.append(element)
    
    def get_list(self):
        return self.__elements.copy()

    def __len__(self):
        return len(self.__elements)