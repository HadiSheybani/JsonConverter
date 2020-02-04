import sys
from Convertor.framework.convertor import Convertor
from Convertor.tests.run_tests import run_tests
from Convertor.help_command import help_command
from django.core.management import execute_from_command_line
import json
import os

if len(sys.argv) == 1:
    print(help_command)
else:
    if sys.stdin.isatty():
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'convertor_server.settings')
        if sys.argv[1] == '--runtests':
            print('Convertor Tests:')
            run_tests()
            print('Rest API Tests:')
            execute_from_command_line(['manage.py', 'test'])
        if sys.argv[1] == '--help':
            print(help_command)
        if sys.argv[1] == '--runserver':
            execute_from_command_line(['manage.py', 'runserver'])
    else:
        data = sys.stdin.readlines()
        input_data = str()
        for d in data:
            input_data = input_data + d
        
        convertor = Convertor()
        result = convertor.convert(input_data, sys.argv[1:])
        print(json.dumps(result, indent=4, sort_keys=True))
