# encoding: utf-8
# module gnome.ui
# from /usr/lib64/python2.6/site-packages/gtk-2.0/gnome/ui.so
# by generator 1.136
# no doc

# imports
import gnome.canvas as __gnome_canvas
import gobject as __gobject
import gobject._gobject as __gobject__gobject
import gtk as __gtk


class Client(__gtk.Object):
    """
    Object GnomeClient
    
    Signals from GnomeClient:
      save-yourself (gint, GnomeSaveStyle, gboolean, GnomeInteractStyle, gboolean) -> gboolean
      die ()
      save-complete ()
      shutdown-cancelled ()
      connect (gboolean)
      disconnect ()
    
    Signals from GtkObject:
      destroy ()
    
    Properties from GtkObject:
      user-data -> gpointer: User Data
        Anonymous User Data Pointer
    
    Signals from GObject:
      notify (GParam)
    """
    def add_static_arg(self, *args, **kwargs): # real signature unknown
        pass

    def connect_to_session_manager(self, *args, **kwargs): # real signature unknown
        pass

    def disconnect(self, *args, **kwargs): # real signature unknown
        pass

    def flush(self, *args, **kwargs): # real signature unknown
        pass

    def get_config_prefix(self, *args, **kwargs): # real signature unknown
        pass

    def get_desktop_id(self, *args, **kwargs): # real signature unknown
        pass

    def get_flags(self, *args, **kwargs): # real signature unknown
        pass

    def get_global_config_prefix(self, *args, **kwargs): # real signature unknown
        pass

    def get_id(self, *args, **kwargs): # real signature unknown
        pass

    def get_previous_id(self, *args, **kwargs): # real signature unknown
        pass

    def request_phase_2(self, *args, **kwargs): # real signature unknown
        pass

    def request_save(self, *args, **kwargs): # real signature unknown
        pass

    def save_any_dialog(self, *args, **kwargs): # real signature unknown
        pass

    def save_error_dialog(self, *args, **kwargs): # real signature unknown
        pass

    def set_clone_command(self, *args, **kwargs): # real signature unknown
        pass

    def set_current_directory(self, *args, **kwargs): # real signature unknown
        pass

    def set_discard_command(self, *args, **kwargs): # real signature unknown
        pass

    def set_environment(self, *args, **kwargs): # real signature unknown
        pass

    def set_global_config_prefix(self, *args, **kwargs): # real signature unknown
        pass

    def set_id(self, *args, **kwargs): # real signature unknown
        pass

    def set_priority(self, *args, **kwargs): # real signature unknown
        pass

    def set_program(self, *args, **kwargs): # real signature unknown
        pass

    def set_resign_command(self, *args, **kwargs): # real signature unknown
        pass

    def set_restart_command(self, *args, **kwargs): # real signature unknown
        pass

    def set_restart_style(self, *args, **kwargs): # real signature unknown
        pass

    def set_shutdown_command(self, *args, **kwargs): # real signature unknown
        pass

    def set_user_id(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


