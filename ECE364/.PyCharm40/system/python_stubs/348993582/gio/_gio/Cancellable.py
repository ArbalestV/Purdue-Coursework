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


class Cancellable(__gobject__gobject.GObject):
    """
    Object GCancellable
    
    Signals from GCancellable:
      cancelled ()
    
    Signals from GObject:
      notify (GParam)
    """
    def cancel(self, *args, **kwargs): # real signature unknown
        pass

    def get_fd(self, *args, **kwargs): # real signature unknown
        pass

    def is_cancelled(self, *args, **kwargs): # real signature unknown
        pass

    def pop_current(self, *args, **kwargs): # real signature unknown
        pass

    def push_current(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self, *args, **kwargs): # real signature unknown
        pass

    def set_error_if_cancelled(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


