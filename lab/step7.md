### Step 7 - Adding the deploy button and loading components
We have all what we need from a UI perspective, the only thing that is missing is the "Deploy" button.
 After the code added in step 6, copy the following. This will create the button and place it in the correct 
position.

```html
<button id="btnDeploy" class="btn btn--success" style="float:right" ng-disabled="loading">
Deploy
</button>
```
