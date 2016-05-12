# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib64/python2.6/site-packages/PyQt4/QtCore.so
# by generator 1.136
# no doc

# imports
import sip as __sip


from property import property

class pyqtProperty(property):
    """
    pyqtProperty(type, fget=None, fset=None, freset=None, fdel=None, doc=None
                 designable=True, scriptable=True, stored=True, user=False)
                 -> property attribute
    
    type is the type of the property.  It is either a type object or a string
    that is the name of a C++ type.
    freset is a function for resetting an attribute to its default value.
    designable sets the DESIGNABLE flag (the default is True for writable
    properties and False otherwise).
    scriptable sets the SCRIPTABLE flag.
    stored sets the STORED flag.
    user sets the USER flag.
    The other parameters are the same as those required by the standard Python
    property type.  Properties defined using pyqtProperty behave as both Python
    and Qt properties.
    """
    def __init__(self, type, fget=None, fset=None, freset=None, fdel=None, doc=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    freset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



