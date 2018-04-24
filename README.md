# Cisco Live US - Devnet workshop 2897
This file will provide you with instructions around how to create JavaScript, HTML and python code to create a 
port automation web user interface on top of Cisco ACI

## Use case

Cisco ACI is an industry leading software defined network solution that enables application agility and data center automation.
ACI has a very intuitive graphical user interface; however, there are new objects that traditional networking teams
need to learn to configure switch ports such as:
 
 * Switch profiles
 * Interface policies
 * Interface policy groups
 * Tenants
 * Application profiles
 * End point groups
 * Bridge domains
 * VRFs
 * VLAN pools
 * Attachable entity profiles
 * Physical domains
 
This new terminology could slow down the usage of this powerful solution

## Solution

In order to get operation teams up to speed, a simplified web user interface that abstract all the objects that 
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
cd CLUS18-DEVNET-2897
virtualenv devnet2897
source devnet2897/bin/activate
pip install -r requirements.txt
```

### Step 2 - Navigating the solution directories and running the server

From the Applications folder, open PyCharm. This is a useful integrated development environment (IDE) that we will use
to edit different files. 

Click on "open" and then select the directory created in step 1 (CLUS18-DEVNET-2897)

There are four directories that you should be aware:

1. web_ui: contains all the server side logic, along with the files that will be sent to the clients (web browsers)
2. web_ui/controllers: contains the apic.py file with all the API calls to ACI. This file is already done, but it is
good to give it a look for your reference
3. web_ui/static: All the JavaScript, CSS, icons and image files that the client will use to render the user interface
4. web_ui/templates: HTML code for the web UI.

To run this app go to the CLUS18-DEVNET-2897 directory 

### Step 3 - Adding the port type HTML interface




### Step 4 - Adding the port selection HTML interface

### Step 5 - Adding the EPG/Vlan creation HTML interface

### Step 6 - Adding the EPG/Vlan selection HTML interface

### Step 7 - Preparing server to receive and reply REST API calls

### Step 8 - Using Angular JS to interact with the server

### Step 9 - Conditional user interface with angular JS

### Step 10 - Adding authentication HTML interface

### Step 11 - Adding authentication API to the server

### Step 12 - Enforcing authentication using Angular JS


