from abc import abstractmethod

class SendResult:

    @abstractmethod
    def send(self, data):
        pass