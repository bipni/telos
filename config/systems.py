from os import getenv as env
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(usecwd = True))

def systems():
    return {
        'server': env('SERVER', 'http'),
        'database': env('DATABASE', 'mongo')
    }