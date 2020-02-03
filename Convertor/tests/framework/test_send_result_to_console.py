import pytest
from hamcrest import *

from Convertor.framework.send_result_to_console import SendResultToConsole

class TestSendResultToConsole:
    def test_GivenWrongDataWhenCallSendItShouldRaiseWrongOutputValueError(self):
        send_result = SendResultToConsole()
        data = {"name", "value"}
        try:
            send_result.send(data)
            assert False
        except ValueError as e:
            assert_that(e.args[0], equal_to("Wrong Output"))

    
    def test_GivenDataWhenCallSendItShouldPrintDataInStdOut(self, capsys):
        send_result = SendResultToConsole()
        data = {"name": "value"}
        send_result.send(data)
        captured = capsys.readouterr()
        assert_that(captured.out, equal_to('{"name": "value"}\n'))