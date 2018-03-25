from .base import *

SECRET_KEY = env('DJANGO_SECRET_KEY', default='u8%+!xi)88&)))83t+sanblhl05@j(l+b!61t5c%u^((#k*tdi')

DEBUG = env.bool('DJANGO_DEBUG',  default=True)
