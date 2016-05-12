# encoding: utf-8
# module gudev
# from /usr/lib64/python2.6/site-packages/gudev.so
# by generator 1.136
# no doc

# imports
import gobject as __gobject
import gobject._gobject as __gobject__gobject


# Variables with simple values

DEVICE_TYPE_BLOCK = 98
DEVICE_TYPE_CHAR = 99
DEVICE_TYPE_NONE = 0

__version__ = '147.1'

# no functions
# classes

class Client(__gobject__gobject.GObject):
    """
    Object GUdevClient
    
    Signals from GUdevClient:
      uevent (gchararray, GUdevDevice)
    
    Properties from GUdevClient:
      subsystems -> GStrv: The subsystems to listen for changes on
        The subsystems to listen for changes on
    
    Signals from GObject:
      notify (GParam)
    """
    def query_by_device_file(self, *args, **kwargs): # real signature unknown
        pass

    def query_by_device_number(self, *args, **kwargs): # real signature unknown
        pass

    def query_by_subsystem(self, *args, **kwargs): # real signature unknown
        pass

    def query_by_subsystem_and_name(self, *args, **kwargs): # real signature unknown
        pass

    def query_by_sysfs_path(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class Device(__gobject__gobject.GObject):
    """
    Object GUdevDevice
    
    Signals from GObject:
      notify (GParam)
    """
    def get_action(self, *args, **kwargs): # real signature unknown
        pass

    def get_device_file(self, *args, **kwargs): # real signature unknown
        pass

    def get_device_file_symlinks(self, *args, **kwargs): # real signature unknown
        pass

    def get_device_number(self, *args, **kwargs): # real signature unknown
        pass

    def get_device_type(self, *args, **kwargs): # real signature unknown
        pass

    def get_devtype(self, *args, **kwargs): # real signature unknown
        pass

    def get_driver(self, *args, **kwargs): # real signature unknown
        pass

    def get_name(self, *args, **kwargs): # real signature unknown
        pass

    def get_number(self, *args, **kwargs): # real signature unknown
        pass

    def get_parent(self, *args, **kwargs): # real signature unknown
        pass

    def get_parent_with_subsystem(self, *args, **kwargs): # real signature unknown
        pass

    def get_property(self, *args, **kwargs): # real signature unknown
        pass

    def get_property_as_boolean(self, *args, **kwargs): # real signature unknown
        pass

    def get_property_as_double(self, *args, **kwargs): # real signature unknown
        pass

    def get_property_as_int(self, *args, **kwargs): # real signature unknown
        pass

    def get_property_as_strv(self, *args, **kwargs): # real signature unknown
        pass

    def get_property_as_uint64(self, *args, **kwargs): # real signature unknown
        pass

    def get_property_keys(self, *args, **kwargs): # real signature unknown
        pass

    def get_seqnum(self, *args, **kwargs): # real signature unknown
        pass

    def get_subsystem(self, *args, **kwargs): # real signature unknown
        pass

    def get_sysfs_attr(self, *args, **kwargs): # real signature unknown
        pass

    def get_sysfs_attr_as_boolean(self, *args, **kwargs): # real signature unknown
        pass

    def get_sysfs_attr_as_double(self, *args, **kwargs): # real signature unknown
        pass

    def get_sysfs_attr_as_int(self, *args, **kwargs): # real signature unknown
        pass

    def get_sysfs_attr_as_strv(self, *args, **kwargs): # real signature unknown
        pass

    def get_sysfs_attr_as_uint64(self, *args, **kwargs): # real signature unknown
        pass

    def get_sysfs_path(self, *args, **kwargs): # real signature unknown
        pass

    def has_property(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class DeviceType(__gobject.GEnum):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __enum_values__ = {
        0: 0,
        98: 98,
        99: 99,
    }
    __gtype__ = None # (!) real value is ''


