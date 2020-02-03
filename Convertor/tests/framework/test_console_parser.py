import pytest
from hamcrest import *
from mock import Mock

from Convertor.framework.console_parser import ConsoleParser
from Convertor.usecase.element_list_factory import ElementListFactory
from Convertor.usecase.nested_convert import NestedConvert
from Convertor.framework.send_result import SendResult
from Convertor.entity.element import Element

class TestConsoleParser:
    def setup_method(self, method):
        self.__element_list_facotory = Mock(spec=ElementListFactory)
        self.__nested_convert = Mock(spec=NestedConvert)
        self.__send_result = Mock(spec=SendResult)
        self.__console_parser = ConsoleParser(self.__element_list_facotory, 
                                                self.__nested_convert,
                                                self.__send_result)

    def test_GivenEmptyInptDataWhenCallParseThenItShouldRaiseNoInputDataValueError(self):
        try:
            self.__console_parser.parse("", {"arg1", "arg2"})
            assert False
        except ValueError as e:
            assert_that(e.args[0], equal_to("No Input Data"))
    
    def test_GivenEmptyArgsListWhenCallParseThenItShouldRaiseNoArgsValueError(self):
        try:
            self.__console_parser.parse("input", [])
            assert False
        except ValueError as e:
            assert_that(e.args[0], equal_to("No Args"))
    
    def test_GivenInputDataWhenCallParseThenItShouldCallElementListFactoryOnce(self):
        input_data = '[{"input": "value"}]'
        args = ["arg1", "arg2"]
        self.__console_parser.parse(input_data, args)
        self.__element_list_facotory.create_element_list_by_json_str.assert_called_once_with(input_data)
    
    def test_GivenInputDataWhenCallParseThenItShouldCallNestedConvertOnce(self):
        input_data = '[{"input": "value"}]'
        args = ["arg1", "arg2"]
        elemets_list = [Element({"input" : "value"})]
        self.__element_list_facotory.create_element_list_by_json_str.return_value = elemets_list
        self.__console_parser.parse(input_data, args)
        self.__nested_convert.convert.assert_called_once_with(elemets_list, args)
    
    def test_GivenInputDataWhenCallParseThenItShouldCallSendResultOnce(self):
        input_data = '[{"input": "value"}]'
        args = ["arg1", "arg2"]
        elemets_list = [Element({"input" : "value"})]
        result = {"input": [{"value"}]}
        self.__element_list_facotory.create_element_list_by_json_str.return_value = elemets_list
        self.__nested_convert.convert.return_value = result
        self.__console_parser.parse(input_data, args)
        self.__send_result.send.assert_called_once_with(result)

    def test_GivenInputDataWhenCallParseAndSendResultInNoneThenItShouldReturnResult(self):
        console_parser = ConsoleParser(self.__element_list_facotory, self.__nested_convert)
        input_data = '[{"input": "value"}]'
        args = ["arg1", "arg2"]
        elemets_list = [Element({"input" : "value"})]
        result = {"input": [{"value"}]}
        self.__element_list_facotory.create_element_list_by_json_str.return_value = elemets_list
        self.__nested_convert.convert.return_value = result
        output = console_parser.parse(input_data, args)
        assert_that(output, equal_to(result))

    
    


