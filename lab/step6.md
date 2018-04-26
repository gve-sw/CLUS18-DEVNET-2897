### Step 6 - Adding the EPG/VLAN selection and creation HTML interface

In this step, we have to build the interface for the two options in the step 5. 
In the case of creation, a text box where the user can insert the VLAN number should be fine; however, for the 
selection of existing EPG/VLAN, a drop down list must be used.

Paste the following code below the one added in step 5, this will create the text box and the drop down list needed
```html
<div id="epg-data" class="col-md-12 text-large">
    <div class="form-group">
        <div class="form-group__text select ">
            <select id="sel_epg" name="sel_epg" ng-model="deployment.selectedEpg"></select>
            <label for="sel_epg">Existing EPG/VLAN</label>
        </div>
    </div>
    <div class="form-group">
        <div class="form-group__text">
            <input id="url" type="text" ng-model="deployment.selectedEpg">
            <label for="url">New EPG/VLAN</label>
        </div>
    </div>
</div>
```
