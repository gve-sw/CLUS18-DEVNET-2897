### Step 11 - Populating the EPGs/VLANs select

The last drop-down list to populate is the EPGs/VLANs. Add the following JavaScript to the app.js file.
 You **must** define this within the _**appModule.controller**_ code block:

```javascript
    $scope.getEpgs = function(){
        // Does a GET call to api/epgs to get the EPG/VLANs list
        $http
            .get('api/epgs')
            .then(function (response, status, headers, config){
                $scope.epgs = response.data
            })
            .catch(function(response, status, headers, config){
                $scope.error = response.data.message
            })
    };
    
    $scope.getEpgs();
```

The $scope.epgs variable is associated to the EPG/VLAN select via the ng-option attribute added in step 6.

Next -> [Step 12 - Requesting the deployment to the server]

[Step 12 - Requesting the deployment to the server]: step12.md