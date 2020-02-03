from Convertor.usecase.element_list import ElementList
from Convertor.entity.element import Element
import copy

class NestedConvert:
    def convert(self, element_list : ElementList, nested_keys : list):
        if len(element_list) == 0:
            raise ValueError("No Input Element")
        
        elements = element_list.get_list()
        return self.__nest_convert(elements, nested_keys)
        

    def __nest_convert(self, elements_list : list, keys : list):
        if len(keys) == 0:
            return self.__get_output_without_key(elements_list)
        nested_output = dict()
        key = keys.pop(0)
        for element in elements_list:
            value = element.get(key)
            if value is None:
                continue
            finded_element = self.__get_all_element_with_value(elements_list, value, key)
            self.__delete_key_from_finded_element(finded_element, key)
            nested_output[value] = self.__nest_convert(finded_element, keys.copy())
        return nested_output


    def __get_all_element_with_value(self, element_list : list, value, key):
        output = list()
        for element in element_list:
            if (element.has_value(value)):
                output.append(element)
        return output

    def __delete_finded_elemets_from_list(self, element_list : list, finded_element : list):
        for element in finded_element:
            element_list.remove(element)
    
    def __delete_key_from_finded_element(self, finded_element : list, key):
        for element in finded_element:
            element.delete(key)

    def __get_output_without_key(self, element_list):
        output = list()
        for element in element_list:
            output.append(element.get_dict())
        return output
        
        
