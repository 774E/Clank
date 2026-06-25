"""
Runs the import pipeline on a configurable interval.
  python scheduler.py           →  runs once immediately, then every N minutes
  python scheduler.py --once    →  single run, then exit
"""

import sys
import time
import schedule
import argparse
sys.path.insert(0, __import__('os').path.dirname(__file__))

from importer import run
from config import SCRAPE_INTERVAL_MINUTES


def job():
    try:
        run()
    except Exception as e:
        print(f'[scheduler] unhandled error: {e}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--once', action='store_true', help='run once and exit')
    args = parser.parse_args()

    print(f'[scheduler] starting — interval: {SCRAPE_INTERVAL_MINUTES} min')
    job()  # always run immediately on start

    if args.once:
        sys.exit(0)

    schedule.every(SCRAPE_INTERVAL_MINUTES).minutes.do(job)
    print(f'[scheduler] next run in {SCRAPE_INTERVAL_MINUTES} min. Ctrl-C to stop.')
    while True:
        schedule.run_pending()
        time.sleep(30)
