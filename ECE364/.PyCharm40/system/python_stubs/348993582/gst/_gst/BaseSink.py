# encoding: utf-8
# module gst._gst
# from /usr/lib64/python2.6/site-packages/gst-0.10/gst/_gst.so
# by generator 1.136
# no doc

# imports
import gobject as __gobject
import gobject._gobject as __gobject__gobject
import gst as __gst


class BaseSink(__gst.Element):
    """
    Object GstBaseSink
    
    Properties from GstBaseSink:
      preroll-queue-len -> guint: Preroll queue length
        Number of buffers to queue during preroll
      sync -> gboolean: Sync
        Sync on the clock
      max-lateness -> gint64: Max Lateness
        Maximum number of nanoseconds that a buffer can be late before it is dropped (-1 unlimited)
      qos -> gboolean: Qos
        Generate Quality-of-Service events upstream
      async -> gboolean: Async
        Go asynchronously to PAUSED
      ts-offset -> gint64: TS Offset
        Timestamp offset in nanoseconds
      last-buffer -> GstBuffer: Last Buffer
        The last buffer received in the sink
      blocksize -> guint: Block size
        Size in bytes to pull per buffer (0 = default)
      render-delay -> guint64: Render Delay
        Additional render delay of the sink in nanoseconds
    
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
    @classmethod
    def do_activate_pull(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_event(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_fixate(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_get_caps(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_get_times(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_preroll(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_render(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_set_caps(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_start(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_stop(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_unlock(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_unlock_stop(cls, *args, **kwargs): # real signature unknown
        pass

    def get_last_buffer(self, *args, **kwargs): # real signature unknown
        pass

    def get_latency(self, *args, **kwargs): # real signature unknown
        pass

    def get_max_lateness(self, *args, **kwargs): # real signature unknown
        pass

    def get_sync(self, *args, **kwargs): # real signature unknown
        pass

    def get_ts_offset(self, *args, **kwargs): # real signature unknown
        pass

    def is_async_enabled(self, *args, **kwargs): # real signature unknown
        pass

    def is_qos_enabled(self, *args, **kwargs): # real signature unknown
        pass

    def query_latency(self, *args, **kwargs): # real signature unknown
        pass

    def set_async_enabled(self, *args, **kwargs): # real signature unknown
        pass

    def set_max_lateness(self, *args, **kwargs): # real signature unknown
        pass

    def set_qos_enabled(self, *args, **kwargs): # real signature unknown
        pass

    def set_sync(self, *args, **kwargs): # real signature unknown
        pass

    def set_ts_offset(self, *args, **kwargs): # real signature unknown
        pass

    def wait_preroll(self, *args, **kwargs): # real signature unknown
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


