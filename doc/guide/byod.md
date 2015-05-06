To work on this lab on your own machine, you will need to install [Python](https://www.python.org/downloads/) and 
[Pip](https://pip.pypa.io/en/latest/installing.html), and clone the project code.

Once you have done that, the project uses standard Python mechanisms, Pip with the `src/setup.py` script, to install all other required components, as explained below.

# Install Python
Whilst the code will work with Python 2.7, we recommend that you install Python 3.x for your operating system.
Download the installer here: https://www.python.org/downloads/

#Check Python install:
If you are using Mac OS X or Linux, enter `python3` to check the version, and expect to see something like:

```
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
`curl -O https://raw.githubusercontent.com/pypa/pip/master/contrib/get-pip.py`
`sudo python3 get-pip.py`

And expect to see something like this:

```
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

On Mac OS X or Linux, that looks like this with an example from the COSC Learning Lab project:

``` 
sudo pip3 install -e .
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

