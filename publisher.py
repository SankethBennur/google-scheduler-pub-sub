import os
from google.cloud import pubsub_v1
from dotenv import load_dotenv

load_dotenv("D:\QUICKMETRIX\google-scheduler-pub-sub\.env")

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.environ["PUB_SUB_KEY"]

publisher = pubsub_v1.PublisherClient()

topic_path = os.environ["TOPIC_PATH"] + "daily-report-test-01"
message = 'Daily Reports message 01'
message = message.encode('utf-8')
attributes = {
    'client_name': 'myntra',
    'clothes_sold': '50'
}

future = publisher.publish(topic_path, message, **attributes)
print(f'published message id {future.result()}')

