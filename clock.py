from apscheduler.schedulers.blocking import BlockingScheduler
from bot import send_congratulations, send_new_podcast

sched = BlockingScheduler()
sched.add_job(send_congratulations, 'cron', day_of_week='mon-sun', hour=16, minute=38)
sched.add_job(send_new_podcast, 'cron', day_of_week='mon-sun', hour=16, minute=39)


sched.start()
