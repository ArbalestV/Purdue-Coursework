# encoding: utf-8
# module gst._gst
# from /usr/lib64/python2.6/site-packages/gst-0.10/gst/_gst.so
# by generator 1.136
# no doc

# imports
import gobject as __gobject
import gobject._gobject as __gobject__gobject
import gst as __gst


class Index(__gst.Object):
    """
    Object GstIndex
    
    Signals from GstIndex:
      entry-added (GstIndexEntry)
    
    Properties from GstIndex:
      resolver -> GstIndexResolver: Resolver
        Select a predefined object to string mapper
    
    Signals from GstObject:
      parent-set (GstObject)
      parent-unset (GstObject)
      object-saved (gpointer)
      deep-notify (GstObject, GParam)
    
    Properties from GstObject:
      name -> gchararray: Name
        The name of the object
    
    Signals from GObject:
      notify (GParam)
    """
    def add_format(self, *args, **kwargs): # real signature unknown
        pass

    def add_id(self, *args, **kwargs): # real signature unknown
        pass

    def commit(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_add_entry(cls, *args, **kwargs): # real signature unknown
        pass

    def get_assoc_entry(self, *args, **kwargs): # real signature unknown
        pass

    def get_certainty(self, *args, **kwargs): # real signature unknown
        pass

    def get_group(self, *args, **kwargs): # real signature unknown
        pass

    def new_group(self, *args, **kwargs): # real signature unknown
        pass

    def set_certainty(self, *args, **kwargs): # real signature unknown
        pass

    def set_group(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    __gtype__ = None # (!) real value is ''


