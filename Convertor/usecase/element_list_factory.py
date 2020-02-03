from Convertor.usecase.element_list import ElementList
from Convertor.entity.element import Element
import json

class ElementListFactory:

    def __init__(self):
        pass

    def create_element_list(self, data : list) -> ElementList:
        element_list = ElementList()
        for itr in data:
            if type(itr) is not dict:
                continue
            element = Element(itr)
            element_list.add(element)
        return element_list

    def create_element_list_by_json_str(self, data_str : str) -> ElementList:
        data = json.loads(data_str)
        return self.create_element_list(data)
