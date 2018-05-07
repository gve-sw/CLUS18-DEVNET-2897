### Step 1 - Setting the environment

To get started, we are going to clone the repository that contains the structure of the 
solution that we are going to use.

#### Clone the repo

Open a terminal :computer: and use git clone:

```bash
git clone https://wwwin-github.cisco.com/sfloresk/CLUS18-DEVNET-2897.git $HOME/CLUS18-DEVNET-2897
```

Then, create a virtual environment and install requirements

```bash
cd $HOME/CLUS18-DEVNET-2897
virtualenv --python=python3 devnet2897
source devnet2897/bin/activate
pip install -r requirements.txt
```

From the Applications folder, open PyCharm. This is a useful integrated development environment 
(IDE) that we will be used to edit different files. 
 
Click on "open" and then choose the directory created before (CLUS18-DEVNET-2897 - inside the home directory)

Within the solution, there are four directories that you should be aware:

1. **web_ui:** contains all the server-side logic coded in python
2. **web_ui/controllers:** contains the apic.py file with all the API calls to ACI. This file is ready to be used.
3. **web_ui/static:** JavaScript, CSS, icon and image files that the client will use to render the user interface
4. **web_ui/templates:** HTML code for the web user interface (UI).

Next -> [Step 2 - Running the server]

[Step 2 - Running the server]: step2.md
