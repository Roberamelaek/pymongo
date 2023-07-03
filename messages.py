import pymongo
from datetime import datetime
from pymongo import MongoClient
from termcolor import colored

uri = "mongodb+srv://roberamelaek451:Robaman464546@cluster0.tsf0bk3.mongodb.net/?retryWrites=true&w=majority"

urii = MongoClient(uri)
db = urii["socialmedia"]["messaging"]
all = db.find({})
time = datetime.now().strftime("%x")

for dbmessage in all:
    try:
        if time != dbmessage['time']:
            print(colored(f"Today - {dbmessage['date']}",'red'))
        else:
            print(colored(f"{dbmessage['time']} - {dbmessage['date']}",'red'))
        print(colored(f"From:", 'green'),dbmessage['id'])
        print(colored(f"message", 'green'),dbmessage['message'])
        print("===============================================")
    except:
        pass


Person = input("name :")
message = input("message :")

date = datetime.now().strftime("%X")

msg = {"id": Person,"message": message, "date": time,"time": date,}
db.insert_one(msg)
