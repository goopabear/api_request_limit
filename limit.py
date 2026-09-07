from datetime import datetime

class RateLimit():
    def __init__(self, bucket, rate):
        self.bucket_capacity = bucket
        self.current_bucket = bucket
        self.replenish_rate = rate  # In tokens per second
        self.time = datetime.now()

    def print_bucket(self):
        print(f"Current bucket value: {round(self.current_bucket, 2)}")
        return self.current_bucket

    def update_bucket(self): # Replenish the bucket based on the time elapsed since the last request
        current_time = datetime.now()
        time_diff = (current_time - self.time).total_seconds()
        self.time = current_time  # Update the last time the bucket was replenished
        
        if self.current_bucket < self.bucket_capacity:
            self.current_bucket += self.replenish_rate * time_diff
            if self.current_bucket > self.bucket_capacity:
                self.current_bucket = self.bucket_capacity
        return

    def availability(self):
        self.update_bucket()
        if self.current_bucket >= 1:
            self.current_bucket -= 1
            self.print_bucket()
            return True
        else:
            wait_time = (1 / self.replenish_rate) - (self.current_bucket / self.replenish_rate)
            print(f"Please wait {round(wait_time, 2)} seconds before making another request.")
            return False


if __name__ == "__main__":
    rate_limit = RateLimit(bucket=15, rate=0.2)  # 15 tokens, replenishing at 0.2 tokens per second
    while True:
        input("Press Enter to make a request...")
        rate_limit.request()
