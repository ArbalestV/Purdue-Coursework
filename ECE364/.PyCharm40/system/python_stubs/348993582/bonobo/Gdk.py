# encoding: utf-8
# module Bonobo.Gdk
# from /usr/lib64/python2.6/site-packages/gtk-2.0/gnomeapplet.so
# by generator 1.136
# no doc

# imports
import CORBA as __CORBA


# Variables with simple values

BUTTON = 3

BUTTON_2_PRESS = 1

BUTTON_3_PRESS = 2

BUTTON_PRESS = 0
BUTTON_RELEASE = 3

CROSSING = 4

ENTER = 0

FOCUS = 0

GRAB = 1

KEY = 1

KEY_PRESS = 0
KEY_RELEASE = 1

LEAVE = 1

MOTION = 2

NORMAL = 0

UNGRAB = 2

# no functions
# classes

class ButtonEvent(__CORBA.Struct):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __typecode__ = None # (!) real value is ''


class ButtonType(__CORBA.Enum):
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
    )
    __typecode__ = None # (!) real value is ''


class CrossingEvent(__CORBA.Struct):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __typecode__ = None # (!) real value is ''


class CrossMode(__CORBA.Enum):
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
    )
    __typecode__ = None # (!) real value is ''


class CrossType(__CORBA.Enum):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __enum_values__ = (
        0,
        1,
    )
    __typecode__ = None # (!) real value is ''


class Event(__CORBA.Union):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    button = None # (!) real value is ''
    crossing = None # (!) real value is ''
    focus = None # (!) real value is ''
    key = None # (!) real value is ''
    motion = None # (!) real value is ''
    __dict__ = None # (!) real value is ''
    __typecode__ = None # (!) real value is ''


class EventType(__CORBA.Enum):
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


class FocusEvent(__CORBA.Struct):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __typecode__ = None # (!) real value is ''


class KeyEvent(__CORBA.Struct):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __typecode__ = None # (!) real value is ''


class KeyType(__CORBA.Enum):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __enum_values__ = (
        0,
        1,
    )
    __typecode__ = None # (!) real value is ''


class MotionEvent(__CORBA.Struct):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __typecode__ = None # (!) real value is ''


