# encoding: utf-8
# module gst._gst
# from /usr/lib64/python2.6/site-packages/gst-0.10/gst/_gst.so
# by generator 1.136
# no doc

# imports
import gobject as __gobject
import gobject._gobject as __gobject__gobject
import gst as __gst


class Element(__gst.Object):
    """
    Object GstElement
    
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
    def abort_state(self, *args, **kwargs): # real signature unknown
        pass

    def add_pad(self, *args, **kwargs): # real signature unknown
        pass

    def change_state(self, *args, **kwargs): # real signature unknown
        pass

    def continue_state(self, *args, **kwargs): # real signature unknown
        pass

    def create_all_pads(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_change_state(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_get_index(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_provide_clock(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_query(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_release_pad(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_request_new_pad(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_send_event(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_set_bus(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_set_clock(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_set_index(cls, *args, **kwargs): # real signature unknown
        pass

    def flags(self, *args, **kwargs): # real signature unknown
        pass

    def found_tags(self, *args, **kwargs): # real signature unknown
        pass

    def found_tags_for_pad(self, *args, **kwargs): # real signature unknown
        pass

    def get_base_time(self, *args, **kwargs): # real signature unknown
        pass

    def get_bus(self, *args, **kwargs): # real signature unknown
        pass

    def get_clock(self, *args, **kwargs): # real signature unknown
        pass

    def get_compatible_pad(self, *args, **kwargs): # real signature unknown
        pass

    def get_compatible_pad_template(self, *args, **kwargs): # real signature unknown
        pass

    def get_factory(self, *args, **kwargs): # real signature unknown
        pass

    def get_index(self, *args, **kwargs): # real signature unknown
        pass

    def get_pad(self, *args, **kwargs): # real signature unknown
        pass

    def get_pad_template(self, *args, **kwargs): # real signature unknown
        pass

    def get_pad_template_list(self, *args, **kwargs): # real signature unknown
        pass

    def get_query_types(self, *args, **kwargs): # real signature unknown
        pass

    def get_request_pad(self, *args, **kwargs): # real signature unknown
        pass

    def get_start_time(self, *args, **kwargs): # real signature unknown
        pass

    def get_state(self, *args, **kwargs): # real signature unknown
        pass

    def get_static_pad(self, *args, **kwargs): # real signature unknown
        pass

    def implements_interface(self, *args, **kwargs): # real signature unknown
        pass

    def is_indexable(self, *args, **kwargs): # real signature unknown
        pass

    def is_locked_state(self, *args, **kwargs): # real signature unknown
        pass

    def link(self, *args, **kwargs): # real signature unknown
        pass

    def link_filtered(self, *args, **kwargs): # real signature unknown
        pass

    def link_pads(self, *args, **kwargs): # real signature unknown
        pass

    def link_pads_filtered(self, *args, **kwargs): # real signature unknown
        pass

    def lost_state(self, *args, **kwargs): # real signature unknown
        pass

    def lost_state_full(self, *args, **kwargs): # real signature unknown
        pass

    def no_more_pads(self, *args, **kwargs): # real signature unknown
        pass

    def pads(self, *args, **kwargs): # real signature unknown
        pass

    def post_message(self, *args, **kwargs): # real signature unknown
        pass

    def provides_clock(self, *args, **kwargs): # real signature unknown
        pass

    def provide_clock(self, *args, **kwargs): # real signature unknown
        pass

    def query(self, *args, **kwargs): # real signature unknown
        pass

    def query_convert(self, *args, **kwargs): # real signature unknown
        pass

    def query_duration(self, *args, **kwargs): # real signature unknown
        pass

    def query_position(self, *args, **kwargs): # real signature unknown
        pass

    def release_request_pad(self, *args, **kwargs): # real signature unknown
        pass

    def remove_pad(self, *args, **kwargs): # real signature unknown
        pass

    def requires_clock(self, *args, **kwargs): # real signature unknown
        pass

    def seek(self, *args, **kwargs): # real signature unknown
        pass

    def seek_simple(self, *args, **kwargs): # real signature unknown
        pass

    def send_event(self, *args, **kwargs): # real signature unknown
        pass

    def set_base_time(self, *args, **kwargs): # real signature unknown
        pass

    def set_bus(self, *args, **kwargs): # real signature unknown
        pass

    def set_clock(self, *args, **kwargs): # real signature unknown
        pass

    def set_index(self, *args, **kwargs): # real signature unknown
        pass

    def set_locked_state(self, *args, **kwargs): # real signature unknown
        pass

    def set_start_time(self, *args, **kwargs): # real signature unknown
        pass

    def set_state(self, *args, **kwargs): # real signature unknown
        pass

    def sink_pads(self, *args, **kwargs): # real signature unknown
        pass

    def src_pads(self, *args, **kwargs): # real signature unknown
        pass

    def sync_state_with_parent(self, *args, **kwargs): # real signature unknown
        pass

    def unlink(self, *args, **kwargs): # real signature unknown
        pass

    def unlink_pads(self, *args, **kwargs): # real signature unknown
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


