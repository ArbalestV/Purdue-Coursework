# encoding: utf-8
# module gst._gst
# from /usr/lib64/python2.6/site-packages/gst-0.10/gst/_gst.so
# by generator 1.136
# no doc

# imports
import gobject as __gobject
import gobject._gobject as __gobject__gobject
import gst as __gst


class Message(__gst.MiniObject):
    # no doc
    def parse_async_start(self, *args, **kwargs): # real signature unknown
        pass

    def parse_buffering(self, *args, **kwargs): # real signature unknown
        pass

    def parse_buffering_stats(self, *args, **kwargs): # real signature unknown
        pass

    def parse_clock_lost(self, *args, **kwargs): # real signature unknown
        pass

    def parse_clock_provide(self, *args, **kwargs): # real signature unknown
        pass

    def parse_duration(self, *args, **kwargs): # real signature unknown
        pass

    def parse_error(self, *args, **kwargs): # real signature unknown
        pass

    def parse_info(self, *args, **kwargs): # real signature unknown
        pass

    def parse_new_clock(self, *args, **kwargs): # real signature unknown
        pass

    def parse_request_state(self, *args, **kwargs): # real signature unknown
        pass

    def parse_segment_done(self, *args, **kwargs): # real signature unknown
        pass

    def parse_segment_start(self, *args, **kwargs): # real signature unknown
        pass

    def parse_state_changed(self, *args, **kwargs): # real signature unknown
        pass

    def parse_step_done(self, *args, **kwargs): # real signature unknown
        pass

    def parse_step_start(self, *args, **kwargs): # real signature unknown
        pass

    def parse_stream_status(self, *args, **kwargs): # real signature unknown
        pass

    def parse_structure_change(self, *args, **kwargs): # real signature unknown
        pass

    def parse_tag(self, *args, **kwargs): # real signature unknown
        pass

    def parse_tag_full(self, *args, **kwargs): # real signature unknown
        pass

    def parse_warning(self, *args, **kwargs): # real signature unknown
        pass

    def set_buffering_stats(self, *args, **kwargs): # real signature unknown
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

    structure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    timestamp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __gtype__ = None # (!) real value is ''


