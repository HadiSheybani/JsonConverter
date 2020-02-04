from django.test import TestCase
from django.test import Client
import json
from hamcrest import *

# Create your tests here.

class ConvertorTestCase(TestCase):
    def test_GivenDataByPostRequestThenCheckResponse(self):
        with open('samples/input.json', 'r') as input_sample:
                input_data = json.load(input_sample)
            
        with open('samples/output.json', 'r') as output_sample:
                output_data = json.load(output_sample)
        
        client = Client()
        content = json.dumps(input_data)
        content_type = 'application/json'
        response = client.post('/convertor/?currency=&country=&city=', content, content_type=content_type)
        assert_that(response.status_code, equal_to(200))
        assert_that(json.loads(response.content), equal_to(output_data))
