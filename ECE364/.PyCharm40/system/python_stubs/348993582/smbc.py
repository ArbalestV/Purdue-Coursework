# encoding: utf-8
# module smbc
# from /usr/lib64/python2.6/site-packages/smbc.so
# by generator 1.136
# no doc
# no imports

# Variables with simple values

COMMS_SHARE = 5

FILE_SHARE = 3

FLAG_FALLBACK_AFTER_KERBEROS = 2

FLAG_NO_AUTO_ANONYMOUS_LOGON = 4

FLAG_USE_KERBEROS = 1

IPC_SHARE = 6

PRINTER_SHARE = 4

SERVER = 2

WORKGROUP = 1

# no functions
# classes

class Context(object):
    """
    SMBC context
    ============
    
      A context for libsmbclient calls.
    """
    def open(self, uri): # real signature unknown; restored from __doc__
        """
        open(uri) -> int
        
        @type uri: string
        @param uri: URI to open
        @return: a L{smbc.File} object for the URI
        """
        return 0

    def opendir(self, uri): # real signature unknown; restored from __doc__
        """
        opendir(uri) -> Dir
        
        @type uri: string
        @param uri: URI to open
        @return: a L{smbc.Dir} object for the URI
        """
        return Dir

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    debug = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Debug level."""

    functionAuthData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Function for obtaining authentication data."""

    netbiosName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Netbios name used for making connections."""

    optionDebugToStderr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether to log to standard error instead of standard output."""

    optionNoAutoAnonymousLogin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether to automatically select anonymous login."""

    workgroup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Workgroup used for making connections."""



class Dir(object):
    """
    SMBC Dir
    ========
    
      A directory object.
    """
    def getdents(self): # real signature unknown; restored from __doc__
        """
        getdents() -> list
        
        @return: a list of L{smbc.Dirent} objects
        """
        return []

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class Dirent(object):
    """
    SMBC Dirent
    ===========
    
      A directory entry object.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    comment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """comment"""

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """name"""

    smbc_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """smbc_type"""



class File(object):
    """
    SMBC File
    =========
    
      A directory object.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


