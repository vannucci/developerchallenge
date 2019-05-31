# based on - https://realpython.com/blog/python/flask-by-example-part-1-project-setup/

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = False
    SECRET_KEY = ''
    DB_CONNECTION_STRING = ''

class ProductionConfig(Config):
    DEBUG = False
    DB_CONNECTION_STRING = 'somewhere in the cloud...'

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    DB_CONNECTION_STRING = '' #really should update this...
