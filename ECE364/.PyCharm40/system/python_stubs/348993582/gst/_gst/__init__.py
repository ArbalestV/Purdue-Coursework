# encoding: utf-8
# module gst._gst
# from /usr/lib64/python2.6/site-packages/gst-0.10/gst/_gst.so
# by generator 1.136
# no doc

# imports
import gobject as __gobject
import gobject._gobject as __gobject__gobject
import gst as __gst


# Variables with simple values

ACTIVATE_NONE = 0
ACTIVATE_PULL = 2
ACTIVATE_PUSH = 1

ALLOC_TRACE_LIVE = 1

ALLOC_TRACE_MEM_LIVE = 2

ASSOCIATION_FLAG_DELTA_UNIT = 2

ASSOCIATION_FLAG_KEY_UNIT = 1

ASSOCIATION_FLAG_LAST = 256
ASSOCIATION_FLAG_NONE = 0

BIN_FLAG_LAST = 33554432

BUFFERING_DOWNLOAD = 1
BUFFERING_LIVE = 3
BUFFERING_STREAM = 0
BUFFERING_TIMESHIFT = 2

BUFFER_COPY_CAPS = 4
BUFFER_COPY_FLAGS = 1
BUFFER_COPY_TIMESTAMPS = 2

BUFFER_FLAG_DELTA_UNIT = 256

BUFFER_FLAG_DISCONT = 32
BUFFER_FLAG_GAP = 128

BUFFER_FLAG_IN_CAPS = 64

BUFFER_FLAG_LAST = 4096
BUFFER_FLAG_MEDIA1 = 512
BUFFER_FLAG_MEDIA2 = 1024
BUFFER_FLAG_MEDIA3 = 2048
BUFFER_FLAG_PREROLL = 16
BUFFER_FLAG_READONLY = 1

BUFFER_LIST_CONTINUE = 0
BUFFER_LIST_END = 2

BUFFER_LIST_SKIP_GROUP = 1

BUFFER_OFFSET_NONE = 18446744073709551615L

BUS_ASYNC = 2
BUS_DROP = 0

BUS_FLAG_LAST = 32

BUS_FLUSHING = 16
BUS_PASS = 1

CAPS_FLAGS_ANY = 1

CLOCK_BADTIME = 4
CLOCK_BUSY = 3
CLOCK_EARLY = 1

CLOCK_ENTRY_PERIODIC = 1
CLOCK_ENTRY_SINGLE = 0

CLOCK_ERROR = 5

CLOCK_FLAG_CAN_DO_PERIODIC_ASYNC = 128
CLOCK_FLAG_CAN_DO_PERIODIC_SYNC = 64

CLOCK_FLAG_CAN_DO_SINGLE_ASYNC = 32
CLOCK_FLAG_CAN_DO_SINGLE_SYNC = 16

CLOCK_FLAG_CAN_SET_MASTER = 512
CLOCK_FLAG_CAN_SET_RESOLUTION = 256

CLOCK_FLAG_LAST = 4096

CLOCK_OK = 0

CLOCK_TIME_NONE = 18446744073709551615L

CLOCK_UNSCHEDULED = 2
CLOCK_UNSUPPORTED = 6

CORE_ERROR = 'gst-core-error-quark'

CORE_ERROR_CAPS = 10
CORE_ERROR_CLOCK = 13
CORE_ERROR_DISABLED = 14
CORE_ERROR_EVENT = 8
CORE_ERROR_FAILED = 1

CORE_ERROR_MISSING_PLUGIN = 12

CORE_ERROR_NEGOTIATION = 7

CORE_ERROR_NOT_IMPLEMENTED = 3

CORE_ERROR_NUM_ERRORS = 15

CORE_ERROR_PAD = 5
CORE_ERROR_SEEK = 9

CORE_ERROR_STATE_CHANGE = 4

CORE_ERROR_TAG = 11
CORE_ERROR_THREAD = 6

CORE_ERROR_TOO_LAZY = 2

DEBUG_BG_BLACK = 0
DEBUG_BG_BLUE = 64
DEBUG_BG_CYAN = 96
DEBUG_BG_GREEN = 32
DEBUG_BG_MAGENTA = 80
DEBUG_BG_RED = 16
DEBUG_BG_WHITE = 112
DEBUG_BG_YELLOW = 48

DEBUG_BOLD = 256

DEBUG_FG_BLACK = 0
DEBUG_FG_BLUE = 4
DEBUG_FG_CYAN = 6
DEBUG_FG_GREEN = 2
DEBUG_FG_MAGENTA = 5
DEBUG_FG_RED = 1
DEBUG_FG_WHITE = 7
DEBUG_FG_YELLOW = 3

DEBUG_GRAPH_SHOW_ALL = 15

DEBUG_GRAPH_SHOW_CAPS_DETAILS = 2

DEBUG_GRAPH_SHOW_MEDIA_TYPE = 1

DEBUG_GRAPH_SHOW_NON_DEFAULT_PARAMS = 4

DEBUG_GRAPH_SHOW_STATES = 8

DEBUG_UNDERLINE = 512

DP Version 0.2 = 1
DP Version 1.0 = 2

DP_HEADER_FLAG_CRC = 3

DP_HEADER_FLAG_CRC_HEADER = 1
DP_HEADER_FLAG_CRC_PAYLOAD = 2

DP_HEADER_FLAG_NONE = 0

DP_PAYLOAD_BUFFER = 1
DP_PAYLOAD_CAPS = 2

DP_PAYLOAD_EVENT_NONE = 64

DP_PAYLOAD_NONE = 0

ELEMENT_FLAG_LAST = 1048576

ELEMENT_IS_SINK = 32

ELEMENT_LOCKED_STATE = 16

ELEMENT_UNPARENTING = 64

EVENT_BUFFERSIZE = 134

EVENT_CUSTOM_BOTH = 519

EVENT_CUSTOM_BOTH_OOB = 515

EVENT_CUSTOM_DOWNSTREAM = 518

EVENT_CUSTOM_DOWNSTREAM_OOB = 514

EVENT_CUSTOM_UPSTREAM = 513

EVENT_EOS = 86

EVENT_FLUSH_START = 19
EVENT_FLUSH_STOP = 39

EVENT_LATENCY = 289
EVENT_NAVIGATION = 273
EVENT_NEWSEGMENT = 102
EVENT_QOS = 241
EVENT_SEEK = 257

EVENT_SINK_MESSAGE = 150

EVENT_STEP = 305
EVENT_TAG = 118

EVENT_TYPE_DOWNSTREAM = 2
EVENT_TYPE_SERIALIZED = 4
EVENT_TYPE_UPSTREAM = 1

EVENT_UNKNOWN = 0

FLOW_CUSTOM_ERROR = -100

FLOW_CUSTOM_ERROR_1 = -101
FLOW_CUSTOM_ERROR_2 = -102

FLOW_CUSTOM_SUCCESS = 100

FLOW_CUSTOM_SUCCESS_1 = 101
FLOW_CUSTOM_SUCCESS_2 = 102

FLOW_ERROR = -5

FLOW_NOT_LINKED = -1
FLOW_NOT_NEGOTIATED = -4
FLOW_NOT_SUPPORTED = -6

FLOW_OK = 0
FLOW_RESEND = 1
FLOW_UNEXPECTED = -3

FLOW_WRONG_STATE = -2

FORMAT_BUFFERS = 4
FORMAT_BYTES = 2
FORMAT_DEFAULT = 1
FORMAT_PERCENT = 5
FORMAT_TIME = 3
FORMAT_UNDEFINED = 0

INDEX_CERTAIN = 1

INDEX_ENTRY_ASSOCIATION = 1
INDEX_ENTRY_FORMAT = 3
INDEX_ENTRY_ID = 0
INDEX_ENTRY_OBJECT = 2

INDEX_FLAG_LAST = 4096

INDEX_FUZZY = 2

INDEX_LOOKUP_AFTER = 2
INDEX_LOOKUP_BEFORE = 1
INDEX_LOOKUP_EXACT = 0

INDEX_READABLE = 32

INDEX_RESOLVER_CUSTOM = 0
INDEX_RESOLVER_GTYPE = 1
INDEX_RESOLVER_PATH = 2

INDEX_UNKNOWN = 0
INDEX_WRITABLE = 16

INTERPOLATE_CUBIC = 4
INTERPOLATE_LINEAR = 2
INTERPOLATE_NONE = 0
INTERPOLATE_QUADRATIC = 3
INTERPOLATE_TRIGGER = 1
INTERPOLATE_USER = 5

ITERATOR_DONE = 0
ITERATOR_ERROR = 3

ITERATOR_ITEM_END = 2
ITERATOR_ITEM_PASS = 1
ITERATOR_ITEM_SKIP = 0

ITERATOR_OK = 1
ITERATOR_RESYNC = 2

LEVEL_COUNT = 10
LEVEL_DEBUG = 4
LEVEL_ERROR = 1
LEVEL_FIXME = 6
LEVEL_INFO = 3
LEVEL_LOG = 5
LEVEL_MEMDUMP = 9
LEVEL_NONE = 0
LEVEL_WARNING = 2

LIBRARY_ERROR = 'gst-library-error-quark'

LIBRARY_ERROR_ENCODE = 6
LIBRARY_ERROR_FAILED = 1
LIBRARY_ERROR_INIT = 3

LIBRARY_ERROR_NUM_ERRORS = 7

LIBRARY_ERROR_SETTINGS = 5
LIBRARY_ERROR_SHUTDOWN = 4

LIBRARY_ERROR_TOO_LAZY = 2

MESSAGE_ANY = 4294967295
MESSAGE_APPLICATION = 16384

MESSAGE_ASYNC_DONE = 2097152
MESSAGE_ASYNC_START = 1048576

MESSAGE_BUFFERING = 32

MESSAGE_CLOCK_LOST = 1024
MESSAGE_CLOCK_PROVIDE = 512

MESSAGE_DURATION = 262144
MESSAGE_ELEMENT = 32768
MESSAGE_EOS = 1
MESSAGE_ERROR = 2
MESSAGE_INFO = 8
MESSAGE_LATENCY = 524288

MESSAGE_NEW_CLOCK = 2048

MESSAGE_QOS = 16777216

MESSAGE_REQUEST_STATE = 4194304

MESSAGE_SEGMENT_DONE = 131072
MESSAGE_SEGMENT_START = 65536

MESSAGE_STATE_CHANGED = 64
MESSAGE_STATE_DIRTY = 128

MESSAGE_STEP_DONE = 256
MESSAGE_STEP_START = 8388608

MESSAGE_STREAM_STATUS = 8192

MESSAGE_STRUCTURE_CHANGE = 4096

MESSAGE_TAG = 16
MESSAGE_UNKNOWN = 0
MESSAGE_WARNING = 4

MINI_OBJECT_FLAG_LAST = 16
MINI_OBJECT_FLAG_READONLY = 1

MSECOND = 1000000

NSECOND = 1

OBJECT_DISPOSING = 1

OBJECT_FLAG_LAST = 16

OBJECT_FLOATING = 2

PAD_ALWAYS = 0
PAD_BLOCKED = 16
PAD_BLOCKING = 256

PAD_FLAG_LAST = 4096

PAD_FLUSHING = 32

PAD_IN_GETCAPS = 64
PAD_IN_SETCAPS = 128

PAD_LINK_NOFORMAT = -4
PAD_LINK_NOSCHED = -5
PAD_LINK_OK = 0
PAD_LINK_REFUSED = -6

PAD_LINK_WAS_LINKED = -2

PAD_LINK_WRONG_DIRECTION = -3
PAD_LINK_WRONG_HIERARCHY = -1

PAD_REQUEST = 2
PAD_SINK = 2
PAD_SOMETIMES = 1
PAD_SRC = 1

PAD_TEMPLATE_FIXED = 16

PAD_TEMPLATE_FLAG_LAST = 256

PAD_UNKNOWN = 0

PARAM_CONTROLLABLE = 512

PARAM_MUTABLE_PAUSED = 2048
PARAM_MUTABLE_PLAYING = 4096
PARAM_MUTABLE_READY = 1024

PARAM_USER_SHIFT = 65536

PARSE_ERROR_COULD_NOT_SET_PROPERTY = 4

PARSE_ERROR_EMPTY = 6

PARSE_ERROR_EMPTY_BIN = 5

PARSE_ERROR_LINK = 3

PARSE_ERROR_NO_SUCH_ELEMENT = 1
PARSE_ERROR_NO_SUCH_PROPERTY = 2

PARSE_ERROR_SYNTAX = 0

PARSE_FLAG_FATAL_ERRORS = 1

PARSE_FLAG_NONE = 0

PIPELINE_FLAG_FIXED_CLOCK = 33554432

PIPELINE_FLAG_LAST = 536870912

PLUGIN_ERROR_DEPENDENCIES = 1
PLUGIN_ERROR_MODULE = 0

PLUGIN_ERROR_NAME_MISMATCH = 2

PLUGIN_FLAG_BLACKLISTED = 2
PLUGIN_FLAG_CACHED = 1

QUERY_BUFFERING = 10
QUERY_CONVERT = 8
QUERY_CUSTOM = 11
QUERY_DURATION = 2
QUERY_FORMATS = 9
QUERY_JITTER = 4
QUERY_LATENCY = 3
QUERY_NONE = 0
QUERY_POSITION = 1
QUERY_RATE = 5
QUERY_SEEKING = 6
QUERY_SEGMENT = 7
QUERY_URI = 12

RANK_MARGINAL = 64
RANK_NONE = 0
RANK_PRIMARY = 256
RANK_SECONDARY = 128

RESOURCE_ERROR = 'gst-resource-error-quark'

RESOURCE_ERROR_BUSY = 4
RESOURCE_ERROR_CLOSE = 8
RESOURCE_ERROR_FAILED = 1

RESOURCE_ERROR_NOT_FOUND = 3

RESOURCE_ERROR_NO_SPACE_LEFT = 14

RESOURCE_ERROR_NUM_ERRORS = 15

RESOURCE_ERROR_OPEN_READ = 5

RESOURCE_ERROR_OPEN_READ_WRITE = 7

RESOURCE_ERROR_OPEN_WRITE = 6

RESOURCE_ERROR_READ = 9
RESOURCE_ERROR_SEEK = 11
RESOURCE_ERROR_SETTINGS = 13
RESOURCE_ERROR_SYNC = 12

RESOURCE_ERROR_TOO_LAZY = 2

RESOURCE_ERROR_WRITE = 10

Reverse saw waveform = 3

Saw waveform = 2

SEARCH_MODE_AFTER = 2
SEARCH_MODE_BEFORE = 1
SEARCH_MODE_EXACT = 0

SECOND = 1000000000

SEEK_FLAG_ACCURATE = 2
SEEK_FLAG_FLUSH = 1

SEEK_FLAG_KEY_UNIT = 4

SEEK_FLAG_NONE = 0
SEEK_FLAG_SEGMENT = 8
SEEK_FLAG_SKIP = 16

SEEK_TYPE_CUR = 1
SEEK_TYPE_END = 3
SEEK_TYPE_NONE = 0
SEEK_TYPE_SET = 2

Sine waveform (default) = 0

Square waveform = 1

STATE_CHANGE_ASYNC = 2
STATE_CHANGE_FAILURE = 0

STATE_CHANGE_NO_PREROLL = 3

STATE_CHANGE_NULL_TO_READY = 10

STATE_CHANGE_PAUSED_TO_PLAYING = 28
STATE_CHANGE_PAUSED_TO_READY = 26

STATE_CHANGE_PLAYING_TO_PAUSED = 35

STATE_CHANGE_READY_TO_NULL = 17
STATE_CHANGE_READY_TO_PAUSED = 19

STATE_CHANGE_SUCCESS = 1

STATE_NULL = 1
STATE_PAUSED = 3
STATE_PLAYING = 4
STATE_READY = 2

STATE_VOID_PENDING = 0

STREAM_ERROR = 'gst-stream-error-quark'

STREAM_ERROR_CODEC_NOT_FOUND = 6

STREAM_ERROR_DECODE = 7
STREAM_ERROR_DECRYPT = 12

STREAM_ERROR_DECRYPT_NOKEY = 13

STREAM_ERROR_DEMUX = 9
STREAM_ERROR_ENCODE = 8
STREAM_ERROR_FAILED = 1
STREAM_ERROR_FORMAT = 11
STREAM_ERROR_MUX = 10

STREAM_ERROR_NOT_IMPLEMENTED = 3

STREAM_ERROR_NUM_ERRORS = 14

STREAM_ERROR_TOO_LAZY = 2

STREAM_ERROR_TYPE_NOT_FOUND = 4

STREAM_ERROR_WRONG_TYPE = 5

STREAM_STATUS_TYPE_CREATE = 0
STREAM_STATUS_TYPE_DESTROY = 3
STREAM_STATUS_TYPE_ENTER = 1
STREAM_STATUS_TYPE_LEAVE = 2
STREAM_STATUS_TYPE_PAUSE = 9
STREAM_STATUS_TYPE_START = 8
STREAM_STATUS_TYPE_STOP = 10

STRUCTURE_CHANGE_TYPE_PAD_LINK = 0
STRUCTURE_CHANGE_TYPE_PAD_UNLINK = 1

TAG_ALBUM = 'album'

TAG_ALBUM_GAIN = 'replaygain-album-gain'
TAG_ALBUM_PEAK = 'replaygain-album-peak'
TAG_ALBUM_SORTNAME = 'album-sortname'

TAG_ALBUM_VOLUME_COUNT = 'album-disc-count'
TAG_ALBUM_VOLUME_NUMBER = 'album-disc-number'

TAG_ARTIST = 'artist'

TAG_ARTIST_SORTNAME = 'musicbrainz-sortname'

TAG_AUDIO_CODEC = 'audio-codec'

TAG_BITRATE = 'bitrate'
TAG_CODEC = 'codec'
TAG_COMMENT = 'comment'
TAG_COMPOSER = 'composer'
TAG_CONTACT = 'contact'
TAG_COPYRIGHT = 'copyright'
TAG_DATE = 'date'
TAG_DESCRIPTION = 'description'
TAG_DURATION = 'duration'
TAG_ENCODER = 'encoder'

TAG_ENCODER_VERSION = 'encoder-version'

TAG_EXTENDED_COMMENT = 'extended-comment'

TAG_FLAG_COUNT = 4
TAG_FLAG_DECODED = 3
TAG_FLAG_ENCODED = 2
TAG_FLAG_META = 1
TAG_FLAG_UNDEFINED = 0

TAG_GENRE = 'genre'
TAG_HOMEPAGE = 'homepage'
TAG_IMAGE = 'image'
TAG_ISRC = 'isrc'

TAG_LANGUAGE_CODE = 'language-code'

TAG_LICENSE = 'license'

TAG_LICENSE_URI = 'license-uri'

TAG_LOCATION = 'location'

TAG_MAXIMUM_BITRATE = 'maximum-bitrate'

TAG_MERGE_APPEND = 3
TAG_MERGE_COUNT = 7
TAG_MERGE_KEEP = 5

TAG_MERGE_KEEP_ALL = 6

TAG_MERGE_PREPEND = 4
TAG_MERGE_REPLACE = 2

TAG_MERGE_REPLACE_ALL = 1

TAG_MERGE_UNDEFINED = 0

TAG_MINIMUM_BITRATE = 'minimum-bitrate'

TAG_NOMINAL_BITRATE = 'nominal-bitrate'

TAG_ORGANIZATION = 'organization'
TAG_PERFORMER = 'performer'

TAG_PREVIEW_IMAGE = 'preview-image'

TAG_SERIAL = 'serial'

TAG_SUBTITLE_CODEC = 'subtitle-codec'

TAG_TITLE = 'title'

TAG_TITLE_SORTNAME = 'title-sortname'

TAG_TRACK_COUNT = 'track-count'
TAG_TRACK_GAIN = 'replaygain-track-gain'
TAG_TRACK_NUMBER = 'track-number'
TAG_TRACK_PEAK = 'replaygain-track-peak'

TAG_VERSION = 'version'

TAG_VIDEO_CODEC = 'video-codec'

TASK_PAUSED = 2
TASK_STARTED = 0
TASK_STOPPED = 1

Triangle waveform = 4

TYPE_FIND_LIKELY = 80
TYPE_FIND_MAXIMUM = 100
TYPE_FIND_MINIMUM = 1

TYPE_FIND_NEARLY_CERTAIN = 99

TYPE_FIND_POSSIBLE = 50

URI_SINK = 1
URI_SRC = 2
URI_UNKNOWN = 0

# functions

def alloc_trace_available(*args, **kwargs): # real signature unknown
    pass

def alloc_trace_live_all(*args, **kwargs): # real signature unknown
    pass

def alloc_trace_print_all(*args, **kwargs): # real signature unknown
    pass

def alloc_trace_print_live(*args, **kwargs): # real signature unknown
    pass

def alloc_trace_set_flags_all(*args, **kwargs): # real signature unknown
    pass

def buffer_new_and_alloc(*args, **kwargs): # real signature unknown
    pass

def buffer_try_new_and_alloc(*args, **kwargs): # real signature unknown
    pass

def caps_from_string(*args, **kwargs): # real signature unknown
    pass

def caps_new_any(*args, **kwargs): # real signature unknown
    pass

def debug(*args, **kwargs): # real signature unknown
    pass

def DEBUG_BIN_TO_DOT_FILE(*args, **kwargs): # real signature unknown
    pass

def DEBUG_BIN_TO_DOT_FILE_WITH_TS(*args, **kwargs): # real signature unknown
    pass

def debug_construct_term_color(*args, **kwargs): # real signature unknown
    pass

def debug_construct_win_color(*args, **kwargs): # real signature unknown
    pass

def debug_get_default_threshold(*args, **kwargs): # real signature unknown
    pass

def debug_is_active(*args, **kwargs): # real signature unknown
    pass

def debug_is_colored(*args, **kwargs): # real signature unknown
    pass

def debug_log(*args, **kwargs): # real signature unknown
    pass

def debug_set_active(*args, **kwargs): # real signature unknown
    pass

def debug_set_colored(*args, **kwargs): # real signature unknown
    pass

def debug_set_default_threshold(*args, **kwargs): # real signature unknown
    pass

def debug_set_threshold_for_name(*args, **kwargs): # real signature unknown
    pass

def debug_unset_threshold_for_name(*args, **kwargs): # real signature unknown
    pass

def default_registry_check_feature_version(*args, **kwargs): # real signature unknown
    pass

def dp_buffer_from_header(*args, **kwargs): # real signature unknown
    pass

def dp_caps_from_packet(*args, **kwargs): # real signature unknown
    pass

def dp_event_from_packet(*args, **kwargs): # real signature unknown
    pass

def dp_header_payload_length(*args, **kwargs): # real signature unknown
    pass

def dp_header_payload_type(*args, **kwargs): # real signature unknown
    pass

def dp_init(*args, **kwargs): # real signature unknown
    pass

def dp_validate_header(*args, **kwargs): # real signature unknown
    pass

def dp_validate_packet(*args, **kwargs): # real signature unknown
    pass

def dp_validate_payload(*args, **kwargs): # real signature unknown
    pass

def element_factory_find(*args, **kwargs): # real signature unknown
    pass

def element_factory_make(*args, **kwargs): # real signature unknown
    pass

def element_link_many(*args, **kwargs): # real signature unknown
    pass

def element_make_from_uri(*args, **kwargs): # real signature unknown
    pass

def element_register(*args, **kwargs): # real signature unknown
    pass

def element_state_get_name(*args, **kwargs): # real signature unknown
    pass

def element_unlink_many(*args, **kwargs): # real signature unknown
    pass

def error(*args, **kwargs): # real signature unknown
    pass

def event_new_buffer_size(*args, **kwargs): # real signature unknown
    pass

def event_new_custom(*args, **kwargs): # real signature unknown
    pass

def event_new_eos(*args, **kwargs): # real signature unknown
    pass

def event_new_flush_start(*args, **kwargs): # real signature unknown
    pass

def event_new_flush_stop(*args, **kwargs): # real signature unknown
    pass

def event_new_latency(*args, **kwargs): # real signature unknown
    pass

def event_new_navigation(*args, **kwargs): # real signature unknown
    pass

def event_new_new_segment(*args, **kwargs): # real signature unknown
    pass

def event_new_new_segment_full(*args, **kwargs): # real signature unknown
    pass

def event_new_qos(*args, **kwargs): # real signature unknown
    pass

def event_new_seek(*args, **kwargs): # real signature unknown
    pass

def event_new_step(*args, **kwargs): # real signature unknown
    pass

def event_new_tag(*args, **kwargs): # real signature unknown
    pass

def fixme(*args, **kwargs): # real signature unknown
    pass

def flow_get_name(*args, **kwargs): # real signature unknown
    pass

def format_get_by_nick(*args, **kwargs): # real signature unknown
    pass

def format_iterate_definitions(*args, **kwargs): # real signature unknown
    pass

def format_register(*args, **kwargs): # real signature unknown
    pass

def get_gst_version(*args, **kwargs): # real signature unknown
    pass

def get_pygst_version(*args, **kwargs): # real signature unknown
    pass

def ghost_pad_new_from_template(*args, **kwargs): # real signature unknown
    pass

def ghost_pad_new_notarget(*args, **kwargs): # real signature unknown
    pass

def ghost_pad_new_no_target_from_template(*args, **kwargs): # real signature unknown
    pass

def gst_object_get_control_source(*args, **kwargs): # real signature unknown
    pass

def gst_object_set_control_source(*args, **kwargs): # real signature unknown
    pass

def index_factory_find(*args, **kwargs): # real signature unknown
    pass

def index_factory_make(*args, **kwargs): # real signature unknown
    pass

def info(*args, **kwargs): # real signature unknown
    pass

def log(*args, **kwargs): # real signature unknown
    pass

def memdump(*args, **kwargs): # real signature unknown
    pass

def message_new_application(*args, **kwargs): # real signature unknown
    pass

def message_new_async_done(*args, **kwargs): # real signature unknown
    pass

def message_new_async_start(*args, **kwargs): # real signature unknown
    pass

def message_new_buffering(*args, **kwargs): # real signature unknown
    pass

def message_new_clock_lost(*args, **kwargs): # real signature unknown
    pass

def message_new_clock_provide(*args, **kwargs): # real signature unknown
    pass

def message_new_custom(*args, **kwargs): # real signature unknown
    pass

def message_new_duration(*args, **kwargs): # real signature unknown
    pass

def message_new_element(*args, **kwargs): # real signature unknown
    pass

def message_new_eos(*args, **kwargs): # real signature unknown
    pass

def message_new_error(*args, **kwargs): # real signature unknown
    pass

def message_new_info(*args, **kwargs): # real signature unknown
    pass

def message_new_latency(*args, **kwargs): # real signature unknown
    pass

def message_new_new_clock(*args, **kwargs): # real signature unknown
    pass

def message_new_request_state(*args, **kwargs): # real signature unknown
    pass

def message_new_segment_done(*args, **kwargs): # real signature unknown
    pass

def message_new_segment_start(*args, **kwargs): # real signature unknown
    pass

def message_new_state_changed(*args, **kwargs): # real signature unknown
    pass

def message_new_state_dirty(*args, **kwargs): # real signature unknown
    pass

def message_new_step_done(*args, **kwargs): # real signature unknown
    pass

def message_new_step_start(*args, **kwargs): # real signature unknown
    pass

def message_new_stream_status(*args, **kwargs): # real signature unknown
    pass

def message_new_structure_change(*args, **kwargs): # real signature unknown
    pass

def message_new_tag(*args, **kwargs): # real signature unknown
    pass

def message_new_tag_full(*args, **kwargs): # real signature unknown
    pass

def message_new_warning(*args, **kwargs): # real signature unknown
    pass

def object_get_controller(*args, **kwargs): # real signature unknown
    pass

def object_get_control_rate(*args, **kwargs): # real signature unknown
    pass

def object_set_controller(*args, **kwargs): # real signature unknown
    pass

def object_set_control_rate(*args, **kwargs): # real signature unknown
    pass

def object_suggest_next_sync(*args, **kwargs): # real signature unknown
    pass

def object_sync_values(*args, **kwargs): # real signature unknown
    pass

def pad_new_from_static_template(*args, **kwargs): # real signature unknown
    pass

def parse_bin_from_description(*args, **kwargs): # real signature unknown
    pass

def parse_launch(*args, **kwargs): # real signature unknown
    pass

def plugin_load_by_name(*args, **kwargs): # real signature unknown
    pass

def plugin_load_file(*args, **kwargs): # real signature unknown
    pass

def query_new_application(*args, **kwargs): # real signature unknown
    pass

def query_new_buffering(*args, **kwargs): # real signature unknown
    pass

def query_new_convert(*args, **kwargs): # real signature unknown
    pass

def query_new_duration(*args, **kwargs): # real signature unknown
    pass

def query_new_formats(*args, **kwargs): # real signature unknown
    pass

def query_new_latency(*args, **kwargs): # real signature unknown
    pass

def query_new_position(*args, **kwargs): # real signature unknown
    pass

def query_new_seeking(*args, **kwargs): # real signature unknown
    pass

def query_new_segment(*args, **kwargs): # real signature unknown
    pass

def query_new_uri(*args, **kwargs): # real signature unknown
    pass

def query_type_get_by_nick(*args, **kwargs): # real signature unknown
    pass

def query_type_iterate_definitions(*args, **kwargs): # real signature unknown
    pass

def query_type_register(*args, **kwargs): # real signature unknown
    pass

def registry_fork_is_enabled(*args, **kwargs): # real signature unknown
    pass

def registry_fork_set_enabled(*args, **kwargs): # real signature unknown
    pass

def registry_get_default(*args, **kwargs): # real signature unknown
    pass

def segtrap_is_enabled(*args, **kwargs): # real signature unknown
    pass

def segtrap_set_enabled(*args, **kwargs): # real signature unknown
    pass

def state_change_return_get_name(*args, **kwargs): # real signature unknown
    pass

def structure_from_string(*args, **kwargs): # real signature unknown
    pass

def system_clock_obtain(*args, **kwargs): # real signature unknown
    pass

def tag_exists(*args, **kwargs): # real signature unknown
    pass

def tag_get_description(*args, **kwargs): # real signature unknown
    pass

def tag_get_flag(*args, **kwargs): # real signature unknown
    pass

def tag_get_nick(*args, **kwargs): # real signature unknown
    pass

def tag_get_tag_type(*args, **kwargs): # real signature unknown
    pass

def tag_is_fixed(*args, **kwargs): # real signature unknown
    pass

def TIME_ARGS(*args, **kwargs): # real signature unknown
    pass

def type_find_factory_get_list(*args, **kwargs): # real signature unknown
    pass

def type_find_helper(*args, **kwargs): # real signature unknown
    pass

def type_find_helper_for_buffer(*args, **kwargs): # real signature unknown
    pass

def type_find_helper_for_extension(*args, **kwargs): # real signature unknown
    pass

def type_find_new(*args, **kwargs): # real signature unknown
    pass

def type_find_register(*args, **kwargs): # real signature unknown
    pass

def update_registry(*args, **kwargs): # real signature unknown
    pass

def uri_construct(*args, **kwargs): # real signature unknown
    pass

def uri_get_location(*args, **kwargs): # real signature unknown
    pass

def uri_get_protocol(*args, **kwargs): # real signature unknown
    pass

def uri_has_protocol(*args, **kwargs): # real signature unknown
    pass

def uri_is_valid(*args, **kwargs): # real signature unknown
    pass

def uri_protocol_is_supported(*args, **kwargs): # real signature unknown
    pass

def uri_protocol_is_valid(*args, **kwargs): # real signature unknown
    pass

def util_dump_mem(*args, **kwargs): # real signature unknown
    pass

def util_gdouble_to_guint64(*args, **kwargs): # real signature unknown
    pass

def util_get_timestamp(*args, **kwargs): # real signature unknown
    pass

def util_guint64_to_gdouble(*args, **kwargs): # real signature unknown
    pass

def util_seqnum_compare(*args, **kwargs): # real signature unknown
    pass

def util_seqnum_next(*args, **kwargs): # real signature unknown
    pass

def util_set_object_arg(*args, **kwargs): # real signature unknown
    pass

def util_uint64_scale(*args, **kwargs): # real signature unknown
    pass

def util_uint64_scale_int(*args, **kwargs): # real signature unknown
    pass

def version_string(*args, **kwargs): # real signature unknown
    pass

def warning(*args, **kwargs): # real signature unknown
    pass

def xml_make_element(*args, **kwargs): # real signature unknown
    pass

def xml_write(*args, **kwargs): # real signature unknown
    pass

def xml_write_file(*args, **kwargs): # real signature unknown
    pass

# classes

from ActivateMode import ActivateMode
from Adapter import Adapter
from AddError import AddError
from AllocTraceFlags import AllocTraceFlags
from AssocFlags import AssocFlags
from Object import Object
from Element import Element
from BaseSink import BaseSink
from BaseSrc import BaseSrc
from BaseTransform import BaseTransform
from Bin import Bin
from BinFlags import BinFlags
from MiniObject import MiniObject
from Buffer import Buffer
from BufferCopyFlags import BufferCopyFlags
from BufferFlag import BufferFlag
from BufferingMode import BufferingMode
from BufferList import BufferList
from BufferListItem import BufferListItem
from Bus import Bus
from BusFlags import BusFlags
from BusSyncReply import BusSyncReply
from Caps import Caps
from CapsFlags import CapsFlags
from Clock import Clock
from ClockEntryType import ClockEntryType
from ClockFlags import ClockFlags
from ClockReturn import ClockReturn
from CollectPads import CollectPads
from Controller import Controller
from ControlSource import ControlSource
from CoreError import CoreError
from DataQueue import DataQueue
from Date import Date
from DebugColorFlags import DebugColorFlags
from DebugGraphDetails import DebugGraphDetails
from DebugLevel import DebugLevel
from DPVersion import DPVersion
from PluginFeature import PluginFeature
from ElementFactory import ElementFactory
from ElementFlags import ElementFlags
from PluginNotFoundError import PluginNotFoundError
from ElementNotFoundError import ElementNotFoundError
from Event import Event
from EventType import EventType
from EventTypeFlags import EventTypeFlags
from FlowReturn import FlowReturn
from Format import Format
from GError import GError
from Pad import Pad
from GhostPad import GhostPad
from ImplementsInterface import ImplementsInterface
from Index import Index
from IndexCertainty import IndexCertainty
from IndexEntry import IndexEntry
from IndexEntryType import IndexEntryType
from IndexFactory import IndexFactory
from IndexFlags import IndexFlags
from IndexLookupMethod import IndexLookupMethod
from IndexResolverMethod import IndexResolverMethod
from InterpolationControlSource import InterpolationControlSource
from Iterator import Iterator
from IteratorItem import IteratorItem
from IteratorResult import IteratorResult
from LFOControlSource import LFOControlSource
from LFOWaveform import LFOWaveform
from LibraryError import LibraryError
from LinkError import LinkError
from Message import Message
from MessageType import MessageType
from MiniObjectFlags import MiniObjectFlags
from SystemClock import SystemClock
from NetClientClock import NetClientClock
from NetTimeProvider import NetTimeProvider
from ObjectFlags import ObjectFlags
from PadDirection import PadDirection
from PadFlags import PadFlags
from PadLinkReturn import PadLinkReturn
from PadPresence import PadPresence
from PadTemplate import PadTemplate
from PadTemplateFlags import PadTemplateFlags
from ParseError import ParseError
from ParseFlags import ParseFlags
from Pipeline import Pipeline
from PipelineFlags import PipelineFlags
from Plugin import Plugin
from PluginError import PluginError
from PluginFlags import PluginFlags
from Preset import Preset
from Query import Query
from QueryError import QueryError
from QueryType import QueryType
from Rank import Rank
from Registry import Registry
from RemoveError import RemoveError
from ResourceError import ResourceError
from SearchMode import SearchMode
from SeekFlags import SeekFlags
from SeekType import SeekType
from Segment import Segment
from State import State
from StateChange import StateChange
from StateChangeReturn import StateChangeReturn
from StaticCaps import StaticCaps
from StaticPadTemplate import StaticPadTemplate
from StreamError import StreamError
from StreamStatusType import StreamStatusType
from Structure import Structure
from StructureChangeType import StructureChangeType
from TagFlag import TagFlag
from TagList import TagList
from TagMergeMode import TagMergeMode
from TagSetter import TagSetter
from Task import Task
from TaskPool import TaskPool
from TaskState import TaskState
from TypeFind import TypeFind
from TypeFindFactory import TypeFindFactory
from TypeFindProbability import TypeFindProbability
from URIHandler import URIHandler
from URIType import URIType
from XML import XML
# variables with complex values

gst_version = (
    0,
    10,
    29,
)

pygst_version = (
    0,
    10,
    16,
)

TYPE_ELEMENT_FACTORY = None # (!) real value is ''

TYPE_INDEX_FACTORY = None # (!) real value is ''

TYPE_TYPE_FIND_FACTORY = None # (!) real value is ''

