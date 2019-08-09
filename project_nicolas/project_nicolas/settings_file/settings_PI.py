# Setting file for python Raspberry PI server
# Change only the needed setting for the PI


import os
from .settings_local import *

ALLOWED_HOSTS = [
    '127.0.0.1',
    '142.122.50.151',
    '192.168.2.37',
    'nicolasgagne.freeddns.org',
]

DEBUG = True