
### Step 12 - Populating the EPGs/VLANs select

The last drop down list to populate is the EPGs/VLANs. Add the following javascript to the app.js file.
 You **must** define this within the appModule.controller code block:

```javascript
$scope.getEpgs = function(){
        $http
            .get('api/epgs')
            .then(function (response, status, headers, config){
                $scope.epgs = response.data
            })
            .catch(function(response, status, headers, config){
                $scope.error = response.data.message
            })
            .finally(function(){
            })
    };
    
    $scope.getEpgs();
```

The $scope.epgs variable is associated to the EPG/VLAN select via the ng-option attribute added in step 4.

Next -> [Step 13 - Requesting the deployment to the server]

[Step 13 - Requesting the deployment to the server]: step13.md