import pytest
from hamcrest import *
from mock import Mock
from mock import patch

from Convertor.framework.convertor import Convertor

class TestConsoleParser:
    def setup_method(self, method):
        self.__convertor = Convertor()

    def test_GivenEmptyInptDataWhenCallParseThenItShouldRaiseNoInputDataValueError(self):
        try:
            self.__convertor.convert("", {"arg1", "arg2"})
            assert False
        except ValueError as e:
            assert_that(e.args[0], equal_to("No Input Data"))
    
    def test_GivenEmptyArgsListWhenCallParseThenItShouldRaiseNoArgsValueError(self):
        try:
            self.__convertor.convert("input", [])
            assert False
        except ValueError as e:
            assert_that(e.args[0], equal_to("No Args"))

    
    


