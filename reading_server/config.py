import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
   SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:93rhdgkd@localhost/smart_reading'
   DEBUG = True
