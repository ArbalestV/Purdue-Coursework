# encoding: utf-8
# module gnomevfs._gnomevfs
# from /usr/lib64/python2.6/site-packages/gtk-2.0/gnomevfs/_gnomevfs.so
# by generator 1.136
# no doc

# imports
import gnomevfs.async as async # <module 'gnomevfs.async' (built-in)>
import gnomevfs as __gnomevfs
import gobject._gobject as __gobject__gobject


class VolumeMonitor(__gobject__gobject.GObject):
    """
    Object GnomeVFSVolumeMonitor
    
    Signals from GnomeVFSVolumeMonitor:
      volume-mounted (GnomeVFSVolume)
      volume-pre-unmount (GnomeVFSVolume)
      volume-unmounted (GnomeVFSVolume)
      drive-connected (GnomeVFSDrive)
      drive-disconnected (GnomeVFSDrive)
    
    Signals from GObject:
      notify (GParam)
    """
    def get_connected_drives(self, *args, **kwargs): # real signature unknown
        pass

    def get_drive_by_id(self, *args, **kwargs): # real signature unknown
        pass

    def get_mounted_volumes(self, *args, **kwargs): # real signature unknown
        pass

    def get_volume_by_id(self, *args, **kwargs): # real signature unknown
        pass

    def get_volume_for_path(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    __gtype__ = None # (!) real value is ''


