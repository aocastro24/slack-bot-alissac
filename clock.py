from apscheduler.schedulers.blocking import BlockingScheduler
from hello import views
from hello.views import slack_bToken, trendingPosts

sched = BlockingScheduler()

# @sched.scheduled_job('interval', minutes=1)
# def timed_job():
#     slack_bToken.api_call(
#         "chat.postMessage",
#         channel="CC4A68V54",
#         text=trendingPosts()
#     )

@sched.scheduled_job('cron', day_of_week='mon-sun', hour=13)
def scheduled_job():
    slack_bToken.api_call(
        "chat.postMessage",
        channel="CC4A68V54",
        text=trendingPosts()
    )

sched.start()