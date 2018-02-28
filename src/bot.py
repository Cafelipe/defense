from telethon import TelegramClient
from telethon.tl.functions.messages import SendMessageRequest

import config

from datetime import datetime
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
    # UTC
    schedule = [7, 15, 23]

    for val in schedule:
        if datetime.hour == val and datetime.minute >= random.randint(54, 58):
            return True

    return False

#TOP KEK FUNCTION
def getTimezone():
    return datetime.now().hour - datetime.utcnow().hour

# Inicia o client
client = TelegramClient(config.session_name, config.api_id, config.api_hash)

try:
    client.start()
except:
    print("Connecting error.")
    quit()

print("Connected.")
print(str(time.tzname[0])+" / Timezone: "+str(getTimezone()))

#Chatwars Channel
chatTarget = 'chtwrsbot'

# Lazy loop, sorry for that
while True:

    # Get current time.
    timeNow = datetime.now()
    timeNowUTC = datetime.utcnow()

    # Get target last message, I know its fallible, but who cares?
    messages = client.get_message_history(chatTarget, limit=1)

    # Check Foray
    if messages[0].message.find('/go') != -1:
        print(str(timeNow) + " - Foray incoming:")
        print("     " + str(messages[0].message))
        forayTime(chatTarget)

    # Check Wartime
    if isWartime(timeNowUTC):
        print(str(timeNow) + " - Defense time!")
        isDefended = True
        defenseTime(chatTarget)

    # Timer, in seconds.
    time.sleep(60)
