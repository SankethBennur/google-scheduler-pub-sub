import asyncio
import sys
import json

class daily_reports():
    def __init__(self, message):
        self.message = json.loads(message)
        asyncio.run(self.print_message())


    async def print_message(self):    
    # def print_message(self):    
        print("Going to sleep for 15 seconds ... ")
        await asyncio.sleep(15)

        print("\n===================")
        print("Daily Reports")
        print("-------------------")
        
        # if(self.message.data): print(self.message.data)
        # if(self.message.attributes): print(self.message.attributes)
        
        print(self.message["data"])
        print(self.message["attributes"])
        print("===================\n")


if __name__ == "__main__":
    daily_reports(sys.argv[1])