# encoding: utf-8
# module PortableServer calls itself ORBit.PortableServer
# from /usr/lib64/python2.6/site-packages/gtk-2.0/gnomevfs/gnomevfsbonobo.so
# by generator 1.136
# no doc

# imports
from ORBit import ObjectAdaptor

import ORBit as __ORBit


# Variables with simple values

MAIN_THREAD_MODEL = 2

ORB_CTRL_MODEL = 0

SINGLE_THREAD_MODEL = 1

# no functions
# classes

class POA(__ORBit.ObjectAdaptor):
    # no doc
    def activate_object(self, *args, **kwargs): # real signature unknown
        pass

    def activate_object_with_id(self, *args, **kwargs): # real signature unknown
        pass

    def create_POA(self, *args, **kwargs): # real signature unknown
        pass

    def create_thread_policy(self, *args, **kwargs): # real signature unknown
        pass

    def deactivate_object(self, *args, **kwargs): # real signature unknown
        pass

    def reference_to_id(self, *args, **kwargs): # real signature unknown
        pass

    def servant_to_id(self, *args, **kwargs): # real signature unknown
        pass

    def servant_to_reference(self, *args, **kwargs): # real signature unknown
        pass

    def _get_the_POAManager(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    the_POAManager = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class POAManager(object):
    # no doc
    def activate(self, *args, **kwargs): # real signature unknown
        pass

    def deactivate(self, *args, **kwargs): # real signature unknown
        pass

    def discard_requests(self, *args, **kwargs): # real signature unknown
        pass

    def get_state(self, *args, **kwargs): # real signature unknown
        pass

    def hold_requests(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class Servant(object):
    # no doc
    def _default_POA(self, *args, **kwargs): # real signature unknown
        pass

    def _this(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    _delegate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """delegate object"""



