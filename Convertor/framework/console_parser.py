from Convertor.framework.parser import Parser
from Convertor.usecase.element_list_factory import ElementListFactory

class ConsoleParser(Parser):
    def __init__(self, element_list_facotory : ElementListFactory):
        self.__element_list_factory = element_list_facotory
    
    def parse(self, input_data : str, args : list):
        if len(input_data) == 0:
            raise ValueError("No Input Data")
        
        if len(args) == 0:
            raise ValueError("No Args")

        element_list = self.__element_list_factory.create_element_list_by_json_str(input_data)