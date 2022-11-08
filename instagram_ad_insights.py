import time
import os

class instagram_ad_insights():
    def __init__(self, message):
        self.message = message


    def print_message(self):    
        print(self.message["data"])
        print("{}: Going to sleep for 10 seconds ... ".format(os.getpid()))
        time.sleep(2)

        print("\n===================")
        print(self.message["data"])
        print("-------------------")
        print(self.message["attributes"])
        print("===================\n")

