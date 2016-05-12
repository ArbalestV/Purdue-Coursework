# encoding: utf-8
# module gst._gst
# from /usr/lib64/python2.6/site-packages/gst-0.10/gst/_gst.so
# by generator 1.136
# no doc

# imports
import gobject as __gobject
import gobject._gobject as __gobject__gobject
import gst as __gst


class DataQueue(__gobject__gobject.GObject):
    """
    Object GstDataQueue
    
    Signals from GstDataQueue:
      empty ()
      full ()
    
    Properties from GstDataQueue:
      current-level-visible -> guint: Current level (visible items)
        Current number of visible items in the queue
      current-level-bytes -> guint: Current level (kB)
        Current amount of data in the queue (bytes)
      current-level-time -> guint64: Current level (ns)
        Current amount of data in the queue (in ns)
    
    Signals from GObject:
      notify (GParam)
    """
    def drop_head(self, *args, **kwargs): # real signature unknown
        pass

    def flush(self, *args, **kwargs): # real signature unknown
        pass

    def is_empty(self, *args, **kwargs): # real signature unknown
        pass

    def is_full(self, *args, **kwargs): # real signature unknown
        pass

    def limits_changed(self, *args, **kwargs): # real signature unknown
        pass

    def set_flushing(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


