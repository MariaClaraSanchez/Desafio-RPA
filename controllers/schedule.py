import schedule
import time


class Schedule:
    def __init__(self, func) -> None:
        print("I'm working...")

        schedule.every().day.at("10:50").do(func)

        while True:
            schedule.run_pending()
            time.sleep(1)
