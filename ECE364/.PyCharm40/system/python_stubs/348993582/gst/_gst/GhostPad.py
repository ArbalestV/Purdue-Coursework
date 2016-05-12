# encoding: utf-8
# module gst._gst
# from /usr/lib64/python2.6/site-packages/gst-0.10/gst/_gst.so
# by generator 1.136
# no doc

# imports
import gobject as __gobject
import gobject._gobject as __gobject__gobject
import gst as __gst


class GhostPad(__gst.Pad):
    """
    Object GstGhostPad
    
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
    def get_target(self, *args, **kwargs): # real signature unknown
        pass

    def set_target(self, *args, **kwargs): # real signature unknown
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


