### Step 15 - Dynamic user interface

Dynamic user interface means to show or hide things according to the value of different variables.
 For example, it doesn't make too much sense to show the "Interface 2" option if we are not deploying 
a port channel. 
 
In the _**web_ui/templates/home.html**_ file, look for the div tag with **id="interface_2_selection"** and add this 
attribute

```html
ng-if="deployment.portType == 'portChannel'"
```
This will make that everything inside this div section to not be shown unless the port type is set to portChannel

Same thing applies to the EPGs/VLANs. If we select "Existing EPG/VLAN" we shouldn't see the New EPG/VLAN field; in 
the other hand, we shouldn't see the list of EPGs/VLANs if we are going to create a new one.
To implement this, look for the div tag with **id="existing_epg_selection"** and add this attribute

```html
ng-if="deployment.epgAction == 'existing'"
```

Then, look for the div tag with **id="new_epg_selection"** and add this attribute

```html
ng-if="deployment.epgAction == 'new'"
```

Refresh your browser and you will be able to hide/show elements according to the VLAN or Port type selection

#### Congratulations! You have finished this workshop :clap::tada::raised_hands: