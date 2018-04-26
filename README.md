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

### Step 9 - Populating the sel_pod drop down list with options

Now that the server is able to accept and reply REST calls with the information about pods, switches and interfaces
it is time to interact with it using the javascript library Angular JS.

The file that we are going to use to implement that logic is in static/web_app/public/js/angular-modules/app.js
We are going to focus on this section to add our code:

```javascript
// App controller is in charge of managing all services for the application
appModule.controller('AppController', function($scope, $location, $http, $window, $rootScope){

    (...)
        
});
```

Lets add a new method, that will get all the pods from the server and store them on memory:
 
```javascript
 $scope.getPods = function(){
        $http
            .get('api/pod')
            .then(function (response, status, headers, config){
                $scope.pods = response.data
            })
            .catch(function(response, status, headers, config){
                $scope.error = response.data.message
            })
            .finally(function(){
            })
    };
    
    $scope.getPods(); 
```

Next, we are going to bind that data to the HTML code so that the user can see the pods. 
In the templates/web_app/home.html, look for the select tag with id="sel_pod" and add the following attribute
```html
ng-options="pod as pod.fabricPod.attributes.dn for pod in pods track by pod.fabricPod.attributes.dn" 
ng-model="deployment.selectedPod"
```

The ng-options tells Angular to populate the drop down list with the items stored in the $scope.pods 
variable


### Step 10 - Populating the sel_switch select with options

We should do the same thing for switches drop down list. This method will get that information from the server

 
```javascript
$scope.getSwitches = function(pod){
        if(pod.fabricPod){
            $http
                .get('api/switch/' + pod.fabricPod.attributes.dn)
                .then(function (response, status, headers, config){
                    $scope.switches = response.data
                })
                .catch(function(response, status, headers, config){
                    $scope.error = response.data.message
                })
                .finally(function(){
                })
        }
    };
 
```

Bind the $scope.switches variable to the select sel_switches for the user to see them adding this attribute:

```html
ng-options="switch as switch.fabricNode.attributes.name for switch in switches track by switch.fabricNode.attributes.dn"
ng-model="deployment.selectedSwitch"
```

There is a catch though. In order to get the switches we need to select a pod first; we can simple instruct the
sel_pod element to execute this method when changed. Add these two attributes to the sel_pod element in the home.html
file

```html
ng-change="getSwitches(deployment.selectedPod)"
```
ng-model is the variable where the selected item is going to be saved. ng-change is executed each time that the
 selection is changed and is set to the name of the method that we created before.

### Step 11 - Populating the interfaces drop down lists with options

Finally, we got the interfaces. The items in these drop down lists depends on what the user selected 
in the sel_switch list. Lets start adding the javascript function that will retrieve the interfaces for
a given switch

```javascript
    $scope.getInterfaces = function(selected_switch){
        if(selected_switch.fabricNode){
            $http
                .get('api/interface/' + selected_switch.fabricNode.attributes.dn )
                .then(function (response, status, headers, config){
                    $scope.interfaces = response.data
                })
                .catch(function(response, status, headers, config){
                    $scope.error = response.data.message
                })
                .finally(function(){
                })
        }
    };

```

We need to bind the $scope.interfaces variable with the two interface selects.
For the select id="sel_port1" add these attributes

```html
ng-options="interface as interface.l1PhysIf.attributes.id for interface in interfaces1 track by interface.l1PhysIf.attributes.dn"
ng-model="deployment.selectedPort1"
```

And for select id="sel_port2_pc" add these:
```html
ng-options="interface as interface.l1PhysIf.attributes.id for interface in interfaces1 track by interface.l1PhysIf.attributes.dn"
ng-model="deployment.selectedPort2"
```

To trigger the interface collection after a switch is selected we add these to the select id="sel_switch" attributes
```html
ng-change="getInterfaces(deployment.selectedSwitch)"
```

### Step 12 - Populating the EPGs/VLANs drop down list with options

The last drop down list to populate is the EPGs/VLANs. Since this is not dependent on any other previous selection
it is simpler. Add the following javascript to the app.js file 

```javascript
$scope.getEpgs = function(){
        $http
            .get('api/epgs')
            .then(function (response, status, headers, config){
                $scope.epgs = response.data
            })
            .catch(function(response, status, headers, config){
                $scope.error = response.data.message
            })
            .finally(function(){
            })
    };
    
    $scope.getEpgs();
```

Bind the $scope.epgs variable to the HTML adding the following attributes to the select id="sel_epg"
```html
ng-options="epg as epg.fvAEPg.attributes.name for epg in epgs track by epg.fvAEPg.attributes.name" 
ng-model="deployment.selectedEpg"
```

### Step  - Conditional user interface with angular JS



### Step  - Adding authentication HTML interface

### Step  - Adding authentication API to the server

### Step  - Enforcing authentication using Angular JS


