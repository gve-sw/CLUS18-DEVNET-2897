### Step 13 - Requesting the deployment to the server
With the pod, switch, interfaces and VLANs we have all the information that we need from the user. We will now code a 
function in the app.js file that will make that possible.

 You **must** define this within the appModule.controller code block.

```javascript
    $scope.deploy = function(){
        $scope.loading = true;
        $http
            .post('api/deploy', {'deployment': $scope.deployment })
            .then(function (response, status, headers, config){

            })
            .catch(function(response, status, headers, config){
                $scope.error = response.data.message
            })
            .finally(function(){
                $scope.loading = false;
            })
    };
```

The **Deploy** button has a ng-click attribute that will execute the method _**deploy**_ each time that the 
button is pressed.


Next -> [Step 14 - Test your app]

[Step 14 - Test your app]: step14.md