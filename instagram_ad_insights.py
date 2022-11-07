# import asyncio
import sys
import json

class instagram_ad_insights():
    def __init__(self, message):
        self.message = json.loads(message)
        self.print_message()


    # async def print_message(self):    
    def print_message(self):    
        print("\n===================")
        print("Instagram Ad Insights")
        print("-------------------")
        
        # asyncio.sleep(15)
        # if(self.message.data): print(self.message.data)
        # if(self.message.attributes): print(self.message.attributes)
        
        print(self.message["data"])
        print(self.message["attributes"])
        print("===================\n")


if __name__ == "__main__":
    instagram_ad_insights(sys.argv[1])