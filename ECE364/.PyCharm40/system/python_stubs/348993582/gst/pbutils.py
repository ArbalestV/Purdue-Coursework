# encoding: utf-8
# module gst.pbutils
# from /usr/lib64/python2.6/site-packages/gst-0.10/gst/pbutils.so
# by generator 1.136
# no doc

# imports
import gobject as __gobject


# Variables with simple values

INSTALL_PLUGINS_CRASHED = 100
INSTALL_PLUGINS_ERROR = 2

INSTALL_PLUGINS_HELPER_MISSING = 202

INSTALL_PLUGINS_INSTALL_IN_PROGRESS = 203

INSTALL_PLUGINS_INTERNAL_FAILURE = 201

INSTALL_PLUGINS_INVALID = 101

INSTALL_PLUGINS_NOT_FOUND = 1

INSTALL_PLUGINS_PARTIAL_SUCCESS = 3

INSTALL_PLUGINS_STARTED_OK = 200

INSTALL_PLUGINS_SUCCESS = 0

INSTALL_PLUGINS_USER_ABORT = 4

# functions

def add_codec_description_to_tag_list(*args, **kwargs): # real signature unknown
    pass

def get_codec_description(*args, **kwargs): # real signature unknown
    pass

def get_decoder_description(*args, **kwargs): # real signature unknown
    pass

def get_element_description(*args, **kwargs): # real signature unknown
    pass

def get_encoder_description(*args, **kwargs): # real signature unknown
    pass

def get_sink_description(*args, **kwargs): # real signature unknown
    pass

def get_source_description(*args, **kwargs): # real signature unknown
    pass

def install_plugins_async(*args, **kwargs): # real signature unknown
    pass

def install_plugins_installation_in_progress(*args, **kwargs): # real signature unknown
    pass

def install_plugins_supported(*args, **kwargs): # real signature unknown
    pass

def install_plugins_sync(*args, **kwargs): # real signature unknown
    pass

def is_missing_plugin_message(*args, **kwargs): # real signature unknown
    pass

def missing_decoder_installer_detail_new(*args, **kwargs): # real signature unknown
    pass

def missing_decoder_message_new(*args, **kwargs): # real signature unknown
    pass

def missing_element_installer_detail_new(*args, **kwargs): # real signature unknown
    pass

def missing_element_message_new(*args, **kwargs): # real signature unknown
    pass

def missing_encoder_installer_detail_new(*args, **kwargs): # real signature unknown
    pass

def missing_encoder_message_new(*args, **kwargs): # real signature unknown
    pass

def missing_plugin_message_get_description(*args, **kwargs): # real signature unknown
    pass

def missing_plugin_message_get_installer_detail(*args, **kwargs): # real signature unknown
    pass

def missing_uri_sink_installer_detail_new(*args, **kwargs): # real signature unknown
    pass

def missing_uri_sink_message_new(*args, **kwargs): # real signature unknown
    pass

def missing_uri_source_installer_detail_new(*args, **kwargs): # real signature unknown
    pass

def missing_uri_source_message_new(*args, **kwargs): # real signature unknown
    pass

# classes

class InstallPluginsContext(__gobject.GBoxed):
    # no doc
    def set_xid(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class InstallPluginsReturn(__gobject.GEnum):
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
        100: 100,
        101: 101,
        200: 200,
        201: 201,
        202: 202,
        203: 203,
    }
    __gtype__ = None # (!) real value is ''


