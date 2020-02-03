from Convertor.framework.parser import Parser
from Convertor.usecase.element_list_factory import ElementListFactory
from Convertor.usecase.nested_convert import NestedConvert
from Convertor.framework.send_result import SendResult

class ConsoleParser(Parser):
    def __init__(self, element_list_facotory : ElementListFactory, 
                    nested_convert : NestedConvert,
                    send_result : SendResult):
        self.__element_list_factory = element_list_facotory
        self.__nested_convert = nested_convert
        self.__send_result = send_result
    
    def parse(self, input_data : str, args : list):
        if len(input_data) == 0:
            raise ValueError("No Input Data")
        
        if len(args) == 0:
            raise ValueError("No Args")

        element_list = self.__element_list_factory.create_element_list_by_json_str(input_data)
        result = self.__nested_convert.convert(element_list, args)
        self.__send_result.send(result)