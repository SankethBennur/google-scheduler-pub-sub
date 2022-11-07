import os
from google.cloud import pubsub_v1
from dotenv import load_dotenv

load_dotenv("D:\QUICKMETRIX\google-scheduler-pub-sub\.env")
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.environ["SERVICE_ACCOUNT_KEY_PUBSUB"]
topic_path = os.environ["TOPIC_PATH"]

publisher = pubsub_v1.PublisherClient()


# message_01 = "Daily Reports"
# message_01 = message_01.encode("utf-8")
# attributes = {
#     "client_name": "Myntra",
#     "shirts_sold": "500"
# }

# future = publisher.publish(topic_path, message_01, **attributes)
# print(f"published message id {future.result()}")


message_02 = "Instagram Ad Post Insights"
message_02 = message_02.encode("utf-8")
attributes = {
    "client_name": "Bethesda",
    "skyrim_copies_sold": "1,000,000,000"
}

future = publisher.publish(topic_path, message_02, **attributes)
print(f'published message id {future.result()}')
