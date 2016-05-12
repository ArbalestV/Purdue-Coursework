# encoding: utf-8
# module gst.tag
# from /usr/lib64/python2.6/site-packages/gst-0.10/gst/tag.so
# by generator 1.136
# no doc

# imports
import gobject as __gobject
import gst as __gst


# Variables with simple values

TAG_DEMUX_RESULT_AGAIN = 1

TAG_DEMUX_RESULT_BROKEN_TAG = 0

TAG_DEMUX_RESULT_OK = 2

TAG_IMAGE_TYPE_ARTIST = 6

TAG_IMAGE_TYPE_BACK_COVER = 2

TAG_IMAGE_TYPE_BAND_ARTIST_LOGO = 17

TAG_IMAGE_TYPE_BAND_ORCHESTRA = 8

TAG_IMAGE_TYPE_COMPOSER = 9
TAG_IMAGE_TYPE_CONDUCTOR = 7

TAG_IMAGE_TYPE_DURING_PERFORMANCE = 13
TAG_IMAGE_TYPE_DURING_RECORDING = 12

TAG_IMAGE_TYPE_FISH = 15

TAG_IMAGE_TYPE_FRONT_COVER = 1

TAG_IMAGE_TYPE_ILLUSTRATION = 16

TAG_IMAGE_TYPE_LEAD_ARTIST = 5

TAG_IMAGE_TYPE_LEAFLET_PAGE = 3

TAG_IMAGE_TYPE_LYRICIST = 10
TAG_IMAGE_TYPE_MEDIUM = 4
TAG_IMAGE_TYPE_NONE = -1

TAG_IMAGE_TYPE_PUBLISHER_STUDIO_LOGO = 18

TAG_IMAGE_TYPE_RECORDING_LOCATION = 11

TAG_IMAGE_TYPE_UNDEFINED = 0

TAG_IMAGE_TYPE_VIDEO_CAPTURE = 14

# functions

def from_id3_tag(*args, **kwargs): # real signature unknown
    pass

def from_id3_user_tag(*args, **kwargs): # real signature unknown
    pass

def from_vorbis_tag(*args, **kwargs): # real signature unknown
    pass

def gst_vorbis_tag_add(*args, **kwargs): # real signature unknown
    pass

def id3_genre_count(*args, **kwargs): # real signature unknown
    pass

def register_musicbrainz_tags(*args, **kwargs): # real signature unknown
    pass

def to_id3_tag(*args, **kwargs): # real signature unknown
    pass

def to_vorbis_comments(*args, **kwargs): # real signature unknown
    pass

def to_vorbis_tag(*args, **kwargs): # real signature unknown
    pass

# classes

class TagDemux(__gst.Element):
    """
    Object GstTagDemux
    
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


class TagDemuxResult(__gobject.GEnum):
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
    }
    __gtype__ = None # (!) real value is ''


class TagImageType(__gobject.GEnum):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __enum_values__ = {
        -1: -1,
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
    }
    __gtype__ = None # (!) real value is ''


