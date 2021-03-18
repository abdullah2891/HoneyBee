import schedule
import time
from main import run_organizer

def job():
    run_organizer()

schedule.every(2).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
