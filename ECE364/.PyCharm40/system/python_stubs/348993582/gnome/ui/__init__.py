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


# Variables with simple values

APP_CONFIGURABLE_ITEM_ABOUT = 20
APP_CONFIGURABLE_ITEM_CLEAR = 12
APP_CONFIGURABLE_ITEM_CLOSE = 7

APP_CONFIGURABLE_ITEM_CLOSE_WINDOW = 23

APP_CONFIGURABLE_ITEM_COPY = 10
APP_CONFIGURABLE_ITEM_CUT = 9

APP_CONFIGURABLE_ITEM_END_GAME = 31

APP_CONFIGURABLE_ITEM_FIND = 15

APP_CONFIGURABLE_ITEM_FIND_AGAIN = 16

APP_CONFIGURABLE_ITEM_HINT = 29
APP_CONFIGURABLE_ITEM_NEW = 0

APP_CONFIGURABLE_ITEM_NEW_GAME = 24
APP_CONFIGURABLE_ITEM_NEW_WINDOW = 22

APP_CONFIGURABLE_ITEM_OPEN = 1
APP_CONFIGURABLE_ITEM_PASTE = 11

APP_CONFIGURABLE_ITEM_PAUSE_GAME = 25

APP_CONFIGURABLE_ITEM_PREFERENCES = 19
APP_CONFIGURABLE_ITEM_PRINT = 5

APP_CONFIGURABLE_ITEM_PRINT_SETUP = 6

APP_CONFIGURABLE_ITEM_PROPERTIES = 18
APP_CONFIGURABLE_ITEM_QUIT = 8
APP_CONFIGURABLE_ITEM_REDO = 14

APP_CONFIGURABLE_ITEM_REDO_MOVE = 28

APP_CONFIGURABLE_ITEM_REPLACE = 17

APP_CONFIGURABLE_ITEM_RESTART_GAME = 26

APP_CONFIGURABLE_ITEM_REVERT = 4
APP_CONFIGURABLE_ITEM_SAVE = 2

APP_CONFIGURABLE_ITEM_SAVE_AS = 3

APP_CONFIGURABLE_ITEM_SCORES = 30

APP_CONFIGURABLE_ITEM_SELECT_ALL = 21

APP_CONFIGURABLE_ITEM_UNDO = 13

APP_CONFIGURABLE_ITEM_UNDO_MOVE = 27

APP_PIXMAP_DATA = 2
APP_PIXMAP_FILENAME = 3
APP_PIXMAP_NONE = 0
APP_PIXMAP_STOCK = 1

APP_UI_BUILDER_DATA = 7

APP_UI_ENDOFINFO = 0
APP_UI_HELP = 6
APP_UI_INCLUDE = 10
APP_UI_ITEM = 1

APP_UI_ITEM_CONFIGURABLE = 8

APP_UI_RADIOITEMS = 3
APP_UI_SEPARATOR = 5
APP_UI_SUBTREE = 4

APP_UI_SUBTREE_STOCK = 9

APP_UI_TOGGLEITEM = 2

CLIENT_DISCONNECTED = 5
CLIENT_FROZEN = 4
CLIENT_IDLE = 0

CLIENT_IS_CONNECTED = 1

CLIENT_REGISTERING = 6
CLIENT_RESTARTED = 2
CLIENT_RESTORED = 4

CLIENT_SAVING_PHASE_1 = 1
CLIENT_SAVING_PHASE_2 = 3

CLIENT_WAITING_FOR_PHASE_2 = 2

DATE_EDIT_24_HR = 2

DATE_EDIT_DISPLAY_SECONDS = 8

DATE_EDIT_SHOW_TIME = 1

DATE_EDIT_WEEK_STARTS_ON_MONDAY = 4

DIALOG_ERROR = 0
DIALOG_NORMAL = 1

EDGE_FINISH = 1
EDGE_LAST = 3
EDGE_OTHER = 2
EDGE_START = 0

FONT_PICKER_MODE_FONT_INFO = 1

FONT_PICKER_MODE_PIXMAP = 0
FONT_PICKER_MODE_UNKNOWN = 3

FONT_PICKER_MODE_USER_WIDGET = 2

ICON_LIST_ICONS = 0

ICON_LIST_TEXT_BELOW = 1
ICON_LIST_TEXT_RIGHT = 2

ICON_LOOKUP_FLAGS_ALLOW_SVG_AS_THEMSELVES = 4

ICON_LOOKUP_FLAGS_EMBEDDING_TEXT = 1

ICON_LOOKUP_FLAGS_NONE = 0

ICON_LOOKUP_FLAGS_SHOW_SMALL_IMAGES_AS_THEMSELVES = 2

ICON_LOOKUP_RESULT_FLAGS_NONE = 0
ICON_LOOKUP_RESULT_FLAGS_THUMBNAIL = 1

INTERACT_ANY = 2
INTERACT_ERRORS = 1
INTERACT_NONE = 0

MDI_DEFAULT_MODE = 42

MDI_MODAL = 2
MDI_NOTEBOOK = 0
MDI_TOPLEVEL = 1

PAD = 8

PAD_BIG = 12
PAD_SMALL = 4

PASSWORD_DIALOG_REMEMBER_FOREVER = 2
PASSWORD_DIALOG_REMEMBER_NOTHING = 0
PASSWORD_DIALOG_REMEMBER_SESSION = 1

PREFERENCES_ALWAYS = 2
PREFERENCES_NEVER = 0
PREFERENCES_USER = 1

RESTART_ANYWAY = 1

RESTART_IF_RUNNING = 0

RESTART_IMMEDIATELY = 2
RESTART_NEVER = 3

SAVE_BOTH = 2
SAVE_GLOBAL = 0
SAVE_LOCAL = 1

THUMBNAIL_SIZE_LARGE = 1
THUMBNAIL_SIZE_NORMAL = 0

__version__ = '  2.28.0'

# functions

def accelerators_sync(*args, **kwargs): # real signature unknown
    pass

def app_helper_gettext(*args, **kwargs): # real signature unknown
    pass

def app_setup_toolbar(*args, **kwargs): # real signature unknown
    pass

def authentication_manager_dialog_is_visible(*args, **kwargs): # real signature unknown
    pass

def authentication_manager_init(*args, **kwargs): # real signature unknown
    pass

def client_disable_master_connection(*args, **kwargs): # real signature unknown
    pass

def client_module_info_get(*args, **kwargs): # real signature unknown
    pass

def error_dialog(*args, **kwargs): # real signature unknown
    pass

def error_dialog_parented(*args, **kwargs): # real signature unknown
    pass

def gdk_pixbuf_new_from_uri(*args, **kwargs): # real signature unknown
    pass

def gtk_module_info_get(*args, **kwargs): # real signature unknown
    pass

def help_display_on_screen(*args, **kwargs): # real signature unknown
    pass

def help_display_uri_on_screen(*args, **kwargs): # real signature unknown
    pass

def ice_init(*args, **kwargs): # real signature unknown
    pass

def icon_lookup(*args, **kwargs): # real signature unknown
    pass

def interaction_key_return(*args, **kwargs): # real signature unknown
    pass

def libgnomeui_module_info_get(*args, **kwargs): # real signature unknown
    pass

def master_client(*args, **kwargs): # real signature unknown
    pass

def mdi_get_app_from_view(*args, **kwargs): # real signature unknown
    pass

def mdi_get_child_from_view(*args, **kwargs): # real signature unknown
    pass

def ok_dialog_parented(*args, **kwargs): # real signature unknown
    pass

def popup_menu_get_accel_group(*args, **kwargs): # real signature unknown
    pass

def scores_display(*args, **kwargs): # real signature unknown
    pass

def scores_display_with_pixmap(*args, **kwargs): # real signature unknown
    pass

def thumbnail_has_uri(*args, **kwargs): # real signature unknown
    pass

def thumbnail_is_valid(*args, **kwargs): # real signature unknown
    pass

def thumbnail_md5(*args, **kwargs): # real signature unknown
    pass

def thumbnail_path_for_uri(*args, **kwargs): # real signature unknown
    pass

def thumbnail_scale_down_pixbuf(*args, **kwargs): # real signature unknown
    pass

def url_show_on_screen(*args, **kwargs): # real signature unknown
    pass

def warning_dialog(*args, **kwargs): # real signature unknown
    pass

def warning_dialog_parented(*args, **kwargs): # real signature unknown
    pass

def window_icon_set_from_default(*args, **kwargs): # real signature unknown
    pass

def window_toplevel_set_title(*args, **kwargs): # real signature unknown
    pass

# classes

from About import About
from App import App
from AppBar import AppBar
from Client import Client
from ClientFlags import ClientFlags
from ClientState import ClientState
from ColorPicker import ColorPicker
from DateEdit import DateEdit
from DateEditFlags import DateEditFlags
from Dialog import Dialog
from DialogType import DialogType
from Druid import Druid
from DruidPage import DruidPage
from DruidPageEdge import DruidPageEdge
from DruidPageStandard import DruidPageStandard
from EdgePosition import EdgePosition
from Entry import Entry
from FileEntry import FileEntry
from FontPicker import FontPicker
from FontPickerMode import FontPickerMode
from GnomeModuleInfo import GnomeModuleInfo
from HRef import HRef
from IconEntry import IconEntry
from IconList import IconList
from IconListMode import IconListMode
from IconLookupFlags import IconLookupFlags
from IconLookupResultFlags import IconLookupResultFlags
from IconSelection import IconSelection
from IconTextItem import IconTextItem
from InteractStyle import InteractStyle
from MDI import MDI
from MDIChild import MDIChild
from MDIGenericChild import MDIGenericChild
from MDIMode import MDIMode
from MessageBox import MessageBox
from PasswordDialogRemember import PasswordDialogRemember
from Pixmap import Pixmap
from PixmapEntry import PixmapEntry
from PreferencesType import PreferencesType
from PropertyBox import PropertyBox
from RestartStyle import RestartStyle
from SaveStyle import SaveStyle
from Scores import Scores
from ThumbnailFactory import ThumbnailFactory
from ThumbnailSize import ThumbnailSize
from UIInfoConfigurableTypes import UIInfoConfigurableTypes
from UIInfoType import UIInfoType
from UIPixmapType import UIPixmapType
