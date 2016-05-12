# encoding: utf-8
# module gio._gio
# from /usr/lib64/python2.6/site-packages/gtk-2.0/gio/_gio.so
# by generator 1.136
# no doc

# imports
import gio as __gio
import glib as __glib
import gobject as __gobject
import gobject._gobject as __gobject__gobject


class Drive(__gobject.GInterface):
    # no doc
    def can_eject(self, *args, **kwargs): # real signature unknown
        pass

    def can_poll_for_media(self, *args, **kwargs): # real signature unknown
        pass

    def eject(self, *args, **kwargs): # real signature unknown
        pass

    def eject_finish(self, *args, **kwargs): # real signature unknown
        pass

    def enumerate_identifiers(self, *args, **kwargs): # real signature unknown
        pass

    def get_icon(self, *args, **kwargs): # real signature unknown
        pass

    def get_identifier(self, *args, **kwargs): # real signature unknown
        pass

    def get_name(self, *args, **kwargs): # real signature unknown
        pass

    def get_volumes(self, *args, **kwargs): # real signature unknown
        pass

    def has_media(self, *args, **kwargs): # real signature unknown
        pass

    def has_volumes(self, *args, **kwargs): # real signature unknown
        pass

    def is_media_check_automatic(self, *args, **kwargs): # real signature unknown
        pass

    def is_media_removable(self, *args, **kwargs): # real signature unknown
        pass

    def poll_for_media(self, *args, **kwargs): # real signature unknown
        pass

    def poll_for_media_finish(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    __gtype__ = None # (!) real value is ''


