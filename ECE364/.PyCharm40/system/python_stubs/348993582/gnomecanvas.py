# encoding: utf-8
# module gnomecanvas
# from /usr/lib64/python2.6/site-packages/gtk-2.0/gnomecanvas.so
# by generator 1.136
# no doc

# imports
import gobject as __gobject
import gtk as __gtk


# Variables with simple values

CURVETO = 2

END = 4

LINETO = 3

MOVETO = 0

MOVETO_OPEN = 1

# functions

def path_def_new(*args, **kwargs): # real signature unknown
    pass

# classes

class Canvas(__gtk.Layout):
    """
    Object GnomeCanvas
    
    Signals from GnomeCanvas:
      draw-background (GdkDrawable, gint, gint, gint, gint)
      render-background (gpointer)
    
    Properties from GnomeCanvas:
      aa -> gboolean: Antialiased
        The antialiasing mode of the canvas.
      focused-item -> GnomeCanvasItem: focused-item
    
    Signals from GtkLayout:
      set-scroll-adjustments (GtkAdjustment, GtkAdjustment)
    
    Properties from GtkLayout:
      hadjustment -> GtkAdjustment: Horizontal adjustment
        The GtkAdjustment for the horizontal position
      vadjustment -> GtkAdjustment: Vertical adjustment
        The GtkAdjustment for the vertical position
      width -> guint: Width
        The width of the layout
      height -> guint: Height
        The height of the layout
    
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
    def c2w(self, *args, **kwargs): # real signature unknown
        pass

    def get_center_scroll_region(self, *args, **kwargs): # real signature unknown
        pass

    def get_color(self, *args, **kwargs): # real signature unknown
        pass

    def get_color_pixel(self, *args, **kwargs): # real signature unknown
        pass

    def get_dither(self, *args, **kwargs): # real signature unknown
        pass

    def get_item_at(self, *args, **kwargs): # real signature unknown
        pass

    def get_scroll_offsets(self, *args, **kwargs): # real signature unknown
        pass

    def get_scroll_region(self, *args, **kwargs): # real signature unknown
        pass

    def root(self, *args, **kwargs): # real signature unknown
        pass

    def scroll_to(self, *args, **kwargs): # real signature unknown
        pass

    def set_center_scroll_region(self, *args, **kwargs): # real signature unknown
        pass

    def set_dither(self, *args, **kwargs): # real signature unknown
        pass

    def set_pixels_per_unit(self, *args, **kwargs): # real signature unknown
        pass

    def set_scroll_region(self, *args, **kwargs): # real signature unknown
        pass

    def update_now(self, *args, **kwargs): # real signature unknown
        pass

    def w2c(self, *args, **kwargs): # real signature unknown
        pass

    def w2c_affine(self, *args, **kwargs): # real signature unknown
        pass

    def w2c_d(self, *args, **kwargs): # real signature unknown
        pass

    def window_to_world(self, *args, **kwargs): # real signature unknown
        pass

    def world_to_window(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self): # real signature unknown; restored from __doc__
        """ x.__iter__() <==> iter(x) """
        pass

    __gtype__ = None # (!) real value is ''


class CanvasItem(__gtk.Object):
    """
    Object GnomeCanvasItem
    
    Signals from GnomeCanvasItem:
      event (GdkEvent) -> gboolean
    
    Properties from GnomeCanvasItem:
      parent -> GnomeCanvasItem: parent
    
    Signals from GtkObject:
      destroy ()
    
    Properties from GtkObject:
      user-data -> gpointer: User Data
        Anonymous User Data Pointer
    
    Signals from GObject:
      notify (GParam)
    """
    def affine_absolute(self, *args, **kwargs): # real signature unknown
        pass

    def affine_relative(self, *args, **kwargs): # real signature unknown
        pass

    def get_bounds(self, *args, **kwargs): # real signature unknown
        pass

    def grab(self, *args, **kwargs): # real signature unknown
        pass

    def grab_focus(self, *args, **kwargs): # real signature unknown
        pass

    def hide(self, *args, **kwargs): # real signature unknown
        pass

    def i2c_affine(self, *args, **kwargs): # real signature unknown
        pass

    def i2w(self, *args, **kwargs): # real signature unknown
        pass

    def i2w_affine(self, *args, **kwargs): # real signature unknown
        pass

    def lower(self, *args, **kwargs): # real signature unknown
        pass

    def lower_to_bottom(self, *args, **kwargs): # real signature unknown
        pass

    def move(self, *args, **kwargs): # real signature unknown
        pass

    def raise_(self, *args, **kwargs): # real signature unknown
        pass

    def raise_to_top(self, *args, **kwargs): # real signature unknown
        pass

    def reparent(self, *args, **kwargs): # real signature unknown
        pass

    def set(self, *args, **kwargs): # real signature unknown
        pass

    def show(self, *args, **kwargs): # real signature unknown
        pass

    def w2i(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class CanvasShape(CanvasItem):
    """
    Object GnomeCanvasShape
    
    Properties from GnomeCanvasShape:
      fill-color -> gchararray: fill-color
      fill-color-gdk -> GdkColor: fill-color-gdk
      fill-color-rgba -> guint: fill-color-rgba
      outline-color -> gchararray: outline-color
      outline-color-gdk -> GdkColor: outline-color-gdk
      outline-color-rgba -> guint: outline-color-rgba
      fill-stipple -> GdkDrawable: fill-stipple
      outline-stipple -> GdkDrawable: outline-stipple
      width-pixels -> guint: width-pixels
      width-units -> gdouble: width-units
      cap-style -> GdkCapStyle: cap-style
      join-style -> GdkJoinStyle: join-style
      wind -> guint: wind
      miterlimit -> gdouble: miterlimit
      dash -> gpointer: dash
    
    Signals from GnomeCanvasItem:
      event (GdkEvent) -> gboolean
    
    Properties from GnomeCanvasItem:
      parent -> GnomeCanvasItem: parent
    
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

    __gtype__ = None # (!) real value is ''


class CanvasBpath(CanvasShape):
    """
    Object GnomeCanvasBpath
    
    Properties from GnomeCanvasBpath:
      bpath -> GnomeCanvasPathDef: bpath
    
    Properties from GnomeCanvasShape:
      fill-color -> gchararray: fill-color
      fill-color-gdk -> GdkColor: fill-color-gdk
      fill-color-rgba -> guint: fill-color-rgba
      outline-color -> gchararray: outline-color
      outline-color-gdk -> GdkColor: outline-color-gdk
      outline-color-rgba -> guint: outline-color-rgba
      fill-stipple -> GdkDrawable: fill-stipple
      outline-stipple -> GdkDrawable: outline-stipple
      width-pixels -> guint: width-pixels
      width-units -> gdouble: width-units
      cap-style -> GdkCapStyle: cap-style
      join-style -> GdkJoinStyle: join-style
      wind -> guint: wind
      miterlimit -> gdouble: miterlimit
      dash -> gpointer: dash
    
    Signals from GnomeCanvasItem:
      event (GdkEvent) -> gboolean
    
    Properties from GnomeCanvasItem:
      parent -> GnomeCanvasItem: parent
    
    Signals from GtkObject:
      destroy ()
    
    Properties from GtkObject:
      user-data -> gpointer: User Data
        Anonymous User Data Pointer
    
    Signals from GObject:
      notify (GParam)
    """
    def set_bpath(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class CanvasGroup(CanvasItem):
    """
    Object GnomeCanvasGroup
    
    Properties from GnomeCanvasGroup:
      x -> gdouble: X
        X
      y -> gdouble: Y
        Y
    
    Signals from GnomeCanvasItem:
      event (GdkEvent) -> gboolean
    
    Properties from GnomeCanvasItem:
      parent -> GnomeCanvasItem: parent
    
    Signals from GtkObject:
      destroy ()
    
    Properties from GtkObject:
      user-data -> gpointer: User Data
        Anonymous User Data Pointer
    
    Signals from GObject:
      notify (GParam)
    """
    def add(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    item_list = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __gtype__ = None # (!) real value is ''


class CanvasClipgroup(CanvasGroup):
    """
    Object GnomeCanvasClipgroup
    
    Properties from GnomeCanvasClipgroup:
      path -> gpointer: path
      wind -> guint: wind
    
    Properties from GnomeCanvasGroup:
      x -> gdouble: X
        X
      y -> gdouble: Y
        Y
    
    Signals from GnomeCanvasItem:
      event (GdkEvent) -> gboolean
    
    Properties from GnomeCanvasItem:
      parent -> GnomeCanvasItem: parent
    
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

    __gtype__ = None # (!) real value is ''


class CanvasRE(CanvasShape):
    """
    Object GnomeCanvasRE
    
    Properties from GnomeCanvasRE:
      x1 -> gdouble: x1
      y1 -> gdouble: y1
      x2 -> gdouble: x2
      y2 -> gdouble: y2
    
    Properties from GnomeCanvasShape:
      fill-color -> gchararray: fill-color
      fill-color-gdk -> GdkColor: fill-color-gdk
      fill-color-rgba -> guint: fill-color-rgba
      outline-color -> gchararray: outline-color
      outline-color-gdk -> GdkColor: outline-color-gdk
      outline-color-rgba -> guint: outline-color-rgba
      fill-stipple -> GdkDrawable: fill-stipple
      outline-stipple -> GdkDrawable: outline-stipple
      width-pixels -> guint: width-pixels
      width-units -> gdouble: width-units
      cap-style -> GdkCapStyle: cap-style
      join-style -> GdkJoinStyle: join-style
      wind -> guint: wind
      miterlimit -> gdouble: miterlimit
      dash -> gpointer: dash
    
    Signals from GnomeCanvasItem:
      event (GdkEvent) -> gboolean
    
    Properties from GnomeCanvasItem:
      parent -> GnomeCanvasItem: parent
    
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

    __gtype__ = None # (!) real value is ''


class CanvasEllipse(CanvasRE):
    """
    Object GnomeCanvasEllipse
    
    Properties from GnomeCanvasRE:
      x1 -> gdouble: x1
      y1 -> gdouble: y1
      x2 -> gdouble: x2
      y2 -> gdouble: y2
    
    Properties from GnomeCanvasShape:
      fill-color -> gchararray: fill-color
      fill-color-gdk -> GdkColor: fill-color-gdk
      fill-color-rgba -> guint: fill-color-rgba
      outline-color -> gchararray: outline-color
      outline-color-gdk -> GdkColor: outline-color-gdk
      outline-color-rgba -> guint: outline-color-rgba
      fill-stipple -> GdkDrawable: fill-stipple
      outline-stipple -> GdkDrawable: outline-stipple
      width-pixels -> guint: width-pixels
      width-units -> gdouble: width-units
      cap-style -> GdkCapStyle: cap-style
      join-style -> GdkJoinStyle: join-style
      wind -> guint: wind
      miterlimit -> gdouble: miterlimit
      dash -> gpointer: dash
    
    Signals from GnomeCanvasItem:
      event (GdkEvent) -> gboolean
    
    Properties from GnomeCanvasItem:
      parent -> GnomeCanvasItem: parent
    
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

    __gtype__ = None # (!) real value is ''


class CanvasLine(CanvasItem):
    """
    Object GnomeCanvasLine
    
    Properties from GnomeCanvasLine:
      points -> GnomeCanvasPoints: points
      fill-color -> gchararray: fill-color
      fill-color-gdk -> GdkColor: fill-color-gdk
      fill-color-rgba -> guint: fill-color-rgba
      fill-stipple -> GdkDrawable: fill-stipple
      width-pixels -> guint: width-pixels
      width-units -> gdouble: width-units
      cap-style -> GdkCapStyle: cap-style
      join-style -> GdkJoinStyle: join-style
      line-style -> GdkLineStyle: line-style
      first-arrowhead -> gboolean: first-arrowhead
      last-arrowhead -> gboolean: last-arrowhead
      smooth -> gboolean: smooth
      spline-steps -> guint: spline-steps
      arrow-shape-a -> gdouble: arrow-shape-a
      arrow-shape-b -> gdouble: arrow-shape-b
      arrow-shape-c -> gdouble: arrow-shape-c
    
    Signals from GnomeCanvasItem:
      event (GdkEvent) -> gboolean
    
    Properties from GnomeCanvasItem:
      parent -> GnomeCanvasItem: parent
    
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

    __gtype__ = None # (!) real value is ''


class CanvasPathDef(__gobject.GBoxed):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class CanvasPixbuf(CanvasItem):
    """
    Object GnomeCanvasPixbuf
    
    Properties from GnomeCanvasPixbuf:
      pixbuf -> GdkPixbuf: pixbuf
      width -> gdouble: width
      width-set -> gboolean: width-set
      width-in-pixels -> gboolean: width-in-pixels
      height -> gdouble: height
      height-set -> gboolean: height-set
      height-in-pixels -> gboolean: height-in-pixels
      x -> gdouble: x
      x-in-pixels -> gboolean: x-in-pixels
      y -> gdouble: y
      y-in-pixels -> gboolean: y-in-pixels
      anchor -> GtkAnchorType: anchor
    
    Signals from GnomeCanvasItem:
      event (GdkEvent) -> gboolean
    
    Properties from GnomeCanvasItem:
      parent -> GnomeCanvasItem: parent
    
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

    __gtype__ = None # (!) real value is ''


class CanvasPolygon(CanvasShape):
    """
    Object GnomeCanvasPolygon
    
    Properties from GnomeCanvasPolygon:
      points -> GnomeCanvasPoints: points
    
    Properties from GnomeCanvasShape:
      fill-color -> gchararray: fill-color
      fill-color-gdk -> GdkColor: fill-color-gdk
      fill-color-rgba -> guint: fill-color-rgba
      outline-color -> gchararray: outline-color
      outline-color-gdk -> GdkColor: outline-color-gdk
      outline-color-rgba -> guint: outline-color-rgba
      fill-stipple -> GdkDrawable: fill-stipple
      outline-stipple -> GdkDrawable: outline-stipple
      width-pixels -> guint: width-pixels
      width-units -> gdouble: width-units
      cap-style -> GdkCapStyle: cap-style
      join-style -> GdkJoinStyle: join-style
      wind -> guint: wind
      miterlimit -> gdouble: miterlimit
      dash -> gpointer: dash
    
    Signals from GnomeCanvasItem:
      event (GdkEvent) -> gboolean
    
    Properties from GnomeCanvasItem:
      parent -> GnomeCanvasItem: parent
    
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

    __gtype__ = None # (!) real value is ''


class CanvasRect(CanvasRE):
    """
    Object GnomeCanvasRect
    
    Properties from GnomeCanvasRE:
      x1 -> gdouble: x1
      y1 -> gdouble: y1
      x2 -> gdouble: x2
      y2 -> gdouble: y2
    
    Properties from GnomeCanvasShape:
      fill-color -> gchararray: fill-color
      fill-color-gdk -> GdkColor: fill-color-gdk
      fill-color-rgba -> guint: fill-color-rgba
      outline-color -> gchararray: outline-color
      outline-color-gdk -> GdkColor: outline-color-gdk
      outline-color-rgba -> guint: outline-color-rgba
      fill-stipple -> GdkDrawable: fill-stipple
      outline-stipple -> GdkDrawable: outline-stipple
      width-pixels -> guint: width-pixels
      width-units -> gdouble: width-units
      cap-style -> GdkCapStyle: cap-style
      join-style -> GdkJoinStyle: join-style
      wind -> guint: wind
      miterlimit -> gdouble: miterlimit
      dash -> gpointer: dash
    
    Signals from GnomeCanvasItem:
      event (GdkEvent) -> gboolean
    
    Properties from GnomeCanvasItem:
      parent -> GnomeCanvasItem: parent
    
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

    __gtype__ = None # (!) real value is ''


class CanvasRichText(CanvasItem):
    """
    Object GnomeCanvasRichText
    
    Signals from GnomeCanvasRichText:
      tag-changed (GObject)
    
    Properties from GnomeCanvasRichText:
      text -> gchararray: Text
        Text to display
      x -> gdouble: X
        X position
      y -> gdouble: Y
        Y position
      width -> gdouble: Width
        Width for text box
      height -> gdouble: Height
        Height for text box
      editable -> gboolean: Editable
        Is this rich text item editable?
      visible -> gboolean: Visible
        Is this rich text item visible?
      cursor-visible -> gboolean: Cursor Visible
        Is the cursor visible in this rich text item?
      cursor-blink -> gboolean: Cursor Blink
        Does the cursor blink in this rich text item?
      grow-height -> gboolean: Grow Height
        Should the text box height grow if the text does not fit?
      wrap-mode -> GtkWrapMode: Wrap Mode
        Wrap mode for multiline text
      justification -> GtkJustification: Justification
        Justification mode
      direction -> GtkDirectionType: Direction
        Text direction
      anchor -> GtkAnchorType: Anchor
        Anchor point for text
      pixels-above-lines -> gint: Pixels Above Lines
        Number of pixels to put above lines
      pixels-below-lines -> gint: Pixels Below Lines
        Number of pixels to put below lines
      pixels-inside-wrap -> gint: Pixels Inside Wrap
        Number of pixels to put inside the wrap
      left-margin -> gint: Left Margin
        Number of pixels in the left margin
      right-margin -> gint: Right Margin
        Number of pixels in the right margin
      indent -> gint: Indentation
        Number of pixels for indentation
    
    Signals from GnomeCanvasItem:
      event (GdkEvent) -> gboolean
    
    Properties from GnomeCanvasItem:
      parent -> GnomeCanvasItem: parent
    
    Signals from GtkObject:
      destroy ()
    
    Properties from GtkObject:
      user-data -> gpointer: User Data
        Anonymous User Data Pointer
    
    Signals from GObject:
      notify (GParam)
    """
    def copy_clipboard(self, *args, **kwargs): # real signature unknown
        pass

    def cut_clipboard(self, *args, **kwargs): # real signature unknown
        pass

    def get_buffer(self, *args, **kwargs): # real signature unknown
        pass

    def get_iter_at_location(self, *args, **kwargs): # real signature unknown
        pass

    def get_iter_location(self, *args, **kwargs): # real signature unknown
        pass

    def paste_clipboard(self, *args, **kwargs): # real signature unknown
        pass

    def set_buffer(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class CanvasText(CanvasItem):
    """
    Object GnomeCanvasText
    
    Properties from GnomeCanvasText:
      text -> gchararray: Text
        Text to render
      markup -> gchararray: Markup
        Marked up text to render
      x -> gdouble: x
      y -> gdouble: y
      font -> gchararray: Font
        Font description as a string
      font-desc -> PangoFontDescription: Font description
        Font description as a PangoFontDescription struct
      family -> gchararray: Font family
        Name of the font family, e.g. Sans, Helvetica, Times, Monospace
      family-set -> gboolean: Font family set
        Whether this tag affects the font family
      attributes -> PangoAttrList: attributes
      style -> PangoStyle: Font style
        Font style
      style-set -> gboolean: Font style set
        Whether this tag affects the font style
      variant -> PangoVariant: Font variant
        Font variant
      variant-set -> gboolean: Font variant set
        Whether this tag affects the font variant
      weight -> gint: Font weight
        Font weight
      weight-set -> gboolean: Font weight set
        Whether this tag affects the font weight
      stretch -> PangoStretch: Font stretch
        Font stretch
      stretch-set -> gboolean: Font stretch set
        Whether this tag affects the font stretch
      size -> gint: Font size
        Font size (as a multiple of PANGO_SCALE, eg. 12*PANGO_SCALE for a 12pt font size)
      size-set -> gboolean: Font size set
        Whether this tag affects the font size
      size-points -> gdouble: Font points
        Font size in points (eg. 12 for a 12pt font size)
      strikethrough -> gboolean: Strikethrough
        Whether to strike through the text
      strikethrough-set -> gboolean: Strikethrough set
        Whether this tag affects strikethrough
      underline -> PangoUnderline: Underline
        Style of underline for this text
      underline-set -> gboolean: Underline set
        Whether this tag affects underlining
      rise -> gint: Rise
        Offset of text above the baseline (below the baseline if rise is negative)
      rise-set -> gboolean: Rise set
        Whether this tag affects the rise
      scale -> gdouble: Scale
        Size of font, relative to default size
      scale-set -> gboolean: Scale set
        Whether this tag affects font scaling
      anchor -> GtkAnchorType: anchor
      justification -> GtkJustification: justification
      clip-width -> gdouble: clip-width
      clip-height -> gdouble: clip-height
      clip -> gboolean: clip
      x-offset -> gdouble: x-offset
      y-offset -> gdouble: y-offset
      fill-color -> gchararray: Color
        Text color, as string
      fill-color-gdk -> GdkColor: Color
        Text color, as a GdkColor
      fill-color-rgba -> guint: Color
        Text color, as an R/G/B/A combined integer
      fill-stipple -> GdkDrawable: fill-stipple
      text-width -> gdouble: Text width
        Width of the rendered text
      text-height -> gdouble: Text height
        Height of the rendered text
    
    Signals from GnomeCanvasItem:
      event (GdkEvent) -> gboolean
    
    Properties from GnomeCanvasItem:
      parent -> GnomeCanvasItem: parent
    
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

    __gtype__ = None # (!) real value is ''


class CanvasWidget(CanvasItem):
    """
    Object GnomeCanvasWidget
    
    Properties from GnomeCanvasWidget:
      widget -> GtkWidget: widget
      x -> gdouble: x
      y -> gdouble: y
      width -> gdouble: width
      height -> gdouble: height
      anchor -> GtkAnchorType: anchor
      size-pixels -> gboolean: size-pixels
    
    Signals from GnomeCanvasItem:
      event (GdkEvent) -> gboolean
    
    Properties from GnomeCanvasItem:
      parent -> GnomeCanvasItem: parent
    
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

    __gtype__ = None # (!) real value is ''


