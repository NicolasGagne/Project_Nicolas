# Setting file for python anywhere server
# Change only the needed setting for python anywhere


import os
from .settings_local import *

ALLOWED_HOSTS = [
    'ngagne.pythonanywhere.com'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Ngagne$project_NGagne',
        'USER': 'Ngagne',
        'PASSWORD': 'project_NGagne922794&',
        'HOST': 'Ngagne.mysql.pythonanywhere-services.com',
    }
}

DEBUG = False