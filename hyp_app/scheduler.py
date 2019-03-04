from apscheduler.schedulers.background import BackgroundScheduler
from . import tasks


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(tasks.test, 'interval', seconds=5)
    scheduler.start()