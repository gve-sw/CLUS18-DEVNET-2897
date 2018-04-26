### Step 6 - Adding the EPG/VLAN selection and creation fields

We have to build the fields for the two options done in the step 5. 
In the case of creation, a text box where the user can insert the VLAN number should be fine; however, for the 
selection of existing EPG/VLAN, a drop down list must be used.

Copy the following code **below** the one added in step 5, this will create the text box and the drop down list needed
```html
<div id="epg-data" class="col-md-12 text-large">
    <br/>
    <div id="existing_epg_selection" class="form-group">
        <div class="form-group__text select ">
            <select id="sel_epg" name="sel_epg" ng-model="deployment.selectedEpg"
            ng-options="epg as epg.fvAEPg.attributes.name for epg in epgs track by epg.fvAEPg.attributes.name"></select>
            <label for="sel_epg">Existing EPG/VLAN</label>
        </div>
    </div>
    <div id="new_epg_selection" class="form-group">
        <div class="form-group__text">
            <input id="epg" type="text" ng-model="deployment.selectedEpg" type="number">
            <label for="epg">New EPG/VLAN</label>
        </div>
    </div>
</div>
```


_Note: Use <kbd>option ⌥</kbd> + <kbd>command ⌘</kbd> + <kbd>L</kbd> to format the HTML file_

Refresh your browser to see the new section in the screen.

![step_6](lab/images/step_6.png)

Next -> [Step 7 - Adding the deploy button]

[Step 7 - Adding the deploy button]: step7.md
