from limit import RateLimit

from functools import wraps
from datetime import datetime

# Wrapper function to check rate limit before executing the main request function
def allow_request(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if self.limit is None:
            raise RuntimeError("MainClass has no rate limit configured; use a subclass that sets bucket/replenish_rate")
        if self.limit.availability() is True:
            print("Request made successfully!")
            return func(self, *args, **kwargs) # Call the main request function.
        else:
            print("Request failed due to rate limiting.")
            return False
    return wrapper


class MainClass:
    bucket = None
    replenish_rate = None

    def __init__(self):
        if self.bucket and self.replenish_rate:
            self.time = datetime.now()
            self.limit = RateLimit(bucket=self.bucket, rate=self.replenish_rate)
        else:
            self.limit = None

    @allow_request
    def request(self):
        print("INSERT LOGIC HERE")


class SubClass(MainClass):
    bucket = 15
    replenish_rate = 0.2 # In tokens per second


if __name__ == "__main__":
    app = MainClass()
    while True:
        input("Press Enter to make a request...")
        app.request()