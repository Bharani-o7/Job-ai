import schedule
import time
from main import run_jobforge


def start_watcher():
    print("Job watcher started...")

    schedule.every(3).hours.do(run_jobforge)

    while True:
        schedule.run_pending()
        time.sleep(60)


start_watcher()