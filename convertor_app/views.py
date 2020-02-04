from django.shortcuts import render

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import sys
sys.path.insert(0, '../')
from Convertor.framework.convertor import Convertor
import json

@api_view(["POST"])
def ConvertorApp(data):
    print(data)
    input_data = data.body
    levels = list(data.query_params.dict().keys())
    try:
        convertor = Convertor()
        result = convertor.convert(input_data, levels)
        return JsonResponse(result, safe=False)
    except ValueError as e:
        return Response(e.args[0])

# Create your views here.
