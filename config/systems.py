from os import getenv as env
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(usecwd = True))

def systems():
    return {
        'servers': env('SERVERS', 'http'),
        'databases': env('DATABASES', 'mongo'),
        'plugins': env('PLUGINS', 'demo')
    }