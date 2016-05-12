# encoding: utf-8
# module egg.recent
# from /usr/lib64/python2.6/site-packages/gtk-2.0/egg/recent.so
# by generator 1.136
# no doc

# imports
import gobject as __gobject
import gobject._gobject as __gobject__gobject
import recent as __recent


# Variables with simple values

RECENT_MODEL_SORT_LRU = 1
RECENT_MODEL_SORT_MRU = 0
RECENT_MODEL_SORT_NONE = 2

__version__ = '2.25.3'

# functions

def recent_item_new_from_uri(*args, **kwargs): # real signature unknown
    pass

def recent_util_escape_underlines(*args, **kwargs): # real signature unknown
    pass

def recent_util_get_unique_id(*args, **kwargs): # real signature unknown
    pass

# classes

class RecentItem(__gobject.GBoxed):
    # no doc
    def add_group(self, *args, **kwargs): # real signature unknown
        pass

    def get_mime_type(self, *args, **kwargs): # real signature unknown
        pass

    def get_private(self, *args, **kwargs): # real signature unknown
        pass

    def get_short_name(self, *args, **kwargs): # real signature unknown
        pass

    def get_timestamp(self, *args, **kwargs): # real signature unknown
        pass

    def get_uri(self, *args, **kwargs): # real signature unknown
        pass

    def get_uri_for_display(self, *args, **kwargs): # real signature unknown
        pass

    def get_uri_utf8(self, *args, **kwargs): # real signature unknown
        pass

    def in_group(self, *args, **kwargs): # real signature unknown
        pass

    def peek_uri(self, *args, **kwargs): # real signature unknown
        pass

    def ref(self, *args, **kwargs): # real signature unknown
        pass

    def remove_group(self, *args, **kwargs): # real signature unknown
        pass

    def set_mime_type(self, *args, **kwargs): # real signature unknown
        pass

    def set_private(self, *args, **kwargs): # real signature unknown
        pass

    def set_timestamp(self, *args, **kwargs): # real signature unknown
        pass

    def set_uri(self, *args, **kwargs): # real signature unknown
        pass

    def unref(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class RecentModel(__gobject__gobject.GObject):
    """
    Object EggRecentModel
    
    Signals from EggRecentModel:
      changed (gpointer)
    
    Properties from EggRecentModel:
      mime-filters -> gpointer: Mime Filters
        List of mime types to be allowed.
      group-filters -> gpointer: Group Filters
        List of groups to be allowed.
      scheme-filters -> gpointer: Scheme Filters
        List of URI schemes to be allowed.
      sort-type -> gint: Sort Type
        Type of sorting to be done.
      limit -> gint: Limit
        Max number of items allowed.
    
    Signals from GObject:
      notify (GParam)
    """
    def add(self, *args, **kwargs): # real signature unknown
        pass

    def add_full(self, *args, **kwargs): # real signature unknown
        pass

    def changed(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self, *args, **kwargs): # real signature unknown
        pass

    def delete(self, *args, **kwargs): # real signature unknown
        pass

    def get_limit(self, *args, **kwargs): # real signature unknown
        pass

    def get_list(self, *args, **kwargs): # real signature unknown
        pass

    def remove_expired(self, *args, **kwargs): # real signature unknown
        pass

    def set_filter_groups(self, *args, **kwargs): # real signature unknown
        pass

    def set_filter_mime_types(self, *args, **kwargs): # real signature unknown
        pass

    def set_filter_uri_schemes(self, *args, **kwargs): # real signature unknown
        pass

    def set_limit(self, *args, **kwargs): # real signature unknown
        pass

    def set_sort(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class RecentModelSort(__gobject.GEnum):
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


class RecentView(__gobject.GInterface):
    # no doc
    def get_model(self, *args, **kwargs): # real signature unknown
        pass

    def set_model(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class RecentViewBonobo(__gobject__gobject.GObject, __recent.RecentView):
    """
    Object EggRecentViewBonobo
    
    Signals from EggRecentViewBonobo:
      activate (EggRecentItem)
    
    Properties from EggRecentViewBonobo:
      ui-component -> BonoboUIComponent: UI Component
        BonoboUIComponent for menus.
      ui-path -> gchararray: Path
        The path to put the menu items.
      show-icons -> gboolean: Show Icons
        Whether or not to show icons
      show-numbers -> gboolean: Show Numbers
        Whether or not to show numbers
      label-width -> gint: Label Width
        The desired width of the menu label, in characters
    
    Signals from GObject:
      notify (GParam)
    """
    def get_icon_size(self, *args, **kwargs): # real signature unknown
        pass

    def get_ui_component(self, *args, **kwargs): # real signature unknown
        pass

    def get_ui_path(self, *args, **kwargs): # real signature unknown
        pass

    def set_icon_size(self, *args, **kwargs): # real signature unknown
        pass

    def set_ui_component(self, *args, **kwargs): # real signature unknown
        pass

    def set_ui_path(self, *args, **kwargs): # real signature unknown
        pass

    def show_icons(self, *args, **kwargs): # real signature unknown
        pass

    def show_numbers(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class RecentViewGtk(__gobject__gobject.GObject, __recent.RecentView):
    """
    Object EggRecentViewGtk
    
    Signals from EggRecentViewGtk:
      activate (EggRecentItem)
    
    Properties from EggRecentViewGtk:
      menu -> GtkMenu: Menu
        The GtkMenuShell this object will update.
      start-menu-item -> GtkMenuItem: Start Menu Item
        The menu item that precedes where are menu items will go
      show-icons -> gboolean: Show Icons
        Whether or not to show icons
      show-numbers -> gboolean: Show Numbers
        Whether or not to show numbers
      label-width -> gint: Label Width
        The desired width of the menu label, in characters
    
    Signals from GObject:
      notify (GParam)
    """
    def get_icon_size(self, *args, **kwargs): # real signature unknown
        pass

    def get_menu(self, *args, **kwargs): # real signature unknown
        pass

    def get_start_menu_item(self, *args, **kwargs): # real signature unknown
        pass

    def set_icon_size(self, *args, **kwargs): # real signature unknown
        pass

    def set_leading_sep(self, *args, **kwargs): # real signature unknown
        pass

    def set_menu(self, *args, **kwargs): # real signature unknown
        pass

    def set_start_menu_item(self, *args, **kwargs): # real signature unknown
        pass

    def set_trailing_sep(self, *args, **kwargs): # real signature unknown
        pass

    def show_icons(self, *args, **kwargs): # real signature unknown
        pass

    def show_numbers(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class RecentViewUIManager(__gobject__gobject.GObject, __recent.RecentView):
    """
    Object EggRecentViewUIManager
    
    Signals from EggRecentViewUIManager:
      activate (EggRecentItem)
    
    Properties from EggRecentViewUIManager:
      uimanager -> GtkUIManager: UI Manager
        The UI manager this object will use to update.the UI
      path -> gchararray: Path
        The UI path this object will update.
      show-icons -> gboolean: Show Icons
        Whether or not to show icons
      show-numbers -> gboolean: Show Numbers
        Whether or not to show numbers
      label-width -> gint: Label Width
        The desired width of the menu label, in characters
    
    Signals from GObject:
      notify (GParam)
    """
    def get_icon_size(self, *args, **kwargs): # real signature unknown
        pass

    def get_item(self, *args, **kwargs): # real signature unknown
        pass

    def get_label_width(self, *args, **kwargs): # real signature unknown
        pass

    def get_path(self, *args, **kwargs): # real signature unknown
        pass

    def get_uimanager(self, *args, **kwargs): # real signature unknown
        pass

    def set_icon_size(self, *args, **kwargs): # real signature unknown
        pass

    def set_label_width(self, *args, **kwargs): # real signature unknown
        pass

    def set_leading_sep(self, *args, **kwargs): # real signature unknown
        pass

    def set_path(self, *args, **kwargs): # real signature unknown
        pass

    def set_trailing_sep(self, *args, **kwargs): # real signature unknown
        pass

    def set_uimanager(self, *args, **kwargs): # real signature unknown
        pass

    def show_icons(self, *args, **kwargs): # real signature unknown
        pass

    def show_numbers(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


