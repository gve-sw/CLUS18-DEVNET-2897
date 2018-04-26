### Step 3 - Adding the port type 

Its coding time! The first thing that we want to do is to define which type of port we want to create. We could create
an access port, a port channel or a virtual port channel. For simplicity, we are going to implement the first two.

Copy the following code in the __**templates/web_app/home.html**__ file. You must include it within the 
```<div id="content-div" class="row">``` tag.

```html
<div id="port-type-div" class="col-md-12 text-large">
    <br/>
    <h4>Port Type
    </h4>
    <hr/>
    <div class="btn-group">
        <button class="btn btn--primary-ghost sn-type port-type selected"
                onclick="$('.port-type').removeClass('selected');$(this).addClass('selected')"
                ng-click="setPortType('access')">
            Individual
        </button>
        <button class="btn btn--primary-ghost sn-type port-type"
                onclick="$('.port-type').removeClass('selected');$(this).addClass('selected')"
                ng-click="setPortType('portChannel')">
            Port Channel
        </button>
    </div>
</div>

```

The code above creates a section with a header and two buttons that will be used to choose the port type to deploy;
either Individual or Port Channel

_Note: After you paste the code, use <kbd>option ⌥</kbd> + <kbd>command ⌘</kbd> + <kbd>L</kbd> to format the HTML file_

Refresh your browser to see the new components shown in the screen.

![step_3](lab/images/step_3.png)

Next -> [Step 4 - Adding the port selection]

[Step 4 - Adding the port selection]: step4.md