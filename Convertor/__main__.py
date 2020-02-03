import sys
import pytest

def main():
    if sys.argv[1] == 'runtests':
        pytest.main(['-v', '-x', 'Convertor/tests'])

if __name__ == "__main__":
    main()