Set environment variable NETWORK_PROFILE to ‘learning_lab’ or any other setting you prefer.
```bash
	export NETWORK_PROFILE=learning_lab
```
The settings are read from Python module with path:
```bash
~/git/cosc-learning-labs/src/settings/${NETWORK_PROFILE}.py
```
… which is a module in the ‘settings’ package, which is in the project’s top level directory ‘src’.

To display the settings:
```bash
cat ~/git/cosc-learning-labs/src/settings/${NETWORK_PROFILE}.py
```
Sample output:
```python
config = {
 'network_device': {'xrvr-1':{
                     'address': '172.16.1.53',
                     'port': 830,
                     'password': 'cisco',
                     'username': 'cisco'},
                    'xrvr-2':{
                     'address': '172.16.1.52',
                     'port': 830,
                     'password': 'cisco',
                     'username': 'cisco'},
                    'xrvr-999':{
                     'address': '172.16.1.999',
                     'port': 830,
                     'password': 'cisco',
                     'username': 'cisco'}},
 'odl_server': {'address': '172.16.1.1',
                'port': 8181,
                'password': 'admin',
                'username': 'admin'}}
```
