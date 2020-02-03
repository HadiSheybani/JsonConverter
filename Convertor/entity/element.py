

class Element:
    def __init__(self):
        self.__data = dict()
    
    def __init__(self, data : "element data dictionary"):
        self.__data = data
    
    def get(self, name):
        if name not in self.__data.keys():
            return None
        return self.__data[name]
    
    def set(self, name, value):
        self.__data[name] = value