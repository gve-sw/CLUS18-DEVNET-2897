### Step 10 - Populating the switch select

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
```

There is a catch though. In order to get the switches we need to select a pod first; we can simple instruct the
sel_pod element to execute the getSwitches method when changed. Add these two attributes to the sel_pod element 
in the home.html file

```html
ng-change="getSwitches(deployment.selectedPod)"
```
Using ng-change, the method getSwitches is executed each time that the selection changes.


Next -> [Step 11 - Populating the interface selects]

[Step 11 - Populating the interface selects]: step11.md