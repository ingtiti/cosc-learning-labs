Cisco Open SDN Controller 1.0 Sandbox v2
Last Updated: 4 May 2015
About This Cisco Solution
The Cisco Open SDN Controller is a commercial distribution of OpenDaylight that delivers business agility through automation of standards-based network infrastructure.
Built as a highly scalable software-defined networking (SDN) platform, the Open SDN Controller abstracts away the complexity of managing heterogeneous networks to improve service delivery and reduce operating costs.
With the Cisco Open SDN Controller, you can integrate business applications with the underlying network devices using Northbound Rest APIs.   The Rest APIs provide a list of supported base network functions, which are agnostic of the underlying network device manufacturer.
About This Demonstration
The purpose of this Sandbox is to give you access to an early view of the Cisco Open SDN controller. This will take your through the steps of accessing the new Open SDN Controller and then allow you to self-discover different aspects of this product. It will also walk you through using Postman to interact with the Open SDN Controller.
Demonstration Requirements
The table below outlines the requirements for this preconfigured demonstration. 
Table 1.	Demonstration Requirements
Required	Optional
•	Computer with Internet Connectivity
•	Cisco.com Login Credentials	•	Cisco AnyConnect
•	Remote Desktop Client Application
Demonstration Configuration
This demonstration contains preconfigured users and components to illustrate the capabilities available to you within the VIRL sandbox. 
All information needed to complete the access components is located in the Topology and Servers menus of your active demonstration. 
Topology Menu. Click on any server in the topology and a popup window will appear with available server options.
Servers Menu. Click on   or  next to any server name to display the available server options and credentials.
Demonstration Topology
When accessing the demo, the topology is a simplified one, as shown in the figure below: 
Figure 1.  	Figure: OSC Topology
 
This demonstration uses Virtual Internet Routing Lab (VIRL). VIRL is a multi-purpose network virtualization platform that provides an easy way to build, configure, and test new or existing network topologies with an intuitive user interface. 
The VIRL topology used for this demonstration, depicted as a single server above, actually consists of:  
•	Eight routers interconnected within the topology.
Each router has a management interface connected to the OSC server. Both VIRL and OSC run as Virtual Machines (VMs) on ESXi.
Figure 2.  	VIRL Topology
 
For additional information on VIRL, watch VIRL (Virtual Internet Routing Lab).
Demonstration Preparation
Follow the steps below to schedule your demonstration and configure your demonstration environment.
1.	Browse to dcloud.cisco.com and login with your Cisco.com credentials.
2.	Schedule a demonstration [Show Me How].
3.	Test your connection from the demonstration location before performing any demonstration scenario.  [Show Me How] 
4.	Verify your demonstration has a status of Active under My Demonstrations on the My Dashboard page in the dCloud UI.
•	It may take up to 30 minutes for your demonstration to become active.
5.	Connect to the Demonstration, using one of the following two options:
•	Using Cisco AnyConnect [Show Me How] ********RECOMMENDED METHOD********
o	After connecting to the demonstration via AnyConnect, use your local RDP client to connect to workstation located at 198.18.133.252. 
o	Alternatively, use your own local Chrome client to access the Open SDN controller at 198.18.1.25 
NOTE: You may need to accept a security certificate warning.
•	Using Cisco dCloud Remote Desktop client [Show Me How] 
NOTE: If you are running RDP, it is highly recommended that you use HTML5 as the default client. [Show Me How].   
TIP: If using the dCloud webRDP, you can make your RDP session screen larger. To resize, select the corners of the remote desktop window and drag to the desired size.  Right-click anywhere within the grey space of the remote desktop window and select Reload. 
6.	If necessary, log into the workstation with the credentials Administrator / C1sco12345 

 
Scenario 1: Accesing the OSC
Demonstration Steps
1.	Access the Open SDN Controller in one of two ways:
•	If you are connected to the demo via web RDP, on the workstation, use the chrome browser to access the OSC GUI interface at 198.18.1.25
•	If you are connected to the demo via Anyconnect:
o	Open your own, local browser window and access the OSC GUI interface at 198.18.1.25
o	Use a local RDP client to connect to the workstation (at 198.18.133.252 – user credentials Administrator / C1sco12345), and use the workstation chrome browser to access the OSC GUI interface at 198.18.1.25.
2.	For the SDN Controller, use the login credentials admin / cisco123 and click Login.
3.	Welcome to the new Open SDN Controller --- Explore!
Figure 3.  	OSC GUI
 
Caveats: 
•	At this time, you are not be able to use the GUI interface to access router configurations; however, you can telnet into the routers using an ssh client.
•	Please disregard any geographical issues you may find ☺

POSTMAN
Many applications and servers today have Representational State Transfer (REST) APIs enabled. REST APIs allow users to access, monitor, and control devices from remote locations. There are many tools available that allow you to exploit the REST API, such as CURL and POSTMAN. This sandbox environment uses POSTMAN to exploit the REST APIs of the OSC. 
This section walks you through the process of using POSTMAN to interact with the Open SDN Controller.
Cisco Open SDN Controller has a security shield enabled. All rest access must be done using tokens.
4.	Connect to POSTMAN in one of three ways:
•	If you are remotely connected to the workstation, via the dCloud web RDP session, or via AnyConnect and a local remote desktop client:
1)	On the workstation, in the Chrome browser, click the Postman tab, as shown in the figure below.
•	If you connected to the demo via AnyConnect and pointed your local Chrome Browser window directly to the OSC (and did NOT RDP to the workstation), do one of the following:
2)	Remotely connect to the dCloud workstation @ 198.18.133.252, via the dCloud web RDP client or your local RDP client, and then proceed as you would with option 1.
3)	(For users familiar with POSTMAN) Use your own, local POSTMAN application. Import the following **collections:
•	OSC-25-Tokenized: https://www.getpostman.com/collections/e6f05baf5a3848bf5796
•	VIRL_Client: https://www.getpostman.com/collections/2bf2256ec14f5d40d314

5.	In POSTMAN, click the Collections link, then click the OSC-25-Tokenized subheading.
6.	Click POST Get token. Then, in the middle panel, click Send. 
7.	Copy the token string from the reply - without quote characters, as highlighted in the figure below.
Figure 4.  	Get Token
 
8.	Next, click the GET Get all topos 
9.	In the middle pane, select the Basic Auth tab. For the username, enter token. Paste the copied token string as a password.
Figure 5.  	Authentication
 
10.	Click Refresh headers.
11.	On the new screen, click Send.
Figure 6.  	Send with Authentication
 

Python DevNet Learning Lab
In the labs section above, you used Postman, which is a browser plugin that allows you to send HTTP requests to REST (Representational State Transfer) APIs on the controller. In the case of the Cisco Open SDN Controller, those APIs are generated from Yang models and exposed via “RESTCONF” . 
Another way to call the same APIs is via Python, which is the focus of this section of the lab. The Python code here is presented as a series of scripts that you can run on an Ubuntu VM, available via “ssh cisco@198.18.134.28”. The password is C1sco12345. When you log in, a script will be run to update the VM for this exercise, and so you will need to provide the password so that the script can run with sudo permissions. You can look at the end of the ~/.bashrc file to see what is happening if you are curious.
The scripts come from this project in GitHub: 
https://github.com/CiscoDevNet/cosc-learning-labs
On the VM those scripts have been “cloned” into in the ~/git/cosc-learning-labs/src/learning_lab directory. The setup script will put you into that directory automatically and set the appropriate environment variables. If anything below does not work as expected, see the “Troubleshooting” section below.
You will then be able to run scripts in the lab, as below:
•	01_inventory_mount.py – Causes the server to use Netconf to mount the XRv instances in the ../settings/dcloud.py configuration file.
$ ./01_inventory_mount.py 
Python Library Documentation: function device_mount in module basics.inventory
device_mount(device_name, device_address, device_port, device_username, device_password)
    Add the specified network device to the inventory of the Controller.
device_mount(lax, cisco, cisco, 830, 198.18.1.51)
device_mount(san, cisco, cisco, 830, 198.18.1.54)
device_mount(sea, cisco, cisco, 830, 198.18.1.55)
device_mount(min, cisco, cisco, 830, 198.18.1.52)
device_mount(por, cisco, cisco, 830, 198.18.1.53)
device_mount(xrvr-999, cisco, cisco, 830, 198.18.1.999)
device_mount(sjc, cisco, cisco, 830, 198.18.1.57)
device_mount(kcy, cisco, cisco, 830, 198.18.1.50)
device_mount(sfc, cisco, cisco, 830, 198.18.1.56)
Note that the xrvr-999 device is there for test purposes, to show that non-existent devices will not be connected.
•	01_inventory_connected.py – Displays the connected devices:
$ ./01_inventory_connected.py 
Python Library Documentation: function inventory_connected in module basics.inventory
inventory_connected()
    Names of network devices connected to the Controller.
    Output a list of names.
    Connected devices are a subset of the inventory.
['sea', 'por', 'san', 'lax', 'sjc', 'sfc', 'kcy', 'min']
The output above indicates that the controller has mounted the XRv devices, and that all devices connected properly. If you do not see that they connected properly, try again. It can take a several minutes for all of the network elements to mount and connect.
After that, there are additional sets of scripts to examine certain components and set properties on those components, as appropriate. To see which scripts there are, use the “ls” command as shown below (note that this is a just an elided example of what you will see, as the contents will change over time): 
$ ls
00_controller.py 01_inventory_unreachable.py 04_static_route_json_all.py
00_devices.py	 02_capability.py 04_static_route_list.py
00_settings.py 02_capability_compare.py	04_story.py
01_device_connect.py 02_capability_discovery.py 04_topology.py
01_device_connected.py 02_capability_matrix.py	05_acl_apply_packet_filter.py
01_device_control.py 03_interface_configuration.py 05_acl_capability.py
…

Some of what these scripts cover includes:  
•	Inventory
•	Netconf/Yang capabilities
•	Interfaces
•	Routes and Topology
•	ACLs
This is a living body of code, and so can vary each time you use this lab.
If you want to modify the list of devices being mounted, edit the ../settings/dcloud.py file. That file is Python code as well.
You can also use the inbuilt Python interpreter to call the functions in the basics library, in the same way that the code in the learning_lab directory does, and you can adapt and modify any of the scripts that you as you like. You will not break anything.
Have at it! 
The Cisco DevNet team – developer.cisco.com.
Troubleshooting
There are two main problems that can typically arise when working with the Open SDN Controller:
•	The controller becomes un-responsive, or responds with 50X errors. This can happen for a variety of reasons, and the simple remedy is to reboot the controller VM as shown below.
•	The network is in some state, with routes, ACLs, interfaces shutdown, or similar, probably because of a previous series of exercises with the same lab instance, that leads to unexpected results. In this case there is a restore_network_state.py script that should reset everything and leave the controller with no mounted devices. If this script does not work, reboot the controller server and try again after five minutes.
The controller “ocs” server can be rebooted from the “Servers” section of your dCloud Dashboard as shown below. Click on the “+” symbol next to the “ocs” server entry, and then select the bottom right “Reboot Guest” button, which has a symbol of circled arrows. This reboot will take approximately five minutes.
 
***THIS CONCLUDES THIS SANDBOX GETTING STARTED GUIDE ***

