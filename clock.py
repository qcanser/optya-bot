from apscheduler.schedulers.blocking import BlockingScheduler
from bot import send_congratulations, send_new_podcast

sched = BlockingScheduler()
sched.add_job(send_congratulations, 'cron', day_of_week='mon-sun', hour=13, minute=35)
sched.add_job(send_new_podcast, 'cron', day_of_week='mon-sun', hour=13, minute=36)


sched.start()
