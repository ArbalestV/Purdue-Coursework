# encoding: utf-8
# module gst.audio
# from /usr/lib64/python2.6/site-packages/gst-0.10/gst/audio.so
# by generator 1.136
# no doc

# imports
import gobject as __gobject
import gst as __gst


# Variables with simple values

AC3 = 37

AUDIO_CHANNEL_POSITION_FRONT_CENTER = 7
AUDIO_CHANNEL_POSITION_FRONT_LEFT = 1

AUDIO_CHANNEL_POSITION_FRONT_LEFT_OF_CENTER = 8

AUDIO_CHANNEL_POSITION_FRONT_MONO = 0
AUDIO_CHANNEL_POSITION_FRONT_RIGHT = 2

AUDIO_CHANNEL_POSITION_FRONT_RIGHT_OF_CENTER = 9

AUDIO_CHANNEL_POSITION_INVALID = -1
AUDIO_CHANNEL_POSITION_LFE = 6
AUDIO_CHANNEL_POSITION_NONE = 12
AUDIO_CHANNEL_POSITION_NUM = 13

AUDIO_CHANNEL_POSITION_REAR_CENTER = 3
AUDIO_CHANNEL_POSITION_REAR_LEFT = 4
AUDIO_CHANNEL_POSITION_REAR_RIGHT = 5

AUDIO_CHANNEL_POSITION_SIDE_LEFT = 10
AUDIO_CHANNEL_POSITION_SIDE_RIGHT = 11

A_LAW = 32

BUFTYPE_AC3 = 8

BUFTYPE_A_LAW = 3

BUFTYPE_DTS = 10
BUFTYPE_EAC3 = 9
BUFTYPE_FLOAT = 1
BUFTYPE_GSM = 6
BUFTYPE_IEC958 = 7

BUFTYPE_IMA_ADPCM = 4

BUFTYPE_LINEAR = 0
BUFTYPE_MPEG = 5

BUFTYPE_MU_LAW = 2

DTS = 39

EAC3 = 38

FLOAT32_BE = 28
FLOAT32_LE = 27

FLOAT64_BE = 30
FLOAT64_LE = 29

GSM = 35

IEC958 = 36

IMA_ADPCM = 33

MPEG = 34

MU_LAW = 31

No slaving = 3

Re-timestamp = 1
Resampling slaving = 0

RING_BUFFER_STATE_PAUSED = 1
RING_BUFFER_STATE_STARTED = 2
RING_BUFFER_STATE_STOPPED = 0

S16_BE = 4
S16_LE = 3

S18_3BE = 24
S18_3LE = 23

S20_3BE = 20
S20_3LE = 19

S24_3BE = 16
S24_3LE = 15
S24_BE = 8
S24_LE = 7

S32_BE = 12
S32_LE = 11

S8 = 1

SEGSTATE_EMPTY = 1
SEGSTATE_FILLED = 2
SEGSTATE_INVALID = 0
SEGSTATE_PARTIAL = 3

Skew = 2
Skew slaving = 1

U16_BE = 6
U16_LE = 5

U18_3BE = 26
U18_3LE = 25

U20_3BE = 22
U20_3LE = 21

U24_3BE = 18
U24_3LE = 17
U24_BE = 10
U24_LE = 9

U32_BE = 14
U32_LE = 13

U8 = 2

UNKNOWN = 0

# functions

def buffer_clip(*args, **kwargs): # real signature unknown
    pass

def clock_adjust(*args, **kwargs): # real signature unknown
    pass

def clock_get_time(*args, **kwargs): # real signature unknown
    pass

def duration_from_pad_buffer(*args, **kwargs): # real signature unknown
    pass

def frame_byte_size(*args, **kwargs): # real signature unknown
    pass

def frame_length(*args, **kwargs): # real signature unknown
    pass

def is_buffer_framed(*args, **kwargs): # real signature unknown
    pass

# classes

class AudioChannelPosition(__gobject.GEnum):
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
    }
    __gtype__ = None # (!) real value is ''


class AudioClock(__gst.SystemClock):
    """
    Object GstAudioClock
    
    Properties from GstSystemClock:
      clock-type -> GstClockType: Clock type
        The type of underlying clock implementation used
    
    Properties from GstClock:
      stats -> gboolean: Stats
        Enable clock stats (unimplemented)
      window-size -> gint: Window size
        The size of the window used to calculate rate and offset
      window-threshold -> gint: Window threshold
        The threshold to start calculating rate and offset
      timeout -> guint64: Timeout
        The amount of time, in nanoseconds, to sample master and slave clocks
    
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
    def reset(self, *args, **kwargs): # real signature unknown
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


class AudioFilter(__gst.BaseTransform):
    """
    Object GstAudioFilter
    
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


class BaseAudioSink(__gst.BaseSink):
    """
    Object GstBaseAudioSink
    
    Properties from GstBaseAudioSink:
      buffer-time -> gint64: Buffer Time
        Size of audio buffer in microseconds
      latency-time -> gint64: Latency Time
        Audio latency in microseconds
      provide-clock -> gboolean: Provide Clock
        Provide a clock to be used as the global pipeline clock
      slave-method -> GstBaseAudioSinkSlaveMethod: Slave Method
        Algorithm to use to match the rate of the masterclock
      can-activate-pull -> gboolean: Allow Pull Scheduling
        Allow pull-based scheduling
      drift-tolerance -> gint64: Drift Tolerance
        Tolerance for timestamp and clock drift in microseconds
    
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
    def create_ringbuffer(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_create_ringbuffer(cls, *args, **kwargs): # real signature unknown
        pass

    def get_provide_clock(self, *args, **kwargs): # real signature unknown
        pass

    def get_slave_method(self, *args, **kwargs): # real signature unknown
        pass

    def set_provide_clock(self, *args, **kwargs): # real signature unknown
        pass

    def set_slave_method(self, *args, **kwargs): # real signature unknown
        pass

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


class AudioSink(BaseAudioSink):
    """
    Object GstAudioSink
    
    Properties from GstBaseAudioSink:
      buffer-time -> gint64: Buffer Time
        Size of audio buffer in microseconds
      latency-time -> gint64: Latency Time
        Audio latency in microseconds
      provide-clock -> gboolean: Provide Clock
        Provide a clock to be used as the global pipeline clock
      slave-method -> GstBaseAudioSinkSlaveMethod: Slave Method
        Algorithm to use to match the rate of the masterclock
      can-activate-pull -> gboolean: Allow Pull Scheduling
        Allow pull-based scheduling
      drift-tolerance -> gint64: Drift Tolerance
        Tolerance for timestamp and clock drift in microseconds
    
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
    @classmethod
    def do_close(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_delay(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_open(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_reset(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_unprepare(cls, *args, **kwargs): # real signature unknown
        pass

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


class BaseAudioSinkSlaveMethod(__gobject.GEnum):
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


class BaseAudioSrcSlaveMethod(__gobject.GEnum):
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


class BufferFormat(__gobject.GEnum):
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
        27: 27,
        28: 28,
        29: 29,
        30: 30,
        31: 31,
        32: 32,
        33: 33,
        34: 34,
        35: 35,
        36: 36,
        37: 37,
        38: 38,
        39: 39,
    }
    __gtype__ = None # (!) real value is ''


class BufferFormatType(__gobject.GEnum):
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
    }
    __gtype__ = None # (!) real value is ''


class RingBuffer(__gst.Object):
    """
    Object GstRingBuffer
    
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
    def activate(self, *args, **kwargs): # real signature unknown
        pass

    def advance(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self, *args, **kwargs): # real signature unknown
        pass

    def clear_all(self, *args, **kwargs): # real signature unknown
        pass

    def close_device(self, *args, **kwargs): # real signature unknown
        pass

    def commit(self, *args, **kwargs): # real signature unknown
        pass

    def delay(self, *args, **kwargs): # real signature unknown
        pass

    def device_is_open(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_activate(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_close_device(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_delay(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_open_device(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_pause(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_release(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_resume(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_start(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_stop(cls, *args, **kwargs): # real signature unknown
        pass

    def is_acquired(self, *args, **kwargs): # real signature unknown
        pass

    def is_active(self, *args, **kwargs): # real signature unknown
        pass

    def may_start(self, *args, **kwargs): # real signature unknown
        pass

    def open_device(self, *args, **kwargs): # real signature unknown
        pass

    def pause(self, *args, **kwargs): # real signature unknown
        pass

    def read(self, *args, **kwargs): # real signature unknown
        pass

    def release(self, *args, **kwargs): # real signature unknown
        pass

    def samples_done(self, *args, **kwargs): # real signature unknown
        pass

    def set_flushing(self, *args, **kwargs): # real signature unknown
        pass

    def set_sample(self, *args, **kwargs): # real signature unknown
        pass

    def start(self, *args, **kwargs): # real signature unknown
        pass

    def stop(self, *args, **kwargs): # real signature unknown
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


class RingBufferSegState(__gobject.GEnum):
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


class RingBufferState(__gobject.GEnum):
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


