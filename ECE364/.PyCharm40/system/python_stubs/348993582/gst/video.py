# encoding: utf-8
# module gst.video
# from /usr/lib64/python2.6/site-packages/gst-0.10/gst/video.so
# by generator 1.136
# no doc

# imports
import gobject as __gobject
import gst as __gst


# Variables with simple values

VIDEO_FORMAT_ABGR = 13
VIDEO_FORMAT_ARGB = 12
VIDEO_FORMAT_AYUV = 5
VIDEO_FORMAT_BGR = 15
VIDEO_FORMAT_BGRA = 11
VIDEO_FORMAT_BGRx = 7

VIDEO_FORMAT_GRAY16_BE = 25
VIDEO_FORMAT_GRAY16_LE = 26

VIDEO_FORMAT_GRAY8 = 24
VIDEO_FORMAT_I420 = 1
VIDEO_FORMAT_NV12 = 22
VIDEO_FORMAT_NV21 = 23
VIDEO_FORMAT_RGB = 14
VIDEO_FORMAT_RGBA = 10
VIDEO_FORMAT_RGBx = 6
VIDEO_FORMAT_UNKNOWN = 0
VIDEO_FORMAT_UYVY = 4
VIDEO_FORMAT_v210 = 20
VIDEO_FORMAT_v216 = 21
VIDEO_FORMAT_xBGR = 9
VIDEO_FORMAT_xRGB = 8
VIDEO_FORMAT_Y41B = 16
VIDEO_FORMAT_Y42B = 17
VIDEO_FORMAT_Y444 = 19
VIDEO_FORMAT_YUY2 = 3
VIDEO_FORMAT_YV12 = 2
VIDEO_FORMAT_YVYU = 18

# functions

def format_from_fourcc(*args, **kwargs): # real signature unknown
    pass

# classes

class VideoFilter(__gst.BaseTransform):
    """
    Object GstVideoFilter
    
    Properties from GstBaseTransform:
      qos -> gboolean: QoS
        Handle Quality-of-Service events
    
    Signals from GstElement:
      pad-added (GstPad)
      pad-removed (GstPad)
      no-more-pads ()
    
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
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self): # real signature unknown; restored from __doc__
        """ x.__iter__() <==> iter(x) """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    __gtype__ = None # (!) real value is ''


class VideoFormat(__gobject.GEnum):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __enum_values__ = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        8: 8,
        9: 9,
        10: 10,
        11: 11,
        12: 12,
        13: 13,
        14: 14,
        15: 15,
        16: 16,
        17: 17,
        18: 18,
        19: 19,
        20: 20,
        21: 21,
        22: 22,
        23: 23,
        24: 24,
        25: 25,
        26: 26,
    }
    __gtype__ = None # (!) real value is ''


class VideoSink(__gst.BaseSink):
    """
    Object GstVideoSink
    
    Properties from GstVideoSink:
      show-preroll-frame -> gboolean: Show preroll frame
        Whether to render video frames during preroll
    
    Properties from GstBaseSink:
      preroll-queue-len -> guint: Preroll queue length
        Number of buffers to queue during preroll
      sync -> gboolean: Sync
        Sync on the clock
      max-lateness -> gint64: Max Lateness
        Maximum number of nanoseconds that a buffer can be late before it is dropped (-1 unlimited)
      qos -> gboolean: Qos
        Generate Quality-of-Service events upstream
      async -> gboolean: Async
        Go asynchronously to PAUSED
      ts-offset -> gint64: TS Offset
        Timestamp offset in nanoseconds
      last-buffer -> GstBuffer: Last Buffer
        The last buffer received in the sink
      blocksize -> guint: Block size
        Size in bytes to pull per buffer (0 = default)
      render-delay -> guint64: Render Delay
        Additional render delay of the sink in nanoseconds
    
    Signals from GstElement:
      pad-added (GstPad)
      pad-removed (GstPad)
      no-more-pads ()
    
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
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self): # real signature unknown; restored from __doc__
        """ x.__iter__() <==> iter(x) """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    __gtype__ = None # (!) real value is ''


