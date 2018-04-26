### Step 8 - Preparing server to receive and reply REST API calls
We will focus now on the server side of the application. In order to show information from ACI (such as Pods, Switches,
interfaces and EPGs) we need to code API calls in server that can return that information to the web client.
Luckily for us, using python is quite easy. Open you urls.py file and copy the following below the last defined URL:

```python
    # APIs Mappings
    url(r'^api/pod/?$', views.api_pod),
    url(r'^api/switch/(?P<podDn>.*)/?$', views.api_switch),
    url(r'^api/interface/(?P<switchDn>.*)/?$', views.api_interface),
    url(r'^api/epgs/?$', views.api_epg),
    url(r'^api/deploy/?$', views.api_deploy),
```
Looking into the code above, it is mapping URLs with specific methods that will manage http calls using that URL.
 We will create those methods in the views.py file. Copy these methods in this file (views.py) below ```====================>>>>>>>> APIs <<<<<<<<====================```

**api_pod method**

```python
@csrf_exempt
def api_pod(request):
    """
       Return a list of pods
       :param request:
       :return:
    """
    if request.method == 'GET':
        try:
            apic = ApicController()
            pods = apic.getPods()
            return JSONResponse(pods)
        except Exception as e:
            print(traceback.print_exc())
            # return the error to web client
            return JSONResponse({'error': e.__class__.__name__, 'message': str(e)}, status=500)
    else:
        return JSONResponse("Bad request. " + request.method + " is not supported", status=400)

```

**api_switch method**

```python
@csrf_exempt
def api_switch(request, podDn):
    """
       Return a list of switches
       :param request:
       :return:
       """
    if request.method == 'GET':
        try:
            apic = ApicController()
            switches = apic.getLeafs(pod_dn=podDn)
            return JSONResponse(switches)
        except Exception as e:
            print(traceback.print_exc())
            # return the error to web client
            return JSONResponse({'error': e.__class__.__name__, 'message': str(e)}, status=500)
    else:
        return JSONResponse("Bad request. " + request.method + " is not supported", status=400)

```

**api_interface method**

```python
@csrf_exempt
def api_interface(request, switchDn):
    """
       Return a list of interfaces
       :param request:
       :return:
    """
    if request.method == 'GET':
        try:
            apic = ApicController()
            interfaces = apic.getInterfaces(switch_dn=switchDn)
            return JSONResponse(interfaces)
        except Exception as e:
            print(traceback.print_exc())
            # return the error to web client
            return JSONResponse({'error': e.__class__.__name__, 'message': str(e)}, status=500)
    else:
        return JSONResponse("Bad request. " + request.method + " is not supported", status=400)

```

**api_epg method**
```python
@csrf_exempt
def api_epg(request):
    """
       Return a list of EPG for a given tenant
       :param request:
       :return:
   """
    if request.method == 'GET':
        try:
            apic = ApicController()
            tenants = apic.getTenants(query_filter='eq(fvTenant.name,"' + PREFIX + '")')
            if len(tenants) == 0:
                return JSONResponse([])
            aps = apic.getAppProfiles(tenant_dn=tenants[0]["fvTenant"]["attributes"]["dn"],
                                      query_filter='eq(fvAp.name,"' + PREFIX + '")')
            if len(aps) == 0:
                return JSONResponse([])
            epgs = apic.getEPGs(ap_dn=aps[0]["fvAp"]["attributes"]["dn"])
            return JSONResponse(epgs)
        except Exception as e:
            print(traceback.print_exc())
            # return the error to web client
            return JSONResponse({'error': e.__class__.__name__, 'message': str(e)}, status=500)
    else:
        return JSONResponse("Bad request. " + request.method + " is not supported", status=400)

```

**api_deploy method**

```python
@csrf_exempt
def api_deploy(request):
    """
   Creates a port deployment in ACI
   :param request:
   :return:
   """
    if request.method == 'POST':
        try:
            payload = json.loads(request.body)
            apic = ApicController()
            apic.createDeployment(payload, PREFIX)
            print("Deployment Done!")
            return JSONResponse("ok")
        except Exception as e:
            print(traceback.print_exc())
            # return the error to web client
            return JSONResponse({'error': e.__class__.__name__, 'message': str(e)}, status=500)
    else:
        return JSONResponse("Bad request. " + request.method + " is not supported", status=400)

```

Next -> [Step 9 - Populating the pod select]

[Step 9 - Populating the pod select]: step9.md