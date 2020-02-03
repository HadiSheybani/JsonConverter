from Convertor.framework.send_result import SendResult
import json

class SendResultToConsole(SendResult):

    def send(self, data):
        try:
            result = json.dumps(data)
            print(result)
        except:
            raise ValueError("Wrong Output")