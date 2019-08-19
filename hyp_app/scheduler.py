from apscheduler.schedulers.background import BackgroundScheduler
from . import tasks


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(tasks.cycles_scheduler, 'interval', seconds=10)
    scheduler.start()