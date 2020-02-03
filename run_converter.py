import sys
from Convertor.__main__ import convert
from Convertor.framework.convertor import Convertor
import json

if len(sys.argv) == 0:
    pass
else:
    if sys.stdin.isatty():
        convert(sys.argv[1:])
    else:
        data = sys.stdin.readlines()
        input_data = str()
        for d in data:
            input_data = input_data + d
        argv = ['console']
        argv.append(input_data)
        for flag in sys.argv[1:]:
            argv.append(flag)
        convertor = Convertor()
        result = convertor.convert(input_data, sys.argv[1:])
        print(json.dumps(result, indent=4, sort_keys=True))
