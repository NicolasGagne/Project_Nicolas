# Setting file for python anywhere server
# Change only the needed setting for python anywhere


import os
from .settings_local import *

SECRET_KEY = os.getenv("SECRET_KEY_ENV")

ALLOWED_HOSTS = [
    'ngagne.pythonanywhere.com'
]

DATABASES = {
    'default': {
        'ENGINE': os.getenv("ENGINE_ENV"),
        'NAME': os.getenv("NAME_ENV"),
        'USER': os.getenv("USER_ENV"),
        'PASSWORD': os.getenv("PASSWORT_ENV"),
        'HOST': os.getenv("HOST_ENV"),
    }
}

DEBUG = False