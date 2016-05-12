# encoding: utf-8
# module gst._gst
# from /usr/lib64/python2.6/site-packages/gst-0.10/gst/_gst.so
# by generator 1.136
# no doc

# imports
import gobject as __gobject
import gobject._gobject as __gobject__gobject
import gst as __gst


class Registry(__gst.Object):
    """
    Object GstRegistry
    
    Signals from GstRegistry:
      plugin-added (gpointer)
      feature-added (gpointer)
    
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
    def add_feature(self, *args, **kwargs): # real signature unknown
        pass

    def add_path(self, *args, **kwargs): # real signature unknown
        pass

    def add_plugin(self, *args, **kwargs): # real signature unknown
        pass

    def find_feature(self, *args, **kwargs): # real signature unknown
        pass

    def find_plugin(self, *args, **kwargs): # real signature unknown
        pass

    def get_feature_list(self, *args, **kwargs): # real signature unknown
        pass

    def get_feature_list_by_plugin(self, *args, **kwargs): # real signature unknown
        pass

    def get_path_list(self, *args, **kwargs): # real signature unknown
        pass

    def get_plugin_list(self, *args, **kwargs): # real signature unknown
        pass

    def lookup(self, *args, **kwargs): # real signature unknown
        pass

    def lookup_feature(self, *args, **kwargs): # real signature unknown
        pass

    def remove_feature(self, *args, **kwargs): # real signature unknown
        pass

    def remove_plugin(self, *args, **kwargs): # real signature unknown
        pass

    def scan_path(self, *args, **kwargs): # real signature unknown
        pass

    def xml_read_cache(self, *args, **kwargs): # real signature unknown
        pass

    def xml_write_cache(self, *args, **kwargs): # real signature unknown
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


