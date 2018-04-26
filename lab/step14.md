### Step 14 - Test your app

You are now ready to create your first access and port-channel port configurations in ACI.
 
| Laptop Number | Ports            | 
| ------------- |:----------------:|
| Laptop-1      | 1/24, 1/25, 1/26 |
| Laptop-2      | 1/27, 1/28, 1/29 |
| Laptop-3      | 1/30, 1/31, 1/32 |
| Laptop-4      | 1/33, 1/34, 1/35 |
| Laptop-5      | 1/36, 1/37, 1/38 |
| Laptop-6      | 1/39, 1/40, 1/41 |
| Laptop-7      | 1/42, 1/43, 1/44 |
| Laptop-8      | 1/45, 1/46, 1/47 |

#### Individual port

1. Select Port Type _Individual_
2. Choose Pod _topology/pod-1_
3. Choose switch _leaf-2_
4. Select your first assigned interface for Interface 1. Leave Interface 2 blank
5. Choose _New EPG/VLAN_ 
6. Use VLAN 1001
7. Press _Deploy_

Go to your terminal to see all the things that are being created in ACI. After you have received a _Deployment Done!_
 go to https://sandboxapicdc.cisco.com/ and loing  using username **admin** and password **ciscopsdt**
 
1. Click on Tenants
2. Double click the one that has the same name as your assigned prefix (the prefix is located at the top banner in the web 
 user interface)
3. Expand Tenant -> Application Profiles -> _Your Prefix_ -> EPGs -> 1001. Select _Static Ports_ 
 
 You will see the interface that you selected before in the web app. :thumbsup:
 

#### Port Channel

1. Select Port Type _Port Channel_
2. Choose Pod _topology/pod-1_
3. Choose switch _leaf-2_
4. Select your second assigned interface for Interface 1. 
5. Select your third assigned interface for Interface 2.
5. Choose _Existing EPG/VLAN_ 
6. Use VLAN 1001
7. Press _Deploy_

Go to your terminal to see all the things that are being created in ACI. After you have received a _Deployment Done!_
 go to https://sandboxapicdc.cisco.com/ and loing  using username **admin** and password **ciscopsdt**
 
1. Click on Tenants
2. Double click the one that has the same name as your assigned prefix (the prefix is located at the top banner in the web 
 user interface)
3. Expand Tenant -> Application Profiles -> _Your Prefix_ -> EPGs -> 1001. Select _Static Ports_ 
 
 You will see a new port-channel entry. :thumbsup:
  
Next -> [Step 15 - Dynamic user interface]

[Step 15 - Dynamic user interface]: step15.md