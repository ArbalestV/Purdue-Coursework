# encoding: utf-8
# module gnome._gnome
# from /usr/lib64/python2.6/site-packages/gtk-2.0/gnome/_gnome.so
# by generator 1.136
# no doc

# imports
import gobject as __gobject
import gobject._gobject as __gobject__gobject


# Variables with simple values

FILE_DOMAIN_APP_CONFIG = 11
FILE_DOMAIN_APP_DATADIR = 8
FILE_DOMAIN_APP_HELP = 12
FILE_DOMAIN_APP_LIBDIR = 7
FILE_DOMAIN_APP_PIXMAP = 10
FILE_DOMAIN_APP_SOUND = 9

FILE_DOMAIN_CONFIG = 5
FILE_DOMAIN_DATADIR = 2
FILE_DOMAIN_HELP = 6
FILE_DOMAIN_LIBDIR = 1
FILE_DOMAIN_PIXMAP = 4
FILE_DOMAIN_SOUND = 3
FILE_DOMAIN_UNKNOWN = 0

HELP_ERROR_INTERNAL = 0

HELP_ERROR_NOT_FOUND = 1

PARAM_APP_DATADIR = 'app-datadir'
PARAM_APP_ID = 'app-id'
PARAM_APP_LIBDIR = 'app-libdir'
PARAM_APP_PREFIX = 'app-prefix'
PARAM_APP_SYSCONFDIR = 'app-sysconfdir'
PARAM_APP_VERSION = 'app-version'

PARAM_CREATE_DIRECTORIES = 'create-directories'

PARAM_ENABLE_SOUND = 'enable-sound'

PARAM_ESPEAKER = 'espeaker'

PARAM_GNOME_DATADIR = 'gnome-datadir'
PARAM_GNOME_LIBDIR = 'gnome-libdir'
PARAM_GNOME_PATH = 'gnome-path'
PARAM_GNOME_PREFIX = 'gnome-prefix'
PARAM_GNOME_SYSCONFDIR = 'gnome-sysconfdir'

PARAM_HUMAN_READABLE_NAME = 'human-readable-name'

PARAM_NONE = None

PARAM_POPT_CONTEXT = 'popt-context'
PARAM_POPT_FLAGS = 'popt-flags'
PARAM_POPT_TABLE = 'popt-table'

POPT_ARGFLAG_AND = 67108864

POPT_ARGFLAG_DOC_HIDDEN = 1073741824

POPT_ARGFLAG_LOGICALOPS = 234881024
POPT_ARGFLAG_NAND = 83886080
POPT_ARGFLAG_NOR = 150994944
POPT_ARGFLAG_NOT = 16777216
POPT_ARGFLAG_ONEDASH = 2147483648
POPT_ARGFLAG_OPTIONAL = 268435456
POPT_ARGFLAG_OR = 134217728

POPT_ARGFLAG_SHOW_DEFAULT = 8388608

POPT_ARGFLAG_STRIP = 536870912
POPT_ARGFLAG_XOR = 33554432

POPT_CONTEXT_ARG_OPTS = 16

POPT_CONTEXT_KEEP_FIRST = 2

POPT_CONTEXT_NO_EXEC = 1

POPT_CONTEXT_POSIXMEHARDER = 4

TRIG_COMMAND = 2
TRIG_FUNCTION = 1
TRIG_MEDIAPLAY = 3
TRIG_NONE = 0

URL_ERROR_CANCELLED = 6
URL_ERROR_LAUNCH = 1

URL_ERROR_NOT_SUPPORTED = 4

URL_ERROR_NO_DEFAULT = 3

URL_ERROR_PARSE = 0
URL_ERROR_URL = 2
URL_ERROR_VFS = 5

__version__ = '  2.28.0'

# functions

def bonobo_module_info_get(*args, **kwargs): # real signature unknown
    pass

def clearenv(*args, **kwargs): # real signature unknown
    pass

def config_clean_file_(*args, **kwargs): # real signature unknown
    pass

def config_clean_key_(*args, **kwargs): # real signature unknown
    pass

def config_clean_section_(*args, **kwargs): # real signature unknown
    pass

def config_drop_all(*args, **kwargs): # real signature unknown
    pass

def config_drop_file_(*args, **kwargs): # real signature unknown
    pass

def config_has_section_(*args, **kwargs): # real signature unknown
    pass

def config_pop_prefix(*args, **kwargs): # real signature unknown
    pass

def config_push_prefix(*args, **kwargs): # real signature unknown
    pass

def config_set_bool_(*args, **kwargs): # real signature unknown
    pass

def config_set_float_(*args, **kwargs): # real signature unknown
    pass

def config_set_int_(*args, **kwargs): # real signature unknown
    pass

def config_set_string_(*args, **kwargs): # real signature unknown
    pass

def config_set_translated_string_(*args, **kwargs): # real signature unknown
    pass

def config_sync(*args, **kwargs): # real signature unknown
    pass

def config_sync_file_(*args, **kwargs): # real signature unknown
    pass

def execute_shell(*args, **kwargs): # real signature unknown
    pass

def execute_shell_fds(*args, **kwargs): # real signature unknown
    pass

def execute_terminal_shell(*args, **kwargs): # real signature unknown
    pass

def execute_terminal_shell_fds(*args, **kwargs): # real signature unknown
    pass

def gconf_get_app_settings_relative(*args, **kwargs): # real signature unknown
    pass

def gconf_get_gnome_libs_settings_relative(*args, **kwargs): # real signature unknown
    pass

def g_extension_pointer(*args, **kwargs): # real signature unknown
    pass

def help_display(*args, **kwargs): # real signature unknown
    pass

def help_display_desktop(*args, **kwargs): # real signature unknown
    pass

def help_display_uri(*args, **kwargs): # real signature unknown
    pass

def help_display_with_doc_id(*args, **kwargs): # real signature unknown
    pass

def i18n_pop_c_numeric_locale(*args, **kwargs): # real signature unknown
    pass

def i18n_push_c_numeric_locale(*args, **kwargs): # real signature unknown
    pass

def libgnome_module_info_get(*args, **kwargs): # real signature unknown
    pass

def popt_parse(*args, **kwargs): # real signature unknown
    pass

def program_get(*args, **kwargs): # real signature unknown
    pass

def program_init(*args, **kwargs): # real signature unknown
    pass

def program_module_load(*args, **kwargs): # real signature unknown
    pass

def program_module_register(*args, **kwargs): # real signature unknown
    pass

def program_module_registered(*args, **kwargs): # real signature unknown
    pass

def score_init(*args, **kwargs): # real signature unknown
    pass

def score_log(*args, **kwargs): # real signature unknown
    pass

def setenv(*args, **kwargs): # real signature unknown
    pass

def sound_connection_get(*args, **kwargs): # real signature unknown
    pass

def sound_init(*args, **kwargs): # real signature unknown
    pass

def sound_play(*args, **kwargs): # real signature unknown
    pass

def sound_sample_load(*args, **kwargs): # real signature unknown
    pass

def sound_shutdown(*args, **kwargs): # real signature unknown
    pass

def unsetenv(*args, **kwargs): # real signature unknown
    pass

def url_show(*args, **kwargs): # real signature unknown
    pass

def user_accels_dir_get(*args, **kwargs): # real signature unknown
    pass

def user_dir_get(*args, **kwargs): # real signature unknown
    pass

def user_private_dir_get(*args, **kwargs): # real signature unknown
    pass

def util_user_shell(*args, **kwargs): # real signature unknown
    pass

# classes

class FileDomain(__gobject.GEnum):
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
        11: 11,
        12: 12,
    }
    __gtype__ = None # (!) real value is ''


class GnomeModuleInfo(__gobject.GBoxed):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __gtype__ = None # (!) real value is ''


class HelpError(__gobject.GEnum):
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


class Program(__gobject__gobject.GObject):
    """
    Object GnomeProgram
    
    Properties from GnomeProgram:
      app-id -> gchararray: App ID
        ID string to use for this application
      app-version -> gchararray: App version
        Version of this application
      human-readable-name -> gchararray: Human readable name
        Human readable name of this application
      gnome-path -> gchararray: GNOME path
        Path in which to look for installed files
      gnome-prefix -> gchararray: GNOME Prefix
        Prefix where GNOME was installed
      gnome-libdir -> gchararray: GNOME Libdir
        Library prefix where GNOME was installed
      gnome-datadir -> gchararray: GNOME Datadir
        Data prefix where GNOME was installed
      gnome-sysconfdir -> gchararray: GNOME Sysconfdir
        Configuration prefix where GNOME was installed
      app-prefix -> gchararray: GNOME App Prefix
        Prefix where this application was installed
      app-libdir -> gchararray: GNOME App Libdir
        Library prefix where this application was installed
      app-datadir -> gchararray: GNOME App Datadir
        Data prefix where this application was installed
      app-sysconfdir -> gchararray: GNOME App Sysconfdir
        Configuration prefix where this application was installed
      create-directories -> gboolean: Create Directories
        Create standard GNOME directories on startup
      enable-sound -> gboolean: Enable Sound
        Enable sound on startup
      espeaker -> gchararray: Espeaker
        How to connect to esd
      popt-table -> gpointer: Popt Table
        The table of options for popt
      popt-flags -> gint: Popt Flags
        The flags to use for popt
      popt-context -> gpointer: Popt Context
        The popt context pointer that GnomeProgram is using
      goption-context -> gpointer: GOption Context
        The goption context pointer that GnomeProgram is using
    
    Signals from GObject:
      notify (GParam)
    """
    def get_app_id(self, *args, **kwargs): # real signature unknown
        pass

    def get_app_version(self, *args, **kwargs): # real signature unknown
        pass

    def get_human_readable_name(self, *args, **kwargs): # real signature unknown
        pass

    def get_popt_args(self, *args, **kwargs): # real signature unknown
        pass

    def locate_file(self, *args, **kwargs): # real signature unknown
        pass

    def parse_args(self, *args, **kwargs): # real signature unknown
        pass

    def postinit(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __gtype__ = None # (!) real value is ''


class TriggerType(__gobject.GEnum):
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


class URLError(__gobject.GEnum):
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
    }
    __gtype__ = None # (!) real value is ''


# variables with complex values

gnome_python_version = (
    2,
    28,
    0,
)

