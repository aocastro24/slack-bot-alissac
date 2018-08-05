from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .models import Greeting

@csrf_exempt
def accessUrl(request):
    reqBody = json.loads(request.body)
    print (reqBody)

    return ""