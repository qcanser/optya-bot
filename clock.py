from apscheduler.schedulers.blocking import BlockingScheduler
from bot import send_congratulations, send_new_podcast

sched = BlockingScheduler()


@sched.scheduled_job('cron', day_of_week='mon-sun', hour=4)
def timed_job():
    send_congratulations()


@sched.scheduled_job('cron', day_of_week='mon-sun', hour=6)
def scheduled_job():
    send_new_podcast()


sched.start()