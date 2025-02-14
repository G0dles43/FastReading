from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

def index(request):
    return HttpResponse("Siemano@")


@api_view(['GET'])
def api_status(request):
    return Response({"message": "API Connected Successfully"})
