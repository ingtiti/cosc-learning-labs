#!/usr/bin/env python

import json
import urllib
import sys

# set up URL
url = 'http://%s:8181/restconf/operational/network-topology:network-topology/topology/example-linkstate-topology' % (sys.argv[1])

# get URL
print "\n".join(sorted([node['l3-unicast-igp-topology:igp-node-attributes']['router-id'][0] for node in json.loads(urllib.urlopen(url).read())['topology'][0]['node']]))
