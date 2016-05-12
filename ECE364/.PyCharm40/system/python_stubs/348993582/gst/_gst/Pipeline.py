# encoding: utf-8
# module gst._gst
# from /usr/lib64/python2.6/site-packages/gst-0.10/gst/_gst.so
# by generator 1.136
# no doc

# imports
import gobject as __gobject
import gobject._gobject as __gobject__gobject
import gst as __gst


class Pipeline(__gst.Bin):
    """
    Object GstPipeline
    
    Properties from GstPipeline:
      delay -> guint64: Delay
        Expected delay needed for elements to spin up to PLAYING in nanoseconds
      auto-flush-bus -> gboolean: Auto Flush Bus
        Whether to automatically flush the pipeline's bus when going from READY into NULL state
    
    Signals from GstChildProxy:
      child-added (GObject)
      child-removed (GObject)
    
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
    def auto_clock(self, *args, **kwargs): # real signature unknown
        pass

    def get_auto_flush_bus(self, *args, **kwargs): # real signature unknown
        pass

    def get_bus(self, *args, **kwargs): # real signature unknown
        pass

    def get_clock(self, *args, **kwargs): # real signature unknown
        pass

    def get_delay(self, *args, **kwargs): # real signature unknown
        pass

    def get_last_stream_time(self, *args, **kwargs): # real signature unknown
        pass

    def set_auto_flush_bus(self, *args, **kwargs): # real signature unknown
        pass

    def set_clock(self, *args, **kwargs): # real signature unknown
        pass

    def set_delay(self, *args, **kwargs): # real signature unknown
        pass

    def set_new_stream_time(self, *args, **kwargs): # real signature unknown
        pass

    def use_clock(self, *args, **kwargs): # real signature unknown
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


