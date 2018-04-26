### Step 9 - Populating the pod select

Now that the server is able to accept and reply REST calls with the information about pods, switches and interfaces
it is time to interact with it using the javascript library Angular JS. The file that we are going to use to implement 
that logic is located in _**static/web_app/public/js/angular-modules/app.js**_ 

Within the app.js file, we are going to focus only on the section defined at the end:

```javascript
// App controller is in charge of managing all services for the application
appModule.controller('AppController', function($scope, $location, $http, $window, $rootScope){

    // NEW CODE HERE
        
});
```

Lets add a new method, that will get all the pods from the server and store them on memory. You **must** define this
within the appModule.controller code block:
 
```javascript
 $scope.getPods = function(){
        $http
            .get('api/pod')
            .then(function (response, status, headers, config){
                $scope.pods = response.data
            })
            .catch(function(response, status, headers, config){
                $scope.error = response.data.message
            })
            .finally(function(){
            })
    };
    
    $scope.getPods(); 
```

The $scope.pods variable is associated to the pods select via the ng-option attribute added in step 4.

Next -> [Step 10 - Populating the switch select]

[Step 10 - Populating the switch select]: step10.md