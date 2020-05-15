from os import getenv as env
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(usecwd = True))

def databases():
    return {
        'mongo': {
            'hosts': env('MONGO_HOSTS', 'localhost'),
            'ports': env('MONGO_PORTS', '27017')
        },
        'redis': {
            'hosts': env('REDIS_HOSTS', 'localhost'),
            'ports': env('REDIS_PORTS', '6379'),
        }
    }