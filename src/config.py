import configparser

# Busca as configuracoes no config.ini
config = configparser.ConfigParser()
config.read('config.ini')

api_id = config['telegramAPI']['api_id']
api_hash = config['telegramAPI']['api_hash']
session_name = config['telegramAPI']['session_name']
