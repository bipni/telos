from setuptools import setup, find_packages
from config.app import app

app_info = dict(**app())

setup(
    name = app_info['name'],
    version = '0.0.0',
    description = 'A framework that everybody needs.',
    author = 'Mirja Wakil',
    author_email = 'bipumirja@gmail.com',
    license = 'MIT',
    zip_safe = False,
    entry_points = {
        'console_scripts': [f'{app_info["name"]}=src.entry.start:main'],
    }
)