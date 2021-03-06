import pytest
from hamcrest import *

from Convertor.entity.element import Element

class TestElement:
    def setup_method(self, method):
        self.__element = Element({"name1": 1, "name2": 2})
    
    def test_CreateElementThenTestGetterFunction(self):
        assert_that(self.__element.get("name1"), equal_to(1))
        assert_that(self.__element.get("name2"), equal_to(2))

    def test_CreateElementWhenSetAValueAgainThenItShouldReturnNewValue(self):
        assert_that(self.__element.get("name1"), equal_to(1))
        assert_that(self.__element.get("name2"), equal_to(2))
        self.__element.set("name1", 3)
        assert_that(self.__element.get("name1"), equal_to(3))
        assert_that(self.__element.get("name2"), equal_to(2))

    def test_CreateElementWhenGiveAWrongNameThenItShouldReturnNone(self):
        assert_that(self.__element.get("name3"), none())
    
    def test_CreateElementWhenCheckForTheKeyThenItShouldReturnTrue(self):
        assert_that(self.__element.has_key("name1"), equal_to(True))

    def test_CreateElementWhenCheckForValueThenItShouldReturnTrue(self):
        assert_that(self.__element.has_value(1), equal_to(True))

    def test_CreateElementWhenDeleteAKeyThenItShouldRemoveKeyCorrectly(self):
        assert_that(self.__element.has_key("name1"), equal_to(True))
        self.__element.delete("name1")
        assert_that(self.__element.has_key("name1"), equal_to(False))

