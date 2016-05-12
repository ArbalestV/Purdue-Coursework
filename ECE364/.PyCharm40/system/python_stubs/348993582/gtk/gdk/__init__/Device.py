# encoding: utf-8
# module gtk.gdk
# from /usr/lib64/python2.6/site-packages/gtk-2.0/wnck.so
# by generator 1.136
# no doc

# imports
from exceptions import Warning

import gio as __gio
import gobject as __gobject
import gobject._gobject as __gobject__gobject
import pango as __pango
import pangocairo as __pangocairo


class Device(__gobject__gobject.GObject):
    """
    Object GdkDevice
    
    Signals from GObject:
      notify (GParam)
    """
    def get_axis(self, *args, **kwargs): # real signature unknown
        pass

    def get_history(self, *args, **kwargs): # real signature unknown
        pass

    def get_state(self, *args, **kwargs): # real signature unknown
        pass

    def set_axis_use(self, *args, **kwargs): # real signature unknown
        pass

    def set_key(self, *args, **kwargs): # real signature unknown
        pass

    def set_mode(self, *args, **kwargs): # real signature unknown
        pass

    def set_source(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    axes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    has_cursor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    keys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    num_axes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    num_keys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    source = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __gtype__ = None # (!) real value is ''


