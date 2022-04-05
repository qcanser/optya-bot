# from apscheduler.schedulers.blocking import BlockingScheduler
from bot import send_congratulations, send_new_podcast

# sched = BlockingScheduler()


# @sched.scheduled_job('cron', day_of_week='mon-sun', hour=11)
# def timed_job():
#     send_congratulations()
#     send_new_podcast()


# sched.start()

from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

sched.add_job(send_congratulations, send_new_podcast, 'cron', day_of_week='mon-sun', hour=12, minute=20)
# @sched.scheduled_job('cron', day_of_week='mon-fri', hour=11, minute=35)
# def scheduled_job():
#     print('This job is run every weekday at 5pm.')


sched.start()
