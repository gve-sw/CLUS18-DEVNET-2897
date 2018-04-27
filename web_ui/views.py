from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import json
import traceback
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from web_ui.controllers.apic import ApicController
import os
import random

### Prefix generation

try:
    base_path = os.path.dirname(os.path.realpath(__file__))
    if not os.path.exists(base_path + '/.prefix'):
        file = open(base_path + '/.prefix', 'w')
        file.write(str(random.randint(1000, 9999)))
        file.close()
    file = open(base_path + '/.prefix', 'r')
    PREFIX = "CLUS2897-" + file.read()
except:
    PREFIX = "CLUS2897"


# ====================>>>>>>>> Utils <<<<<<<<====================
class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


# ====================>>>>>>>> Templates <<<<<<<<====================


def index(request):
    return render(request, 'web_app/index.html')


def home(request):
    return render(request, 'web_app/home.html', context={"prefix": PREFIX})


# ====================>>>>>>>> APIs <<<<<<<<====================

### STEP 8 - API METHODS CODE BELOW