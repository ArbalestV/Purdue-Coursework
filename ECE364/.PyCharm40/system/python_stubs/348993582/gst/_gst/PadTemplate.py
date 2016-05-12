# encoding: utf-8
# module gst._gst
# from /usr/lib64/python2.6/site-packages/gst-0.10/gst/_gst.so
# by generator 1.136
# no doc

# imports
import gobject as __gobject
import gobject._gobject as __gobject__gobject
import gst as __gst


class PadTemplate(__gst.Object):
    """
    Object GstPadTemplate
    
    Signals from GstPadTemplate:
      pad-created (GstPad)
    
    Properties from GstPadTemplate:
      name-template -> gchararray: Name template
        The name template of the pad template
      direction -> GstPadDirection: Direction
        The direction of the pad described by the pad template
      presence -> GstPadPresence: Presence
        When the pad described by the pad template will become available
      caps -> GstCaps: Caps
        The capabilities of the pad described by the pad template
    
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
    def get_caps(self, *args, **kwargs): # real signature unknown
        pass

    def pad_created(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    caps = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    direction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name_template = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    presence = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __gtype__ = None # (!) real value is ''


