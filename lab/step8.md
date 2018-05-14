### Step 8 - Populating the pod select

It is time to interact with the server using the javascript library Angular JS. The file that we are going to use to implement 
that logic is located in _**web_ui/static/web_app/app.js**_. We are going to focus only on the section defined at the end.

Lets add a new method that will get all the pods from the server and store them on memory. You **must** define this
within the _**appModule.controller**_ code block:
 
```javascript
 $scope.getPods = function(){
        
        $scope.loading = true;
        // Does a GET call to api/pod to get the pod list
        $http
            .get('api/pod')
            .then(function (response, status, headers, config){
                // Save the data into the $scope.pods variable
                $scope.pods = response.data
            })
            .catch(function(response, status, headers, config){
                $scope.error = response.data.message
            })
            .finally(function(){
                $scope.loading = false;
            })
    };
    
    $scope.getPods(); 
```

The $scope.pods variable is associated to the pods select via the ng-option attribute defined in the step 4 HTML code.

Next -> [Step 9 - Populating the switch select]

[Step 9 - Populating the switch select]: step9.md