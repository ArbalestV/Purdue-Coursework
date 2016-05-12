# encoding: utf-8
# module gst.interfaces
# from /usr/lib64/python2.6/site-packages/gst-0.10/gst/interfaces.so
# by generator 1.136
# no doc

# imports
import gobject as __gobject
import gobject._gobject as __gobject__gobject


# Variables with simple values

COLOR_BALANCE_HARDWARE = 0
COLOR_BALANCE_SOFTWARE = 1

MIXER_FLAG_AUTO_NOTIFICATIONS = 1

MIXER_FLAG_GROUPING = 4

MIXER_FLAG_HAS_WHITELIST = 2

MIXER_FLAG_NONE = 0

MIXER_HARDWARE = 0

MIXER_MESSAGE_INVALID = 0

MIXER_MESSAGE_MIXER_CHANGED = 6

MIXER_MESSAGE_MUTE_TOGGLED = 1

MIXER_MESSAGE_OPTIONS_LIST_CHANGED = 5

MIXER_MESSAGE_OPTION_CHANGED = 4

MIXER_MESSAGE_RECORD_TOGGLED = 2

MIXER_MESSAGE_VOLUME_CHANGED = 3

MIXER_SOFTWARE = 1

MIXER_TRACK_INPUT = 1
MIXER_TRACK_MASTER = 16
MIXER_TRACK_MUTE = 4

MIXER_TRACK_NO_MUTE = 128
MIXER_TRACK_NO_RECORD = 64

MIXER_TRACK_OUTPUT = 2
MIXER_TRACK_READONLY = 512
MIXER_TRACK_RECORD = 8
MIXER_TRACK_SOFTWARE = 32
MIXER_TRACK_WHITELIST = 256
MIXER_TRACK_WRITEONLY = 1024

NAVIGATION_COMMAND_ACTIVATE = 24
NAVIGATION_COMMAND_DOWN = 23
NAVIGATION_COMMAND_INVALID = 0
NAVIGATION_COMMAND_LEFT = 20
NAVIGATION_COMMAND_MENU1 = 1
NAVIGATION_COMMAND_MENU2 = 2
NAVIGATION_COMMAND_MENU3 = 3
NAVIGATION_COMMAND_MENU4 = 4
NAVIGATION_COMMAND_MENU5 = 5
NAVIGATION_COMMAND_MENU6 = 6
NAVIGATION_COMMAND_MENU7 = 7

NAVIGATION_COMMAND_NEXT_ANGLE = 31

NAVIGATION_COMMAND_PREV_ANGLE = 30

NAVIGATION_COMMAND_RIGHT = 21
NAVIGATION_COMMAND_UP = 22

NAVIGATION_EVENT_COMMAND = 6
NAVIGATION_EVENT_INVALID = 0

NAVIGATION_EVENT_KEY_PRESS = 1
NAVIGATION_EVENT_KEY_RELEASE = 2

NAVIGATION_EVENT_MOUSE_BUTTON_PRESS = 3
NAVIGATION_EVENT_MOUSE_BUTTON_RELEASE = 4

NAVIGATION_EVENT_MOUSE_MOVE = 5

NAVIGATION_MESSAGE_ANGLES_CHANGED = 3

NAVIGATION_MESSAGE_COMMANDS_CHANGED = 2

NAVIGATION_MESSAGE_INVALID = 0

NAVIGATION_MESSAGE_MOUSE_OVER = 1

NAVIGATION_QUERY_ANGLES = 2
NAVIGATION_QUERY_COMMANDS = 1
NAVIGATION_QUERY_INVALID = 0

TUNER_CHANNEL_AUDIO = 8
TUNER_CHANNEL_FREQUENCY = 4
TUNER_CHANNEL_INPUT = 1
TUNER_CHANNEL_OUTPUT = 2

# functions

def mixer_message_parse_mute_toggled(*args, **kwargs): # real signature unknown
    pass

def mixer_message_parse_option_changed(*args, **kwargs): # real signature unknown
    pass

def mixer_message_parse_record_toggled(*args, **kwargs): # real signature unknown
    pass

def mixer_message_parse_volume_changed(*args, **kwargs): # real signature unknown
    pass

def navigation_message_new_angles_changed(*args, **kwargs): # real signature unknown
    pass

def navigation_message_new_commands_changed(*args, **kwargs): # real signature unknown
    pass

def navigation_message_new_mouse_over(*args, **kwargs): # real signature unknown
    pass

def navigation_query_new_angles(*args, **kwargs): # real signature unknown
    pass

def navigation_query_new_commands(*args, **kwargs): # real signature unknown
    pass

def navigation_query_set_angles(*args, **kwargs): # real signature unknown
    pass

# classes

class ColorBalance(__gobject.GInterface):
    # no doc
    @classmethod
    def do_get_value(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_set_value(cls, *args, **kwargs): # real signature unknown
        pass

    def get_value(self, *args, **kwargs): # real signature unknown
        pass

    def list_colorbalance_channels(self, *args, **kwargs): # real signature unknown
        pass

    def set_value(self, *args, **kwargs): # real signature unknown
        pass

    def value_changed(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class ColorBalanceChannel(__gobject__gobject.GObject):
    """
    Object GstColorBalanceChannel
    
    Signals from GstColorBalanceChannel:
      value-changed (gint)
    
    Signals from GObject:
      notify (GParam)
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    label = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    max_value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    min_value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __gtype__ = None # (!) real value is ''


class ColorBalanceType(__gobject.GEnum):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __enum_values__ = {
        0: 0,
        1: 1,
    }
    __gtype__ = None # (!) real value is ''


class Mixer(__gobject.GInterface):
    # no doc
    @classmethod
    def do_set_mute(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_set_record(cls, *args, **kwargs): # real signature unknown
        pass

    def get_mixer_flags(self, *args, **kwargs): # real signature unknown
        pass

    def get_option(self, *args, **kwargs): # real signature unknown
        pass

    def get_volume(self, *args, **kwargs): # real signature unknown
        pass

    def list_tracks(self, *args, **kwargs): # real signature unknown
        pass

    def mute_toggled(self, *args, **kwargs): # real signature unknown
        pass

    def option_changed(self, *args, **kwargs): # real signature unknown
        pass

    def record_toggled(self, *args, **kwargs): # real signature unknown
        pass

    def set_mute(self, *args, **kwargs): # real signature unknown
        pass

    def set_option(self, *args, **kwargs): # real signature unknown
        pass

    def set_record(self, *args, **kwargs): # real signature unknown
        pass

    def set_volume(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class MixerFlags(__gobject.GFlags):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __flags_values__ = {
        0: 0,
        1: 1,
        2: 2,
        4: 4,
    }
    __gtype__ = None # (!) real value is ''


class MixerMessageType(__gobject.GEnum):
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
    }
    __gtype__ = None # (!) real value is ''


class MixerTrack(__gobject__gobject.GObject):
    """
    Object GstMixerTrack
    
    Properties from GstMixerTrack:
      label -> gchararray: Track label
        The label assigned to the track (may be translated)
      untranslated-label -> gchararray: Untranslated track label
        The untranslated label assigned to the track (since 0.10.13)
      index -> guint: Index
        Track index
      min-volume -> gint: Minimum volume level
        The minimum possible volume level
      max-volume -> gint: Maximum volume level
        The maximum possible volume level
      flags -> guint: Flags
        Flags indicating the type of mixer track
      num-channels -> gint: Number of channels
        The number of channels contained within the track
    
    Signals from GObject:
      notify (GParam)
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    label = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    max_volume = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    min_volume = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    num_channels = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __gtype__ = None # (!) real value is ''


class MixerOptions(MixerTrack):
    """
    Object GstMixerOptions
    
    Properties from GstMixerTrack:
      label -> gchararray: Track label
        The label assigned to the track (may be translated)
      untranslated-label -> gchararray: Untranslated track label
        The untranslated label assigned to the track (since 0.10.13)
      index -> guint: Index
        Track index
      min-volume -> gint: Minimum volume level
        The minimum possible volume level
      max-volume -> gint: Maximum volume level
        The maximum possible volume level
      flags -> guint: Flags
        Flags indicating the type of mixer track
      num-channels -> gint: Number of channels
        The number of channels contained within the track
    
    Signals from GObject:
      notify (GParam)
    """
    def get_values(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class MixerTrackFlags(__gobject.GFlags):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __flags_values__ = {
        1: 1,
        2: 2,
        4: 4,
        8: 8,
        16: 16,
        32: 32,
        64: 64,
        128: 128,
        256: 256,
        512: 512,
        1024: 1024,
    }
    __gtype__ = None # (!) real value is ''


class MixerType(__gobject.GEnum):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __enum_values__ = {
        0: 0,
        1: 1,
    }
    __gtype__ = None # (!) real value is ''


class Navigation(__gobject.GInterface):
    # no doc
    @classmethod
    def do_send_event(cls, *args, **kwargs): # real signature unknown
        pass

    def send_command(self, *args, **kwargs): # real signature unknown
        pass

    def send_event(self, *args, **kwargs): # real signature unknown
        pass

    def send_key_event(self, *args, **kwargs): # real signature unknown
        pass

    def send_mouse_event(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class NavigationCommand(__gobject.GEnum):
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
        20: 20,
        21: 21,
        22: 22,
        23: 23,
        24: 24,
        30: 30,
        31: 31,
    }
    __gtype__ = None # (!) real value is ''


class NavigationEventType(__gobject.GEnum):
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
    }
    __gtype__ = None # (!) real value is ''


class NavigationMessageType(__gobject.GEnum):
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
    }
    __gtype__ = None # (!) real value is ''


class NavigationQueryType(__gobject.GEnum):
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


class PropertyProbe(__gobject.GInterface):
    # no doc
    def needs_probe_name(self, *args, **kwargs): # real signature unknown
        pass

    def probe_get_properties(self, *args, **kwargs): # real signature unknown
        pass

    def probe_get_property(self, *args, **kwargs): # real signature unknown
        pass

    def probe_get_values_name(self, *args, **kwargs): # real signature unknown
        pass

    def probe_property_name(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class Tuner(__gobject.GInterface):
    # no doc
    def channel_changed(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_get_channel(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_get_frequency(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_get_norm(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_set_channel(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_set_frequency(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_set_norm(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_signal_strength(cls, *args, **kwargs): # real signature unknown
        pass

    def find_channel_by_name(self, *args, **kwargs): # real signature unknown
        pass

    def find_norm_by_name(self, *args, **kwargs): # real signature unknown
        pass

    def frequency_changed(self, *args, **kwargs): # real signature unknown
        pass

    def get_channel(self, *args, **kwargs): # real signature unknown
        pass

    def get_frequency(self, *args, **kwargs): # real signature unknown
        pass

    def get_norm(self, *args, **kwargs): # real signature unknown
        pass

    def list_channels(self, *args, **kwargs): # real signature unknown
        pass

    def list_norms(self, *args, **kwargs): # real signature unknown
        pass

    def norm_changed(self, *args, **kwargs): # real signature unknown
        pass

    def set_channel(self, *args, **kwargs): # real signature unknown
        pass

    def set_frequency(self, *args, **kwargs): # real signature unknown
        pass

    def set_norm(self, *args, **kwargs): # real signature unknown
        pass

    def signal_changed(self, *args, **kwargs): # real signature unknown
        pass

    def signal_strength(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class TunerChannel(__gobject__gobject.GObject):
    """
    Object GstTunerChannel
    
    Signals from GstTunerChannel:
      frequency-changed (gulong)
      signal-changed (gint)
    
    Signals from GObject:
      notify (GParam)
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    freq_multiplicator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    label = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    max_frequency = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    max_signal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    min_frequency = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    min_signal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __gtype__ = None # (!) real value is ''


class TunerChannelFlags(__gobject.GFlags):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __flags_values__ = {
        1: 1,
        2: 2,
        4: 4,
        8: 8,
    }
    __gtype__ = None # (!) real value is ''


class TunerNorm(__gobject__gobject.GObject):
    """
    Object GstTunerNorm
    
    Signals from GObject:
      notify (GParam)
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    label = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __gtype__ = None # (!) real value is ''


class VideoOrientation(__gobject.GInterface):
    # no doc
    def get_hcenter(self, *args, **kwargs): # real signature unknown
        pass

    def get_hflip(self, *args, **kwargs): # real signature unknown
        pass

    def get_vcenter(self, *args, **kwargs): # real signature unknown
        pass

    def get_vflip(self, *args, **kwargs): # real signature unknown
        pass

    def set_hcenter(self, *args, **kwargs): # real signature unknown
        pass

    def set_hflip(self, *args, **kwargs): # real signature unknown
        pass

    def set_vcenter(self, *args, **kwargs): # real signature unknown
        pass

    def set_vflip(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class XOverlay(__gobject.GInterface):
    # no doc
    def expose(self, *args, **kwargs): # real signature unknown
        pass

    def got_xwindow_id(self, *args, **kwargs): # real signature unknown
        pass

    def prepare_xwindow_id(self, *args, **kwargs): # real signature unknown
        pass

    def set_xwindow_id(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


