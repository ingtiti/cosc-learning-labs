#Integration of this project into the Python environment

The Python modules of project cosc-learning-labs must be appended to the Python 'path'.

Suggested techniques for achieving the required integration:
* Modify the current Python environment of your computer
* Create and modify a virtual, temporary Python environment
* Load the project into an IDE such as Eclipse or PyCharm.

##Virtual Environment

The use of a virtual environment is optional. If an entire computer is dedicated to running the client application then a virtual environment is not necessary. If a virtual computer is used then it is already a virtual environment.

If multiple Python applications run on the same computer then use a separate virtual environment for each. There are multiple tools that provide a virtual environment. The example below uses virtualenv. See also: venv, pyenv, pythonz.

On Ubuntu, OSX, Linux:

pip install virtualenv 
cd ~/git/cosc-learning-labs
virtualenv –p python2.7 env
source env/bin/activate

The final command, above, enters a shell or mode. Eventually, when you want to exit:

deactivate 

Before you deactivate the virtualenv shell:

pip install -e src

To run the test suite:

cd ~/git/cosc-learning-labs/src
pytest -t ../test
or
python setup.py test –a ../test

Pre-requisitives (Ubuntu):

sudo apt-get install -y python-logilab-common
