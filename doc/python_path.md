#Integration of this project into the Python environment
All required packages will also be downloaded and installed.

Suggested techniques for achieving the required integration:
* Modify the current Python environment of your computer
* Create and modify a virtual, temporary Python environment


##Modify the current Python environment of your computer
This technique is recommended when your computer is a virtual computer, such as Ubuntu running on VMWare.

####Python 2
```bash
sudo pip install -e src
```
####Python 3
```bash
sudo pip3 install -e src
```

##Create and modify a virtual, temporary Python environment
This technique is recommended when your computer is used to run multiple Python projects or multiple versions of Python.

There are multiple tools that provide a virtual environment. The example below uses virtualenv. See also: venv, pyenv, pythonz.

On Ubuntu, OSX, Linux:
```bash
pip install virtualenv 
cd ~/git/cosc-learning-labs
virtualenv –p python2.7 env
source env/bin/activate
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
