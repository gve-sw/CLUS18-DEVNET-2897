
### Step 12 - Populating the EPGs/VLANs drop down list with options

The last drop down list to populate is the EPGs/VLANs. Since this is not dependent on any other previous selection
it is simpler. Add the following javascript to the app.js file 

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

Bind the $scope.epgs variable to the HTML adding the following attributes to the select id="sel_epg"
```html
ng-options="epg as epg.fvAEPg.attributes.name for epg in epgs track by epg.fvAEPg.attributes.name" 
ng-model="deployment.selectedEpg"
```