# encoding: utf-8
# module gst._gst
# from /usr/lib64/python2.6/site-packages/gst-0.10/gst/_gst.so
# by generator 1.136
# no doc

# imports
import gobject as __gobject
import gobject._gobject as __gobject__gobject
import gst as __gst


class ElementFactory(__gst.PluginFeature):
    """
    Object GstElementFactory
    
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
    def can_sink_caps(self, *args, **kwargs): # real signature unknown
        pass

    def can_src_caps(self, *args, **kwargs): # real signature unknown
        pass

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def get_author(self, *args, **kwargs): # real signature unknown
        pass

    def get_description(self, *args, **kwargs): # real signature unknown
        pass

    def get_element_type(self, *args, **kwargs): # real signature unknown
        pass

    def get_klass(self, *args, **kwargs): # real signature unknown
        pass

    def get_longname(self, *args, **kwargs): # real signature unknown
        pass

    def get_num_pad_templates(self, *args, **kwargs): # real signature unknown
        pass

    def get_static_pad_templates(self, *args, **kwargs): # real signature unknown
        pass

    def get_uri_protocols(self, *args, **kwargs): # real signature unknown
        pass

    def get_uri_type(self, *args, **kwargs): # real signature unknown
        pass

    def has_interface(self, *args, **kwargs): # real signature unknown
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


