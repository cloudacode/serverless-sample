import random
import time
import os
from locust import HttpUser, task

id = [
    '0PUK6V6EV0',
    '1YMWWN1N4O',
    '2ZYFJ3GM2N',
    '66VCHSJNUP',
    '6E92ZMYYFZ',
    '9SIQT8TOJO',
    'L9ECAV7KIM',
    'LS4PSXUNUM',
    'OLJCESPC7Z']

candidate = [
    'Apple',
    'Blueberry',
    'Banana',
    'Orange']

class LambdaVoting(HttpUser):
    @task
    def put_items(self):
        for item_id in range(10):
            self.client.post(os.environ['API_ENDPOINT'], json={"id":random.choice(id), "candidate":random.choice(candidate)})
            time.sleep(1)

    def on_start(self):
        self.client.post(os.environ['API_ENDPOINT'], json={"id":"foo", "candidate":"bar"})
