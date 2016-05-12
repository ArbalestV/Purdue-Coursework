# encoding: utf-8
# module gst._gst
# from /usr/lib64/python2.6/site-packages/gst-0.10/gst/_gst.so
# by generator 1.136
# no doc

# imports
import gobject as __gobject
import gobject._gobject as __gobject__gobject
import gst as __gst


class Bin(__gst.Element, __gst.__main__.GstChildProxy):
    """
    Object GstBin
    
    Signals from GstBin:
      element-added (GstElement)
      element-removed (GstElement)
      do-latency () -> gboolean
    
    Properties from GstBin:
      async-handling -> gboolean: Async Handling
        The bin will handle Asynchronous state changes
    
    Signals from GstChildProxy:
      child-added (GObject)
      child-removed (GObject)
    
    Signals from GstElement:
      pad-added (GstPad)
      pad-removed (GstPad)
      no-more-pads ()
    
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
    def add(self, *args, **kwargs): # real signature unknown
        pass

    def add_many(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_add_element(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_handle_message(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_remove_element(cls, *args, **kwargs): # real signature unknown
        pass

    def elements(self, *args, **kwargs): # real signature unknown
        pass

    def find_unconnected_pad(self, *args, **kwargs): # real signature unknown
        pass

    def find_unlinked_pad(self, *args, **kwargs): # real signature unknown
        pass

    def get_by_interface(self, *args, **kwargs): # real signature unknown
        pass

    def get_by_name(self, *args, **kwargs): # real signature unknown
        pass

    def iterate_all_by_interface(self, *args, **kwargs): # real signature unknown
        pass

    def iterate_sources(self, *args, **kwargs): # real signature unknown
        pass

    def recalculate_latency(self, *args, **kwargs): # real signature unknown
        pass

    def recurse(self, *args, **kwargs): # real signature unknown
        pass

    def remove(self, *args, **kwargs): # real signature unknown
        pass

    def remove_many(self, *args, **kwargs): # real signature unknown
        pass

    def sinks(self, *args, **kwargs): # real signature unknown
        pass

    def sorted(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self): # real signature unknown; restored from __doc__
        """ x.__iter__() <==> iter(x) """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    __gtype__ = None # (!) real value is ''


