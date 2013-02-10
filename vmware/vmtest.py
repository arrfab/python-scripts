#!/usr/bin/env python

# Complete the following variables
#

vcenterhost="vcenter1.mydomain.com"
vcenteruser="mydomain.com\myuser"
vcenterpwd="mypassword"

######################################################
from pysphere import *
import pprint
server = VIServer()
server.connect(vcenterhost,vcenteruser,vcenterpwd)

vm = server.get_vm_by_path('[N6060_SAS_VMRD07] S999JILNX016-Veeam-RHEL5/S999JILNX016-Veeam-RHEL5.vmx')
print '='*70
#prop = vm.get_properties()

#print prop
print "=" * 70
print vm.properties.storage.perDatastoreUsage
for item in vm.properties.storage.perDatastoreUsage:
  print vm.properties.storage.perDatastoreUsage.committed

server.disconnect
