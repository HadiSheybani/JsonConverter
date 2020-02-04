from django.shortcuts import render

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import ..Convertor.framework.
# from Convertor.framework.convertor import Convertor

@api_view(["POST"])
def ConvertorApp(data):
    input_data = data.body
    levels = list(data.query_params.dict().keys())
    convertor = Conver
    return JsonResponse(json.loads(input_data))

# Create your views here.
