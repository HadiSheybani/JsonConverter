from django.shortcuts import render

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes
from rest_framework.decorators import permission_classes
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings

from Convertor.framework.convertor import Convertor
import json

@api_view(["POST"])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def ConvertorApp(request, format=None):
    input_data = request.body
    levels = list(request.query_params.dict().keys())
    try:
        convertor = Convertor()
        result = convertor.convert(input_data, levels)
        return JsonResponse(result, safe=False)
    except ValueError as e:
        return Response(e.args[0])

