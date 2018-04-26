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
            <select id="sel_pod" name="sel_pod" ng-model="deployment.selectedPod"></select>
            <label for="sel_pod">Pod</label>
        </div>
    </div>
    <div class="form-group">
        <div class="form-group__text select">
            <select id="sel_switch" ng-model="deployment.selectedSwitch"></select>
            <label for="sel_switch">Switch</label>
        </div>
    </div>
    <div class="form-group">
        <div class="form-group__text select">
            <select id="sel_port1" ng-model="deployment.selectedPort1"></select>
            <label for="sel_port1">Interface 1</label>
        </div>
    </div>
    <div id="interface_2_selection">
        <div class="form-group">
            <div class="form-group__text select">
                <select id="sel_port2_pc" ng-model="deployment.selectedPort2"></select>
                <label for="sel_port2_pc">Interface 2</label>
            </div>
        </div>
    </div>
</div>
```