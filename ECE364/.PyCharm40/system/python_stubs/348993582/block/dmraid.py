# encoding: utf-8
# module block.dmraid
# from /usr/lib64/python2.6/site-packages/block/dmraidmodule.so
# by generator 1.136
# no doc
# no imports

# Variables with simple values

date = '(2010.01.19)'

device_list = 1

disk_status_broken = 2
disk_status_inconsistent = 4
disk_status_nosync = 8
disk_status_ok = 16
disk_status_setup = 32
disk_status_undef = 1

format_list = 0

raid_device_list = 2

raid_set_list = 3

version = '1'

# no functions
# classes

class context(object):
    """ The dmraid context.  Is needed for all the dmraid actions. It mainly contains the dmraid lib context. """
    def discover_disks(self, *args, **kwargs): # real signature unknown
        """ Discover all disks in the system. Expects a list of filesystem nodes where the disks should be searched.  It will search in sysfs if no list is given.  Returns number of disks found. """
        pass

    def discover_raiddevs(self, *args, **kwargs): # real signature unknown
        """ Identifies which disks are part of a raid set. Expects a list of devices and returns the number of raid devices found.  It will search all devices if no list is provided. """
        pass

    def discover_raidsets(self, *args, **kwargs): # real signature unknown
        """ Discovers the raid sets in the system """
        pass

    def get_raidsets(self, *args, **kwargs): # real signature unknown
        """ Returns a list of raid sets in the system.  This function identifies all the disks in the system, identifies what disks are part of raid sets and identifies these raid sets.  It expects a list of devices and/or nodes where to search for disks and raid devs.  If not list is provided all the raidsets in the system are returned. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    disks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """disks"""

    raiddevs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """raiddevs"""

    raidsets = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """raidsets"""



class device(object):
    """ The system device """
    def rmpart(self, *args, **kwargs): # real signature unknown
        """ Removes the partition defined by the partno argument """
        pass

    def scanparts(self, *args, **kwargs): # real signature unknown
        """ (Re)scans all partitions for the current device """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """path"""

    sectors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """sectors"""

    serial = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """serial"""



class GroupingError(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class list(object):
    # no doc
    def __contains__(self, y): # real signature unknown; restored from __doc__
        """ x.__contains__(y) <==> y in x """
        pass

    def __getitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class raiddev(object):
    """ The raid device.  These are devices that contain raid sets. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    device = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """device"""

    sectors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """sectors"""

    set = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """set"""

    status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """status"""



class raidset(object):
    """ The raid set.  Metadata for dmraid devices. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    broken = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """broken"""

    children = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """children"""

    degraded = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """degraded"""

    dmTable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """block.dm.Table"""

    dmtype = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """dmtype"""

    found_devs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """found_devs"""

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """name"""

    sectors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """sectors"""

    set_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """set_type"""

    spares = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """spares"""

    status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """status"""

    table = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """table"""

    total_devs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """total_devs"""

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """type"""



