import asyncio

class instagram_ad_insights():
    def __init__(self, message):
        self.message = message
        
    async def print_message(self):    
        print("\n===================")
        print("Instagram Ad Insights")
        print("---------------------")
        # await asyncio.sleep(15)
        if(self.message.data): print(self.message.data)
        if(self.message.attributes): print(self.message.attributes)
        print("===================\n")

def print_insta(message):
    print("\n===================")
    print("Instagram Ad Insights")
    print("---------------------")
    asyncio.sleep(15)
    if(message.data): print(message.data)
    if(message.attributes): print(message.attributes)
    print("===================\n")