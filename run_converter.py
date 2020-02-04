import sys
from Convertor.framework.convertor import Convertor
from Convertor.tests.run_tests import run_tests
from Convertor.help_command import help_command
import json

if len(sys.argv) == 1:
    print(help_command)
else:
    if sys.stdin.isatty():
        if sys.argv[1] == '--runtests':
            run_tests()
        if sys.argv[1] == '--help':
            print(help_command)
    else:
        data = sys.stdin.readlines()
        input_data = str()
        for d in data:
            input_data = input_data + d
        
        convertor = Convertor()
        result = convertor.convert(input_data, sys.argv[1:])
        print(json.dumps(result, indent=4, sort_keys=True))
