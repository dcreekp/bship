try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
    
config = {
    'description': 'command line battleship game in python3',
    'author': 'Tarbo',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'dcreekp@gmail.com',
    'version': '0.1',
    'install_requires': 'requirements.txt',
    'packages': ['battleship'],
    'scripts': ['run'],
    'name': 'bship3'
}

setup(**config)
