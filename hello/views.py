from os import environ

import slackclient
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from tweepy import OAuthHandler, API
import json

# oAuth_token = environ.get('oAuth_token', None)
slack_aToken = slackclient.SlackClient(environ.get('oAuth_token', None))
# bot_token = environ.get('bot_token', None)
slack_bToken = slackclient.SlackClient(environ.get('bot_token', None))

twitter_cKey = environ.get('consumer_key', None)
twitter_sKey = environ.get('consumer_secret', None)
twitter_aToken = environ.get('access_token', None)
twitter_aSToken = environ.get('access_token_secret', None)

auth = OAuthHandler(twitter_cKey, twitter_sKey)
auth.set_access_token(twitter_aToken, twitter_aSToken)
api = API(auth)

def trendingPosts():
    WOE_ID = 1
    trending = api.trends_place(WOE_ID)
    trending = json.loads(json.dumps(trending, indent=1))
    trend_list = [].sort()
    for trend in trending[0]["trends"]:
        trend_list.append((trend["name"]))
    trend_list = ', \n'.join(trend_list[:10])

    return trend_list

def responseBot(request):
    channel_event = json.loads(request.body)
    get_eventChannel = channel_event["event"]["channel"]
    get_eventText = channel_event["event"]["text"]
    if ("top" in get_eventText) or ("trending" in get_eventText):
        slack_bToken.api_call(
            "chat.postMessage",
            channel=get_eventChannel,
            text=trendingPosts()
        )
    else:
        slack_bToken.api_call(
            "chat.postMessage",
            channel=get_eventChannel,
            text="Can't find trending posts. Sorry! Try other keywords such as top or trending"
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
    return HttpResponse(request)