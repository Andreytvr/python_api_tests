import os
from dotenv import dotenv_values

ENV_FILE = os.getenv('ENV')

if ENV_FILE is None:
    raise Exception("Unknown value of ENV variable. You need to set ENV variable. Example: '.env'")

config = dotenv_values(ENV_FILE)

