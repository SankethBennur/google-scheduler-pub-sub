def exec_01(message):
    print("\n===================")
    print("Daily Reports")
    print("---------------------")
    if(message.data): print(message.data)
    if(message.attributes): print(message.attributes)

