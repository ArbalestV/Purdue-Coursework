# encoding: utf-8
# module libiscsi
# from /usr/lib64/python2.6/site-packages/libiscsimodule.so
# by generator 1.136
# no doc
# no imports

# functions

def discover_firmware(*args, **kwargs): # real signature unknown
    """ Do firmware discovery and return a list of found nodes) """
    pass

def discover_sendtargets(*args, **kwargs): # real signature unknown
    """ Do sendtargets discovery and return a list of found nodes) """
    pass

def get_firmware_initiator_name(*args, **kwargs): # real signature unknown
    """ Get initator name (iqn) from firmware """
    pass

# classes

class chapAuthInfo(object):
    """ iscsi chap authentication information. """
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

    password = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """password"""

    reverse_password = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """reverse_password"""

    reverse_username = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """reverse_username"""

    username = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """username"""



class node(object):
    """ The iscsi node contains iscsi node information. """
    def getAuth(self, *args, **kwargs): # real signature unknown
        """ Get authentication information """
        pass

    def getParameter(self, *args, **kwargs): # real signature unknown
        """ Get an iscsi node parameter """
        pass

    def login(self, *args, **kwargs): # real signature unknown
        """ Log in to the node """
        pass

    def logout(self, *args, **kwargs): # real signature unknown
        """ Log out of the node """
        pass

    def setAuth(self, *args, **kwargs): # real signature unknown
        """ Set authentication information """
        pass

    def setParameter(self, *args, **kwargs): # real signature unknown
        """ Set an iscsi node parameter """
        pass

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

    address = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """address"""

    iface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """iface"""

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """name"""

    port = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """port"""

    tpgt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """tpgt"""



