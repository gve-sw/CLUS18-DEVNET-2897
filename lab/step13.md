### Step 13 - Test your app

You are now ready to create your first access and port-channel port configurations in ACI. Before start, check that 
your app is running in the terminal that you used for the step 2 (Running the server). 

If you see that the app is not running anymore, execute the following commands in a terminal:

```bash
cd $HOME/CLUS18-DEVNET-2897
python manage.py runserver 0.0.0.0:8080
```


#### Port assignments
 
| Laptop Number | Switch           | Ports             | 
| ------------- |:----------------:|:-----------------:|
| Laptop-1      | leaf-2           | 1/24, 1/25, 1/26  |
| Laptop-2      | leaf-2           | 1/27, 1/28, 1/29  |
| Laptop-3      | leaf-2           | 1/30, 1/31, 1/32  |
| Laptop-4      | leaf-2           | 1/33, 1/34, 1/35  |
| Laptop-5      | leaf-2           | 1/36, 1/37, 1/38  |
| Laptop-6      | leaf-2           | 1/39, 1/40, 1/41  |
| Laptop-7      | leaf-2           | 1/42, 1/43, 1/44  |
| Laptop-8      | leaf-2           | 1/45, 1/46, 1/47  |


Note: A

#### Individual port

1. To force the browser to refresh JavaScript files, open chrome in incognito mode and go to http://0.0.0.0:8080
_Note: Open chrome and use <kbd>command ⌘</kbd> + <kbd>Shift</kbd> + <kbd>N</kbd> to open a new incognito window_
2. Select Port Type _Individual_
3. Choose Pod _topology/pod-1_
4. Choose switch _leaf-2_
5. Select your first assigned interface for Interface 1. Leave Interface 2 blank
6. Choose _New EPG/VLAN_ 
7. Use VLAN 1001
8. Press _Deploy_

Go to your terminal to see all the things that are being created in ACI. After you have received a _Deployment Done!_
 go to https://apic1.dcloud.cisco.com/ and login using username **admin** and password **C1sco12345**. 
 
1. Click on Tenants
2. Double click the one that has the same name as your assigned prefix (the prefix is located at the top banner in the web 
 user interface)
3. Expand Tenant -> Application Profiles -> _Your Prefix_ -> EPGs -> 1001. Select _Static Ports_ 
 
 You will see the interface that you selected before in the web app. :thumbsup:
 

#### Port Channel

1. To force the browser to refresh JavaScript files, open chrome in incognito mode and go to http://0.0.0.0:8080
_Note: Open chrome and use <kbd>command ⌘</kbd> + <kbd>Shift</kbd> + <kbd>N</kbd> to open a new incognito window_
2. Select Port Type _Port Channel_
3. Choose Pod _topology/pod-1_
4. Choose switch _leaf-2_
5. Select your second assigned interface for Interface 1. 
6. Select your third assigned interface for Interface 2.
7. Choose _Existing EPG/VLAN_ 
8. Use VLAN 1001
9. Press _Deploy_

Go to your terminal to see all the things that are being created in ACI. After you have received a _Deployment Done!_
 go to https://apic1.dcloud.cisco.com/ and loing  using username **admin** and password **C1sco12345**
 
1. Click on Tenants
2. Double click the one that has the same name as your assigned prefix (the prefix is located at the top banner in the web 
 user interface)
3. Expand Tenant -> Application Profiles -> _Your Prefix_ -> EPGs -> 1001. Select _Static Ports_ 
 
 You will see a new port-channel entry. :thumbsup:
  
#### Congratulations! You have finished this workshop :clap::tada::raised_hands: