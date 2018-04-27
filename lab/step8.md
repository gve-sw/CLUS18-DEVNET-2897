### Step 8 - Preparing server to receive and reply REST API calls
We will focus now on the server side of the application. In order to show information from ACI (such as Pods, Switches,
interfaces and EPGs) we need to code API calls in the server that can return that information to the web clients.
Luckily for us, doing this with Python is quite easy. Open you _**web_ui/urls.py**_ file and copy the following below the last defined URL:

```python
    # APIs Mappings
    
    url(r'^api/pod/?$', views.api_pod), # Maps the URL web/api/pod to the method api_pod inside views.py
    url(r'^api/switch/(?P<podDn>.*)/?$', views.api_switch), # Maps the URL web/api/switch/ to the method api_switch inside views.py
    url(r'^api/interface/(?P<switchDn>.*)/?$', views.api_interface), # Maps the URL web/api/interface/ to the method api_switch inside views.py
    url(r'^api/epgs/?$', views.api_epg), # Maps the URL web/api/epg to the method api_epg inside views.py
    url(r'^api/deploy/?$', views.api_deploy), # Maps the URL web/api/deploy to the method api_deploy inside views.py
```
Reading the code above, we can see that it is mapping URLs with specific methods that will manage http calls using that URL.
 
Now, we will create those methods.  Copy the methods below to the end of the _**web_ui/views.py**_ file. 

#### api_pod method

Returns a json with the list of pods

```python
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

```

#### api_switch method

Returns a json with the list of switches for a given pod

```python
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

```

#### api_interface method

Returns a json with the list of interfaces for a given switch

```python
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

```

#### api_epg method

Returns a list of EPGs for a specific tenant.

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

```

#### api_deploy method

Deploys an individual or port-channel port

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

```

The server is now ready to provide all the functions that the web clients will need.


Next -> [Step 9 - Populating the pod select]

[Step 9 - Populating the pod select]: step9.md