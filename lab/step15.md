### Step 15 - Dynamic user interface

Dynamic user interface means to show or hide things according to the value of different variables.
 For example, it doesn't make too much sense to show the "Interface 2" option if we are not deploying 
a port-channel. 
 
In the _**web_ui/templates/home.html**_ file, look for the div tag with **id="interface_2_selection"** and add this 
attribute

```html
ng-if="deployment.portType == 'portChannel'"
```

It should look like this:
```html
<div id="interface_2_selection" 
      ng-if="deployment.portType == 'portChannel'">
    <div class="form-group">
        <div class="form-group__text select">
            <select id="sel_port2_pc" ng-model="deployment.selectedPort2"
            ng-options="interface as interface.l1PhysIf.attributes.id for interface in interfaces1 track by interface.l1PhysIf.attributes.dn"></select>
            <label for="sel_port2_pc">Interface 2</label>
        </div>
    </div>
</div>
```

This will make that everything inside this div section to not be shown unless the port type is set to portChannel

Same thing applies to the EPGs/VLANs. If we select "Existing EPG/VLAN" we shouldn't see the New EPG/VLAN field; in 
the other hand, we shouldn't see the list of EPGs/VLANs if we are going to create a new one.
To implement this, look for the div tag with **id="existing_epg_selection"** and add this attribute

```html
ng-if="deployment.epgAction == 'existing'"
```

It should look like this:

```html
    <div id="existing_epg_selection" class="form-group" ng-if="deployment.epgAction == 'existing'">
        <div class="form-group__text select ">
            <select id="sel_epg" name="sel_epg" ng-model="deployment.selectedEpg"
            ng-options="epg as epg.fvAEPg.attributes.name for epg in epgs track by epg.fvAEPg.attributes.name"></select>
            <label for="sel_epg">Existing EPG/VLAN</label>
        </div>
    </div>
```

Then, look for the div tag with **id="new_epg_selection"** and add this attribute

```html
ng-if="deployment.epgAction == 'new'"
```

It should look like this:

```html
    <div id="new_epg_selection" class="form-group" ng-if="deployment.epgAction == 'new'">
        <div class="form-group__text">
            <input id="epg" type="text" ng-model="deployment.selectedEpg" type="number">
            <label for="epg">New EPG/VLAN</label>
        </div>
    </div>
```


Refresh your browser and you will be able to hide/show elements according to the VLAN or Port type selection

#### Congratulations! You have finished this workshop :clap::tada::raised_hands: