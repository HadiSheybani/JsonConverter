

class Element:

    def __init__(self, data : "element data dictionary" = None):
        if data is None:
            self.__data = dict()
        else:
            self.__data = data.copy()
    
    def get(self, name):
        if name not in self.__data.keys():
            return None
        return self.__data[name]
    
    def set(self, name, value):
        self.__data[name] = value