import pytest
from hamcrest import *
import json

from Convertor.framework.console_parser import ConsoleParser
from Convertor.usecase.element_list_factory import ElementListFactory
from Convertor.usecase.nested_convert import NestedConvert

class TestIntegratedConsoleParser:
    def setup_method(self, method):
        self.__input_sample = 'Convertor/tests/samples/input.json'
        self.__output_sample = 'Convertor/tests/samples/output.json'

    def test_ReadInputAndOutputSamplesFromFileWhenCallParseItShouldReturnCorrectOutput(self):
        with open(self.__input_sample, 'r') as input_sample:
            input_data = json.load(input_sample)
        
        with open(self.__output_sample, 'r') as output_sample:
            output_data = json.load(output_sample)
        
        element_list_factory = ElementListFactory()
        nested_convert = NestedConvert()
        console_parser = ConsoleParser(element_list_factory, nested_convert)
        args = ["currency", "country", "city"]
        result = console_parser.parse(json.dumps(input_data), args)
        assert_that(result, equal_to(output_data))
