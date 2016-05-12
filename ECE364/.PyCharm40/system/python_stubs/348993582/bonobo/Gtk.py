# encoding: utf-8
# module Bonobo.Gtk
# from /usr/lib64/python2.6/site-packages/gtk-2.0/gnomeapplet.so
# by generator 1.136
# no doc

# imports
import CORBA as __CORBA


# Variables with simple values

DirectionDown = 3
DirectionLeft = 4
DirectionRight = 5
DirectionTabBackward = 1
DirectionTabForward = 0
DirectionUp = 2

StateActive = 1
StateInsensitive = 4
StateNormal = 0
StatePrelight = 2
StateSelected = 3

# no functions
# classes

class Direction(__CORBA.Enum):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __enum_values__ = (
        0,
        1,
        2,
        3,
        4,
        5,
    )
    __typecode__ = None # (!) real value is ''


class Requisition(__CORBA.Struct):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __typecode__ = None # (!) real value is ''


class State(__CORBA.Enum):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __enum_values__ = (
        0,
        1,
        2,
        3,
        4,
    )
    __typecode__ = None # (!) real value is ''


