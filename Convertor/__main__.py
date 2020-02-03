import sys
import pytest
from Convertor.framework.console_parser import ConsoleParser
from Convertor.framework.send_result_to_console import SendResultToConsole
from Convertor.usecase.nested_convert import NestedConvert
from Convertor.usecase.element_list_factory import ElementListFactory
from Convertor.help_command import help_command

def convert(argv):
    if argv[0] == 'runtests':
        pytest.main(['-v', '-x', 'Convertor/tests'])
        return
    if argv[0] == 'console':
        data = argv[1]
        flags = argv[2:]
        element_list_factory = ElementListFactory()
        nested_convert = NestedConvert()
        send_result_to_console = SendResultToConsole()
        console_parser = ConsoleParser(element_list_factory, nested_convert, send_result_to_console)
        console_parser.parse(data, flags)
        return
    if argv[0] == 'help':
        print(help_command)
        return


if __name__ == "__main__":
    convert(sys.argv[1:])