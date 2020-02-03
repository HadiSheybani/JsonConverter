import pytest
from hamcrest import *

from Convertor.usecase.element_list_factory import ElementListFactory
from Convertor.usecase.element_list import ElementList
from Convertor.entity.element import Element

class TestElementListFactory:
    def setup_method(self, method):
        self.__element_list_factory = ElementListFactory()
    
    def test_GivenAListOfDictionaryWhenCallCreateElementListThenItShouldReturnAnElementListWithData(self):
        data = [{"name": "reza", "family": "rezaei"},
                {"name": "ali", "family": "alizadeh"}]
        element_list = self.__element_list_factory.create_element_list(data)
        assert_that(len(element_list), equal_to(2))
        assert_that(element_list.get_list()[0].get("name"), equal_to("reza"))
        assert_that(element_list.get_list()[1].get("name"), equal_to("ali"))
    
    def test_GivenAJsonStrWhenCallCreateElementListByJsonStrThenItShouldReturnAnElementListWithData(self):
        data_str = '[{"name": "reza", "family": "rezaei"}, {"name": "ali", "family": "alizadeh"}]'
        element_list = self.__element_list_factory.create_element_list_by_json_str(data_str)
        assert_that(len(element_list), equal_to(2))
        assert_that(element_list.get_list()[0].get("name"), equal_to("reza"))
        assert_that(element_list.get_list()[1].get("name"), equal_to("ali"))
    
    def test_GivenWrongJsonStrWhenCallCreateElementListByJsonThenItShouldRaiseValueError(self):
        data_str = '[{{}'
        try:
            element_list = self.__element_list_factory.create_element_list_by_json_str(data_str)
            assert False
        except ValueError as e:
            assert True