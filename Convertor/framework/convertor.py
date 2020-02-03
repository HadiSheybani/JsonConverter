from Convertor.usecase.nested_convert import NestedConvert
from Convertor.usecase.element_list_factory import ElementListFactory

class Convertor:

    def __init__(self):
        self.__nested_convert = NestedConvert()
        self.__element_list_factory = ElementListFactory()
    
    def convert(self, input_data : str, nesting_levels : list):
        if len(input_data) == 0:
            raise ValueError("No Input Data")
        
        if len(nesting_levels) == 0:
            raise ValueError("No Args")
        
        element_list = self.__element_list_factory.create_element_list_by_json_str(input_data)
        return self.__nested_convert.convert(element_list, nesting_levels)
    
