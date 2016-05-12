# encoding: utf-8
# module gst._gst
# from /usr/lib64/python2.6/site-packages/gst-0.10/gst/_gst.so
# by generator 1.136
# no doc

# imports
import gobject as __gobject
import gobject._gobject as __gobject__gobject
import gst as __gst


class Pad(__gst.Object):
    """
    Object GstPad
    
    Signals from GstPad:
      linked (GstPad)
      unlinked (GstPad)
      request-link ()
      have-data (GstMiniObject) -> gboolean
    
    Properties from GstPad:
      caps -> GstCaps: Caps
        The capabilities of the pad
      direction -> GstPadDirection: Direction
        The direction of the pad
      template -> GstPadTemplate: Template
        The GstPadTemplate of this pad
    
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
    def accept_caps(self, *args, **kwargs): # real signature unknown
        pass

    def activate_pull(self, *args, **kwargs): # real signature unknown
        pass

    def activate_push(self, *args, **kwargs): # real signature unknown
        pass

    def add_buffer_probe(self, *args, **kwargs): # real signature unknown
        pass

    def add_data_probe(self, *args, **kwargs): # real signature unknown
        pass

    def add_event_probe(self, *args, **kwargs): # real signature unknown
        pass

    def alloc_buffer(self, *args, **kwargs): # real signature unknown
        pass

    def alloc_buffer_and_set_caps(self, *args, **kwargs): # real signature unknown
        pass

    def can_link(self, *args, **kwargs): # real signature unknown
        pass

    def chain(self, *args, **kwargs): # real signature unknown
        pass

    def chain_list(self, *args, **kwargs): # real signature unknown
        pass

    def check_pull_range(self, *args, **kwargs): # real signature unknown
        pass

    def event_default(self, *args, **kwargs): # real signature unknown
        pass

    def fixate_caps(self, *args, **kwargs): # real signature unknown
        pass

    def get_allowed_caps(self, *args, **kwargs): # real signature unknown
        pass

    def get_caps(self, *args, **kwargs): # real signature unknown
        pass

    def get_direction(self, *args, **kwargs): # real signature unknown
        pass

    def get_fixed_caps_func(self, *args, **kwargs): # real signature unknown
        pass

    def get_internal_links(self, *args, **kwargs): # real signature unknown
        pass

    def get_internal_links_default(self, *args, **kwargs): # real signature unknown
        pass

    def get_negotiated_caps(self, *args, **kwargs): # real signature unknown
        pass

    def get_pad_template(self, *args, **kwargs): # real signature unknown
        pass

    def get_pad_template_caps(self, *args, **kwargs): # real signature unknown
        pass

    def get_parent_element(self, *args, **kwargs): # real signature unknown
        pass

    def get_peer(self, *args, **kwargs): # real signature unknown
        pass

    def get_query_types(self, *args, **kwargs): # real signature unknown
        pass

    def get_query_types_default(self, *args, **kwargs): # real signature unknown
        pass

    def get_range(self, *args, **kwargs): # real signature unknown
        pass

    def is_active(self, *args, **kwargs): # real signature unknown
        pass

    def is_blocked(self, *args, **kwargs): # real signature unknown
        pass

    def is_linked(self, *args, **kwargs): # real signature unknown
        pass

    def iterate_internal_links(self, *args, **kwargs): # real signature unknown
        pass

    def iterate_internal_links_default(self, *args, **kwargs): # real signature unknown
        pass

    def link(self, *args, **kwargs): # real signature unknown
        pass

    def pause_task(self, *args, **kwargs): # real signature unknown
        pass

    def peer_accept_caps(self, *args, **kwargs): # real signature unknown
        pass

    def peer_get_caps(self, *args, **kwargs): # real signature unknown
        pass

    def peer_query(self, *args, **kwargs): # real signature unknown
        pass

    def proxy_getcaps(self, *args, **kwargs): # real signature unknown
        pass

    def proxy_setcaps(self, *args, **kwargs): # real signature unknown
        pass

    def pull_range(self, *args, **kwargs): # real signature unknown
        pass

    def push(self, *args, **kwargs): # real signature unknown
        pass

    def push_event(self, *args, **kwargs): # real signature unknown
        pass

    def push_list(self, *args, **kwargs): # real signature unknown
        pass

    def query(self, *args, **kwargs): # real signature unknown
        pass

    def query_convert(self, *args, **kwargs): # real signature unknown
        pass

    def query_default(self, *args, **kwargs): # real signature unknown
        pass

    def query_duration(self, *args, **kwargs): # real signature unknown
        pass

    def query_peer_convert(self, *args, **kwargs): # real signature unknown
        pass

    def query_peer_duration(self, *args, **kwargs): # real signature unknown
        pass

    def query_peer_position(self, *args, **kwargs): # real signature unknown
        pass

    def query_position(self, *args, **kwargs): # real signature unknown
        pass

    def remove_buffer_probe(self, *args, **kwargs): # real signature unknown
        pass

    def remove_data_probe(self, *args, **kwargs): # real signature unknown
        pass

    def remove_event_probe(self, *args, **kwargs): # real signature unknown
        pass

    def send_event(self, *args, **kwargs): # real signature unknown
        pass

    def set_activatepull_function(self, *args, **kwargs): # real signature unknown
        pass

    def set_activatepush_function(self, *args, **kwargs): # real signature unknown
        pass

    def set_activate_function(self, *args, **kwargs): # real signature unknown
        pass

    def set_active(self, *args, **kwargs): # real signature unknown
        pass

    def set_blocked(self, *args, **kwargs): # real signature unknown
        pass

    def set_blocked_async(self, *args, **kwargs): # real signature unknown
        pass

    def set_caps(self, *args, **kwargs): # real signature unknown
        pass

    def set_chain_function(self, *args, **kwargs): # real signature unknown
        pass

    def set_event_function(self, *args, **kwargs): # real signature unknown
        pass

    def set_getcaps_function(self, *args, **kwargs): # real signature unknown
        pass

    def set_link_function(self, *args, **kwargs): # real signature unknown
        pass

    def set_query_function(self, *args, **kwargs): # real signature unknown
        pass

    def set_setcaps_function(self, *args, **kwargs): # real signature unknown
        pass

    def start_task(self, *args, **kwargs): # real signature unknown
        pass

    def stop_task(self, *args, **kwargs): # real signature unknown
        pass

    def unlink(self, *args, **kwargs): # real signature unknown
        pass

    def use_fixed_caps(self, *args, **kwargs): # real signature unknown
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


