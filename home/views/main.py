# https://youtu.be/zCRIp0zVdVo?list=PLC0eYK7mhf_TnOUwpLaNjOgtAjgneVfGM FIXME celery
'''
myenv\scripts\activate.bat
python manage.py runserver

'''
from django.http import HttpResponse 
from .task import *

def index(request):
    # sleepy.delay(10)
    return HttpResponse('ashabb')
 
