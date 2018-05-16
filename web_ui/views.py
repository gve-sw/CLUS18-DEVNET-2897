"""
Copyright (c) 2018 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.0 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.

"""
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

@csrf_exempt
def api_pod(request):
    """
       Return a json list of pods
       :param request:
       :return:
    """
    if request.method == 'GET':
        try:
            # Create a new controller
            apic = ApicController()

            # Get the pods
            pods = apic.getPods()

            # Send pods to the web client
            return JSONResponse(pods)
        except Exception as e:
            print(traceback.print_exc())
            # return the error to web client
            return JSONResponse({'error': e.__class__.__name__, 'message': str(e)}, status=500)
    else:
        # return the error to web client
        return JSONResponse("Bad request. " + request.method + " is not supported", status=400)


@csrf_exempt
def api_switch(request, podDn):
    """
       Return a list of switches for a given pod
       :param request:
       :return:
       """
    if request.method == 'GET':
        try:
            # Create a new controller
            apic = ApicController()

            # Get the leaf switches for a given pod
            switches = apic.getLeafs(pod_dn=podDn)

            # Send the leaf switches to the web client
            return JSONResponse(switches)
        except Exception as e:
            print(traceback.print_exc())
            # return the error to web client
            return JSONResponse({'error': e.__class__.__name__, 'message': str(e)}, status=500)
    else:
        # return the error to web client
        return JSONResponse("Bad request. " + request.method + " is not supported", status=400)


@csrf_exempt
def api_interface(request, switchDn):
    """
       Return a list of interfaces for a given switch
       :param request:
       :return:
    """
    if request.method == 'GET':
        try:
            # Create a new controller
            apic = ApicController()

            # Get the interfaces for a given switch
            interfaces = apic.getInterfaces(switch_dn=switchDn)

            # Send the interfaces to the web client
            return JSONResponse(interfaces)
        except Exception as e:
            print(traceback.print_exc())
            # return the error to web client
            return JSONResponse({'error': e.__class__.__name__, 'message': str(e)}, status=500)
    else:
        # return the error to web client
        return JSONResponse("Bad request. " + request.method + " is not supported", status=400)


@csrf_exempt
def api_epg(request):
    """
       Return a list of EPG for a given tenant
       :param request:
       :return:
   """
    if request.method == 'GET':
        try:
            # Create a new controller
            apic = ApicController()

            # Get all tenants for the configured prefix
            tenants = apic.getTenants(query_filter='eq(fvTenant.name,"' + PREFIX + '")')
            if len(tenants) == 0:
                return JSONResponse([])

            # Get all application profiles for the tenant
            aps = apic.getAppProfiles(tenant_dn=tenants[0]["fvTenant"]["attributes"]["dn"],
                                      query_filter='eq(fvAp.name,"' + PREFIX + '")')
            if len(aps) == 0:
                return JSONResponse([])

            # Get all EPGs from the first application profile
            epgs = apic.getEPGs(ap_dn=aps[0]["fvAp"]["attributes"]["dn"])

            # Send EPGs to web client
            return JSONResponse(epgs)
        except Exception as e:
            print(traceback.print_exc())
            # return the error to web client
            return JSONResponse({'error': e.__class__.__name__, 'message': str(e)}, status=500)
    else:
        # return the error to web client
        return JSONResponse("Bad request. " + request.method + " is not supported", status=400)


@csrf_exempt
def api_deploy(request):
    """
   Creates a port deployment in ACI
   :param request:
   :return:
   """
    if request.method == 'POST':
        try:
            # Parse request body to json
            payload = json.loads(request.body)

            # Create a new controller
            apic = ApicController()

            # Create a new deployment
            apic.createDeployment(payload, PREFIX)
            print("Deployment Done!")

            # Reply ok to the web client
            return JSONResponse("ok")
        except Exception as e:
            print(traceback.print_exc())
            # return the error to web client
            return JSONResponse({'error': e.__class__.__name__, 'message': str(e)}, status=500)
    else:
        # return the error to web client
        return JSONResponse("Bad request. " + request.method + " is not supported", status=400)
