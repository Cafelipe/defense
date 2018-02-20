from telethon import TelegramClient
from telethon.tl.functions.messages import SendMessageRequest
from datetime import datetime

import config

import datetime
import time
import random

from src.playerStatus import PlayerStatus


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
    schedule = [0, 4, 8, 12, 16, 20]

    for val in schedule:
        if datetime.hour == val and datetime.minute >= random.randint(54, 58):
            return True

    return False

# Returns the delta Time between now() and the parameter.
# Copied from: https://stackoverflow.com/a/14978116
def delta_time_ms(t):
   dt = datetime.datetime.now() - t
   ms = (dt.days * 24 * 60 * 60 + dt.seconds) * 1000 + dt.microseconds / 1000.0
   return ms


# Posts /hero and awaits for the player status message
def getPlayerStatus():
    client(SendMessageRequest(chatTarget, message="/hero"))
    print("Posted /hero. Waiting for reply")

    status_timeout = 60*1000  # Timeout in milisseconds

    startTime = datetime.datetime.now()

    done = False

    # Waits for reply
    while not done and delta_time_ms(startTime) <= status_timeout:
        time.sleep(1)
        messages = client.get_message_history(chatTarget, limit=1)
        done = isHeroReplyMessage(messages[0])

    if done:
        print("Got reply from the server")
    else:
        print("Server did not reply in time.")






# Returns true if this message is a reply to the /hero command
# TODO: Make it work (probably using regex)
def isHeroReplyMessage(message):
    #

    if message.message.find('PEPE') != -1: ## This line detects if this message is the reply we expect. TODO: Fix it.
        print("This Message is the one I want: "+message.message)
    else:
        print("This is not the message I want "+message.message)

    return message.message.find('PEPE') != -1

# Inicia o client
client = TelegramClient(config.session_name, config.api_id, config.api_hash)

try:
    client.start()
except:
    print("Connecting error.")
    quit()

print("Connected to telegram.")

chatTarget = 'chtwrsbot'

# Bot initialization:

print("Starting bot. Getting player status...")

status = PlayerStatus()

getPlayerStatus()


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
