# encoding: utf-8
# module gnomevfs._gnomevfs
# from /usr/lib64/python2.6/site-packages/gtk-2.0/gnomevfs/_gnomevfs.so
# by generator 1.136
# no doc

# imports
import gnomevfs.async as async # <module 'gnomevfs.async' (built-in)>
import gnomevfs as __gnomevfs
import gobject._gobject as __gobject__gobject


# Variables with simple values

DEVICE_TYPE_APPLE = 13

DEVICE_TYPE_AUDIO_CD = 1

DEVICE_TYPE_AUTOFS = 9
DEVICE_TYPE_CAMERA = 10
DEVICE_TYPE_CDROM = 4
DEVICE_TYPE_FLOPPY = 5
DEVICE_TYPE_HARDDRIVE = 3
DEVICE_TYPE_JAZ = 7
DEVICE_TYPE_LOOPBACK = 16

DEVICE_TYPE_MEMORY_STICK = 11

DEVICE_TYPE_MUSIC_PLAYER = 14

DEVICE_TYPE_NETWORK = 17
DEVICE_TYPE_NFS = 8
DEVICE_TYPE_SMB = 12
DEVICE_TYPE_UNKNOWN = 0

DEVICE_TYPE_VIDEO_DVD = 2

DEVICE_TYPE_WINDOWS = 15
DEVICE_TYPE_ZIP = 6

DIRECTORY_KIND_DESKTOP = 1000
DIRECTORY_KIND_TRASH = 1001

DIRECTORY_VISIT_DEFAULT = 0
DIRECTORY_VISIT_LOOPCHECK = 2
DIRECTORY_VISIT_SAMEFS = 1

FILE_FLAGS_LOCAL = 2
FILE_FLAGS_NONE = 0
FILE_FLAGS_SYMLINK = 1

FILE_INFO_DEFAULT = 0

FILE_INFO_FIELDS_ACCESS = 16384
FILE_INFO_FIELDS_ATIME = 512

FILE_INFO_FIELDS_BLOCK_COUNT = 128

FILE_INFO_FIELDS_CTIME = 2048
FILE_INFO_FIELDS_DEVICE = 8
FILE_INFO_FIELDS_FLAGS = 4
FILE_INFO_FIELDS_IDS = 32768
FILE_INFO_FIELDS_INODE = 16

FILE_INFO_FIELDS_IO_BLOCK_SIZE = 256

FILE_INFO_FIELDS_LINK_COUNT = 32

FILE_INFO_FIELDS_MIME_TYPE = 8192

FILE_INFO_FIELDS_MTIME = 1024
FILE_INFO_FIELDS_NONE = 0
FILE_INFO_FIELDS_PERMISSIONS = 2
FILE_INFO_FIELDS_SIZE = 64

FILE_INFO_FIELDS_SYMLINK_NAME = 4096

FILE_INFO_FIELDS_TYPE = 1

FILE_INFO_FOLLOW_LINKS = 8

FILE_INFO_FORCE_FAST_MIME_TYPE = 2

FILE_INFO_FORCE_SLOW_MIME_TYPE = 4

FILE_INFO_GET_ACCESS_RIGHTS = 16

FILE_INFO_GET_MIME_TYPE = 1

FILE_INFO_NAME_ONLY = 32

FILE_TYPE_BLOCK_DEVICE = 6

FILE_TYPE_CHARACTER_DEVICE = 5

FILE_TYPE_DIRECTORY = 2
FILE_TYPE_FIFO = 3
FILE_TYPE_REGULAR = 1
FILE_TYPE_SOCKET = 4

FILE_TYPE_SYMBOLIC_LINK = 7

FILE_TYPE_UNKNOWN = 0

MIME_APPLICATION_ARGUMENT_TYPE_PATHS = 1
MIME_APPLICATION_ARGUMENT_TYPE_URIS = 0

MIME_APPLICATION_ARGUMENT_TYPE_URIS_FOR_NON_FILES = 2

MIME_IDENTICAL = 1
MIME_PARENT = 2
MIME_UNRELATED = 0

MONITOR_DIRECTORY = 1

MONITOR_EVENT_CHANGED = 0
MONITOR_EVENT_CREATED = 4
MONITOR_EVENT_DELETED = 1

MONITOR_EVENT_METADATA_CHANGED = 5

MONITOR_EVENT_STARTEXECUTING = 2
MONITOR_EVENT_STOPEXECUTING = 3

MONITOR_FILE = 0

OPEN_NONE = 0
OPEN_RANDOM = 4
OPEN_READ = 1
OPEN_TRUNCATE = 8
OPEN_WRITE = 2

PERM_ACCESS_EXECUTABLE = 262144
PERM_ACCESS_READABLE = 65536
PERM_ACCESS_WRITABLE = 131072

PERM_GROUP_ALL = 56
PERM_GROUP_EXEC = 8
PERM_GROUP_READ = 32
PERM_GROUP_WRITE = 16

PERM_OTHER_ALL = 7
PERM_OTHER_EXEC = 1
PERM_OTHER_READ = 4
PERM_OTHER_WRITE = 2

PERM_SGID = 1024
PERM_STICKY = 512
PERM_SUID = 2048

PERM_USER_ALL = 448
PERM_USER_EXEC = 64
PERM_USER_READ = 256
PERM_USER_WRITE = 128

PRIORITY_DEFAULT = 0
PRIORITY_MAX = 10
PRIORITY_MIN = -10

SEEK_CURRENT = 1
SEEK_END = 2
SEEK_START = 0

SET_FILE_INFO_NAME = 1
SET_FILE_INFO_NONE = 0
SET_FILE_INFO_OWNER = 4
SET_FILE_INFO_PERMISSIONS = 2
SET_FILE_INFO_TIME = 8

VOLUME_TYPE_CONNECTED_SERVER = 2

VOLUME_TYPE_MOUNTPOINT = 0

VOLUME_TYPE_VFS_MOUNT = 1

XFER_CHECKING_DESTINATION = 1

XFER_DEFAULT = 0

XFER_DELETE_ITEMS = 32

XFER_EMPTY_DIRECTORIES = 64

XFER_ERROR_ACTION_ABORT = 0
XFER_ERROR_ACTION_RETRY = 1
XFER_ERROR_ACTION_SKIP = 2

XFER_ERROR_MODE_ABORT = 0
XFER_ERROR_MODE_QUERY = 1

XFER_FOLLOW_LINKS = 2

XFER_FOLLOW_LINKS_RECURSIVE = 2048

XFER_LINK_ITEMS = 1024

XFER_NEW_UNIQUE_DIRECTORY = 128

XFER_OVERWRITE_ACTION_ABORT = 0
XFER_OVERWRITE_ACTION_REPLACE = 1

XFER_OVERWRITE_ACTION_REPLACE_ALL = 2

XFER_OVERWRITE_ACTION_SKIP = 3

XFER_OVERWRITE_ACTION_SKIP_ALL = 4

XFER_OVERWRITE_MODE_ABORT = 0
XFER_OVERWRITE_MODE_QUERY = 1
XFER_OVERWRITE_MODE_REPLACE = 2
XFER_OVERWRITE_MODE_SKIP = 3

XFER_PHASE_CLEANUP = 15
XFER_PHASE_CLOSESOURCE = 10
XFER_PHASE_CLOSETARGET = 11
XFER_PHASE_COLLECTING = 2
XFER_PHASE_COMPLETED = 16
XFER_PHASE_COPYING = 6
XFER_PHASE_DELETESOURCE = 12
XFER_PHASE_FILECOMPLETED = 14
XFER_PHASE_INITIAL = 0
XFER_PHASE_MOVING = 7
XFER_PHASE_OPENSOURCE = 4
XFER_PHASE_OPENTARGET = 5
XFER_PHASE_READSOURCE = 8
XFER_PHASE_READYTOGO = 3
XFER_PHASE_SETATTRIBUTES = 13
XFER_PHASE_WRITETARGET = 9

XFER_PROGRESS_STATUS_DUPLICATE = 3
XFER_PROGRESS_STATUS_OK = 0
XFER_PROGRESS_STATUS_OVERWRITE = 2
XFER_PROGRESS_STATUS_VFSERROR = 1

XFER_RECURSIVE = 8
XFER_REMOVESOURCE = 256
XFER_SAMEFS = 16

XFER_USE_UNIQUE_NAMES = 512

# functions

def connect_to_server(*args, **kwargs): # real signature unknown
    pass

def create(*args, **kwargs): # real signature unknown
    pass

def create_symbolic_link(*args, **kwargs): # real signature unknown
    pass

def dns_sd_browse_sync(*args, **kwargs): # real signature unknown
    pass

def dns_sd_list_browse_domains_sync(*args, **kwargs): # real signature unknown
    pass

def dns_sd_resolve_sync(*args, **kwargs): # real signature unknown
    pass

def escape_host_and_path_string(*args, **kwargs): # real signature unknown
    pass

def escape_path_string(*args, **kwargs): # real signature unknown
    pass

def escape_set(*args, **kwargs): # real signature unknown
    pass

def escape_slashes(*args, **kwargs): # real signature unknown
    pass

def escape_string(*args, **kwargs): # real signature unknown
    pass

def exists(*args, **kwargs): # real signature unknown
    pass

def format_file_size_for_display(*args, **kwargs): # real signature unknown
    pass

def format_uri_for_display(*args, **kwargs): # real signature unknown
    pass

def get_default_browse_domains(*args, **kwargs): # real signature unknown
    pass

def get_file_info(*args, **kwargs): # real signature unknown
    pass

def get_file_mime_type(*args, **kwargs): # real signature unknown
    pass

def get_local_path_from_uri(*args, **kwargs): # real signature unknown
    pass

def get_mime_type(*args, **kwargs): # real signature unknown
    pass

def get_mime_type_for_data(*args, **kwargs): # real signature unknown
    pass

def get_uri_from_local_path(*args, **kwargs): # real signature unknown
    pass

def get_uri_scheme(*args, **kwargs): # real signature unknown
    pass

def get_volume_free_space(*args, **kwargs): # real signature unknown
    pass

def icon_path_from_filename(*args, **kwargs): # real signature unknown
    pass

def is_executable_command_string(*args, **kwargs): # real signature unknown
    pass

def is_primary_thread(*args, **kwargs): # real signature unknown
    pass

def make_directory(*args, **kwargs): # real signature unknown
    pass

def make_path_name_canonical(*args, **kwargs): # real signature unknown
    pass

def make_uri_canonical(*args, **kwargs): # real signature unknown
    pass

def make_uri_canonical_strip_fragment(*args, **kwargs): # real signature unknown
    pass

def make_uri_from_input(*args, **kwargs): # real signature unknown
    pass

def make_uri_from_input_with_dirs(*args, **kwargs): # real signature unknown
    pass

def make_uri_from_shell_arg(*args, **kwargs): # real signature unknown
    pass

def mime_add_application_to_short_list(*args, **kwargs): # real signature unknown
    pass

def mime_add_component_to_short_list(*args, **kwargs): # real signature unknown
    pass

def mime_add_extension(*args, **kwargs): # real signature unknown
    pass

def mime_application_new_from_id(*args, **kwargs): # real signature unknown
    pass

def mime_can_be_executable(*args, **kwargs): # real signature unknown
    pass

def mime_extend_all_applications(*args, **kwargs): # real signature unknown
    pass

def mime_get_all_applications(*args, **kwargs): # real signature unknown
    pass

def mime_get_default_action(*args, **kwargs): # real signature unknown
    pass

def mime_get_default_action_type(*args, **kwargs): # real signature unknown
    pass

def mime_get_default_application(*args, **kwargs): # real signature unknown
    pass

def mime_get_description(*args, **kwargs): # real signature unknown
    pass

def mime_get_icon(*args, **kwargs): # real signature unknown
    pass

def mime_get_short_list_applications(*args, **kwargs): # real signature unknown
    pass

def mime_remove_application_from_short_list(*args, **kwargs): # real signature unknown
    pass

def mime_remove_component_from_short_list(*args, **kwargs): # real signature unknown
    pass

def mime_remove_extension(*args, **kwargs): # real signature unknown
    pass

def mime_remove_from_all_applications(*args, **kwargs): # real signature unknown
    pass

def mime_set_can_be_executable(*args, **kwargs): # real signature unknown
    pass

def mime_set_default_action_type(*args, **kwargs): # real signature unknown
    pass

def mime_set_default_application(*args, **kwargs): # real signature unknown
    pass

def mime_set_default_component(*args, **kwargs): # real signature unknown
    pass

def mime_set_description(*args, **kwargs): # real signature unknown
    pass

def mime_set_icon(*args, **kwargs): # real signature unknown
    pass

def mime_set_short_list_applications(*args, **kwargs): # real signature unknown
    pass

def mime_set_short_list_components(*args, **kwargs): # real signature unknown
    pass

def mime_type_get_equivalence(*args, **kwargs): # real signature unknown
    pass

def monitor_add(*args, **kwargs): # real signature unknown
    pass

def monitor_cancel(*args, **kwargs): # real signature unknown
    pass

def open_fd(*args, **kwargs): # real signature unknown
    pass

def read_entire_file(*args, **kwargs): # real signature unknown
    pass

def remove_directory(*args, **kwargs): # real signature unknown
    pass

def resolve(*args, **kwargs): # real signature unknown
    pass

def set_file_info(*args, **kwargs): # real signature unknown
    pass

def truncate(*args, **kwargs): # real signature unknown
    pass

def unescape_string(*args, **kwargs): # real signature unknown
    pass

def unescape_string_for_display(*args, **kwargs): # real signature unknown
    pass

def unlink(*args, **kwargs): # real signature unknown
    pass

def uris_match(*args, **kwargs): # real signature unknown
    pass

def url_show(*args, **kwargs): # real signature unknown
    pass

def xfer_delete_list(*args, **kwargs): # real signature unknown
    pass

def xfer_uri(*args, **kwargs): # real signature unknown
    pass

def xfer_uri_list(*args, **kwargs): # real signature unknown
    pass

# classes

from Error import Error
from AccessDeniedError import AccessDeniedError
from BadFileError import BadFileError
from BadParametersError import BadParametersError
from CancelledError import CancelledError
from Context import Context
from CorruptedDataError import CorruptedDataError
from DirectoryBusyError import DirectoryBusyError
from open_directory import open_directory
from DirectoryHandle import DirectoryHandle
from DirectoryNotEmptyError import DirectoryNotEmptyError
from Drive import Drive
from EOFError import EOFError
from FileExistsError import FileExistsError
from FileInfo import FileInfo
from GenericError import GenericError
from open import open
from Handle import Handle
from HostHasNoAddressError import HostHasNoAddressError
from HostNotFoundError import HostNotFoundError
from InProgressError import InProgressError
from InternalError import InternalError
from InterruptedError import InterruptedError
from InvalidHostNameError import InvalidHostNameError
from InvalidOpenModeError import InvalidOpenModeError
from InvalidURIError import InvalidURIError
from IOError import IOError
from IsDirectoryError import IsDirectoryError
from LoginFailedError import LoginFailedError
from LoopError import LoopError
from NameTooLongError import NameTooLongError
from NoMasterBrowserError import NoMasterBrowserError
from NoMemoryError import NoMemoryError
from NoSpaceError import NoSpaceError
from NotADirectoryError import NotADirectoryError
from NotFoundError import NotFoundError
from NotOpenError import NotOpenError
from NotPermittedError import NotPermittedError
from NotSameFileSystemError import NotSameFileSystemError
from NotSupportedError import NotSupportedError
from ProtocolErrorError import ProtocolErrorError
from ReadOnlyError import ReadOnlyError
from ReadOnlyFileSystemError import ReadOnlyFileSystemError
from ServiceNotAvailableError import ServiceNotAvailableError
from ServiceObsoleteError import ServiceObsoleteError
from TooBigError import TooBigError
from TooManyLinksError import TooManyLinksError
from TooManyOpenFilesError import TooManyOpenFilesError
from URI import URI
from Volume import Volume
from VolumeMonitor import VolumeMonitor
from WrongFormatError import WrongFormatError
# variables with complex values

_PyGnomeVFS_API = None # (!) real value is ''

