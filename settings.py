import os
from dotenv import load_dotenv


load_dotenv()

DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_ENGINE'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
    }
}

SECRET_KEY = os.getenv('SECRET_KEY')

INSTALLED_APPS = ['datacenter']

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

