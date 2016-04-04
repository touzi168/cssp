#-*- coding: utf-8 -*-

import libvirt
import os
import re
import sys
import xml.etree.ElementTree as ET

VM_XML_TEMPLATE = '/root/cssp/virtscripts/vm.xml'
VM_QCOW2_TEMPLATE = '/root/cssp/virtscripts/FreeDOS.qcow2'

def createVMPath(path=None):
    try:
        os.mkdir(path)
    except:
        pass

def createVM(name=None, vcpu=1, mem=102400, path=None):
    vmpath = path + '/' + name
    createVMPath(vmpath)
    diskfile = vmpath + '/' + name + '.qcow2'
    with open(VM_XML_TEMPLATE) as fp:
        domainXMLString = fp.read()
    domainXMLString = domainXMLString.replace('{ $name }', name)
    domainXMLString = domainXMLString.replace('{ $vcpu }', '%d' % vcpu)
    domainXMLString = domainXMLString.replace('{ $mem }', '%d' % mem)
    domainXMLString = domainXMLString.replace('{ $disk }', diskfile)
    cmd = 'qemu-img create -f qcow2 %s -b %s' % (diskfile, VM_QCOW2_TEMPLATE)
    os.system(cmd)
    hostUri = 'qemu:///system'
    host = libvirt.open(hostUri)
    domain = host.createXML(domainXMLString, 0)
    return True

def startVM(name=None):
    hostUri = 'qemu:///system'
    host = libvirt.open(hostUri)
    domain = host.lookupByName(name)
    domain.create()

def shutdownVM(name=None):
    hostUri = 'qemu:///system'
    host = libvirt.open(hostUri)
    domain = host.lookupByName(name)
    domain.destroy()

def getVNCPort(name=None):
    hostUri = 'qemu:///system'
    host = libvirt.open(hostUri)
    domain = host.lookupByName(name)
    root = ET.fromstring(domain.XMLDesc())
    port = root.find('devices').find('graphics').get('port')
    return port

def rebootVM(name=None):
    hostUri = 'qemu:///system'
    host = libvirt.open(hostUri)
    domain = host.lookupByName(name)
    domain.reboot()

def deleteVM(name=None):
    hostUri = 'qemu:///system'
    host = libvirt.open(hostUri)
    domain = host.lookupByName(name)
    domain.destroy()
    domain.undefine()

if __name__ == '__main__':
    vmname = 'vm1'
    print getVNCPort(vmname)
    sys.exit()
    vmpath = '/root/cssp/vms'
    createVMPath(vmpath)
    ret = createVM(vmname, 1, 102400, vmpath)
    if (ret == True):
        print('create %s success!' % vmname)
