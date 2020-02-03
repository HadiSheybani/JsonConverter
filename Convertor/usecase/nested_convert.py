from Convertor.usecase.element_list import ElementList
from Convertor.entity.element import Element
import copy

class NestedConvert:
    def convert(self, element_list : ElementList, nested_keys : list):
        if len(element_list) == 0:
            raise ValueError("No Input Element")
        

    def __nest_convert(self, element_list : list, keys : list):

        elemens = elemens_list.copy()
        nested_output = dict()
        
        
