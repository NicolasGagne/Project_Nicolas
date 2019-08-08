# Setting file for python Raspberry PI server
# Change only the needed setting for the PI


import os
from .settings_local import *

ALLOWED_HOSTS = [
    '127.0.0.1:8008'
]

DEBUG = True