import pytest
from hamcrest import *
import json

from Convertor.framework.convertor import Convertor

class TestIntegratedConsoleParser:
    def setup_method(self, method):
        self.__input_sample = 'samples/input.json'
        self.__output_sample = 'samples/output.json'

    def test_ReadInputAndOutputSamplesFromFileWhenCallParseItShouldReturnCorrectOutput(self):
        with open(self.__input_sample, 'r') as input_sample:
            input_data = json.load(input_sample)
        
        with open(self.__output_sample, 'r') as output_sample:
            output_data = json.load(output_sample)
        
        convertor = Convertor()
        args = ["currency", "country", "city"]
        result = convertor.convert(json.dumps(input_data), args)
        assert_that(result, equal_to(output_data))
