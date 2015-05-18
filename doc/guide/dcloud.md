Welcome to the DevNet learning lab for the Cisco Open SDN Controller 1.0 Sandbox v2, with Python!

# About This Cisco Solution
The Cisco Open SDN Controller (COSC) is a commercial distribution of [OpenDaylight](http://http://www.opendaylight.org) that delivers business agility through automation of standards-based network infrastructure.

Built as a highly scalable software-defined networking (SDN) platform, the Open SDN Controller abstracts away the complexity of managing heterogeneous networks to improve service delivery and reduce operating costs.

With the Cisco Open SDN Controller, you can integrate business applications with the underlying network devices using Northbound Rest APIs.  The Rest APIs provide a list of supported base network functions, which are agnostic of the underlying network device manufacturer.

Developer support for COSC may be found in the [COSC community at DevNet.](https://communities.cisco.com/community/developer/networking/cisco-one/extensible-network-controller)

# About This Learning Lab
This learning lab is part of a series of such labs offered by Cisco's [DevNet](http://developer.cisco.com). More such labs are to be found at the [Learning Labs section of DevNet](https://developer.cisco.com/site/devnet/learningLabs/overview.gsp). The code for this lab may be found in the [DevNet organisation in GitHub](https://github.com/CiscoDevNet/cosc-learning-labs). 

These instructions are for a specific instance of the learning lab hosted on [Cisco's dCloud platform](http://dcloud.cisco.com). If you have a dCloud account, you can access this learning lab at any time as part of the "Cisco Open SDN Controller 1.0 Sandbox". If you do not have a dCloud account yourself, please contact your Cisco account manager or systems engineer and they will be able to arrange access for you.

# About This Demonstration
The purpose of this Sandbox is to give you access to the Cisco Open SDN controller. This will take your through the steps of accessing the new Open SDN Controller and then allow you to self-discover different aspects of this product. It will also walk you through using Postman and Python to interact with the Open SDN Controller.

# Demonstration Configuration

This learning lab contains preconfigured users and components, running on the [Cisco VIRL](http://virl.cisco.com) platform.
 
All information needed to complete the access components is located in the Topology and Servers menus of your active demonstration. 

* Topology Menu. Click on any server in the topology and a popup window will appear with available server options.
* Servers Menu. Click on the green triangle in the Topology View, or '+' next to any server name in the Servers view, to display the available server options and credentials.

# Demonstration Topology
When accessing the demo, you will see a simplified topology, as shown in the figure below: 

![OSC Topology](dcloud_images/osc_topology.png)
 
This demonstration uses Virtual Internet Routing Lab [(VIRL)](http://virl.cisco.com). VIRL is a multi-purpose network virtualization platform that provides an easy way to build, configure, and test new or existing network topologies with an intuitive user interface. 

The VIRL topology used for this demonstration, depicted as a single server above, actually consists of eight routers interconnected within the topology. Each router has a management interface connected to the OSC server. Both VIRL and OSC run as Virtual Machines (VMs) on ESXi.

![VIRL Topology](dcloud_images/virl_topology.png)

For additional information on VIRL, see this [VIRL video at YouTube.](http://www.youtube.com/watch?v=nsbzHmwUz6I)

# Accessing the OSC
Demonstration Steps:

1. Access the Open SDN Controller GUI using the Chrome browser at http://198.18.1.25
2. Use the login credentials admin/cisco123 and click Login.
3. Welcome to the Open SDN Controller GUI --- Explore!

![OSC GUI](dcloud_images/osc_gui.png)
 
Caveats: 
* At this time, you are not be able to use the GUI interface to access router configurations; however, you can telnet into the routers using an ssh client.
* Please disregard any geographical issues you may find.
* XRv devices, accessed via Netconf from the controller, do appear in the inventory, but no device details are shown. 

# Python DevNet Learning Lab
In the section above, you used Postman, which is a browser plugin that allows you to send HTTP requests to REST (Representational State Transfer) APIs on the controller. In the case of the Cisco Open SDN Controller, those APIs are generated from Yang models and exposed via [“RESTCONF”](https://tools.ietf.org/html/draft-ietf-netconf-restconf-04) . 

Another way to call the same APIs is via Python, which is the focus of this section of the lab. The Python code here is presented as a series of scripts that you can run on an Ubuntu VM, available via “ssh cisco@198.18.134.28”. The password is C1sco12345. When you log in, a script will be run to update the VM for this exercise, and so you will need to provide the password so that the script can run with sudo permissions. You can look at the end of the ~/.bashrc file to see what is happening if you are curious.

The scripts (and this document) come from this project in GitHub: 

https://github.com/CiscoDevNet/cosc-learning-labs

On the VM those scripts have been “cloned” into in the ~/git/cosc-learning-labs/src/learning_lab directory. The setup script will put you into that directory automatically and set the appropriate environment variables. If anything below does not work as expected, see the “Troubleshooting” section below.

You will then be able to run scripts in the lab, with the steps below:

## Step 0 Check That the Controller is There



## Step 1 Mounting Netconf Devices

Use the 01_inventory_mount.py script which causes the server to use Netconf to mount the XRv instances in the ../settings/dcloud.py configuration file.

```bash
$ ./01_inventory_mount.py 
Python Library Documentation: function device_mount in module basics.inventory\n
device_mount(device_name, device_address, device_port, device_username, device_password)\n
Add the specified network device to the inventory of the Controller.\n
device_mount(lax, cisco, cisco, 830, 198.18.1.51)
device_mount(san, cisco, cisco, 830, 198.18.1.54)
device_mount(sea, cisco, cisco, 830, 198.18.1.55)
device_mount(min, cisco, cisco, 830, 198.18.1.52)
device_mount(por, cisco, cisco, 830, 198.18.1.53)
device_mount(sjc, cisco, cisco, 830, 198.18.1.57)
device_mount(kcy, cisco, cisco, 830, 198.18.1.50)
device_mount(sfc, cisco, cisco, 830, 198.18.1.56)
```

## Step 2 Displaying the Connected Devices

Use the	01_inventory_connected.py scripts to display the connected devices:

```bash
$ ./01_inventory_connected.py 
Python Library Documentation: function inventory_connected in module basics.inventory
inventory_connected()
    Names of network devices connected to the Controller.
    Output a list of names.
    Connected devices are a subset of the inventory.
['sea', 'por', 'san', 'lax', 'sjc', 'sfc', 'kcy', 'min']
```

The output above indicates that the controller has mounted the XRv devices, and that all devices connected properly. If you do not see that they connected properly, try again. It can take a several minutes for all of the network elements to mount and connect.
After that, there are additional sets of scripts to examine certain components and set properties on those components, as appropriate. 

## Step 3 Seeing What Else You Can Do

One the key concepts in [Netconf](https://tools.ietf.org/html/rfc6241) is ["capabilities"](https://tools.ietf.org/html/rfc6241#section-1.3). These capabilities are implemented by the network elements that the controller manages, and the controller acts as an agent for the network elements, passing through what it discovers on the network elements. What this means overall, then, is that the main factor determining what you can do next is what the network elements support.

To what the network elements mounted in your controller supports, use the "*capability*" scripts, which will show you what is possible.

* 02_capability.py - Prints the capabilities supported by each device.

```bash
./02_capability.py 
cosc authentication url: https://198.18.1.25/controller-auth
cosc authentication parameters:
   ...
por (http://cisco.com/ns/yang/Cisco-IOS-XR-shellutil-cfg?revision=2013-07-22)Cisco-IOS-XR-shellutil-cfg
por (http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-oper?revision=2013-07-22)Cisco-IOS-XR-ifmgr-oper
por (http://cisco.com/ns/yang/Cisco-IOS-XR-infra-infra-cfg?revision=2013-07-22)Cisco-IOS-XR-infra-infra-cfg
...
```

* 02_capability_discovery.py - Checks which devices have specific, advanced, capabilities such as ACLs and static routes.

```bash
 ./02_capability_discovery.py 
cosc authentication url: https://198.18.1.25/controller-auth
cosc authentication parameters:
  ...

capability_discovery(Cisco-IOS-XR-ipv4-acl-cfg, http://cisco.com/ns/yang/):
	 None

capability_discovery(Cisco-IOS-XR-ip-static-cfg, http://cisco.com/ns/yang/):
	 None
...
```
For each section of scripts for a given feature, there is also a script that will test which devices have the required capability to work with the feature, e.g.:
		
* 04_static_route_capability.py - Iterate through connected devices looking for the capability to add static routes.

```bash
./04_static_route_capability.py
cosc authentication url: https://198.18.1.25/controller-auth
cosc authentication parameters:
  ...
Python Library Documentation: function capability_discovery in module basics.inventory

capability_discovery(capability_name=None, capability_ns=None, capability_revision=None, device_name=None)
    Discover the revision of the specified capability for a set of devices.
    
    The entire inventory will be examined unless a single device is specified.
    Function output is a list of tuples. 
    Each tuple consists of (device_name, (capability_name, capability_ns, capability_revision).

capability_discovery(device_name=sjc, capability_name=Cisco-IOS-XR-ip-static-cfg, capability_ns=http://cisco.com/ns/yang/)
None
...
```

* 05_acl_capability.py - Iterate through the connected devices looking for the capability to configure ACLs.

```bash
./05_acl_capability.py
cosc authentication url: https://198.18.1.25/controller-auth
cosc authentication parameters:
..
Python Library Documentation: function capability_discovery in module basics.inventory

capability_discovery(capability_name=None, capability_ns=None, capability_revision=None, device_name=None)
    Discover the revision of the specified capability for a set of devices.
    
    The entire inventory will be examined unless a single device is specified.
    Function output is a list of tuples. 
    Each tuple consists of (device_name, (capability_name, capability_ns, capability_revision).

capability_discovery(device_name=sjc, capability_name=Cisco-IOS-XR-ipv4-acl-cfg, capability_ns=http://cisco.com/ns/yang/)
None
...
```

As this is a growing body of code, to see which scripts there are, use the “ls” command as shown below (note that this is a just an elided example of what you will see, as the contents will change over time): 

```bash
$ ls
00_controller.py 01_inventory_unreachable.py 04_static_route_json_all.py
00_devices.py	 02_capability.py 04_static_route_list.py
00_settings.py 02_capability_compare.py	04_story.py
01_device_connect.py 02_capability_discovery.py 04_topology.py
01_device_connected.py 02_capability_matrix.py	05_acl_apply_packet_filter.py
01_device_control.py 03_interface_configuration.py 05_acl_capability.py
…
```

Some of what these scripts cover includes:  

* Inventory
* Interfaces
* Routes and Topology
* ACLs

This is a living body of code, and so can vary each time you use this lab.

If you want to modify the list of devices being mounted, edit the ../settings/dcloud.py file. That file is Python code as well.
You can also use the inbuilt Python interpreter to call the functions in the basics library, in the same way that the code in the learning_lab directory does, and you can adapt and modify any of the scripts that you as you like. You will not break anything.

Have at it! 

The Cisco DevNet team – developer.cisco.com.

# Troubleshooting

Some problems that can arise when working with the Open SDN Controller are discussed below:

* Chrome caches the progress bar and does not move beyond that when accessing the GUI of the controller. If you have Firefox available, then use that.
* The controller becomes un-responsive, or responds with 50X errors. This can happen for a variety of reasons, and the simple remedy is to reboot the controller VM as shown below.
* The network is in some state, with routes, ACLs, interfaces shutdown, or similar, probably because of a previous series of exercises with the same lab instance, that leads to unexpected results. In this case there is a `restore_network_state.py` script that should reset everything and leave the controller with no mounted devices. If this script does not work, reboot the controller server and try again after five minutes.

The controller “ocs” server can be rebooted from the “Servers” section of your dCloud Dashboard as shown below. Click on the “+” symbol next to the “ocs” server entry, and then select the bottom right “Reboot Guest” button, which has a symbol of circled arrows. 

![Server Reboot](dcloud_images/server_reset.png)

This reboot will take approximately five minutes.