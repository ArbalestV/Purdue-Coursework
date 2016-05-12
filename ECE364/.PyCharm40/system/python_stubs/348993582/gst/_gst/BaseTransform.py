# encoding: utf-8
# module gst._gst
# from /usr/lib64/python2.6/site-packages/gst-0.10/gst/_gst.so
# by generator 1.136
# no doc

# imports
import gobject as __gobject
import gobject._gobject as __gobject__gobject
import gst as __gst


class BaseTransform(__gst.Element):
    """
    Object GstBaseTransform
    
    Properties from GstBaseTransform:
      qos -> gboolean: QoS
        Handle Quality-of-Service events
    
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
    def do_event(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_fixate_caps(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_get_unit_size(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_set_caps(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_src_event(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_start(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_stop(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_transform(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_transform_caps(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_transform_ip(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_transform_size(cls, *args, **kwargs): # real signature unknown
        pass

    def is_in_place(self, *args, **kwargs): # real signature unknown
        pass

    def is_passthrough(self, *args, **kwargs): # real signature unknown
        pass

    def is_qos_enabled(self, *args, **kwargs): # real signature unknown
        pass

    def reconfigure(self, *args, **kwargs): # real signature unknown
        pass

    def set_gap_aware(self, *args, **kwargs): # real signature unknown
        pass

    def set_in_place(self, *args, **kwargs): # real signature unknown
        pass

    def set_passthrough(self, *args, **kwargs): # real signature unknown
        pass

    def set_qos_enabled(self, *args, **kwargs): # real signature unknown
        pass

    def suggest(self, *args, **kwargs): # real signature unknown
        pass

    def update_qos(self, *args, **kwargs): # real signature unknown
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


