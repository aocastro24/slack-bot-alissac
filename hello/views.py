import os

import SlackClient as SlackClient
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

slack_aToken = SlackClient(os.environ.get('oAuth_token', None))
slack_bToken = SlackClient(os.environ.get('bot_token', None))

from .models import Greeting

def trendingPosts():


def responseBot(request):
    channel_event = json.loads(request.body)
    get_eventChannel = channel_event["event"]["channel"]
    get_eventText = channel_event["event"]["text"]
    if ("top" in get_eventText) or ("trending" in get_eventText):
        slack_aToken.api_call(
            "chat.postMessage",
            channel = "CC4A68V54",
            text = trendingPosts()
        )
    else:
        slack_aToken.api_call(
            "chat.postMessage",
            channel="CC4A68V54",
            text="Can't find trending posts. Sorry! Try again tomorrow :D"
        )
    return ""

@csrf_exempt
def accessUrl(request):
    reqBody = json.loads(request.body)
    token_Jrequest = reqBody["token"]
    if os.environ.get("ver_token") == token_Jrequest:
        # challenge = reqBody["challenge"]
        getChannel(request)
    else:
        challenge = "Your token is not the same"
    return HttpResponse(challenge, content_type="text/plain")