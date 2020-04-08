from os import getenv as env
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(usecwd = True))

def servers():
    return {
        'http': {
            'host': env('HTTP_HOST', 'localhost'),
            'port': env('HTTP_PORT', '8080')
        }
    }