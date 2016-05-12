# encoding: utf-8
# module gst._gst
# from /usr/lib64/python2.6/site-packages/gst-0.10/gst/_gst.so
# by generator 1.136
# no doc

# imports
import gobject as __gobject
import gobject._gobject as __gobject__gobject
import gst as __gst


class Clock(__gst.Object):
    """
    Object GstClock
    
    Properties from GstClock:
      stats -> gboolean: Stats
        Enable clock stats (unimplemented)
      window-size -> gint: Window size
        The size of the window used to calculate rate and offset
      window-threshold -> gint: Window threshold
        The threshold to start calculating rate and offset
      timeout -> guint64: Timeout
        The amount of time, in nanoseconds, to sample master and slave clocks
    
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
    def add_observation(self, *args, **kwargs): # real signature unknown
        pass

    def adjust_unlocked(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_change_resolution(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_get_internal_time(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_get_resolution(cls, *args, **kwargs): # real signature unknown
        pass

    def get_calibration(self, *args, **kwargs): # real signature unknown
        pass

    def get_internal_time(self, *args, **kwargs): # real signature unknown
        pass

    def get_master(self, *args, **kwargs): # real signature unknown
        pass

    def get_resolution(self, *args, **kwargs): # real signature unknown
        pass

    def get_time(self, *args, **kwargs): # real signature unknown
        pass

    def new_periodic_id(self, *args, **kwargs): # real signature unknown
        pass

    def new_single_shot_id(self, *args, **kwargs): # real signature unknown
        pass

    def set_calibration(self, *args, **kwargs): # real signature unknown
        pass

    def set_master(self, *args, **kwargs): # real signature unknown
        pass

    def set_resolution(self, *args, **kwargs): # real signature unknown
        pass

    def unadjust_unlocked(self, *args, **kwargs): # real signature unknown
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


