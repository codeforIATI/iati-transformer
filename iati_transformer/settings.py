"""Application configuration.

Most configuration is set via environment variables.

For local development, use a .env file to set
environment variables.
"""
from environs import Env


env = Env()  # pylint: disable=invalid-name
env.read_env()

ENV = env.str('FLASK_ENV', default='production')
DEBUG = ENV == 'development'
SECRET_KEY = env.str('SECRET_KEY')
DEBUG_TB_ENABLED = DEBUG
DEBUG_TB_INTERCEPT_REDIRECTS = False
CACHE_TYPE = 'simple'  # Can be "memcached", "redis", etc.
