### Step 11 - Populating the interface selects

Lets work on the interfaces. First, add the javascript function that will retrieve the interfaces for
a given switch.  You **must** define this within the appModule.controller code block:

```javascript
    $scope.getInterfaces = function(selected_switch){
        if(selected_switch.fabricNode){
            $http
                .get('api/interface/' + selected_switch.fabricNode.attributes.dn )
                .then(function (response, status, headers, config){
                    $scope.interfaces = response.data
                })
                .catch(function(response, status, headers, config){
                    $scope.error = response.data.message
                })
                .finally(function(){
                })
        }
    };

``` 

The $scope.interfaces variable is associated to the interface selects via the ng-option attribute added in step 4.

Next -> [Step 12 - Populating the EPGs/VLANs select]

[Step 12 - Populating the EPGs/VLANs select]: step12.md