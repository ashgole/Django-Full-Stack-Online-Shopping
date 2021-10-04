from django.db.models.fields import DateTimeField
from django.http.response import HttpResponse
from home.models import *
from django.template import Context, Template
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from  home.views.productsJson import *