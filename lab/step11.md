### Step 11 - Populating the interfaces drop down lists with options

Lets work on the interfaces. First, add the javascript function that will retrieve the interfaces for
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
For the select id="sel_port1" add this attribute

```html
ng-options="interface as interface.l1PhysIf.attributes.id for interface in interfaces1 track by interface.l1PhysIf.attributes.dn"
```

And for select id="sel_port2_pc" add this attribute:
```html
ng-options="interface as interface.l1PhysIf.attributes.id for interface in interfaces1 track by interface.l1PhysIf.attributes.dn"
```

The items in these drop down lists depend on what the user selected in the sel_switch list. 
To trigger the interface collection after a switch is selected we add this to the select id="sel_switch" attributes
```html
ng-change="getInterfaces(deployment.selectedSwitch)"
```
