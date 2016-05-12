# encoding: utf-8
# module block.dm
# from /usr/lib64/python2.6/site-packages/block/dmmodule.so
# by generator 1.136
# no doc
# no imports

# Variables with simple values

log_debug = 7
log_err = 3
log_fatal = 2
log_info = 6
log_notice = 5
log_warn = 4

# functions

def maps(*args, **kwargs): # real signature unknown
    """ Scans the system for mapped devices.  It does not expect any arguments.  It returns a list of map objects. """
    pass

def rmpart(*args, **kwargs): # real signature unknown
    """ Deletes a partition from the specified device.  Expects a string representing the device with the keyword dev_path and an long representing the partition number with the keyword partno.  Returns None on success and NULL on failure. """
    pass

def scanparts(*args, **kwargs): # real signature unknown
    """ Rescans the partition talbe for the specified device.  Expects a string representing the device with the keyword dev_path. returns None on success and NULL on failure. """
    pass

def set_logger(*args, **kwargs): # real signature unknown
    """ Defines the log function to be used.  Expects a callable object.  Will return None on success and NULL on failure. """
    pass

def targets(*args, **kwargs): # real signature unknown
    """ Scans for suppoerted targets.  It does not expect any args.  It returns a list of target objects. """
    pass

# classes

class device(object):
    """ The device mapper device.  Contains device file information. """
    def mknod(self, *args, **kwargs): # real signature unknown
        """ Create the node for the current device """
        pass

    def __cmp__(self, y): # real signature unknown; restored from __doc__
        """ x.__cmp__(y) <==> cmp(x,y) """
        pass

    def __hash__(self): # real signature unknown; restored from __doc__
        """ x.__hash__() <==> hash(x) """
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

    context = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """context"""

    dev = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """dev"""

    major = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """major"""

    minor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """minor"""

    mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """mode"""



class DmError(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class map(object):
    """ The device mapper device map.  Has most of the related metadata. """
    def remove(self, *args, **kwargs): # real signature unknown
        pass

    def __cmp__(self, y): # real signature unknown; restored from __doc__
        """ x.__cmp__(y) <==> cmp(x,y) """
        pass

    def __hash__(self): # real signature unknown; restored from __doc__
        """ x.__hash__() <==> hash(x) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    deps = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """deps"""

    dev = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """dev"""

    exists = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """exists"""

    inactive_table = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """inactive_table"""

    live_table = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """live_table"""

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """name"""

    open_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """open_count"""

    suspended = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """suspended"""

    table = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """table"""

    uuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """uuid"""



class table(object):
    """ The device mapper device table """
    def __cmp__(self, y): # real signature unknown; restored from __doc__
        """ x.__cmp__(y) <==> cmp(x,y) """
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

    params = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """params"""

    size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """size"""

    start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """start"""

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """type"""



class target(object):
    """ The device mapper type """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    major = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """major"""

    micro = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """micro"""

    minor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """minor"""

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """name"""



