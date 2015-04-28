# cosc-learning-labs
Cisco Open SDN Controller Learning Labs code.
Learning Lab for Cisco Open Software-Defined-Network Controller (COSC).

The licence that applies to this Learning Lab is in file [LICENCE](LICENSE)

##Pre-requisites
* Python 2.7 or 3.4 (including pip or pip3)
* SDN Controller (such as ODL or COSC)
* Network Devices

##Add this project to your Python Path
Follow these [instructions](doc/python_path.md)

##Configure the settings
* SDN Controller
* Network Devices
Follow these [instructions](doc/settings.md)
```
cd <git>/cosc-learning-labs/src/settings
```

##Go to the src/learning_lab directory
```
cd <git>/cosc-learning-labs/src/learning_lab
```

##Run the sample scripts
```
./01_inventory_connected.py
```

The instructions are in file:

	doc/guide/sandbox.pdf

Notes about ordering of scripts.

Suggested order of ‘groups’ of scripts is by numeric prefix:

01 inventory
02 capabilities
03 interface
04 ACL

Within each group the suggested order of scripts can be seen in this file (which we visited in the webex):

http://gerrit-open1.cisco.com/gerrit/gitweb?p=cosc-learning-labs.git;a=blob;f=src/learning_lab/suite.py;hb=HEAD

Right now the ‘suite’ does not have ACL so I will make that a top priority.

Hints: to get the network into a particular state the following two scripts are useful:

01_inventory_mount.py

01_inventory_dismount.py

You will see that I use these two scripts a lot in ‘suite’ to establish a specific context.

Note: each script tries to demonstrate one simple thing. We don’t want a one line script performing ten lines of ‘setup’ or ’tear down'. Therefore, each script tries to do its thing but may not succeed.

E.g.mount one device. If all devices are already mounted then it does nothing except print a message on stdout.

I have been evolving an idea that each script returns normally (exit code 0) when it succeeds and abnormal (exit code 1) when it is unable to demonstrate/proceed. Some scripts have this but not all (yet).

Example of usage: run script 01_device_dismount until the exit code is non-zero. All devices are thus not mounted.

Notes on terminology: 

Mount: verb, introduce a device to the controller and attempt connection.
Dismount: verb, complement of mount
Mounted: adjective, the ‘mount’ operation was applied
Unmounted: adjective, available to ‘mount’, unknown to controller, specified in settings/config

PS: we did not discuss the HTTP layer but it is considered by some people to be of importance. One of the constructive criticisms of the LL many months ago was that it did not teach people how to communicate with ODL/COSC using HTTP. We responded by capturing the HTTP requests and responses that occur as the Python (high level) library API is used. The HTTP details appear in the HTML pages.

Here is a sample link to a HTML page where the HTTP details can be seen:

http://nbviewer.ipython.org/url/gerrit-open1.cisco.com/gerrit/gitweb/%3Fp%3Dcosc-learning-labs.git%3Ba%3Dblob_plain%3Bf%3Dsrc/notebook/01_device_connected.ipynb%3Bhb%3DHEAD

Notes on settings: the scripts prefixed with 00 are for administrative purposes. They don’t modify anything (so far) – they just report. They inform you about the settings that the Python sample scripts will ‘see’.

Notes on known bugs:

Modifying interface configuration does not currently succeed if there is no IP address. I will try to fix this by omitting the XML element for the IP address when there is no IP address.

Notes on Python 2 and 3:

All the sample scripts in groups 01, 02 and 03 run in both Python 2 and 3. Group 04 is currently Python 2 only.

Notes on capability and device versions:

Network devices have different capabilities for each version. The sample scripts are currently not sophisticated at checking if a required capability is supported by an individual device. The sample scripts will fail if there is a capability/version mismatch. We have some excellent work in the pipeline to address this issue in an elegant and robust manner. For example, query the inventory for all devices with a specific capability.

I have put this text into the README.txt file, which is here:

http://gerrit-open1.cisco.com/gerrit/gitweb?p=cosc-learning-labs.git;a=blob;f=README.txt;hb=HEAD
