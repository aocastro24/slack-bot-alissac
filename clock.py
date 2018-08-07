import os

from apscheduler.schedulers.blocking import BlockingScheduler
from hello import views
from hello.views import slack_bToken, trendingPosts

sched = BlockingScheduler()

# @sched.scheduled_job('interval', minutes=1)
# def timed_job():
#     slack_bToken.api_call(
#         "chat.postMessage",
#         channel="CC316TH17",
#         text=trendingPosts()
#     )
google = "google.com"
ping_google = os.system("ping " + google)

@sched.scheduled_job('interval', minutes=15)
def timed_job():
    if ping_google == 0:
        print ("Server is awake")
    else:
        print ("Server is sleeping")

@sched.scheduled_job('cron', day_of_week='mon-sun', hour=13)
def scheduled_job():
    slack_bToken.api_call(
        "chat.postMessage",
        channel="CC316TH17",
        text=trendingPosts()
    )

sched.start()