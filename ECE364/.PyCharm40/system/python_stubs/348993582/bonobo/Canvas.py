# encoding: utf-8
# module Bonobo.Canvas
# from /usr/lib64/python2.6/site-packages/gtk-2.0/gnomeapplet.so
# by generator 1.136
# no doc

# imports
import Bonobo as __Bonobo
import CORBA as __CORBA


# no functions
# classes

class ArtUTA(__CORBA.Struct):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __typecode__ = None # (!) real value is ''


class Buf(__CORBA.Struct):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __typecode__ = None # (!) real value is ''


class Component(__Bonobo.Unknown):
    # no doc
    def bounds(self, state): # real signature unknown; restored from __doc__
        """ bounds(state) -> 'IDL:omg.org/CORBA/void:1.0', x1, x2, y1, y2 """
        pass

    def contains(self, x, y): # real signature unknown; restored from __doc__
        """ contains(x, y) -> 'IDL:omg.org/CORBA/boolean:1.0' """
        pass

    def draw(self, state, drawable, x, y, width, height): # real signature unknown; restored from __doc__
        """ draw(state, drawable, x, y, width, height) -> 'IDL:omg.org/CORBA/void:1.0' """
        pass

    def event(self, state, event): # real signature unknown; restored from __doc__
        """ event(state, event) -> 'IDL:omg.org/CORBA/boolean:1.0' """
        pass

    def map(self): # real signature unknown; restored from __doc__
        """ map() -> 'IDL:omg.org/CORBA/void:1.0' """
        pass

    def realize(self, drawable): # real signature unknown; restored from __doc__
        """ realize(drawable) -> 'IDL:omg.org/CORBA/void:1.0' """
        pass

    def render(self, buf): # real signature unknown; restored from __doc__
        """ render(buf) -> 'IDL:omg.org/CORBA/void:1.0', buf """
        pass

    def setBounds(self, bbox): # real signature unknown; restored from __doc__
        """ setBounds(bbox) -> 'IDL:omg.org/CORBA/void:1.0' """
        pass

    def setCanvasSize(self, x, y, width, height): # real signature unknown; restored from __doc__
        """ setCanvasSize(x, y, width, height) -> 'IDL:omg.org/CORBA/void:1.0' """
        pass

    def unImplemented1(self): # real signature unknown; restored from __doc__
        """ unImplemented1() -> 'IDL:omg.org/CORBA/void:1.0' """
        pass

    def unImplemented2(self): # real signature unknown; restored from __doc__
        """ unImplemented2() -> 'IDL:omg.org/CORBA/void:1.0' """
        pass

    def unImplemented3(self): # real signature unknown; restored from __doc__
        """ unImplemented3() -> 'IDL:omg.org/CORBA/void:1.0' """
        pass

    def unImplemented4(self): # real signature unknown; restored from __doc__
        """ unImplemented4() -> 'IDL:omg.org/CORBA/void:1.0' """
        pass

    def unImplemented5(self): # real signature unknown; restored from __doc__
        """ unImplemented5() -> 'IDL:omg.org/CORBA/void:1.0' """
        pass

    def unImplemented6(self): # real signature unknown; restored from __doc__
        """ unImplemented6() -> 'IDL:omg.org/CORBA/void:1.0' """
        pass

    def unImplemented7(self): # real signature unknown; restored from __doc__
        """ unImplemented7() -> 'IDL:omg.org/CORBA/void:1.0' """
        pass

    def unImplemented8(self): # real signature unknown; restored from __doc__
        """ unImplemented8() -> 'IDL:omg.org/CORBA/void:1.0' """
        pass

    def unmap(self): # real signature unknown; restored from __doc__
        """ unmap() -> 'IDL:omg.org/CORBA/void:1.0' """
        pass

    def unrealize(self): # real signature unknown; restored from __doc__
        """ unrealize() -> 'IDL:omg.org/CORBA/void:1.0' """
        pass

    def update(self, state, aff, clip_path, flags): # real signature unknown; restored from __doc__
        """ update(state, aff, clip_path, flags) -> 'IDL:Bonobo/Canvas/ArtUTA:1.0', x1, y1, x2, y2 """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __slots__ = ()
    __typecode__ = None # (!) real value is ''


class ComponentProxy(__CORBA.Object):
    # no doc
    def getUIContainer(self): # real signature unknown; restored from __doc__
        """ getUIContainer() -> 'IDL:Bonobo/UIContainer:1.0' """
        pass

    def grabFocus(self, mask, cursor, time): # real signature unknown; restored from __doc__
        """ grabFocus(mask, cursor, time) -> 'IDL:omg.org/CORBA/void:1.0' """
        pass

    def requestUpdate(self): # real signature unknown; restored from __doc__
        """ requestUpdate() -> 'IDL:omg.org/CORBA/void:1.0' """
        pass

    def ungrabFocus(self, time): # real signature unknown; restored from __doc__
        """ ungrabFocus(time) -> 'IDL:omg.org/CORBA/void:1.0' """
        pass

    def unImplemented1(self): # real signature unknown; restored from __doc__
        """ unImplemented1() -> 'IDL:omg.org/CORBA/void:1.0' """
        pass

    def unImplemented2(self): # real signature unknown; restored from __doc__
        """ unImplemented2() -> 'IDL:omg.org/CORBA/void:1.0' """
        pass

    def unImplemented3(self): # real signature unknown; restored from __doc__
        """ unImplemented3() -> 'IDL:omg.org/CORBA/void:1.0' """
        pass

    def unImplemented4(self): # real signature unknown; restored from __doc__
        """ unImplemented4() -> 'IDL:omg.org/CORBA/void:1.0' """
        pass

    def unImplemented5(self): # real signature unknown; restored from __doc__
        """ unImplemented5() -> 'IDL:omg.org/CORBA/void:1.0' """
        pass

    def unImplemented6(self): # real signature unknown; restored from __doc__
        """ unImplemented6() -> 'IDL:omg.org/CORBA/void:1.0' """
        pass

    def unImplemented7(self): # real signature unknown; restored from __doc__
        """ unImplemented7() -> 'IDL:omg.org/CORBA/void:1.0' """
        pass

    def unImplemented8(self): # real signature unknown; restored from __doc__
        """ unImplemented8() -> 'IDL:omg.org/CORBA/void:1.0' """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __slots__ = ()
    __typecode__ = None # (!) real value is ''


class DRect(__CORBA.Struct):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __typecode__ = None # (!) real value is ''


class IRect(__CORBA.Struct):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __typecode__ = None # (!) real value is ''


class Point(__CORBA.Struct):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __typecode__ = None # (!) real value is ''


class State(__CORBA.Struct):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __typecode__ = None # (!) real value is ''


class SVPSegment(__CORBA.Struct):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __typecode__ = None # (!) real value is ''


