### Step 13 - Sending the deployment information to the server
With the pod, switch, interfaces and VLANs we have all the information that we need from the user. We will now code a 
function in the app.js file that will make that possible:

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
And in the home.html file, look for the button id="btnDeploy"; Add this attribute to the tag

```html
ng-click="deploy();" 
```

ng-click will execute the method deploy each time that the button is clicked.
