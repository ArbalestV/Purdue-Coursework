# encoding: utf-8
# module lxml.etree
# from /usr/lib64/python2.6/site-packages/lxml/etree.so
# by generator 1.136
"""
The ``lxml.etree`` module implements the extended ElementTree API
for XML.
"""

# imports
import __builtin__ as __builtins__ # <module '__builtin__' (built-in)>

from _ProcessingInstruction import _ProcessingInstruction

class PIBase(_ProcessingInstruction):
    """
    All custom Processing Instruction classes must inherit from this one.
    
        Note that you cannot (and must not) instantiate this class or its
        subclasses.
    
        Subclasses *must not* override __init__ or __new__ as it is
        absolutely undefined when these objects will be created or
        destroyed.  All persistent state of PIs must be stored in the
        underlying XML.  If you really need to initialize the object after
        creation, you can implement an ``_init(self)`` method that will be
        called after object creation.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    __pyx_vtable__ = None # (!) real value is ''


