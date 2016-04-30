#!/usr/bin/env python

#using Arista management API. It should be enable on the switch first:
#conf t
#management api http-commands
#no shutdown
#100.100.100.4 is management IP address
#API could be tested in sandbox by going to http://100.100.100.4 via browser

import jsonrpclib
import json
urlString="https://admin:admin@100.100.100.4/command-api"
myReq=jsonrpclib.Server(urlString)
try:
  response=myReq.runCmds(1,["show lldp neighbors"], "json")
except jsonrpclib.jsonrpc.ProtocolError as err:
  for code, msg in err:
    print "Code: {0}, Error message: {1}".format(code, msg)

print json.dumps(response, sort_keys=True, indent=3)
