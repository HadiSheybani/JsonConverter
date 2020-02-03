from abc import abstractmethod

class Parser:

    @abstractmethod
    def parse(self, input_data, args):
        pass