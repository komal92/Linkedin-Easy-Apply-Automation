import os

from dotenv import load_dotenv

load_dotenv()

LINKEDIN_URL = os.getenv('LINKEDIN_URL')
USER_NAME = os.getenv('USER_NAME')
PASSWORD = os.getenv('PASSWORD')