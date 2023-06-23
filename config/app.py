from os import getenv as env
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(usecwd=True))


def app():
    return {
        'name': env('NAME', 'telos'),
        'region': env('REGION', 'Bangladesh')
    }
