import sys
from Convertor.__main__ import convertor

if len(sys.argv) == 0:
    pass
else:
    if sys.stdin.isatty():
        convertor(sys.argv[1:])
    else:
        data = sys.stdin.readlines()
        input_data = str()
        for d in data:
            input_data = input_data + d
        argv = ['console']
        argv.append(input_data)
        for flag in sys.argv[1:]:
            argv.append(flag)
        convertor(argv)
