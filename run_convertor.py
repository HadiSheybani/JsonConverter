
try:
    import sys
    from Convertor.framework.convertor import Convertor
    from Convertor.help_command import help_command
    from django.core.management import execute_from_command_line
    import json
    import os
    import pytest

    if len(sys.argv) == 1:
        print(help_command)
    else:
        if sys.stdin.isatty():
            os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'convertor_server.settings')
            if sys.argv[1] == '--runtests':
                pytest.main(['-v'])
            if sys.argv[1] == '--help':
                print(help_command)
            if sys.argv[1] == '--runserver':
                execute_from_command_line(['manage.py', 'runserver'])
            if sys.argv[1] == '--django-command':
                argv = sys.argv[1:]
                execute_from_command_line(argv)
        else:
            data = sys.stdin.readlines()
            input_data = str()
            for d in data:
                input_data = input_data + d
            
            convertor = Convertor()
            result = convertor.convert(input_data, sys.argv[1:])
            print(json.dumps(result, indent=4, sort_keys=True))
except:
    print(
    """"
    Couldn't import Requirements. Are you sure it's installed and
    available on your PYTHONPATH environment variable? Did you
    forget to activate a virtual environment?
    You can install Requirements like this:
    pip install -r requirements.txt
    """)
