# encoding: utf-8
# module gst._gst
# from /usr/lib64/python2.6/site-packages/gst-0.10/gst/_gst.so
# by generator 1.136
# no doc

# imports
import gobject as __gobject
import gobject._gobject as __gobject__gobject
import gst as __gst


class BaseSrc(__gst.Element):
    """
    Object GstBaseSrc
    
    Properties from GstBaseSrc:
      blocksize -> gulong: Block size
        Size in bytes to read per buffer (-1 = default)
      num-buffers -> gint: num-buffers
        Number of buffers to output before sending EOS (-1 = unlimited)
      typefind -> gboolean: Typefind
        Run typefind before negotiating
      do-timestamp -> gboolean: Do timestamp
        Apply current stream time to buffers
    
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
    def do_check_get_range(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_create(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_do_seek(cls, *args, **kwargs): # real signature unknown
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
    def do_get_size(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_get_times(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_is_seekable(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_negotiate(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_newsegment(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_prepare_seek_segment(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_query(cls, *args, **kwargs): # real signature unknown
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

    def get_do_timestamp(self, *args, **kwargs): # real signature unknown
        pass

    def is_live(self, *args, **kwargs): # real signature unknown
        pass

    def query_latency(self, *args, **kwargs): # real signature unknown
        pass

    def set_do_timestamp(self, *args, **kwargs): # real signature unknown
        pass

    def set_format(self, *args, **kwargs): # real signature unknown
        pass

    def set_live(self, *args, **kwargs): # real signature unknown
        pass

    def wait_playing(self, *args, **kwargs): # real signature unknown
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


