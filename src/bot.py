from telethon import TelegramClient
from telethon.tl.functions.messages import SendMessageRequest

import config

import datetime
import time
import random


def forayTime(chatTarget):
    time.sleep(random.randint(1, 10))
    client(SendMessageRequest(chatTarget, message="/go"))
    print("Sent /GO order. ")


def defenseTime(chatTarget):
    time.sleep(random.randint(1, 30))
    client(SendMessageRequest(chatTarget, message="🛡Defend"))
    print("Sent defense order.")

    # Waiting 5 minutes for end of battle
    time.sleep(300)


def isWartime(datetime):
    schedule = [4, 12, 20]

    for val in schedule:
        if datetime.hour == val and datetime.minute >= random.randint(54, 58):
            return True

    return False


# Inicia o client
client = TelegramClient(config.session_name, config.api_id, config.api_hash)

try:
    client.start()
except:
    print("Connecting error.")
    quit()

print("Connected.")

chatTarget = 'chtwrsbot'

# Lazy loop, sorry for that
while True:

    # Get current time.
    timeNow = datetime.datetime.now()

    # Get target last message, I know its fallible, but who cares?
    messages = client.get_message_history(chatTarget, limit=1)

    # Check Foray
    if messages[0].message.find('/go') != -1:
        print(str(timeNow) + " - Foray incoming:")
        print("     " + str(messages[0].message))
        forayTime(chatTarget)

    # Check Wartime
    if isWartime(timeNow):
        print(str(timeNow) + " - Defense time!")
        isDefended = True
        defenseTime(chatTarget)

    # Timer, in seconds.
    time.sleep(60)
