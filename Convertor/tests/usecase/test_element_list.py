import pytest
from hamcrest import *
from mock import Mock

from Convertor.usecase.element_list import ElementList
from Convertor.entity.element import Element

class TestElementList:
    def setup_method(self, method):
        self.__elements_list = ElementList()
    
    def test_CreateElementListWhenCallLengthThenItsLengthShouldBeZero(self):
        assert_that(len(self.__elements_list), equal_to(0))
    
    def test_CreateElementListWhenCallGetListThenItShouldRetrunEmptyList(self):
        assert_that(self.__elements_list.get_list(), has_length(0))

    def test_CreateElementListAndAddElementToItWhenCallGetListAndLengthItShouldReturnListOfElementAndLengthOne(self):
        element = Mock(spec=Element)
        self.__elements_list.add(element)
        assert_that(len(self.__elements_list), equal_to(1))
        assert_that(self.__elements_list.get_list(), has_length(1))