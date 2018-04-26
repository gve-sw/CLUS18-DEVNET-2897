### Step 9 - Populating the sel_pod drop down list with options

Now that the server is able to accept and reply REST calls with the information about pods, switches and interfaces
it is time to interact with it using the javascript library Angular JS.

The file that we are going to use to implement that logic is in static/web_app/public/js/angular-modules/app.js
We are going to focus on this section to add our code:

```javascript
// App controller is in charge of managing all services for the application
appModule.controller('AppController', function($scope, $location, $http, $window, $rootScope){

    (...)
        
});
```

Lets add a new method, that will get all the pods from the server and store them on memory:
 
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

Next, we are going to bind that data to the HTML code so that the user can see the pods. 
In the templates/web_app/home.html, look for the select tag with id="sel_pod" and add the following attribute
```html
ng-options="pod as pod.fabricPod.attributes.dn for pod in pods track by pod.fabricPod.attributes.dn" 
ng-model="deployment.selectedPod"
```

The ng-options tells Angular to populate the drop down list with the items stored in the $scope.pods 
variable