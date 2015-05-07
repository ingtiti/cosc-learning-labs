To work on this lab on your own machine, you will need to install [Python](https://www.python.org/downloads/) and 
[Pip](https://pip.pypa.io/en/latest/installing.html), and clone the project code.

Once you have done that, the project uses standard Python mechanisms, Pip with the `src/setup.py` script, and [virtualenv](https://virtualenv.pypa.io/en/latest/) as required, to install all other required components, as explained below.

When your environment is setup correctly, you should create a network profile, in the `src/settings` directory and set that via the NETWORK-PROFILE environment variable, as described below.

# Install Python
Whilst the code will work with Python 2.7, we recommend that you install Python 3.x for your operating system.
Download the installer here: https://www.python.org/downloads/

#Check Python install:
If you are using Mac OS X or Linux, enter `python3` to check the version, and expect to see something like:

```bash
$ python3 
Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 23 2015, 02:52:03) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> ^D
```
The `^D` shown above exits from the Python shell.

On Windows, open a command shell by running the `cmd` command and enter `py –3 —version` at the CLI to check the python version. You may use `python —version` if there is only one Python version installed or your PATH is set for Python version 3.

# Install Pip
Pip is the [PyPA recommended tool](https://python-packaging-user-guide.readthedocs.org/en/latest/current.html) for installing Python packages. 

To install Pip for Python 3 on Mac OS X or Linux, use these commands at the CLI:

```bash
$ curl -O https://raw.githubusercontent.com/pypa/pip/master/contrib/get-pip.py
$ sudo python3 get-pip.py
```

And expect to see something like this:

```bash
$ curl -O https://raw.githubusercontent.com/pypa/pip/master/contrib/get-pip.py
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 1387k  100 1387k    0     0   346k      0  0:00:04  0:00:04 --:--:--  346k

$ sudo python3 get-pip.py
Password:
...
Collecting pip
  Downloading pip-6.1.1-py2.py3-none-any.whl (1.1MB)
    100% |████████████████████████████████| 1.1MB 446kB/s 
Installing collected packages: pip
  Found existing installation: pip 6.0.8
    Uninstalling pip-6.0.8:
      Successfully uninstalled pip-6.0.8
Successfully installed pip-6.1.1
```

Pip comes with Python 3.4 Windows. To check to see if Pip is in your python 3 path use these commands at the CLI:

`C:\>pip –V`

and expect to see something like:

`pip 1.5.6 from C:\Python34\lib\site-packages`

# Installing Git
[Git](http://git-scm.com/) is a source code management (SCM) tool. There are many [Git UI tools available](http://git-scm.com/downloads/guis). The Git CLI client is installed as with one of the platform specific [Git downloads](http://git-scm.com/downloads).

# Cloning the Code
Assuming you have a Git client installed, you can clone the project code. If you do not have a Git Client, see above. For a project hosted in GitHub, such as the [COSC Learning Loba](https://github.com/CiscoDevNet/cosc-learning-labs) you should [fork a repository](https://help.github.com/articles/fork-a-repo/) using the "Fork" button at the top right of a project page, as illustrated below.

![Forking a GitHub project](byod_images/fork.png) 

# Setting Up the Environment
Having installed Python and Pip, you can then use `pip3 install -e` in the project `src` directory, which, in turn, uses the contents of the `src/setup.py` script to install required components in your environment. 

The outcome is that the Python packages of this project will be appended to the Python *path*, and all required packages will be downloaded and appended to the Python *path*.

There are two suggested techniques for achieving the required integration:
* Modify the current Python environment of your computer, which is suitable for a Dev VM, say, which would only be used for single project.
* Create and modify a virtual, temporary Python environment, which is recommended when you have multiple projects being developed in parallel on your own laptop, say. 

##Modify the Current Python Environment of Your Computer
This technique is recommended when your computer is a virtual computer, such as Ubuntu running on VMWare, dedicated to this single project.

####Python 2
```bash
sudo pip install -e src
```
####Python 3
```bash
sudo pip3 install -e src
```

On Mac OS X or Linux, that looks like this (with an example from the COSC Learning Lab project being run in the `src` directory):

``` 
$ sudo pip3 install -e .
...
Obtaining file:...git/cosc-learning-labs/src
Collecting requests (from COSC-Learning-Lab==1.0)
  Downloading requests-2.7.0-py2.py3-none-any.whl (470kB)
    100% |################################| 471kB 1.1MB/s 
Collecting ipaddress (from COSC-Learning-Lab==1.0)
  Downloading ipaddress-1.0.7.tar.gz
Collecting lxml (from COSC-Learning-Lab==1.0)
  Downloading lxml-3.4.4.tar.gz (3.5MB)
    100% |################################| 3.5MB 146kB/s 
    Building lxml version 3.4.4.
    Building without Cython.
    Using build configuration of libxslt 1.1.28
  ...
Installing collected packages: COSC-Learning-Lab, lxml, ipaddress, requests
  Running setup.py develop for COSC-Learning-Lab
    Creating /Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/site-packages/COSC-Learning-Lab.egg-link (link to .)
    Adding COSC-Learning-Lab 1.0 to easy-install.pth file
  Running setup.py install for lxml
    Building lxml version 3.4.4.
    Building without Cython.
    Using build configuration of libxslt 1.1.28
    building 'lxml.etree' extension
...  
Running setup.py install for ipaddress

Successfully installed COSC-Learning-Lab ipaddress-1.0.7 lxml-3.4.4 requests-2.7.0
```

##Create and Modify a Virtual, Temporary, Python Environment
This technique is recommended when your computer is used to run multiple Python projects or multiple versions of Python.

There are multiple tools that provide a virtual environment. The example below uses [virtualenv](https://virtualenv.pypa.io/en/latest/). See also: [venv](https://docs.python.org/3/library/venv.html), [pyenv](https://github.com/yyuu/pyenv), [pythonz](https://github.com/saghul/pythonz).

On Ubuntu, Mac OS X and other Linux/Unix variants:

```bash
$ pip install virtualenv 
$ cd ~/git/cosc-learning-labs
$ virtualenv –p python2.7 env
$ ource env/bin/activate
```

The final command, above, enters a shell or mode. When you are finished with the virtualenv:
```bash
deactivate 
```

Whilst the virtualenv shell is active:
```
cd ~/git/cosc-learning-labs
pip install -e src
```

To run the test suite:
```bash
cd ~/git/cosc-learning-labs/src
pytest -t ../test
```
or
```bash
python setup.py test –a ../test
```

Pre-requisitives (Ubuntu):
```bash
sudo apt-get install -y python-logilab-common
```
#Creating and Setting the Network Profile
The network profile settings file defines variables and data that the learning lab code needs to identify the controller and network elements that are being used in a given instance of the lab. 

The first step us to set an environment variable, `NETWORK_PROFILE`, to the name of a settings fle. We shall use `learning_lab.py` in this example, which is based Mac OS X or Linux.

```bash
$ export NETWORK_PROFILE=learning_lab
```
The settings are read from the `settings` Python module, which is in:

```bash
~/git/cosc-learning-labs/src/settings
```

In this example, then, to display the settings:
```bash
$ cat ~/git/cosc-learning-labs/src/settings/learning_lab.py
```

Which would look like this for the open source [OpenDaylight Controller](http://www.opendaylight.org/) (yours may differ for IP addresses):

```python
odl_server_hostname = '198.18.1.25:8181'

odl_server_url_prefix = "http://%s/restconf/" % odl_server_hostname

config = {
    'odl_server' : {
        'url_prefix' : odl_server_url_prefix,
        'username' : 'admin',
        'password' : 'admin'},
 'network_device': {'kcy':{
                     'address': '198.18.1.50',
                     'port': 830,
                     'password': 'cisco',
                     'username': 'cisco'},
...
```
What this says is that there is a controller at `198.18.1.25` with the REST API exposed on port `8181`, for which the credentials are "admin/admin", and that there is a network element, with a management IP address of `198.18.1.50`, managed via Netconf, on port 830, with the credentials "cisco/cisco". Note that the management network must be reachable from where the controller is running.

If you are using the commercial [Cisco Open SDN Controller](http://www.cisco.com/c/en/us/products/cloud-systems-management/open-sdn-controller/index.html), then you would have settings like this:

```python
odl_server_url_prefix = "https://%s/controller/restconf/" % odl_server_hostname

config = {
    'odl_server' : {
        'url_prefix' : odl_server_url_prefix,
        'username' : 'token',
        'password' : cosc_authentication_token(odl_server_hostname, 8181, 'admin', 'cisco123')},
...
```
Which uses an OAuth authentication token.
