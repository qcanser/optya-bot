# from apscheduler.schedulers.blocking import BlockingScheduler
from bot import send_congratulations, send_new_podcast

# sched = BlockingScheduler()


# @sched.scheduled_job('cron', day_of_week='mon-sun', hour=11)
# def timed_job():
#     send_congratulations()
#     send_new_podcast()


# sched.start()

from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler(timezone="Europe/Moscow")

sched.add_job(send_congratulations, send_new_podcast, 'cron', day_of_week='mon-sun', hour=15, minute=8)
# @sched.scheduled_job('cron', day_of_week='mon-fri', hour=11, minute=35)
# def scheduled_job():
#     print('This job is run every weekday at 5pm.')


sched.start()
