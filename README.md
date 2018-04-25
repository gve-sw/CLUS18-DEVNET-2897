# Cisco Live US - Devnet workshop 2897
This file will provide you with instructions around how to create JavaScript, HTML and python code to create a 
port automation web user interface on top of Cisco ACI

## Use case

TODO: Workflow use and diagram

## Solution

In order to support this workflow, a simplified web user interface that abstract all the objects that 
we saw before can be made with the comprehensive set of APIs that ACI provides. 

In this solution, an operator can simply select the port type, switch-port and VLAN, and the solution will create all 
the needed configuration in ACI.

For your reference, we are going to use the following frameworks

* django Web Framework - https://www.djangoproject.com/
* Angular JS Framework - https://angularjs.org/ 
* Cisco UI Framework - https://developer.cisco.com/site/uiux/ 

### Step 1 - Setting the environment
To get started, we are going to clone this repo, which contains the structure of the solution that we are going to use.

In your computer's terminal:

```bash
git clone https://wwwin-github.cisco.com/sfloresk/CLUS18-DEVNET-2897.git $HOME/CLUS18-DEVNET-2897
```

Then, create a virtual environment and install requirements

```bash
cd $HOME/CLUS18-DEVNET-2897
virtualenv devnet2897
source devnet2897/bin/activate
pip install -r requirements.txt
```

### Step 2 - Navigating the solution directories and running the server

From the Applications folder, open PyCharm. This is a useful integrated development environment (IDE) that we will use
to edit different files. 

Click on "open" and then select the directory created in step 1 (CLUS18-DEVNET-2897 - inside the home directory)

There are four directories that you should be aware:

1. web_ui: contains all the server side logic, along with the files that will be sent to the clients (web browsers)
2. web_ui/controllers: contains the apic.py file with all the API calls to ACI. This file is already done, but it is
good to give it a look for your reference
3. web_ui/static: All the JavaScript, CSS, icons and image files that the client will use to render the user interface
4. web_ui/templates: HTML code for the web UI.

Now, to run the app go you can use these commands:

```bash
cd $HOME/CLUS18-DEVNET-2897
python manage.py runserver 0.0.0.0:8080
```
The command above executes the manage.py file and pass as a parameter the action (runserver) along with the 
IPs that are allowed to connect (0.0.0.0 or anyone) with the port where the server will be listening (8080)

You can go to http://0.0.0.0:8080/ to see the base layout. You have now a web application up and running in your machine

### Step 3 - Adding the port type HTML interface

Its coding time! The first thing that we want to do is to define which type of port we want to create. We could create
an access port, a port channel or a virtual port channel. For simplicity, we are going to implement the first two.

Copy the following code in the templates/web_app/home.html file. You must include it within the 
```<div id="content-div" class="row">``` tag.

```html

<div id="port-type-div" class="col-md-12 text-large">
    <br/>
    <h4>Port Type
    </h4>
    <hr/>
    <div class="btn-group">
        <button class="btn btn--primary-ghost sn-type port-type"
                onclick="$('.port-type').removeClass('selected');$(this).addClass('selected')">
            Individual
        </button>
        <button class="btn btn--primary-ghost sn-type port-type"
                onclick="$('.port-type').removeClass('selected');$(this).addClass('selected')">
            Port Channel
        </button>
    </div>
</div>

```
This add a section with a header and two buttons that will be used to choose the port type to deploy.

```Note: After you paste the code, use <kbd>option ⌥</kbd> + <kbd>command ⌘</kbd> + <kbd>L</kbd> to format the HTML file``

### Step 4 - Adding the port selection HTML interface

As we are implementing access and port-channel scenarios we have to include a drop down list for the pods, 
the switches and the ports.

The following code will create four drop down list. We will be populating them with real data in a next step; but for now
lets focus only on the HTML code. Copy the following code below after the one added in step 3

```html

<div class="col-md-12 text-large">
    <br/>
    <h4>Interfaces</h4>
    <hr/>
    <div class="form-group">
        <div class="form-group__text select ">
            <select id="sel_pod" name="sel_pod"></select>
            <label for="sel_pod">Pod</label>
        </div>
    </div>
    <div class="form-group">
        <div class="form-group__text select">
            <select id="sel_switch"></select>
            <label for="sel_switch">Switch</label>
        </div>
    </div>
    <div class="form-group">
        <div class="form-group__text select">
            <select id="sel_port1"></select>
            <label for="sel_port1">Interface 1</label>
        </div>
    </div>
    <div>
        <div class="form-group">
            <div class="form-group__text select">
                <select id="sel_port2_pc"></select>
                <label for="sel_port2_pc">Interface 2</label>
            </div>
        </div>
    </div>
</div>
```

### Step 5 - Adding the EPG/VLAN options HTML interface

Now, we will create the interface to select or create a new EPG/VLAN that the ports will be associated.
The following code will create two buttons where the user is going to be able to select if a new EPG needs to be created
or if an existing one should be used.
Paste this code below the one added in step 4.

```html
<div id="epg-action" class="col-md-12 text-large">
    <br/>
    <h4>EPG/VLAN</h4>
    <hr/>
    <div class="btn-group">
        <button class="btn btn--primary-ghost sn-type epg-action"
                onclick="$('.epg-action').removeClass('selected');$(this).addClass('selected')">
            Existing EPG/VLAN
        </button>
        <button class="btn btn--primary-ghost sn-type epg-action"
                onclick="$('.epg-action').removeClass('selected');$(this).addClass('selected')">
            New EPG/VLAN
        </button>
    </div>
</div>
```

### Step 6 - Adding the EPG/VLAN selection and creation HTML interface

In this step, we have to build the interface for the two options in the step 5. 
In the case of creation, a text box where the user can insert the VLAN number should be fine; however, for the 
selection of existing EPG/VLAN, a drop down list must be used.

Paste the following code below the one added in step 5, this will create the text box and the drop down list needed
```html
<div id="epg-data" class="col-md-12 text-large">
    <div class="form-group">
        <div class="form-group__text select ">
            <select id="sel_epg" name="sel_epg"></select>
            <label for="sel_epg">Existing EPG/VLAN</label>
        </div>
    </div>
    <div class="form-group">
        <div class="form-group__text">
            <input id="url" type="text">
            <label for="url">New EPG/VLAN</label>
        </div>
    </div>
</div>
```

### Step 7 - Adding the deploy button and loading components
We have all what we need from a UI perspective, the only thing that is missing is the "Deploy" button.
 After the code added in step 6, copy the following. This will create the button and place it in the correct 
position.

```html
<button class="btn btn--success" style="float:right">
Deploy
</button>
```

### Step 8 - Preparing server to receive and reply REST API calls
We will focus now on the server side of the application. In order to show information from ACI (such as Pods, Switches,
interfaces and EPGs) we need to code API calls in server that can return that information to the web client.
Luckily for us, using python is quite easy. Open you urls.py file and copy the following below the last defined URL:

```python
# APIs Mappings
url(r'^api/pod/?$', views.api_pod),
url(r'^api/switch/get/?$', views.api_switch),
url(r'^api/interface/get/?$', views.api_interface),
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
            apic.url = apic_url
            apic.token = apic_token
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
def api_switch(request):
    """
       Return a list of switches
       :param request:
       :return:
       """
    if request.method == 'GET':
        try:
            apic = ApicController()
            switches = apic.getLeafs(pod_dn=payload["pod"]["fabricPod"]["attributes"]["dn"])
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
def api_interface(request):
    """
       Return a list of interfaces
       :param request:
       :return:
    """
    if request.method == 'GET':
        try:
            apic = ApicController()
            interfaces = apic.getInterfaces(switch_dn=payload["switch"]["fabricNode"]["attributes"]["dn"])
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
   Creates if does not exist:
   - EPG
   - App Profile
   - BD
   - VRF
   - Tenant
   :param request:
   :return:
   """
    if request.method == 'POST':
        try:
            payload = json.loads(request.body)
            apic = ApicController()

            print("Creating tenant if not present")
            tenants = apic.getTenants(query_filter='eq(fvTenant.name,"' + PREFIX + '")')
            if len(tenants) == 0:
                tenants = apic.createTenant(PREFIX)

            print("Creating application profile if not present")
            aps = apic.getAppProfiles(tenant_dn=tenants[0]["fvTenant"]["attributes"]["dn"],
                                      query_filter='eq(fvAp.name,"' + PREFIX + '")')
            if len(aps) == 0:
                aps = apic.createAppProfile(tenant_dn=tenants[0]["fvTenant"]["attributes"]["dn"],
                                            app_prof_name=PREFIX)

            print("Creating VRF if not present")
            vrfs = apic.getVRFs(tenant_dn=tenants[0]["fvTenant"]["attributes"]["dn"],
                                query_filter='eq(fvCtx.name,"' + PREFIX + '")')

            if len(vrfs) == 0:
                vrfs = apic.createVRF(tenant_dn=tenants[0]["fvTenant"]["attributes"]["dn"],
                                      vrf_name=PREFIX)

            print("Creating Bridge Domain if not present")
            bds = apic.getBridgeDomains(tenant_dn=tenants[0]["fvTenant"]["attributes"]["dn"],
                                        query_filter='eq(fvBD.name,"' + PREFIX + '")')

            if len(bds) == 0:
                bds = apic.createBridgeDomain(tenant_dn=tenants[0]["fvTenant"]["attributes"]["dn"],
                                              bd_name=PREFIX,
                                              vrf_name=vrfs[0]["fvCtx"]["attributes"]["name"])

            print("Creating Endpoint Group if not present")
            if payload["deployment"]["epgAction"] == "new":
                epgName = payload["deployment"]["epgVlan"]
            else:
                epgName = payload["deployment"]["selectedEpg"]["fvAEPg"]["attributes"]["name"]
            
            # Check if EPG already exists
            epgs = apic.getEPGs(ap_dn=aps[0]["fvAp"]["attributes"]["dn"],
                                query_filter='eq(fvAEPg.name,"' + epgName + '")')
            if len(epgs) == 0:
                # Create only if does not exist
                epgs = apic.createEPG(ap_dn=aps[0]["fvAp"]["attributes"]["dn"],
                                      bridge_domain_name=bds[0]["fvBD"]["attributes"]["name"],
                                      epg_name=epgName)

            print("Creating VLAN Pool if not present")
            vpools = apic.getVlanPools(query_filter='eq(fvnsVlanInstP.name,"' + PREFIX + '")')

            if len(vpools) == 0:
                # Create vlan pool
                vpools = apic.createVlanPool(name=PREFIX)

            print("Add selected VLANs to pool if not present")
            apic.addVlansToPool(pool_name=vpools[0]["fvnsVlanInstP"]["attributes"]["name"],
                                from_vlan=epgName, to_vlan=epgName)

            print("Creating Physical Domain if not present")
            phyDoms = apic.getPhysicalDomains(query_filter='eq(physDomP.name,"' + PREFIX + '")')
            if len(phyDoms) == 0:
                phyDoms = apic.createPhysicalDomain(name=PREFIX,
                                                    vlan_pool_dn=vpools[0]["fvnsVlanInstP"]["attributes"]["dn"])

            print("Creating Attachable Entity Profile if not present")
            atthEntProfiles = apic.getAttachEntityProfile(query_filter='eq(infraAttEntityP.name,"' + PREFIX + '")')
            if len(atthEntProfiles) == 0:
                atthEntProfiles = apic.createAttachEntityProfile(name=PREFIX,
                                                                 phy_domain_dn=phyDoms[0]["physDomP"]["attributes"][
                                                                     "dn"])
            port1 = payload["deployment"]["selectedInterface1"]["l1PhysIf"]["attributes"]["id"].replace(
                "eth1/", "")

            leaf1_id = payload["deployment"]["selectedSwitch1"]["fabricNode"]["attributes"]["id"]

            if payload["deployment"]["portType"] == "access":
                # ## Access ##
                # Create Policy Group default options with attachable entity profile
                print("**** Deployment Port Type: Access *****")
                intPolGroups = apic.createAccessInterfacePolicyGroup(
                    name=PREFIX + "-access",
                    attEntPro_dn=atthEntProfiles[0]["infraAttEntityP"]["attributes"]["dn"])

                print("Creating Interface Policy if not present")
                # Create access interface policy
                intAccessProfiles = apic.createAccessInterfaceProfile(name=PREFIX + "-access-" + port1)

                print("Creating Interface Selector if not present")
                # Add selected port
                apic.createInterfaceSelector(
                    name=payload["deployment"]["selectedInterface1"]["l1PhysIf"]["attributes"]["id"].replace(
                        "/", "-"),
                    from_port=port1,
                    to_port=port1,
                    interface_profile_dn=intAccessProfiles[0]["infraAccPortP"]["attributes"]["dn"],
                    interface_policy_group_dn=intPolGroups[0]["infraAccPortGrp"]["attributes"]["dn"])

                print("Creating Switch Profile if not present")
                # Create switch profile
                sProfile = apic.createSwitchProfile(name=PREFIX, leaf_id=leaf1_id)

                print("Associating interface profiles to switch profile if not present")
                # Associate interface profiles to switch profile sw_prof_dn, int_prof_dn
                apic.associateIntProfToSwProf(
                    sw_prof_dn=sProfile["infraNodeP"]["attributes"]["dn"],
                    int_prof_dn=intAccessProfiles[0]["infraAccPortP"]["attributes"]["dn"])

                print("Associating port to EPG if not present")
                # Associate port to EPG
                apic.addStaticPortToEpg(
                    vlan=epgName,
                    leaf_id=leaf1_id,
                    port_id=payload["deployment"]["selectedInterface1"]["l1PhysIf"]["attributes"]["id"],
                    epg_dn=epgs[0]["fvAEPg"]["attributes"]["dn"])

            elif payload["deployment"]["portType"] == "portChannel":

                print("**** Deployment Port Type: PortChannel *****")
                # ## Port Channel ##
                port2 = payload["deployment"]["selectedInterface2"]["l1PhysIf"]["attributes"]["id"].replace(
                    "eth1/", "")

                print("Creating LACP Profile if not present")
                # make sure lacp_profile exists
                lapc_prof = apic.addLacpProf(name=PREFIX + '-LACP-ACTIVE')

                print("Creating port channel policy group if not present")
                # make sure portchannel policy group exists
                portchannel_policy = apic.addPortchannelIntPolicyGroup(
                    name=PREFIX + '-portchannel',
                    att_ent_prof_dn=atthEntProfiles[0]["infraAttEntityP"]["attributes"]["dn"],
                    lacp_prof_name=lapc_prof["lacpLagPol"]["attributes"]["name"])

                print("Creating port channel profile if not present")
                # make sure portchannel profile exists for port 1
                portchannel_profile = apic.addPortchannelIntProfile(
                    name=PREFIX + '-portchannel-' + port1 + '-' + port2)

                print("Creating Interface Selector for interfaces if not present")
                # Add selected port1
                apic.createInterfaceSelector(
                    name=payload["deployment"]["selectedInterface1"]["l1PhysIf"]["attributes"]["id"].replace(
                        "/", "-"),
                    from_port=port1,
                    to_port=port1,
                    interface_profile_dn=portchannel_profile["infraAccPortP"]["attributes"]["dn"],
                    interface_policy_group_dn=portchannel_policy["infraAccBndlGrp"]["attributes"]["dn"])

                # Add selected port2
                apic.createInterfaceSelector(
                    name=payload["deployment"]["selectedInterface2"]["l1PhysIf"]["attributes"]["id"].replace(
                        "/", "-"),
                    from_port=port2,
                    to_port=port2,
                    interface_profile_dn=portchannel_profile["infraAccPortP"]["attributes"]["dn"],
                    interface_policy_group_dn=portchannel_policy["infraAccBndlGrp"]["attributes"]["dn"])

                print("Creating Switch Profile if not present")
                # Create switch Profile
                sProfile = apic.createSwitchProfile(name=PREFIX, leaf_id=leaf1_id)

                print("Associating interface profiles to switch profile if not present")
                # Associate interface profiles to switch profile sw_prof_dn, int_prof_dn
                apic.associateIntProfToSwProf(
                    sw_prof_dn=sProfile["infraNodeP"]["attributes"]["dn"],
                    int_prof_dn=portchannel_profile["infraAccPortP"]["attributes"]["dn"])

                print("Associating port to EPG if not present")
                # Associate port to EPG
                apic.addStaticPortchannelToEpg(
                    vlan=epgName,
                    leaf_id=leaf1_id,
                    portchannel_pol_grp_name=portchannel_policy["infraAccBndlGrp"]["attributes"]["name"],
                    epg_dn=epgs[0]["fvAEPg"]["attributes"]["dn"])

            print("Deployment Done!")
            return JSONResponse("ok")
        except Exception as e:
            print(traceback.print_exc())
            # return the error to web client
            return JSONResponse({'error': e.__class__.__name__, 'message': str(e)}, status=500)
    else:
        return JSONResponse("Bad request. " + request.method + " is not supported", status=400)
```

### Step 9 - Using Angular JS to interact with the server

### Step 10 - Conditional user interface with angular JS

### Step 11 - Adding authentication HTML interface

### Step 12 - Adding authentication API to the server

### Step 13 - Enforcing authentication using Angular JS


