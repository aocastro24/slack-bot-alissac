from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .models import Greeting

@csrf_exempt
def accessUrl(request):
    reqBody = json.loads(request.body)
    token_Jrequest = reqBody["Challenge"]
    if os.environ.get("ver_token") == token_Jrequest:
        challenge = reqBody["Challenge"]
    else:
        challenge = "Your token is not the same"
    return HttpResponse(challenge, content_type="text/plain")