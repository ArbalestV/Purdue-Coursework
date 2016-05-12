# encoding: utf-8
# module gtksourceview2
# from /usr/lib64/python2.6/site-packages/gtksourceview2.so
# by generator 1.136
# no doc

# imports
import gobject as __gobject
import gobject._gobject as __gobject__gobject
import gtk as __gtk


# Variables with simple values

DRAW_SPACES_ALL = 15
DRAW_SPACES_NBSP = 8
DRAW_SPACES_NEWLINE = 4
DRAW_SPACES_SPACE = 1
DRAW_SPACES_TAB = 2

SEARCH_CASE_INSENSITIVE = 4

SEARCH_TEXT_ONLY = 2

SEARCH_VISIBLE_ONLY = 1

SMART_HOME_END_AFTER = 2
SMART_HOME_END_ALWAYS = 3
SMART_HOME_END_BEFORE = 1
SMART_HOME_END_DISABLED = 0

__version__ = '2.8.0'

# functions

def iter_backward_search(*args, **kwargs): # real signature unknown
    pass

def iter_forward_search(*args, **kwargs): # real signature unknown
    pass

def language_manager_get_default(*args, **kwargs): # real signature unknown
    pass

def print_compositor_new_from_view(*args, **kwargs): # real signature unknown
    pass

def style_scheme_manager_get_default(*args, **kwargs): # real signature unknown
    pass

# classes

class Buffer(__gtk.TextBuffer):
    """
    Object GtkSourceBuffer
    
    Signals from GtkSourceBuffer:
      highlight-updated (GtkTextIter, GtkTextIter)
      source-mark-updated (GtkTextMark)
    
    Properties from GtkSourceBuffer:
      can-undo -> gboolean: Can undo
        Whether Undo operation is possible
      can-redo -> gboolean: Can redo
        Whether Redo operation is possible
      highlight-syntax -> gboolean: Highlight Syntax
        Whether to highlight syntax in the buffer
      highlight-matching-brackets -> gboolean: Highlight Matching Brackets
        Whether to highlight matching brackets
      max-undo-levels -> gint: Maximum Undo Levels
        Number of undo levels for the buffer
      language -> GtkSourceLanguage: Language
        Language object to get highlighting patterns from
      style-scheme -> GtkSourceStyleScheme: Style scheme
        Style scheme
    
    Signals from GtkTextBuffer:
      insert-text (GtkTextIter, gchararray, gint)
      insert-pixbuf (GtkTextIter, GdkPixbuf)
      insert-child-anchor (GtkTextIter, GtkTextChildAnchor)
      delete-range (GtkTextIter, GtkTextIter)
      changed ()
      modified-changed ()
      mark-set (GtkTextIter, GtkTextMark)
      mark-deleted (GtkTextMark)
      apply-tag (GtkTextTag, GtkTextIter, GtkTextIter)
      remove-tag (GtkTextTag, GtkTextIter, GtkTextIter)
      begin-user-action ()
      end-user-action ()
      paste-done (GtkClipboard)
    
    Properties from GtkTextBuffer:
      tag-table -> GtkTextTagTable: Tag Table
        Text Tag Table
      text -> gchararray: Text
        Current text of the buffer
      has-selection -> gboolean: Has selection
        Whether the buffer has some text currently selected
      cursor-position -> gint: Cursor position
        The position of the insert mark (as offset from the beginning of the buffer)
      copy-target-list -> GtkTargetList: Copy target list
        The list of targets this buffer supports for clipboard copying and DND source
      paste-target-list -> GtkTargetList: Paste target list
        The list of targets this buffer supports for clipboard pasting and DND destination
    
    Signals from GObject:
      notify (GParam)
    """
    def backward_iter_to_source_mark(self, *args, **kwargs): # real signature unknown
        pass

    def begin_not_undoable_action(self, *args, **kwargs): # real signature unknown
        pass

    def can_redo(self, *args, **kwargs): # real signature unknown
        pass

    def can_undo(self, *args, **kwargs): # real signature unknown
        pass

    def create_source_mark(self, *args, **kwargs): # real signature unknown
        pass

    def end_not_undoable_action(self, *args, **kwargs): # real signature unknown
        pass

    def ensure_highlight(self, *args, **kwargs): # real signature unknown
        pass

    def forward_iter_to_source_mark(self, *args, **kwargs): # real signature unknown
        pass

    def get_highlight_matching_brackets(self, *args, **kwargs): # real signature unknown
        pass

    def get_highlight_syntax(self, *args, **kwargs): # real signature unknown
        pass

    def get_language(self, *args, **kwargs): # real signature unknown
        pass

    def get_max_undo_levels(self, *args, **kwargs): # real signature unknown
        pass

    def get_source_marks_at_iter(self, *args, **kwargs): # real signature unknown
        pass

    def get_source_marks_at_line(self, *args, **kwargs): # real signature unknown
        pass

    def get_style_scheme(self, *args, **kwargs): # real signature unknown
        pass

    def redo(self, *args, **kwargs): # real signature unknown
        pass

    def remove_source_marks(self, *args, **kwargs): # real signature unknown
        pass

    def set_highlight_matching_brackets(self, *args, **kwargs): # real signature unknown
        pass

    def set_highlight_syntax(self, *args, **kwargs): # real signature unknown
        pass

    def set_language(self, *args, **kwargs): # real signature unknown
        pass

    def set_max_undo_levels(self, *args, **kwargs): # real signature unknown
        pass

    def set_style_scheme(self, *args, **kwargs): # real signature unknown
        pass

    def undo(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class DrawSpacesFlags(__gobject.GFlags):
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
        15: 15,
    }
    __gtype__ = None # (!) real value is ''


class Gutter(__gobject__gobject.GObject):
    """
    Object GtkSourceGutter
    
    Signals from GtkSourceGutter:
      query-tooltip (GtkCellRenderer, GtkTextIter, GtkTooltip) -> gboolean
      cell-activated (GtkCellRenderer, GtkTextIter, GdkEvent)
    
    Properties from GtkSourceGutter:
      view -> GtkSourceView: View
        The gutters' GtkSourceView
      window-type -> GtkTextWindowType: Window Type
        The gutters text window type
    
    Signals from GObject:
      notify (GParam)
    """
    @classmethod
    def do_cell_activated(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_query_tooltip(cls, *args, **kwargs): # real signature unknown
        pass

    def get_window(self, *args, **kwargs): # real signature unknown
        pass

    def insert(self, *args, **kwargs): # real signature unknown
        pass

    def queue_draw(self, *args, **kwargs): # real signature unknown
        pass

    def remove(self, *args, **kwargs): # real signature unknown
        pass

    def reorder(self, *args, **kwargs): # real signature unknown
        pass

    def set_cell_data_func(self, *args, **kwargs): # real signature unknown
        pass

    def set_cell_size_func(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class Language(__gobject__gobject.GObject):
    """
    Object GtkSourceLanguage
    
    Properties from GtkSourceLanguage:
      id -> gchararray: Language id
        Language id
      name -> gchararray: Language name
        Language name
      section -> gchararray: Language section
        Language section
      hidden -> gboolean: Hidden
        Whether the language should be hidden from the user
    
    Signals from GObject:
      notify (GParam)
    """
    def get_globs(self, *args, **kwargs): # real signature unknown
        pass

    def get_hidden(self, *args, **kwargs): # real signature unknown
        pass

    def get_id(self, *args, **kwargs): # real signature unknown
        pass

    def get_metadata(self, *args, **kwargs): # real signature unknown
        pass

    def get_mime_types(self, *args, **kwargs): # real signature unknown
        pass

    def get_name(self, *args, **kwargs): # real signature unknown
        pass

    def get_section(self, *args, **kwargs): # real signature unknown
        pass

    def get_style_ids(self, *args, **kwargs): # real signature unknown
        pass

    def get_style_name(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    __gtype__ = None # (!) real value is ''


class LanguageManager(__gobject__gobject.GObject):
    """
    Object GtkSourceLanguageManager
    
    Properties from GtkSourceLanguageManager:
      search-path -> GStrv: Language specification directories
        List of directories where the language specification files (.lang) are located
      language-ids -> GStrv: Language ids
        List of the ids of the available languages
    
    Signals from GObject:
      notify (GParam)
    """
    def get_language(self, *args, **kwargs): # real signature unknown
        pass

    def get_language_ids(self, *args, **kwargs): # real signature unknown
        pass

    def get_search_path(self, *args, **kwargs): # real signature unknown
        pass

    def guess_language(self, *args, **kwargs): # real signature unknown
        pass

    def set_search_path(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class Mark(__gtk.TextMark):
    """
    Object GtkSourceMark
    
    Properties from GtkSourceMark:
      category -> gchararray: category
        The mark category
    
    Properties from GtkTextMark:
      name -> gchararray: Name
        Mark name
      left-gravity -> gboolean: Left gravity
        Whether the mark has left gravity
    
    Signals from GObject:
      notify (GParam)
    """
    def get_category(self, *args, **kwargs): # real signature unknown
        pass

    def next(self, *args, **kwargs): # real signature unknown
        pass

    def prev(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class PrintCompositor(__gobject__gobject.GObject):
    """
    Object GtkSourcePrintCompositor
    
    Properties from GtkSourcePrintCompositor:
      buffer -> GtkSourceBuffer: Source Buffer
        The GtkSourceBuffer object to print
      tab-width -> guint: Tab Width
        Width of a tab character expressed in spaces
      wrap-mode -> GtkWrapMode: Wrap Mode
        Whether to wrap lines never, at word boundaries, or at character boundaries.
      highlight-syntax -> gboolean: Highlight Syntax
        Whether to print the document with highlighted syntax
      print-line-numbers -> guint: Print Line Numbers
        Interval of printed line numbers (0 means no numbers)
      print-header -> gboolean: Print Header
        Whether to print a header in each page
      print-footer -> gboolean: Print Footer
        Whether to print a footer in each page
      body-font-name -> gchararray: Body Font Name
        Name of the font to use for the text body (e.g. "Monospace 10")
      line-numbers-font-name -> gchararray: Line Numbers Font Name
        Name of the font to use for the line numbers (e.g. "Monospace 10")
      header-font-name -> gchararray: Header Font Name
        Name of the font to use for the page header (e.g. "Monospace 10")
      footer-font-name -> gchararray: Footer Font Name
        Name of the font to use for the page footer (e.g. "Monospace 10")
      n-pages -> gint: Number of pages
        The number of pages in the document (-1 means the document has not been completely paginated).
    
    Signals from GObject:
      notify (GParam)
    """
    def draw_page(self, *args, **kwargs): # real signature unknown
        pass

    def get_body_font_name(self, *args, **kwargs): # real signature unknown
        pass

    def get_bottom_margin(self, *args, **kwargs): # real signature unknown
        pass

    def get_buffer(self, *args, **kwargs): # real signature unknown
        pass

    def get_footer_font_name(self, *args, **kwargs): # real signature unknown
        pass

    def get_header_font_name(self, *args, **kwargs): # real signature unknown
        pass

    def get_highlight_syntax(self, *args, **kwargs): # real signature unknown
        pass

    def get_left_margin(self, *args, **kwargs): # real signature unknown
        pass

    def get_line_numbers_font_name(self, *args, **kwargs): # real signature unknown
        pass

    def get_n_pages(self, *args, **kwargs): # real signature unknown
        pass

    def get_pagination_progress(self, *args, **kwargs): # real signature unknown
        pass

    def get_print_footer(self, *args, **kwargs): # real signature unknown
        pass

    def get_print_header(self, *args, **kwargs): # real signature unknown
        pass

    def get_print_line_numbers(self, *args, **kwargs): # real signature unknown
        pass

    def get_right_margin(self, *args, **kwargs): # real signature unknown
        pass

    def get_tab_width(self, *args, **kwargs): # real signature unknown
        pass

    def get_top_margin(self, *args, **kwargs): # real signature unknown
        pass

    def get_wrap_mode(self, *args, **kwargs): # real signature unknown
        pass

    def paginate(self, *args, **kwargs): # real signature unknown
        pass

    def set_body_font_name(self, *args, **kwargs): # real signature unknown
        pass

    def set_bottom_margin(self, *args, **kwargs): # real signature unknown
        pass

    def set_footer_font_name(self, *args, **kwargs): # real signature unknown
        pass

    def set_footer_format(self, *args, **kwargs): # real signature unknown
        pass

    def set_header_font_name(self, *args, **kwargs): # real signature unknown
        pass

    def set_header_format(self, *args, **kwargs): # real signature unknown
        pass

    def set_highlight_syntax(self, *args, **kwargs): # real signature unknown
        pass

    def set_left_margin(self, *args, **kwargs): # real signature unknown
        pass

    def set_line_numbers_font_name(self, *args, **kwargs): # real signature unknown
        pass

    def set_print_footer(self, *args, **kwargs): # real signature unknown
        pass

    def set_print_header(self, *args, **kwargs): # real signature unknown
        pass

    def set_print_line_numbers(self, *args, **kwargs): # real signature unknown
        pass

    def set_right_margin(self, *args, **kwargs): # real signature unknown
        pass

    def set_tab_width(self, *args, **kwargs): # real signature unknown
        pass

    def set_top_margin(self, *args, **kwargs): # real signature unknown
        pass

    def set_wrap_mode(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class SearchFlags(__gobject.GFlags):
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
    }
    __gtype__ = None # (!) real value is ''


class SmartHomeEndType(__gobject.GEnum):
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


class Style(__gobject__gobject.GObject):
    """
    Object GtkSourceStyle
    
    Properties from GtkSourceStyle:
      line-background -> gchararray: Line background
        Line background color
      line-background-set -> gboolean: Line background set
        Whether line background color is set
      background -> gchararray: Background
        Background color
      background-set -> gboolean: Background set
        Whether background color is set
      foreground -> gchararray: Foreground
        Foreground color
      foreground-set -> gboolean: Foreground set
        Whether foreground color is set
      bold -> gboolean: Bold
        Bold
      bold-set -> gboolean: Bold set
        Whether bold attribute is set
      italic -> gboolean: Italic
        Italic
      italic-set -> gboolean: Italic set
        Whether italic attribute is set
      underline -> gboolean: Underline
        Underline
      underline-set -> gboolean: Underline set
        Whether underline attribute is set
      strikethrough -> gboolean: Strikethrough
        Strikethrough
      strikethrough-set -> gboolean: Strikethrough set
        Whether strikethrough attribute is set
    
    Signals from GObject:
      notify (GParam)
    """
    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class StyleScheme(__gobject__gobject.GObject):
    """
    Object GtkSourceStyleScheme
    
    Properties from GtkSourceStyleScheme:
      id -> gchararray: Style scheme id
        Style scheme id
      name -> gchararray: Style scheme name
        Style scheme name
      description -> gchararray: Style scheme description
        Style scheme description
      filename -> gchararray: Style scheme filename
        Style scheme filename
    
    Signals from GObject:
      notify (GParam)
    """
    def get_authors(self, *args, **kwargs): # real signature unknown
        pass

    def get_description(self, *args, **kwargs): # real signature unknown
        pass

    def get_filename(self, *args, **kwargs): # real signature unknown
        pass

    def get_id(self, *args, **kwargs): # real signature unknown
        pass

    def get_name(self, *args, **kwargs): # real signature unknown
        pass

    def get_style(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    __gtype__ = None # (!) real value is ''


class StyleSchemeManager(__gobject__gobject.GObject):
    """
    Object GtkSourceStyleSchemeManager
    
    Properties from GtkSourceStyleSchemeManager:
      search-path -> GStrv: Style scheme search path
        List of directories and files where the style schemes are located
      scheme-ids -> GStrv: Scheme ids
        List of the ids of the available style schemes
    
    Signals from GObject:
      notify (GParam)
    """
    def append_search_path(self, *args, **kwargs): # real signature unknown
        pass

    def force_rescan(self, *args, **kwargs): # real signature unknown
        pass

    def get_scheme(self, *args, **kwargs): # real signature unknown
        pass

    def get_scheme_ids(self, *args, **kwargs): # real signature unknown
        pass

    def get_search_path(self, *args, **kwargs): # real signature unknown
        pass

    def prepend_search_path(self, *args, **kwargs): # real signature unknown
        pass

    def set_search_path(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class View(__gtk.TextView):
    """
    Object GtkSourceView
    
    Signals from GtkSourceView:
      undo ()
      redo ()
      line-mark-activated (GtkTextIter, GdkEvent)
    
    Properties from GtkSourceView:
      show-line-numbers -> gboolean: Show Line Numbers
        Whether to display line numbers
      show-line-marks -> gboolean: Show Line Marks
        Whether to display line mark pixbufs
      tab-width -> guint: Tab Width
        Width of a tab character expressed in spaces
      indent-width -> gint: Indent Width
        Number of spaces to use for each step of indent
      auto-indent -> gboolean: Auto Indentation
        Whether to enable auto indentation
      insert-spaces-instead-of-tabs -> gboolean: Insert Spaces Instead of Tabs
        Whether to insert spaces instead of tabs
      show-right-margin -> gboolean: Show Right Margin
        Whether to display the right margin
      right-margin-position -> guint: Right Margin Position
        Position of the right margin
      smart-home-end -> GtkSourceSmartHomeEndType: Smart Home/End
        HOME and END keys move to first/last non whitespace characters on line before going to the start/end of the line
      highlight-current-line -> gboolean: Highlight current line
        Whether to highlight the current line
      indent-on-tab -> gboolean: Indent on tab
        Whether to indent the selected text when the tab key is pressed
      draw-spaces -> GtkSourceDrawSpacesFlags: Draw Spaces
        Set if and how the spaces should be visualized
    
    Signals from GtkTextView:
      set-scroll-adjustments (GtkAdjustment, GtkAdjustment)
      move-cursor (GtkMovementStep, gint, gboolean)
      select-all (gboolean)
      page-horizontally (gint, gboolean)
      move-viewport (GtkScrollStep, gint)
      set-anchor ()
      insert-at-cursor (gchararray)
      delete-from-cursor (GtkDeleteType, gint)
      backspace ()
      cut-clipboard ()
      copy-clipboard ()
      paste-clipboard ()
      toggle-overwrite ()
      populate-popup (GtkMenu)
      toggle-cursor-visible ()
      preedit-changed (gchararray)
    
    Properties from GtkTextView:
      pixels-above-lines -> gint: Pixels Above Lines
        Pixels of blank space above paragraphs
      pixels-below-lines -> gint: Pixels Below Lines
        Pixels of blank space below paragraphs
      pixels-inside-wrap -> gint: Pixels Inside Wrap
        Pixels of blank space between wrapped lines in a paragraph
      editable -> gboolean: Editable
        Whether the text can be modified by the user
      wrap-mode -> GtkWrapMode: Wrap Mode
        Whether to wrap lines never, at word boundaries, or at character boundaries
      justification -> GtkJustification: Justification
        Left, right, or center justification
      left-margin -> gint: Left Margin
        Width of the left margin in pixels
      right-margin -> gint: Right Margin
        Width of the right margin in pixels
      indent -> gint: Indent
        Amount to indent the paragraph, in pixels
      tabs -> PangoTabArray: Tabs
        Custom tabs for this text
      cursor-visible -> gboolean: Cursor Visible
        If the insertion cursor is shown
      buffer -> GtkTextBuffer: Buffer
        The buffer which is displayed
      overwrite -> gboolean: Overwrite mode
        Whether entered text overwrites existing contents
      accepts-tab -> gboolean: Accepts tab
        Whether Tab will result in a tab character being entered
      im-module -> gchararray: IM module
        Which IM module should be used
    
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
    @classmethod
    def do_line_mark_activated(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_redo(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def do_undo(cls, *args, **kwargs): # real signature unknown
        pass

    def get_auto_indent(self, *args, **kwargs): # real signature unknown
        pass

    def get_draw_spaces(self, *args, **kwargs): # real signature unknown
        pass

    def get_gutter(self, *args, **kwargs): # real signature unknown
        pass

    def get_highlight_current_line(self, *args, **kwargs): # real signature unknown
        pass

    def get_indent_on_tab(self, *args, **kwargs): # real signature unknown
        pass

    def get_indent_width(self, *args, **kwargs): # real signature unknown
        pass

    def get_insert_spaces_instead_of_tabs(self, *args, **kwargs): # real signature unknown
        pass

    def get_mark_category_background(self, *args, **kwargs): # real signature unknown
        pass

    def get_mark_category_pixbuf(self, *args, **kwargs): # real signature unknown
        pass

    def get_mark_category_priority(self, *args, **kwargs): # real signature unknown
        pass

    def get_right_margin_position(self, *args, **kwargs): # real signature unknown
        pass

    def get_show_line_marks(self, *args, **kwargs): # real signature unknown
        pass

    def get_show_line_numbers(self, *args, **kwargs): # real signature unknown
        pass

    def get_show_right_margin(self, *args, **kwargs): # real signature unknown
        pass

    def get_smart_home_end(self, *args, **kwargs): # real signature unknown
        pass

    def get_tab_width(self, *args, **kwargs): # real signature unknown
        pass

    def set_auto_indent(self, *args, **kwargs): # real signature unknown
        pass

    def set_draw_spaces(self, *args, **kwargs): # real signature unknown
        pass

    def set_highlight_current_line(self, *args, **kwargs): # real signature unknown
        pass

    def set_indent_on_tab(self, *args, **kwargs): # real signature unknown
        pass

    def set_indent_width(self, *args, **kwargs): # real signature unknown
        pass

    def set_insert_spaces_instead_of_tabs(self, *args, **kwargs): # real signature unknown
        pass

    def set_mark_category_background(self, *args, **kwargs): # real signature unknown
        pass

    def set_mark_category_icon_from_icon_name(self, *args, **kwargs): # real signature unknown
        pass

    def set_mark_category_icon_from_pixbuf(self, *args, **kwargs): # real signature unknown
        pass

    def set_mark_category_icon_from_stock(self, *args, **kwargs): # real signature unknown
        pass

    def set_mark_category_pixbuf(self, *args, **kwargs): # real signature unknown
        pass

    def set_mark_category_priority(self, *args, **kwargs): # real signature unknown
        pass

    def set_mark_category_tooltip_func(self, *args, **kwargs): # real signature unknown
        pass

    def set_mark_category_tooltip_markup_func(self, *args, **kwargs): # real signature unknown
        pass

    def set_right_margin_position(self, *args, **kwargs): # real signature unknown
        pass

    def set_show_line_marks(self, *args, **kwargs): # real signature unknown
        pass

    def set_show_line_numbers(self, *args, **kwargs): # real signature unknown
        pass

    def set_show_right_margin(self, *args, **kwargs): # real signature unknown
        pass

    def set_smart_home_end(self, *args, **kwargs): # real signature unknown
        pass

    def set_tab_width(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self): # real signature unknown; restored from __doc__
        """ x.__iter__() <==> iter(x) """
        pass

    __gtype__ = None # (!) real value is ''


# variables with complex values

pygtksourceview2_version = (
    2,
    8,
    0,
)

