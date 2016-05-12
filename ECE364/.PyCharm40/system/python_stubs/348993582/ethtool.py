# encoding: utf-8
# module ethtool
# from /usr/lib64/python2.6/site-packages/ethtool.so
# by generator 1.136
""" Python ethtool module """
# no imports

# Variables with simple values

AF_INET = 2
AF_INET6 = 10

IFF_ALLMULTI = 512
IFF_AUTOMEDIA = 16384
IFF_BROADCAST = 2
IFF_DEBUG = 4
IFF_DYNAMIC = 32768
IFF_LOOPBACK = 8
IFF_MASTER = 1024
IFF_MULTICAST = 4096
IFF_NOARP = 128
IFF_NOTRAILERS = 32
IFF_POINTOPOINT = 16
IFF_PORTSEL = 8192
IFF_PROMISC = 256
IFF_RUNNING = 64
IFF_SLAVE = 2048
IFF_UP = 1

version = 'python-ethtool v0.6'

# functions

def get_active_devices(*args, **kwargs): # real signature unknown
    pass

def get_broadcast(*args, **kwargs): # real signature unknown
    pass

def get_businfo(*args, **kwargs): # real signature unknown
    pass

def get_coalesce(*args, **kwargs): # real signature unknown
    pass

def get_devices(*args, **kwargs): # real signature unknown
    pass

def get_flags(*args, **kwargs): # real signature unknown
    pass

def get_gso(*args, **kwargs): # real signature unknown
    pass

def get_hwaddr(*args, **kwargs): # real signature unknown
    pass

def get_interfaces_info(*args, **kwargs): # real signature unknown
    """ Accepts a string, list or tupples of interface names. Returns a list of ethtool.etherinfo objets with device information. """
    pass

def get_ipaddr(*args, **kwargs): # real signature unknown
    pass

def get_module(*args, **kwargs): # real signature unknown
    pass

def get_netmask(*args, **kwargs): # real signature unknown
    pass

def get_ringparam(*args, **kwargs): # real signature unknown
    pass

def get_sg(*args, **kwargs): # real signature unknown
    pass

def get_tso(*args, **kwargs): # real signature unknown
    pass

def get_ufo(*args, **kwargs): # real signature unknown
    pass

def set_coalesce(*args, **kwargs): # real signature unknown
    pass

def set_ringparam(*args, **kwargs): # real signature unknown
    pass

def set_tso(*args, **kwargs): # real signature unknown
    pass

# classes

class etherinfo(object):
    """ Contains information about a specific ethernet device """
    def get_ipv4_addresses(self, *args, **kwargs): # real signature unknown
        """ Retrieve configured IPv4 addresses.  Returns a list of NetlinkIP4Address objects """
        pass

    def get_ipv6_addresses(self, *args, **kwargs): # real signature unknown
        """ Retrieve configured IPv6 addresses.  Returns a tuple list of etherinfo_ipv6addr objects """
        pass

    def __delattr__(self, name): # real signature unknown; restored from __doc__
        """ x.__delattr__('name') <==> del x.name """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __setattr__(self, name, value): # real signature unknown; restored from __doc__
        """ x.__setattr__('name', value) <==> x.name = value """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass


class etherinfo_ipv6addr(object):
    """ IPv6 address information """
    def __delattr__(self, name): # real signature unknown; restored from __doc__
        """ x.__delattr__('name') <==> del x.name """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __setattr__(self, name, value): # real signature unknown; restored from __doc__
        """ x.__setattr__('name', value) <==> x.name = value """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    address = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """IPv6 address"""

    netmask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """IPv6 netmask"""

    scope = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """IPv6 IP address scope"""



# variables with complex values

__nlconnection = None # (!) real value is ''

