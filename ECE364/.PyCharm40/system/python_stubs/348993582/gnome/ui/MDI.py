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


class MDI(__gtk.Object):
    """
    Object GnomeMDI
    
    Signals from GnomeMDI:
      add-child (GnomeMDIChild) -> gboolean
      remove-child (GnomeMDIChild) -> gboolean
      add-view (GtkWidget) -> gboolean
      remove-view (GtkWidget) -> gboolean
      child-changed (GnomeMDIChild)
      view-changed (GtkWidget)
      app-created (GnomeApp)
    
    Signals from GtkObject:
      destroy ()
    
    Properties from GtkObject:
      user-data -> gpointer: User Data
        Anonymous User Data Pointer
    
    Signals from GObject:
      notify (GParam)
    """
    def add_child(self, *args, **kwargs): # real signature unknown
        pass

    def add_toplevel_view(self, *args, **kwargs): # real signature unknown
        pass

    def add_view(self, *args, **kwargs): # real signature unknown
        pass

    def find_child(self, *args, **kwargs): # real signature unknown
        pass

    def get_active_child(self, *args, **kwargs): # real signature unknown
        pass

    def get_active_view(self, *args, **kwargs): # real signature unknown
        pass

    def get_active_window(self, *args, **kwargs): # real signature unknown
        pass

    def get_view_from_window(self, *args, **kwargs): # real signature unknown
        pass

    def open_toplevel(self, *args, **kwargs): # real signature unknown
        pass

    def register(self, *args, **kwargs): # real signature unknown
        pass

    def remove_all(self, *args, **kwargs): # real signature unknown
        pass

    def remove_child(self, *args, **kwargs): # real signature unknown
        pass

    def remove_view(self, *args, **kwargs): # real signature unknown
        pass

    def save_state(self, *args, **kwargs): # real signature unknown
        pass

    def set_active_view(self, *args, **kwargs): # real signature unknown
        pass

    def set_child_list_path(self, *args, **kwargs): # real signature unknown
        pass

    def set_child_menu_path(self, *args, **kwargs): # real signature unknown
        pass

    def set_mode(self, *args, **kwargs): # real signature unknown
        pass

    def unregister(self, *args, **kwargs): # real signature unknown
        pass

    def update_child(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


