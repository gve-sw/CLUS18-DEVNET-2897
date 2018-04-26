### Step 7 - Adding the deploy button
The only thing that is missing is the "Deploy" button.
 After the code added in step 6, copy the following:

```html
<button id="btnDeploy" class="btn btn--success" style="float:right" ng-disabled="loading"
ng-click="deploy();" >
Deploy
</button>
```

This will create the button and will place it in the correct  position.
Refresh your browser to see the new button in the screen.

Next -> [Step 8 - Preparing server to receive and reply REST API calls]

[Step 8 - Preparing server to receive and reply REST API calls]: step8.md