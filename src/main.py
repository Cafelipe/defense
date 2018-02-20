# coding=utf-8
from telethon import TelegramClient
from telethon.utils import get_display_name
from telethon.tl.functions.messages import SendMessageRequest
from telethon.tl.types import PeerChannel
from telethon.tl.types import PeerUser

import configparser
import json
import os


def printJSON(var):
    print(json.dumps(var, sort_keys=True, indent=4, separators=(',', ': ')))


def returnPeer(dialogo):
    if dialogo.__class__.__name__ == "Channel":
        peer = PeerChannel(dialogo.id)
        return peer
    elif dialogo.__class__.__name__ == "User":
        peer = PeerUser(dialogo.id)
        return peer


def carregaChat(dialogo, lim=10):
    while True:
        messages = client.get_message_history(dialogo, limit=lim)
        for x in range(lim - 1, -1, -1):
            print(str(messages[x].from_id) + ":")
            print("     " + messages[x].message)
            print()

        print("------------------------------------------")
        resp = input('>: ')
        if resp == "!q":
            break
        elif resp == '':
            None
        else:
            client(SendMessageRequest(peer=returnPeer(dialogo), message=resp))

    return


# Busca as configurações no config.ini
config = configparser.ConfigParser()
config.read('config.ini')
api_id = config["telegramAPI"]['api_id']
api_hash = config["telegramAPI"]['api_hash']
session_name = config['telegramAPI']['session_name'

# Inicia o client
client = TelegramClient(session_name, api_id, api_hash)
client.start()

# Variaveis de controle
total_resultados = 10
isLoop = True
i = None

while isLoop:

    # Busca os ultimos N conversar ativas
    dialog = client.get_dialogs(limit=total_resultados)
    os.system('cls')
    print("------------------------------------------")
    print("Listando ultimas " + str(total_resultados) + " conversas:")

    for x in range(0, int(total_resultados)):
        print(str(x) + ' - ' + get_display_name(dialog[x].entity))

    print("------------------------------------------")
    print('  Digite o código da conversa para selecionar.')
    print('  !Lim: Alterar limite de conversas listadas.')
    print('  !S: Pesquisar contato por usuário.')
    print('  !Q: Finaliza.')
    print("------------------------------------------")
    i = input('Entre com o CHAT ID ou um comando: ')

    if i == '!Q':
        isLoop = False

    elif i == '!S':
        usuario = client.get_entity(input('Pesquisar por: '))
        print('Nome: ' + str(usuario.first_name) + ' ' + str(usuario.last_name))
        print('Usuário: ' + str(usuario.username))
        print('Chat ID: ' + str(usuario.id))

    elif i == '!Lim':
        total_resultados = input('Digite o nome limite de conversas: ')

    else:
        os.system('cls')
        print("Selecionado " + get_display_name(dialog[int(i)].entity) + " - ID: " + str(dialog[int(i)].entity.id))
        print()
        carregaChat(dialog[int(i)].entity)

    print()