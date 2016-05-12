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


class NativeVolumeMonitor(__gio.VolumeMonitor):
    """
    Object GNativeVolumeMonitor
    
    Signals from GVolumeMonitor:
      volume-added (GVolume)
      volume-removed (GVolume)
      volume-changed (GVolume)
      mount-added (GMount)
      mount-removed (GMount)
      mount-pre-unmount (GMount)
      mount-changed (GMount)
      drive-connected (GDrive)
      drive-disconnected (GDrive)
      drive-changed (GDrive)
      drive-eject-button (GDrive)
      drive-stop-button (GDrive)
    
    Signals from GObject:
      notify (GParam)
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


