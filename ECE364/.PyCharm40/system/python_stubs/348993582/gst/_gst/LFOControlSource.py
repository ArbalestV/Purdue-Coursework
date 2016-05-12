# encoding: utf-8
# module gst._gst
# from /usr/lib64/python2.6/site-packages/gst-0.10/gst/_gst.so
# by generator 1.136
# no doc

# imports
import gobject as __gobject
import gobject._gobject as __gobject__gobject
import gst as __gst


class LFOControlSource(__gst.ControlSource):
    """
    Object GstLFOControlSource
    
    Properties from GstLFOControlSource:
      waveform -> GstLFOWaveform: Waveform
        Waveform
      frequency -> gdouble: Frequency
        Frequency of the waveform
      timeshift -> guint64: Timeshift
        Timeshift of the waveform to the right
      amplitude -> GValue: Amplitude
        Amplitude of the waveform
      offset -> GValue: Offset
        Offset of the waveform
    
    Signals from GObject:
      notify (GParam)
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


