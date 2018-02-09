# coding=utf-8
from telethon import TelegramClient

api_id = 12345
api_hash = '0123456789abcdef0123456789abcdef'

client = TelegramClient('session_name', api_id, api_hash)
client.start()

print ("Hello world")

print ("Pessoas que já conseguiram configurar o repositório e o projeto:")
print ("Tales")
print ("Vini")
print ("Manu")

print (".")
print ("Noobs que ainda não:")
print ("")
