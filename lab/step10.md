### Step 10 - Populating the interface selects

Let's work on the interfaces. First, add the JavaScript function that will retrieve the interfaces for
a given switch.  You **must** define this within the appModule.controller code block:

```javascript
    $scope.getInterfaces = function(selected_switch){
        if(selected_switch.fabricNode){
            // Does a GET call to api/interface to get the interfaces list
            $scope.loading = true;
            $http
                .get('api/interface/' + selected_switch.fabricNode.attributes.dn )
                .then(function (response, status, headers, config){
                    $scope.interfaces = response.data
                })
                .catch(function(response, status, headers, config){
                    $scope.error = response.data.message
                })
                .finally(function(){
                    $scope.loading = false;
                })
        }
    };

``` 

The $scope.interfaces variable is associated to the interface selects via the ng-option attribute defined in the step 4 HTML code.

Next -> [Step 11 - Populating the EPGs/VLANs select]

[Step 11 - Populating the EPGs/VLANs select]: step11.md