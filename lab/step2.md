
### Step 2 - Running the server

From the Applications folder, open PyCharm. This is a useful integrated development environment (IDE) that we will use
to edit different files. 

Click on "open" and then select the directory created in step 1 (CLUS18-DEVNET-2897 - inside the home directory)

There are four directories that you should be aware:

1. web_ui: contains all the server side logic, along with the files that will be sent to the clients (web browsers)
2. web_ui/controllers: contains the apic.py file with all the API calls to ACI. This file is already done, but it is
good to give it a look for your reference
3. web_ui/static: All the JavaScript, CSS, icons and image files that the client will use to render the user interface
4. web_ui/templates: HTML code for the web UI.

Now, to run the app go you can use these commands:

```bash
cd $HOME/CLUS18-DEVNET-2897
python manage.py runserver 0.0.0.0:8080
```
The command above executes the manage.py file and pass as a parameter the action (runserver) along with the 
IPs that are allowed to connect (0.0.0.0 or anyone) with the port where the server will be listening (8080)

You can go to http://0.0.0.0:8080/ to see the base layout. You have now a web application up and running in your machine

Previous - [Step 1] --------------------------------------------------------- Next - [Step 3]   
[Step 3]: step3.md
[Step 1]: step1.md