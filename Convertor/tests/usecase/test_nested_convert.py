import pytest
from hamcrest import *
from mock import MagicMock

from Convertor.usecase.nested_convert import NestedConvert
from Convertor.usecase.element_list import ElementList
from Convertor.entity.element import Element

class TestNestedConvert:
    def setup_method(self, method):
        self.__nested_convert = NestedConvert()
        self.__elements = list()

    def __generate_elements(self):
        self.__elements.append(Element({"country": "US",
                                        "city": "Boston",
                                        "currency": "USD",
                                        "amount": 100}))

    def test_GivenElementListWithZeroLengthWhenCallConvertItShouldRaiseNoInputElementValueError(self):
        element_list = MagicMock(spec=ElementList)
        element_list.__len__.return_value = 0
        try:
            self.__nested_convert.convert(element_list, list())
            assert False
        except ValueError as e:
            assert_that(e.args[0], equal_to("No Input Element"))
    
    
    def test_GivenElementListWhenCallConvertItShouldReturnCorrectData(self):
        self.__generate_elements()
        keys = ["currency", "country", "city"]
        correct_output = {"USD": {"US": {"Boston": [{"amount": 100}]}}}
        element_list = MagicMock(spec=ElementList)
        element_list.get_list.return_value = self.__elements
        element_list.__len__.return_value = 1
        nested_output = self.__nested_convert.convert(element_list, keys)
        assert_that(nested_output, equal_to(correct_output))
        