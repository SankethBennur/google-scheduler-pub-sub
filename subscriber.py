import os
import asyncio

from google.cloud import pubsub_v1
from concurrent.futures import TimeoutError
from dotenv import load_dotenv

from controller import *


load_dotenv("D:\QUICKMETRIX\google-scheduler-pub-sub\.env")
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.environ["SERVICE_ACCOUNT_KEY_PUBSUB"]

subscription_enum = ["daily-reports-01", "instagram-ad-insights-01"]

timeout = 10.0      # timeout in seconds
subscriber = pubsub_v1.SubscriberClient()
subscription_path = os.environ["SUBSCRIPTION_PATH"] + subscription_enum[0]


# Callback function - what do i do when i get the message (PULL published message from topic)
def callback(message):
    print("-------------------")
    print(f"Received message: {message}")
    message.ack()

    if(message.data): controller(message).exec()
    
    print("executing ... ")


streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
print(f"Listening for messages on {subscription_path}")


with subscriber:                                                # wrap subscriber in a "with" block to automatically call close() when done
    try:
        streaming_pull_future.result(timeout=timeout)
        # streaming_pull_future.result()                        # going without a timeout will wait & block indefinitely
    except TimeoutError:
        streaming_pull_future.cancel()                          # trigger the shutdown
        streaming_pull_future.result()                          # block until the shutdown is complete

