from os import environ
import slackclient
# from django.shortcuts import render
# from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from tweepy import OAuthHandler, API
import json

oAuth_token = environ.get('oAuth_token', None)
slack_aToken = slackclient.SlackClient(oAuth_token)
bot_token = environ.get('bot_token', None)
slack_bToken = slackclient.SlackClient(bot_token)

def trendingPosts():
    twitter_cKey = environ('consumer_key', None)
    twitter_sKey = environ('consumer_secret', None)
    twitter_aToken = environ('access_token', None)
    twitter_aSToken = environ('access_token_secret', None)

    auth = OAuthHandler(twitter_cKey, twitter_sKey)
    auth.set_access_token(twitter_aToken, twitter_aSToken)
    api = API(auth)

    WOE_ID = 1
    trending = api.trends_place(WOE_ID)
    print(trending)
    trending = json.loads(json.dumps(trending, indent=1))
    return trending

def responseBot(request):
    channel_event = json.loads(request.body)
    get_eventChannel = channel_event["event"]["channel"]
    get_eventText = channel_event["event"]["text"]

    if ("top" in get_eventText) or ("trending" in get_eventText):
        slack_aToken.api_call(
            "chat.postMessage",
            channel = get_eventChannel,
            text = trendingPosts
        )
    else:
        slack_aToken.api_call(
            "chat.postMessage",
            channel=get_eventChannel,
            text="Can't find trending posts. Sorry! Try again tomorrow :D"
        )
    return ""

@csrf_exempt
def accessUrl(request):
    reqBody = json.loads(request.body)
    token_Jrequest = reqBody["token"]
    if environ.get("ver_token") == token_Jrequest:
        # challenge = reqBody["challenge"]
        responseBot(request)
    else:
        challenge = "Your token is not the same"
    return request