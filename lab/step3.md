### Step 3 - Adding the port type HTML interface

Its coding time! The first thing that we want to do is to define which type of port we want to create. We could create
an access port, a port channel or a virtual port channel. For simplicity, we are going to implement the first two.

Copy the following code in the templates/web_app/home.html file. You must include it within the 
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
This add a section with a header and two buttons that will be used to choose the port type to deploy.

```Note: After you paste the code, use <kbd>option ⌥</kbd> + <kbd>command ⌘</kbd> + <kbd>L</kbd> to format the HTML file``
