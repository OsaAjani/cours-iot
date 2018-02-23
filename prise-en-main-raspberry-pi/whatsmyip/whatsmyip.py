#!/usr/bin/env python
# # -*- coding: utf-8 -*-

"""Script that do a query to a server to renseign internal ip and hostname
"""
import socket
import fcntl
import struct
import urllib2

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

server_script_url = 'http://plebweb.fr/cours-iot/whatsmyip.php'
interface_name = 'wlan0'

hostname = socket.gethostname()
local_ip = get_ip_address(interface_name)

request_url = server_script_url + '?local_ip=' + local_ip + '&hostname=' + hostname

urllib2.urlopen(request_url).read()


