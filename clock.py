from apscheduler.schedulers.blocking import BlockingScheduler
from bot import send_congratulations, send_new_podcast

sched = BlockingScheduler()
sched.add_job(send_congratulations, send_new_podcast, 'cron', day_of_week='mon-sun', hour=12, minute=35)


sched.start()
