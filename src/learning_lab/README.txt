I want to clarify that the sample scripts are deliberately as simple as possible.

Where there is a requirement for additional functionality then it will be provided in a separate script. That is one reason we have a lot of scripts (50+).

I bend the rules a little bit when a function can return None. In those situations I continue to call the function until the output is interesting.

For example, we might continue sampling network interfaces until we find one that has an ip address.

People will be running the sample scripts and then examining all the HTTP requests and responses. For the elemental sample scripts there will ideally be no more than 3 HTTP requests.

As we build comprehensive/composite scripts there will be too many HTTP requests and we will not make them available. It is too much information. Instead we will refer people to the elemental scripts.

So, if you see sample code like:

for device in inventory:
	if demonstrate(device):
		stop

Then you know why that loops stops asap.
