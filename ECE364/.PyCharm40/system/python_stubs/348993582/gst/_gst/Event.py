# encoding: utf-8
# module gst._gst
# from /usr/lib64/python2.6/site-packages/gst-0.10/gst/_gst.so
# by generator 1.136
# no doc

# imports
import gobject as __gobject
import gobject._gobject as __gobject__gobject
import gst as __gst


class Event(__gst.MiniObject):
    # no doc
    def get_seqnum(self, *args, **kwargs): # real signature unknown
        pass

    def get_structure(self, *args, **kwargs): # real signature unknown
        pass

    def has_name(self, *args, **kwargs): # real signature unknown
        pass

    def parse_buffer_size(self, *args, **kwargs): # real signature unknown
        pass

    def parse_latency(self, *args, **kwargs): # real signature unknown
        pass

    def parse_new_segment(self, *args, **kwargs): # real signature unknown
        pass

    def parse_new_segment_full(self, *args, **kwargs): # real signature unknown
        pass

    def parse_qos(self, *args, **kwargs): # real signature unknown
        pass

    def parse_seek(self, *args, **kwargs): # real signature unknown
        pass

    def parse_step(self, *args, **kwargs): # real signature unknown
        pass

    def parse_tag(self, *args, **kwargs): # real signature unknown
        pass

    def set_seqnum(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    src = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    timestamp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __gtype__ = None # (!) real value is ''


