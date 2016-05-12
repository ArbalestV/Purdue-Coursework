# encoding: utf-8
# module gst._gst
# from /usr/lib64/python2.6/site-packages/gst-0.10/gst/_gst.so
# by generator 1.136
# no doc

# imports
import gobject as __gobject
import gobject._gobject as __gobject__gobject
import gst as __gst


class Bus(__gst.Object):
    """
    Object GstBus
    
    Signals from GstBus:
      message (GstMessage)
      sync-message (GstMessage)
    
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
    def add_signal_watch(self, *args, **kwargs): # real signature unknown
        pass

    def add_signal_watch_full(self, *args, **kwargs): # real signature unknown
        pass

    def add_watch(self, *args, **kwargs): # real signature unknown
        pass

    def disable_sync_message_emission(self, *args, **kwargs): # real signature unknown
        pass

    def enable_sync_message_emission(self, *args, **kwargs): # real signature unknown
        pass

    def have_pending(self, *args, **kwargs): # real signature unknown
        pass

    def peek(self, *args, **kwargs): # real signature unknown
        pass

    def poll(self, *args, **kwargs): # real signature unknown
        pass

    def pop(self, *args, **kwargs): # real signature unknown
        pass

    def pop_filtered(self, *args, **kwargs): # real signature unknown
        pass

    def post(self, *args, **kwargs): # real signature unknown
        pass

    def remove_signal_watch(self, *args, **kwargs): # real signature unknown
        pass

    def set_flushing(self, *args, **kwargs): # real signature unknown
        pass

    def set_sync_handler(self, *args, **kwargs): # real signature unknown
        pass

    def timed_pop(self, *args, **kwargs): # real signature unknown
        pass

    def timed_pop_filtered(self, *args, **kwargs): # real signature unknown
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


