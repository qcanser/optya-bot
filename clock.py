from apscheduler.schedulers.blocking import BlockingScheduler
from bot import send_congratulations

sched = BlockingScheduler()
sched.add_job(send_congratulations, 'cron', day_of_week='mon-sun', hour=12, minute=29)


sched.start()
