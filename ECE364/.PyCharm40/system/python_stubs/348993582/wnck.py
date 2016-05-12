# encoding: utf-8
# module wnck
# from /usr/lib64/python2.6/site-packages/gtk-2.0/wnck.so
# by generator 1.136
# no doc

# imports
import gobject as __gobject
import gobject._gobject as __gobject__gobject
import gtk as __gtk


# Variables with simple values

CLIENT_TYPE_APPLICATION = 1
CLIENT_TYPE_PAGER = 2

MOTION_DOWN = -2
MOTION_LEFT = -3
MOTION_RIGHT = -4
MOTION_UP = -1

PAGER_DISPLAY_CONTENT = 1
PAGER_DISPLAY_NAME = 0

TASKLIST_ALWAYS_GROUP = 2

TASKLIST_AUTO_GROUP = 1

TASKLIST_NEVER_GROUP = 0

WINDOW_DESKTOP = 1
WINDOW_DIALOG = 3
WINDOW_DOCK = 2

WINDOW_GRAVITY_CENTER = 5
WINDOW_GRAVITY_CURRENT = 0
WINDOW_GRAVITY_EAST = 6
WINDOW_GRAVITY_NORTH = 2
WINDOW_GRAVITY_NORTHEAST = 3
WINDOW_GRAVITY_NORTHWEST = 1
WINDOW_GRAVITY_SOUTH = 8
WINDOW_GRAVITY_SOUTHEAST = 9
WINDOW_GRAVITY_SOUTHWEST = 7
WINDOW_GRAVITY_STATIC = 10
WINDOW_GRAVITY_WEST = 4

WINDOW_MENU = 5
WINDOW_NORMAL = 0
WINDOW_SPLASHSCREEN = 7
WINDOW_TOOLBAR = 4
WINDOW_UTILITY = 6

__version__ = '2.28.0'

# functions

def application_get(*args, **kwargs): # real signature unknown
    pass

def class_group_get(*args, **kwargs): # real signature unknown
    pass

def create_window_action_menu(*args, **kwargs): # real signature unknown
    pass

def gtk_window_set_dock_type(*args, **kwargs): # real signature unknown
    pass

def screen_get(*args, **kwargs): # real signature unknown
    pass

def screen_get_default(*args, **kwargs): # real signature unknown
    pass

def screen_get_for_root(*args, **kwargs): # real signature unknown
    pass

def set_client_type(*args, **kwargs): # real signature unknown
    pass

def window_get(*args, **kwargs): # real signature unknown
    pass

# classes

class Application(__gobject__gobject.GObject):
    """
    Object WnckApplication
    
    Signals from WnckApplication:
      name-changed ()
      icon-changed ()
    
    Signals from GObject:
      notify (GParam)
    """
    def get_icon(self, *args, **kwargs): # real signature unknown
        pass

    def get_icon_is_fallback(self, *args, **kwargs): # real signature unknown
        pass

    def get_icon_name(self, *args, **kwargs): # real signature unknown
        pass

    def get_mini_icon(self, *args, **kwargs): # real signature unknown
        pass

    def get_name(self, *args, **kwargs): # real signature unknown
        pass

    def get_n_windows(self, *args, **kwargs): # real signature unknown
        pass

    def get_pid(self, *args, **kwargs): # real signature unknown
        pass

    def get_startup_id(self, *args, **kwargs): # real signature unknown
        pass

    def get_windows(self, *args, **kwargs): # real signature unknown
        pass

    def get_xid(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class ClassGroup(__gobject__gobject.GObject):
    """
    Object WnckClassGroup
    
    Signals from WnckClassGroup:
      name-changed ()
      icon-changed ()
    
    Signals from GObject:
      notify (GParam)
    """
    def get_icon(self, *args, **kwargs): # real signature unknown
        pass

    def get_mini_icon(self, *args, **kwargs): # real signature unknown
        pass

    def get_name(self, *args, **kwargs): # real signature unknown
        pass

    def get_res_class(self, *args, **kwargs): # real signature unknown
        pass

    def get_windows(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class MotionDirection(__gobject.GEnum):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __enum_values__ = {
        -4: -4,
        -3: -3,
        -2: -2,
        -1: -1,
    }
    __gtype__ = None # (!) real value is ''


class Pager(__gtk.Container):
    """
    Object WnckPager
    
    Signals from GtkWidget:
      composited-changed ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-request (GtkRequisition)
      size-allocate (GdkRectangle)
      state-changed (GtkStateType)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      direction-changed (GtkTextDirection)
      grab-notify (gboolean)
      child-notify (GParam)
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      event (GdkEvent) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      keynav-failed (GtkDirectionType) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      expose-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      client-event (GdkEvent) -> gboolean
      no-expose-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      extension-events -> GdkExtensionMode: Extension events
        The mask that decides what kind of extension events this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      double-buffered -> gboolean: Double Buffered
        Whether or not the widget is double buffered
    
    Signals from GtkObject:
      destroy ()
    
    Properties from GtkObject:
      user-data -> gpointer: User Data
        Anonymous User Data Pointer
    
    Signals from GObject:
      notify (GParam)
    """
    def set_display_mode(self, *args, **kwargs): # real signature unknown
        pass

    def set_n_rows(self, *args, **kwargs): # real signature unknown
        pass

    def set_orientation(self, *args, **kwargs): # real signature unknown
        pass

    def set_screen(self, *args, **kwargs): # real signature unknown
        pass

    def set_shadow_type(self, *args, **kwargs): # real signature unknown
        pass

    def set_show_all(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self): # real signature unknown; restored from __doc__
        """ x.__iter__() <==> iter(x) """
        pass

    __gtype__ = None # (!) real value is ''


class PagerDisplayMode(__gobject.GEnum):
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


class Screen(__gobject__gobject.GObject):
    """
    Object WnckScreen
    
    Signals from WnckScreen:
      window-manager-changed ()
      active-window-changed (WnckWindow)
      active-workspace-changed (WnckWorkspace)
      window-stacking-changed ()
      window-opened (WnckWindow)
      window-closed (WnckWindow)
      workspace-created (WnckWorkspace)
      workspace-destroyed (WnckWorkspace)
      application-opened (WnckApplication)
      application-closed (WnckApplication)
      class-group-opened (WnckClassGroup)
      class-group-closed (WnckClassGroup)
      background-changed ()
      showing-desktop-changed ()
      viewports-changed ()
    
    Signals from GObject:
      notify (GParam)
    """
    def change_workspace_count(self, *args, **kwargs): # real signature unknown
        pass

    def force_update(self, *args, **kwargs): # real signature unknown
        pass

    def get_active_window(self, *args, **kwargs): # real signature unknown
        pass

    def get_active_workspace(self, *args, **kwargs): # real signature unknown
        pass

    def get_background_pixmap(self, *args, **kwargs): # real signature unknown
        pass

    def get_height(self, *args, **kwargs): # real signature unknown
        pass

    def get_number(self, *args, **kwargs): # real signature unknown
        pass

    def get_previously_active_window(self, *args, **kwargs): # real signature unknown
        pass

    def get_showing_desktop(self, *args, **kwargs): # real signature unknown
        pass

    def get_width(self, *args, **kwargs): # real signature unknown
        pass

    def get_windows(self, *args, **kwargs): # real signature unknown
        pass

    def get_windows_stacked(self, *args, **kwargs): # real signature unknown
        pass

    def get_window_manager_name(self, *args, **kwargs): # real signature unknown
        pass

    def get_workspace(self, *args, **kwargs): # real signature unknown
        pass

    def get_workspaces(self, *args, **kwargs): # real signature unknown
        pass

    def get_workspace_count(self, *args, **kwargs): # real signature unknown
        pass

    def get_workspace_index(self, *args, **kwargs): # real signature unknown
        pass

    def get_workspace_neighbor(self, *args, **kwargs): # real signature unknown
        pass

    def move_viewport(self, *args, **kwargs): # real signature unknown
        pass

    def net_wm_supports(self, *args, **kwargs): # real signature unknown
        pass

    def release_workspace_layout(self, *args, **kwargs): # real signature unknown
        pass

    def toggle_showing_desktop(self, *args, **kwargs): # real signature unknown
        pass

    def try_set_workspace_layout(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class Selector(__gtk.MenuBar):
    """
    Object WnckSelector
    
    Properties from GtkMenuBar:
      pack-direction -> GtkPackDirection: Pack direction
        The pack direction of the menubar
      child-pack-direction -> GtkPackDirection: Child Pack direction
        The child pack direction of the menubar
    
    Signals from GtkMenuShell:
      deactivate ()
      selection-done ()
      move-current (GtkMenuDirectionType)
      activate-current (gboolean)
      cancel ()
      cycle-focus (GtkDirectionType)
      move-selected (gint) -> gboolean
      insert (GtkWidget, gint)
    
    Properties from GtkMenuShell:
      take-focus -> gboolean: Take Focus
        A boolean that determines whether the menu grabs the keyboard focus
    
    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)
    
    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container
    
    Signals from GtkWidget:
      composited-changed ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-request (GtkRequisition)
      size-allocate (GdkRectangle)
      state-changed (GtkStateType)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      direction-changed (GtkTextDirection)
      grab-notify (gboolean)
      child-notify (GParam)
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      event (GdkEvent) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      keynav-failed (GtkDirectionType) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      expose-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      client-event (GdkEvent) -> gboolean
      no-expose-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      extension-events -> GdkExtensionMode: Extension events
        The mask that decides what kind of extension events this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      double-buffered -> gboolean: Double Buffered
        Whether or not the widget is double buffered
    
    Signals from GtkObject:
      destroy ()
    
    Properties from GtkObject:
      user-data -> gpointer: User Data
        Anonymous User Data Pointer
    
    Signals from GObject:
      notify (GParam)
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self): # real signature unknown; restored from __doc__
        """ x.__iter__() <==> iter(x) """
        pass

    __gtype__ = None # (!) real value is ''


class Tasklist(__gtk.Container):
    """
    Object WnckTasklist
    
    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)
    
    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container
    
    Signals from GtkWidget:
      composited-changed ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-request (GtkRequisition)
      size-allocate (GdkRectangle)
      state-changed (GtkStateType)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      direction-changed (GtkTextDirection)
      grab-notify (gboolean)
      child-notify (GParam)
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      event (GdkEvent) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      keynav-failed (GtkDirectionType) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      expose-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      client-event (GdkEvent) -> gboolean
      no-expose-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      extension-events -> GdkExtensionMode: Extension events
        The mask that decides what kind of extension events this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      double-buffered -> gboolean: Double Buffered
        Whether or not the widget is double buffered
    
    Signals from GtkObject:
      destroy ()
    
    Properties from GtkObject:
      user-data -> gpointer: User Data
        Anonymous User Data Pointer
    
    Signals from GObject:
      notify (GParam)
    """
    def get_minimum_height(self, *args, **kwargs): # real signature unknown
        pass

    def get_minimum_width(self, *args, **kwargs): # real signature unknown
        pass

    def get_size_hint_list(self, *args, **kwargs): # real signature unknown
        pass

    def set_button_relief(self, *args, **kwargs): # real signature unknown
        pass

    def set_grouping(self, *args, **kwargs): # real signature unknown
        pass

    def set_grouping_limit(self, *args, **kwargs): # real signature unknown
        pass

    def set_include_all_workspaces(self, *args, **kwargs): # real signature unknown
        pass

    def set_minimum_height(self, *args, **kwargs): # real signature unknown
        pass

    def set_minimum_width(self, *args, **kwargs): # real signature unknown
        pass

    def set_screen(self, *args, **kwargs): # real signature unknown
        pass

    def set_switch_workspace_on_unminimize(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self): # real signature unknown; restored from __doc__
        """ x.__iter__() <==> iter(x) """
        pass

    __gtype__ = None # (!) real value is ''


class TasklistGroupingType(__gobject.GEnum):
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


class Window(__gobject__gobject.GObject):
    """
    Object WnckWindow
    
    Signals from WnckWindow:
      state-changed (WnckWindowState, WnckWindowState)
      name-changed ()
      icon-changed ()
      workspace-changed ()
      actions-changed (WnckWindowActions, WnckWindowActions)
      geometry-changed ()
    
    Signals from GObject:
      notify (GParam)
    """
    def activate(self, *args, **kwargs): # real signature unknown
        pass

    def activate_transient(self, *args, **kwargs): # real signature unknown
        pass

    def close(self, *args, **kwargs): # real signature unknown
        pass

    def get_actions(self, *args, **kwargs): # real signature unknown
        pass

    def get_application(self, *args, **kwargs): # real signature unknown
        pass

    def get_class_group(self, *args, **kwargs): # real signature unknown
        pass

    def get_client_window_geometry(self, *args, **kwargs): # real signature unknown
        pass

    def get_geometry(self, *args, **kwargs): # real signature unknown
        pass

    def get_group_leader(self, *args, **kwargs): # real signature unknown
        pass

    def get_icon(self, *args, **kwargs): # real signature unknown
        pass

    def get_icon_is_fallback(self, *args, **kwargs): # real signature unknown
        pass

    def get_icon_name(self, *args, **kwargs): # real signature unknown
        pass

    def get_mini_icon(self, *args, **kwargs): # real signature unknown
        pass

    def get_name(self, *args, **kwargs): # real signature unknown
        pass

    def get_pid(self, *args, **kwargs): # real signature unknown
        pass

    def get_screen(self, *args, **kwargs): # real signature unknown
        pass

    def get_session_id(self, *args, **kwargs): # real signature unknown
        pass

    def get_session_id_utf8(self, *args, **kwargs): # real signature unknown
        pass

    def get_sort_order(self, *args, **kwargs): # real signature unknown
        pass

    def get_state(self, *args, **kwargs): # real signature unknown
        pass

    def get_transient(self, *args, **kwargs): # real signature unknown
        pass

    def get_window_type(self, *args, **kwargs): # real signature unknown
        pass

    def get_workspace(self, *args, **kwargs): # real signature unknown
        pass

    def get_xid(self, *args, **kwargs): # real signature unknown
        pass

    def has_icon_name(self, *args, **kwargs): # real signature unknown
        pass

    def has_name(self, *args, **kwargs): # real signature unknown
        pass

    def is_above(self, *args, **kwargs): # real signature unknown
        pass

    def is_active(self, *args, **kwargs): # real signature unknown
        pass

    def is_below(self, *args, **kwargs): # real signature unknown
        pass

    def is_fullscreen(self, *args, **kwargs): # real signature unknown
        pass

    def is_in_viewport(self, *args, **kwargs): # real signature unknown
        pass

    def is_maximized(self, *args, **kwargs): # real signature unknown
        pass

    def is_maximized_horizontally(self, *args, **kwargs): # real signature unknown
        pass

    def is_maximized_vertically(self, *args, **kwargs): # real signature unknown
        pass

    def is_minimized(self, *args, **kwargs): # real signature unknown
        pass

    def is_most_recently_activated(self, *args, **kwargs): # real signature unknown
        pass

    def is_on_workspace(self, *args, **kwargs): # real signature unknown
        pass

    def is_pinned(self, *args, **kwargs): # real signature unknown
        pass

    def is_shaded(self, *args, **kwargs): # real signature unknown
        pass

    def is_skip_pager(self, *args, **kwargs): # real signature unknown
        pass

    def is_skip_tasklist(self, *args, **kwargs): # real signature unknown
        pass

    def is_sticky(self, *args, **kwargs): # real signature unknown
        pass

    def is_visible_on_workspace(self, *args, **kwargs): # real signature unknown
        pass

    def keyboard_move(self, *args, **kwargs): # real signature unknown
        pass

    def keyboard_size(self, *args, **kwargs): # real signature unknown
        pass

    def make_above(self, *args, **kwargs): # real signature unknown
        pass

    def make_below(self, *args, **kwargs): # real signature unknown
        pass

    def maximize(self, *args, **kwargs): # real signature unknown
        pass

    def maximize_horizontally(self, *args, **kwargs): # real signature unknown
        pass

    def maximize_vertically(self, *args, **kwargs): # real signature unknown
        pass

    def minimize(self, *args, **kwargs): # real signature unknown
        pass

    def move_to_workspace(self, *args, **kwargs): # real signature unknown
        pass

    def needs_attention(self, *args, **kwargs): # real signature unknown
        pass

    def or_transient_needs_attention(self, *args, **kwargs): # real signature unknown
        pass

    def pin(self, *args, **kwargs): # real signature unknown
        pass

    def set_fullscreen(self, *args, **kwargs): # real signature unknown
        pass

    def set_geometry(self, *args, **kwargs): # real signature unknown
        pass

    def set_icon_geometry(self, *args, **kwargs): # real signature unknown
        pass

    def set_skip_pager(self, *args, **kwargs): # real signature unknown
        pass

    def set_skip_tasklist(self, *args, **kwargs): # real signature unknown
        pass

    def set_sort_order(self, *args, **kwargs): # real signature unknown
        pass

    def set_window_type(self, *args, **kwargs): # real signature unknown
        pass

    def shade(self, *args, **kwargs): # real signature unknown
        pass

    def stick(self, *args, **kwargs): # real signature unknown
        pass

    def transient_is_most_recently_activated(self, *args, **kwargs): # real signature unknown
        pass

    def unmake_above(self, *args, **kwargs): # real signature unknown
        pass

    def unmake_below(self, *args, **kwargs): # real signature unknown
        pass

    def unmaximize(self, *args, **kwargs): # real signature unknown
        pass

    def unmaximize_horizontally(self, *args, **kwargs): # real signature unknown
        pass

    def unmaximize_vertically(self, *args, **kwargs): # real signature unknown
        pass

    def unminimize(self, *args, **kwargs): # real signature unknown
        pass

    def unpin(self, *args, **kwargs): # real signature unknown
        pass

    def unshade(self, *args, **kwargs): # real signature unknown
        pass

    def unstick(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class WindowGravity(__gobject.GEnum):
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


class WindowType(__gobject.GEnum):
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
    }
    __gtype__ = None # (!) real value is ''


class Workspace(__gobject__gobject.GObject):
    """
    Object WnckWorkspace
    
    Signals from WnckWorkspace:
      name-changed ()
    
    Signals from GObject:
      notify (GParam)
    """
    def activate(self, *args, **kwargs): # real signature unknown
        pass

    def change_name(self, *args, **kwargs): # real signature unknown
        pass

    def get_height(self, *args, **kwargs): # real signature unknown
        pass

    def get_layout_column(self, *args, **kwargs): # real signature unknown
        pass

    def get_layout_row(self, *args, **kwargs): # real signature unknown
        pass

    def get_name(self, *args, **kwargs): # real signature unknown
        pass

    def get_neighbor(self, *args, **kwargs): # real signature unknown
        pass

    def get_number(self, *args, **kwargs): # real signature unknown
        pass

    def get_screen(self, *args, **kwargs): # real signature unknown
        pass

    def get_viewport_x(self, *args, **kwargs): # real signature unknown
        pass

    def get_viewport_y(self, *args, **kwargs): # real signature unknown
        pass

    def get_width(self, *args, **kwargs): # real signature unknown
        pass

    def is_virtual(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


