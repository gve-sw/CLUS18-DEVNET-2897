### Step 10 - Populating the switch select

We should do the same thing for switches drop down list. This method will get that information from the server.
 You **must** define this within the appModule.controller code block:

 
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

The $scope.switches variable is associated to the switch select via the ng-option attribute added in step 4.

Next -> [Step 11 - Populating the interface selects]

[Step 11 - Populating the interface selects]: step11.md