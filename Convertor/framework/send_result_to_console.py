from Convertor.framework.send_result import SendResult
import json

class SendResultToConsole(SendResult):

    def send(self, data, prety_output = False):
        try:
            if prety_output:
                result = json.dumps(data, indent=4, sort_keys=True)
            else:
                result = json.dumps(data)
            print(result)
        except:
            raise ValueError("Wrong Output")