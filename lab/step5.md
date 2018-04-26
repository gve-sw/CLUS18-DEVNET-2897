### Step 5 - Adding the EPG/VLAN options HTML interface

Now, we will create the interface to select or create a new EPG/VLAN that the ports will be associated.
The following code will create two buttons where the user is going to be able to select if a new EPG needs to be created
or if an existing one should be used.
Paste this code below the one added in step 4.

```html
<div id="epg-action" class="col-md-12 text-large">
    <br/>
    <h4>EPG/VLAN</h4>
    <hr/>
    <div class="btn-group">
        <button class="btn btn--primary-ghost sn-type epg-action selected"
                onclick="$('.epg-action').removeClass('selected');$(this).addClass('selected')"
                ng-click="setEpgAction('existing')">
            Existing EPG/VLAN
        </button>
        <button class="btn btn--primary-ghost sn-type epg-action"
                onclick="$('.epg-action').removeClass('selected');$(this).addClass('selected')"
                ng-click="setEpgAction('new')">
            New EPG/VLAN
        </button>
    </div>
</div>
```