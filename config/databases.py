from os import getenv as env
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(usecwd = True))

def databases():
    return {
        'mongo': {
            'host': env('MONGO_HOST', 'localhost'),
            'port': env('MONGO_PORT', '27017'),
            'name': env('MONGO_DB_NAME', 'telos')
        },
        'redis': {
            'host': env('REDIS_HOST', 'localhost'),
            'port': env('REDIS_PORT', '6379'),
        }
    }