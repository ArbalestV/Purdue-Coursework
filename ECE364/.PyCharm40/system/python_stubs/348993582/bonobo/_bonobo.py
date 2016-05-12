# encoding: utf-8
# module bonobo._bonobo
# from /usr/lib64/python2.6/site-packages/gtk-2.0/bonobo/_bonobo.so
# by generator 1.136
# no doc

# imports
import bonobo as __bonobo
import gobject._gobject as __gobject__gobject


# Variables with simple values

PROPERTY_NO_AUTONOTIFY = 8
PROPERTY_NO_LISTENING = 4

PROPERTY_READABLE = 1
PROPERTY_WRITEABLE = 2

# functions

def activate(*args, **kwargs): # real signature unknown
    pass

def arg_type_from_gtype(*args, **kwargs): # real signature unknown
    pass

def context_add(*args, **kwargs): # real signature unknown
    pass

def context_running_get(*args, **kwargs): # real signature unknown
    pass

def debug_shutdown(*args, **kwargs): # real signature unknown
    pass

def event_idl_path(*args, **kwargs): # real signature unknown
    pass

def event_kind(*args, **kwargs): # real signature unknown
    pass

def event_make_name(*args, **kwargs): # real signature unknown
    pass

def event_source_client_add_listener(*args, **kwargs): # real signature unknown
    pass

def event_source_client_add_listener_closure(*args, **kwargs): # real signature unknown
    pass

def event_source_client_add_listener_full(*args, **kwargs): # real signature unknown
    pass

def event_source_client_remove_listener(*args, **kwargs): # real signature unknown
    pass

def event_subtype(*args, **kwargs): # real signature unknown
    pass

def event_type(*args, **kwargs): # real signature unknown
    pass

def exception_add_handler_str(*args, **kwargs): # real signature unknown
    pass

def exception_general_error_get(*args, **kwargs): # real signature unknown
    pass

def exception_repoid_to_text(*args, **kwargs): # real signature unknown
    pass

def generic_factory_main(*args, **kwargs): # real signature unknown
    pass

def get_object(*args, **kwargs): # real signature unknown
    pass

def get_object_async(*args, **kwargs): # real signature unknown
    pass

def main(*args, **kwargs): # real signature unknown
    pass

def main_quit(*args, **kwargs): # real signature unknown
    pass

def moniker_client_equal(*args, **kwargs): # real signature unknown
    pass

def moniker_client_get_name(*args, **kwargs): # real signature unknown
    pass

def moniker_client_new_from_name(*args, **kwargs): # real signature unknown
    pass

def moniker_client_resolve_default(*args, **kwargs): # real signature unknown
    pass

def moniker_util_escape(*args, **kwargs): # real signature unknown
    pass

def moniker_util_get_parent_name(*args, **kwargs): # real signature unknown
    pass

def moniker_util_qi_return(*args, **kwargs): # real signature unknown
    pass

def moniker_util_seek_std_separator(*args, **kwargs): # real signature unknown
    pass

def moniker_util_unescape(*args, **kwargs): # real signature unknown
    pass

def object_dup_ref(*args, **kwargs): # real signature unknown
    pass

def object_from_stream(*args, **kwargs): # real signature unknown
    pass

def object_release_unref(*args, **kwargs): # real signature unknown
    pass

def orb(*args, **kwargs): # real signature unknown
    pass

def pbclient_get_boolean(*args, **kwargs): # real signature unknown
    pass

def pbclient_get_char(*args, **kwargs): # real signature unknown
    pass

def pbclient_get_default_boolean(*args, **kwargs): # real signature unknown
    pass

def pbclient_get_default_char(*args, **kwargs): # real signature unknown
    pass

def pbclient_get_default_double(*args, **kwargs): # real signature unknown
    pass

def pbclient_get_default_float(*args, **kwargs): # real signature unknown
    pass

def pbclient_get_default_long(*args, **kwargs): # real signature unknown
    pass

def pbclient_get_default_short(*args, **kwargs): # real signature unknown
    pass

def pbclient_get_default_string(*args, **kwargs): # real signature unknown
    pass

def pbclient_get_default_ulong(*args, **kwargs): # real signature unknown
    pass

def pbclient_get_default_ushort(*args, **kwargs): # real signature unknown
    pass

def pbclient_get_default_value(*args, **kwargs): # real signature unknown
    pass

def pbclient_get_doc(*args, **kwargs): # real signature unknown
    pass

def pbclient_get_doc_title(*args, **kwargs): # real signature unknown
    pass

def pbclient_get_double(*args, **kwargs): # real signature unknown
    pass

def pbclient_get_flags(*args, **kwargs): # real signature unknown
    pass

def pbclient_get_float(*args, **kwargs): # real signature unknown
    pass

def pbclient_get_long(*args, **kwargs): # real signature unknown
    pass

def pbclient_get_short(*args, **kwargs): # real signature unknown
    pass

def pbclient_get_string(*args, **kwargs): # real signature unknown
    pass

def pbclient_get_ulong(*args, **kwargs): # real signature unknown
    pass

def pbclient_get_ushort(*args, **kwargs): # real signature unknown
    pass

def pbclient_get_value(*args, **kwargs): # real signature unknown
    pass

def pbclient_set_boolean(*args, **kwargs): # real signature unknown
    pass

def pbclient_set_char(*args, **kwargs): # real signature unknown
    pass

def pbclient_set_double(*args, **kwargs): # real signature unknown
    pass

def pbclient_set_float(*args, **kwargs): # real signature unknown
    pass

def pbclient_set_long(*args, **kwargs): # real signature unknown
    pass

def pbclient_set_short(*args, **kwargs): # real signature unknown
    pass

def pbclient_set_string(*args, **kwargs): # real signature unknown
    pass

def pbclient_set_ulong(*args, **kwargs): # real signature unknown
    pass

def pbclient_set_ushort(*args, **kwargs): # real signature unknown
    pass

def pbclient_set_value(*args, **kwargs): # real signature unknown
    pass

def poa(*args, **kwargs): # real signature unknown
    pass

def poa_manager(*args, **kwargs): # real signature unknown
    pass

def property_bag_new_full(*args, **kwargs): # real signature unknown
    pass

def running_context_auto_exit_unref(*args, **kwargs): # real signature unknown
    pass

def storage_mem_create(*args, **kwargs): # real signature unknown
    pass

def stream_client_get_length(*args, **kwargs): # real signature unknown
    pass

def stream_client_read(*args, **kwargs): # real signature unknown
    pass

def url_lookup(*args, **kwargs): # real signature unknown
    pass

def url_register(*args, **kwargs): # real signature unknown
    pass

def url_unregister(*args, **kwargs): # real signature unknown
    pass

# classes

class AppClient(__gobject__gobject.GObject):
    """
    Object BonoboAppClient
    
    Signals from GObject:
      notify (GParam)
    """
    def msg_list(self, *args, **kwargs): # real signature unknown
        pass

    def msg_send(self, *args, **kwargs): # real signature unknown
        pass

    def new_instance(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class Object(__gobject__gobject.GObject):
    """
    Object BonoboObject
    
    Signals from BonoboObject:
      destroy ()
      system-exception (CorbaObject, BonoboCorbaException)
    
    Properties from BonoboObject:
      poa -> gpointer: POA
        Custom CORBA POA
    
    Signals from GObject:
      notify (GParam)
    """
    def add_interface(self, *args, **kwargs): # real signature unknown
        pass

    def check_env(self, *args, **kwargs): # real signature unknown
        pass

    def corba_objref(self, *args, **kwargs): # real signature unknown
        pass

    def dump_interfaces(self, *args, **kwargs): # real signature unknown
        pass

    def idle_unref(self, *args, **kwargs): # real signature unknown
        pass

    def query_interface(self, *args, **kwargs): # real signature unknown
        pass

    def query_local_interface(self, *args, **kwargs): # real signature unknown
        pass

    def ref(self, *args, **kwargs): # real signature unknown
        pass

    def set_immortal(self, *args, **kwargs): # real signature unknown
        pass

    def unref(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class Application(__bonobo.Object):
    """
    Object BonoboApplication
    
    Signals from BonoboApplication:
      message (gchararray, GValueArray) -> GValue
      new-instance (gint, GStrv) -> gint
    
    Properties from BonoboApplication:
      name -> gchararray: Name
        Application unique name
    
    Signals from BonoboObject:
      destroy ()
      system-exception (CorbaObject, BonoboCorbaException)
    
    Properties from BonoboObject:
      poa -> gpointer: POA
        Custom CORBA POA
    
    Signals from GObject:
      notify (GParam)
    """
    def create_serverinfo(self, *args, **kwargs): # real signature unknown
        pass

    def new_instance(self, *args, **kwargs): # real signature unknown
        pass

    def register_message(self, *args, **kwargs): # real signature unknown
        pass

    def register_unique(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class EventSource(__bonobo.Object):
    """
    Object BonoboEventSource
    
    Signals from BonoboObject:
      destroy ()
      system-exception (CorbaObject, BonoboCorbaException)
    
    Properties from BonoboObject:
      poa -> gpointer: POA
        Custom CORBA POA
    
    Signals from GObject:
      notify (GParam)
    """
    def ignore_listeners(self, *args, **kwargs): # real signature unknown
        pass

    def notify_listeners(self, *args, **kwargs): # real signature unknown
        pass

    def notify_listeners_full(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class ForeignObject(__bonobo.Object):
    """
    Object BonoboForeignObject
    
    Signals from BonoboObject:
      destroy ()
      system-exception (CorbaObject, BonoboCorbaException)
    
    Properties from BonoboObject:
      poa -> gpointer: POA
        Custom CORBA POA
    
    Signals from GObject:
      notify (GParam)
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class GenericFactory(__bonobo.Object):
    """
    Object BonoboGenericFactory
    
    Signals from BonoboObject:
      destroy ()
      system-exception (CorbaObject, BonoboCorbaException)
    
    Properties from BonoboObject:
      poa -> gpointer: POA
        Custom CORBA POA
    
    Signals from GObject:
      notify (GParam)
    """
    def construct_noreg(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class ItemHandler(__bonobo.Object):
    """
    Object BonoboItemHandler
    
    Signals from BonoboObject:
      destroy ()
      system-exception (CorbaObject, BonoboCorbaException)
    
    Properties from BonoboObject:
      poa -> gpointer: POA
        Custom CORBA POA
    
    Signals from GObject:
      notify (GParam)
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class Listener(__bonobo.Object):
    """
    Object BonoboListener
    
    Signals from BonoboListener:
      event-notify (gchararray, BonoboCorbaAny, BonoboCorbaException)
    
    Signals from BonoboObject:
      destroy ()
      system-exception (CorbaObject, BonoboCorbaException)
    
    Properties from BonoboObject:
      poa -> gpointer: POA
        Custom CORBA POA
    
    Signals from GObject:
      notify (GParam)
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class Moniker(__bonobo.Object):
    """
    Object BonoboMoniker
    
    Signals from BonoboObject:
      destroy ()
      system-exception (CorbaObject, BonoboCorbaException)
    
    Properties from BonoboObject:
      poa -> gpointer: POA
        Custom CORBA POA
    
    Signals from GObject:
      notify (GParam)
    """
    def get_case_sensitive(self, *args, **kwargs): # real signature unknown
        pass

    def get_name(self, *args, **kwargs): # real signature unknown
        pass

    def get_name_escaped(self, *args, **kwargs): # real signature unknown
        pass

    def get_name_full(self, *args, **kwargs): # real signature unknown
        pass

    def get_parent(self, *args, **kwargs): # real signature unknown
        pass

    def get_prefix(self, *args, **kwargs): # real signature unknown
        pass

    def set_case_sensitive(self, *args, **kwargs): # real signature unknown
        pass

    def set_name(self, *args, **kwargs): # real signature unknown
        pass

    def set_parent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class MonikerSimple(__bonobo.Moniker):
    """
    Object BonoboMonikerSimple
    
    Signals from BonoboObject:
      destroy ()
      system-exception (CorbaObject, BonoboCorbaException)
    
    Properties from BonoboObject:
      poa -> gpointer: POA
        Custom CORBA POA
    
    Signals from GObject:
      notify (GParam)
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class Persist(__bonobo.Object):
    """
    Object BonoboPersist
    
    Signals from BonoboObject:
      destroy ()
      system-exception (CorbaObject, BonoboCorbaException)
    
    Properties from BonoboObject:
      poa -> gpointer: POA
        Custom CORBA POA
    
    Signals from GObject:
      notify (GParam)
    """
    def set_dirty(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class PersistFile(__bonobo.Persist):
    """
    Object BonoboPersistFile
    
    Signals from BonoboObject:
      destroy ()
      system-exception (CorbaObject, BonoboCorbaException)
    
    Properties from BonoboObject:
      poa -> gpointer: POA
        Custom CORBA POA
    
    Signals from GObject:
      notify (GParam)
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class PersistStream(__bonobo.Persist):
    """
    Object BonoboPersistStream
    
    Signals from BonoboObject:
      destroy ()
      system-exception (CorbaObject, BonoboCorbaException)
    
    Properties from BonoboObject:
      poa -> gpointer: POA
        Custom CORBA POA
    
    Signals from GObject:
      notify (GParam)
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class PropertyBag(__bonobo.Object):
    """
    Object BonoboPropertyBag
    
    Signals from BonoboObject:
      destroy ()
      system-exception (CorbaObject, BonoboCorbaException)
    
    Properties from BonoboObject:
      poa -> gpointer: POA
        Custom CORBA POA
    
    Signals from GObject:
      notify (GParam)
    """
    def add(self, *args, **kwargs): # real signature unknown
        pass

    def add_full(self, *args, **kwargs): # real signature unknown
        pass

    def remove(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class StreamMem(__bonobo.Object):
    """
    Object BonoboStreamMem
    
    Signals from BonoboObject:
      destroy ()
      system-exception (CorbaObject, BonoboCorbaException)
    
    Properties from BonoboObject:
      poa -> gpointer: POA
        Custom CORBA POA
    
    Signals from GObject:
      notify (GParam)
    """
    def get_buffer(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


