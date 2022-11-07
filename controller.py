import asyncio
import time


class daily_reports():
    def __init__(self, message):
        self.message = message

    async def print_message(self):
        print("\n===================")
        print("Daily Reports")
        print("---------------------")
        print("I am going to sleep for 5 seconds...")
        await time.sleep(5)
        print("I am awake!")
        if(self.message.data): print(self.message.data)
        if(self.message.attributes): print(self.message.attributes)
        print("===================\n")


class instagram_ad_insights():
    def __init__(self, message):
        self.message = message
        
    async def print_message(self):
        print("\n===================")
        print("Instagram Ad Insights")
        print("---------------------")
        print("I am going to sleep for 5 seconds...")
        await time.sleep(5)
        print("I am awake!")
        if(self.message.data): print(self.message.data)
        if(self.message.attributes): print(self.message.attributes)
        print("===================\n")
