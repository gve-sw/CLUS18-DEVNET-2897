### Step 7 - Adding the deploy button
The only thing that is missing is the "Deploy" button.
 After the code added in step 6, copy the following:

```html
<div class="col-md-12 text-large">
    <br/>
    <!-- ****** Button to send deployment to the server ****** -->
    <button id="btnDeploy" class="btn btn--success" style="float:right"
            ng-disabled="loading"
            ng-click="deploy();">
        Deploy
    </button>
</div>
```

This code defines the button in the user interface and places it in the correct position.

_Note: Use <kbd>option ⌥</kbd> + <kbd>command ⌘</kbd> + <kbd>L</kbd> to format the HTML file_

Refresh your browser to see the new section in the screen.

![step_7](images/step7.png)


Next -> [Step 8 - Populating the pod select]

[Step 8 - Populating the pod select]: step8.md
