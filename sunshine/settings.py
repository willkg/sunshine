import os


def truthy(item):
    return item.lower().startswith('t')


DEBUG = truthy(os.environ.get('DEBUG', 'True'))
