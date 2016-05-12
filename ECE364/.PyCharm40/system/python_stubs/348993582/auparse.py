# encoding: utf-8
# module auparse
# from /usr/lib64/python2.6/site-packages/auparse.so
# by generator 1.136
"""
Parsing library for audit messages.

The module defines the following exceptions:

NoParser: Raised if the underlying C code parser is not bound to the AuParser object.
"""
# no imports

# Variables with simple values

AUPARSE_CB_EVENT_READY = 0

AUPARSE_TYPE_A0 = 14
AUPARSE_TYPE_A1 = 15
AUPARSE_TYPE_A2 = 16
AUPARSE_TYPE_ARCH = 4
AUPARSE_TYPE_CAPABILITY = 12
AUPARSE_TYPE_ESCAPED = 6
AUPARSE_TYPE_EXIT = 5
AUPARSE_TYPE_FLAGS = 10
AUPARSE_TYPE_GID = 2
AUPARSE_TYPE_LIST = 19
AUPARSE_TYPE_MODE = 8
AUPARSE_TYPE_PERM = 7
AUPARSE_TYPE_PROMISC = 11
AUPARSE_TYPE_SIGNAL = 18
AUPARSE_TYPE_SOCKADDR = 9
AUPARSE_TYPE_SUCCESS = 13
AUPARSE_TYPE_SYSCALL = 3
AUPARSE_TYPE_UID = 1
AUPARSE_TYPE_UNCLASSIFIED = 0

AUSEARCH_EQUAL = 2
AUSEARCH_EXISTS = 1

AUSEARCH_NOT_EQUAL = 3

AUSEARCH_RULE_AND = 2
AUSEARCH_RULE_CLEAR = 0
AUSEARCH_RULE_OR = 1
AUSEARCH_RULE_REGEX = 3

AUSEARCH_STOP_EVENT = 0
AUSEARCH_STOP_FIELD = 2
AUSEARCH_STOP_RECORD = 1

AUSEARCH_UNSET = 0

AUSOURCE_BUFFER = 3

AUSOURCE_BUFFER_ARRAY = 4

AUSOURCE_DESCRIPTOR = 5
AUSOURCE_FEED = 7
AUSOURCE_FILE = 1

AUSOURCE_FILE_ARRAY = 2
AUSOURCE_FILE_POINTER = 6

AUSOURCE_LOGS = 0

# no functions
# classes

class AuEvent(object):
    """
    An internal object which encapsulates the timestamp, serial number
    and host information of an audit event. The object cannot be
    instantiated from python code, rather it is returned from the
    audit parsing API.
    """
    def __cmp__(self, y): # real signature unknown; restored from __doc__
        """ x.__cmp__(y) <==> cmp(x,y) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    host = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Machine's name"""

    milli = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """millisecond of the timestamp"""

    sec = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Event seconds"""

    serial = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Serial number of the event"""



class AuParser(object):
    """
    AuParser(source_type, source)
    
    Construct a new audit parser object and bind it to input data.
    source_type: one of the AUSOURCE_* constants.
    source:      the input data, dependent on the source_type as follows:
    
    AUSOURCE_LOGS:         None (system log files will be parsed)
    AUSOURCE_FILE:         string containing file path name
    AUSOURCE_FILE_ARRAY:   list or tuple of strings each containing a file path name
    AUSOURCE_BUFFER:       string containing audit data to parse
    AUSOURCE_BUFFER_ARRAY: list or tuple of strings each containing audit data to parse
    AUSOURCE_DESCRIPTOR:   integer file descriptor (e.g. fileno)
    AUSOURCE_FILE_POINTER: file object (e.g. types.FileType)
    AUSOURCE_FEED:         None (data supplied via feed()
    """
    def add_callback(self, callback, user_data): # real signature unknown; restored from __doc__
        """
        add_callback(callback, user_data) add a callback handler for notifications.
        
        auparse_add_callback adds a callback function to the parse state which
        is invoked to notify the application of parsing events.
        
        The signature of the callback is:
        
        callback(au, cb_event_type,user_data)
        
        When the callback is invoked it is passed:
        au: the AuParser object
        cb_event_type: enumerated value indicating the reason why the callback was invoked
        user_data: user supplied private data
        
        The cb_event_type argument indicates why the callback was invoked.
        It's possible values are:
        
        AUPARSE_CB_EVENT_READY
        A complete event has been parsed and is ready to be examined.
        This is logically equivalent to the parse state immediately following
        auparse_next_event()
        
        Returns None.
        Raises exception (EnvironmentError) on error
        """
        pass

    def feed(self, data): # real signature unknown; restored from __doc__
        """
        feed(data) supplies new data for the parser to consume.
        
        AuParser() must have been called with a source type of AUSOURCE_FEED.
        The parser consumes as much data as it can invoking a user supplied
        callback specified with add_callback() with a cb_event_type of
        AUPARSE_CB_EVENT_READY each time the parser recognizes a complete event
        in the data stream. Data not fully parsed will persist and be prepended
        to the next feed data. After all data has been feed to the parser flush_feed()
        should be called to signal the end of input data and flush any pending
        parse data through the parsing system.
        
        Returns None.
        Raises exception (EnvironmentError) on error
        """
        pass

    def find_field(self, name): # real signature unknown; restored from __doc__
        """
        find_field(name) Search for field name.
        
        find_field() will scan all records in an event to find the first
        occurance of the field name passed to it. Searching begins from the
        cursor’s current position. The field name is stored for subsequent
        searching.
        
        Returns value associated with field or None if not found.
        """
        pass

    def find_field_next(self): # real signature unknown; restored from __doc__
        """
        find_field_next() Get next occurrance of field name
        
        find_field_next() returns the value associated next occurrance of field name.
        Returns value associated with field or None if there is no next field.
        Raises exception (EnvironmentError) on error.
        """
        pass

    def first_field(self): # real signature unknown; restored from __doc__
        """
        first_field() Reposition field cursor.
        
        Returns True on success, False if there is no event data
        """
        pass

    def first_record(self): # real signature unknown; restored from __doc__
        """
        first_record() Reposition record cursor.
        
        first_record() repositions the internal cursors of the parsing library
        to point to the first record in the current event.
        
        Return True for success, False if there is no event data.
        Raises exception (EnvironmentError) on error.
        """
        pass

    def flush_feed(self): # real signature unknown; restored from __doc__
        """
        flush_feed() flush any unconsumed feed data through parser
        
        flush_feed() should be called to signal the end of feed input data
        and flush any pending parse data through the parsing system.
        
        Returns None.
        Raises exception (EnvironmentError) on error
        """
        pass

    def get_field_int(self): # real signature unknown; restored from __doc__
        """
        get_field_int() Get current field’s value as an integer.
        
        get_field_int() allows access to the value as an int of the current
        field of the current record in the current event.
        
        Returns None if the field value is unavailable.
        """
        pass

    def get_field_name(self): # real signature unknown; restored from __doc__
        """
        get_field_name() Get current field’s name.
        
        get_field_name() allows access to the current field name of the
        current record in the current event.
        
        Returns None if the field value is unavailable.
        """
        pass

    def get_field_str(self): # real signature unknown; restored from __doc__
        """
        get_field_str() get current field’s value
        
        get_field_str() allows access to the value in the current field of the
        current record in the current event.
        
        Returns None if the field value is unavailable.
        """
        pass

    def get_field_type(self): # real signature unknown; restored from __doc__
        """
        get_field_type() Get current field’s data type value.
        
        get_field_type() returns a value from the auparse_type_t enum that
        describes the kind of data in the current field of the current record
        in the current event.
        
        Returns AUPARSE_TYPE_UNCLASSIFIED if the field’s data type has no
        known description or is an integer. Otherwise it returns another enum.
        Fields with the type AUPARSE_TYPE_ESCAPED must be interpretted to access
        their value since those field’s raw value is encoded.
        """
        pass

    def get_filename(self): # real signature unknown; restored from __doc__
        """
        auparse_get_filename() get the filename where record was found
        get_filename() will return the name of the source file where the
        record was found if the source type is AUSOURCE_FILE or
        AUSOURCE_FILE_ARRAY. For other source types the return value will be
        None.
        """
        pass

    def get_line_number(self): # real signature unknown; restored from __doc__
        """
        auparse_get_line_number() get line number where record was found
        
        get_line_number will return the source input line number for
        the current record of the current event. Line numbers start at 1.  If
        the source input type is AUSOURCE_FILE_ARRAY the line numbering will
        reset back to 1 each time a new life in the file array is opened.
        """
        pass

    def get_num_fields(self): # real signature unknown; restored from __doc__
        """
        get_num_fields() Get the number of fields.
        
        Returns the number of fields in the current event.
        Raises exception (EnvironmentError) on error.
        """
        pass

    def get_num_records(self): # real signature unknown; restored from __doc__
        """
        get_num_records() Get the number of records.
        
        Returns the number of records in the current event.
        Raises exception (EnvironmentError) on error.
        """
        pass

    def get_record_text(self): # real signature unknown; restored from __doc__
        """
        get_record_text() Return unparsed record data
        
        get_record_text() returns the full unparsed record.
        Raises exception (EnvironmentError) on error.
        """
        pass

    def get_timestamp(self): # real signature unknown; restored from __doc__
        """
        get_timestamp() Return current event's timestamp.
        
        Returns the current event's timestamp info as an AuEvent object.
        No Return value, raises exception (EnvironmentError) on error.
        """
        pass

    def get_type(self): # real signature unknown; restored from __doc__
        """
        get_type() Get record’s type.
        
        get_type() will return the integer value for the current record of the
        current event.
        
        Returns record type.
        Raises exception (LookupError) on error.
        """
        pass

    def goto_record_num(self): # real signature unknown; restored from __doc__
        """
        goto_record_num() Move record cursor to specific position.
        
        goto_record_num() will move the internal library cursors to point
        to a specific physical record number. Records within the same event are
        numbered  starting  from  0. This is generally not needed but there are
        some cases where one may want precise control  over  the  exact  record
        being looked at.
        
        Returns True on success, False if no more records in current event
        Raises exception (EnvironmentError) on error.
        """
        pass

    def interpret_field(self): # real signature unknown; restored from __doc__
        """
        interpret_field() Return an interpretation of the current field as a string.
        
        If the field cannot be interpreted the field is returned unmodified.
        Returns None if the field value is unavailable.
        """
        pass

    def next_field(self): # real signature unknown; restored from __doc__
        """
        next_field() Advance the field cursor.
        
        next_field() moves the library’s internal cursor to point to the next
        field in the current record of the current event.
        
        Returns True on success, False if there is no more fields exist
        """
        pass

    def next_record(self): # real signature unknown; restored from __doc__
        """
        next_record() Advance record cursor.
        
        next_record() will move the internal library cursors to point to the
        next record of the current event.
        
        Returns True on success, False if no more records in current event
        Raises exception (EnvironmentError) on error.
        """
        pass

    def parse_next_event(self): # real signature unknown; restored from __doc__
        """
        parse_next_event() Advance the parser to the next event.
        
        parse_next_event() will position the cursors at the first field of the first
        record of the next event in a file or buffer. It does not skip events
        or honor any search criteria that may be stored.
        
        Returns True if parser advances to next event.
        Returns False if there are no more events to parse
        
        Raises exception (EnvironmentError) on error
        """
        pass

    def reset(self): # real signature unknown; restored from __doc__
        """
        reset() Reset audit parser instance
        
        reset resets all internal cursors to the beginning.
        It closes files and descriptors.
        
        Returns None.
        Raises exception (EnvironmentError) on error
        """
        pass

    def search_add_expression(self, expression, how): # real signature unknown; restored from __doc__
        """
        search_add_expression(expression, how) Build up search expression
        
        
        ausearch_add_item adds an expression to the current audit search
        expression.  The search conditions can then be used to scan logs,
        files, or buffers for something of interest.  The expression parameter
        contains an expression, as specified in ausearch-expression(5).
        
        The how parameter determines how this search expression will affect the
        existing search expression, if one is already defined.  The possible
        values are:
        
        AUSEARCH_RULE_CLEAR:
        Clear the current search expression, if any, and use only this search
        expression.
        
        AUSEARCH_RULE_OR:
        
        If a search expression E is already configured, replace it by
        (E || this_search_expression).
        
        AUSEARCH_RULE_AND:
        If a search expression E is already configured, replace it by
        (E && this_search_expression).
        
        No Return value, raises exception (EnvironmentError) on error.
        """
        pass

    def search_add_interpreted_item(self, field, op, value, how): # real signature unknown; restored from __doc__
        """
        search_add_interpreted_item(field, op, value, how) Build up search rule
        
        
        search_add_interpreted_item() adds one search condition to the current audit
        search expression. The search conditions can then be used to scan logs,
        files, or buffers for something of interest. The field value is the field
        name that the value will be checked for. The op variable describes what
        kind of check is to be done. Legal op values are:
        
        'exists':
        Just check that a field name exists
        
        '=':
        locate the field name and check that the value associated with it
        is equal to the value given in this rule.
        
        '!=':
        locate the field name and check that the value associated with
        it is NOT equal to the value given in this rule.
        
        The value parameter is compared to the interpreted field value (the value
        that would be returned by AuParser.interpret_field).
        
        The how parameter determines how this search expression will affect the
        existing search expression, if one is already defined.  The possible
        values are:
        
        AUSEARCH_RULE_CLEAR:
        Clear the current search expression, if any, and use only this search
        expression.
        
        AUSEARCH_RULE_OR:
        
        If a search expression E is already configured, replace it by
        (E || this_search_expression).
        
        AUSEARCH_RULE_AND:
        If a search expression E is already configured, replace it by
        (E && this_search_expression).
        
        No Return value, raises exception (EnvironmentError) on error.
        """
        pass

    def search_add_item(self, field, op, value, how): # real signature unknown; restored from __doc__
        """
        search_add_item(field, op, value, how) Build up search rule
        
        
        search_add_item() adds one search condition to the current audit search
        expression. The search conditions can then be used to scan logs, files, or
        buffers for something of interest. The field value is the field name
        that the value will be checked for. The op variable describes what
        kind of check is to be done. Legal op values are:
        
        'exists':
        Just check that a field name exists
        
        '=':
        locate the field name and check that the value associated with it
        is equal to the value given in this rule.
        
        '!=':
        locate the field name and check that the value associated with
        it is NOT equal to the value given in this rule.
        
        The value parameter is compared to the uninterpreted field value.
        
        The how parameter determines how this search expression will affect the
        existing search expression, if one is already defined.  The possible
        values are:
        
        AUSEARCH_RULE_CLEAR:
        Clear the current search expression, if any, and use only this search
        expression.
        
        AUSEARCH_RULE_OR:
        
        If a search expression E is already configured, replace it by
        (E || this_search_expression).
        
        AUSEARCH_RULE_AND:
        If a search expression E is already configured, replace it by
        (E && this_search_expression).
        
        No Return value, raises exception (EnvironmentError) on error.
        """
        pass

    def search_add_regex(self, regexp): # real signature unknown; restored from __doc__
        """
        search_add_regex(regexp) Add a regular expression to the search criteria.
        
        No Return value, raises exception (EnvironmentError) on error.
        """
        pass

    def search_add_timestamp_item(self, op, sec, milli, how): # real signature unknown; restored from __doc__
        """
        search_add_timestamp_item(op, sec, milli, how) Build up search rule
        
        
        search_add_timestamp_item adds an event time condition to the current audit
        search expression. The search conditions can then be used to scan logs,
        files, or buffers for something of interest. The op parameter specifies the
        desired comparison. Legal op values are "<", "<=", ">=", ">" and
        "=". The left operand of the comparison operator is the timestamp of the
        examined event, the right operand is specified by the sec and milli
        parameters.
        
        The how parameter determines how this search expression will affect the
        existing search expression, if one is already defined.  The possible
        values are:
        
        AUSEARCH_RULE_CLEAR:
        Clear the current search expression, if any, and use only this search
        expression.
        
        AUSEARCH_RULE_OR:
        
        If a search expression E is already configured, replace it by
        (E || this_search_expression).
        
        AUSEARCH_RULE_AND:
        If a search expression E is already configured, replace it by
        (E && this_search_expression).
        
        No Return value, raises exception (EnvironmentError) on error.
        """
        pass

    def search_clear(self): # real signature unknown; restored from __doc__
        """
        search_clear() Clear search parameters.
        
        ausearch_clear clears any search parameters stored in the parser
        instance and frees memory associated with it.
        
        No Return value.
        """
        pass

    def search_next_event(self): # real signature unknown; restored from __doc__
        """
        search_next_event() Find the next event that meets search criteria.
        
        search_next_event() will scan the input source and evaluate whether
        any record in an event contains the data being searched
        for. Evaluation is done at the record level.
        
        Returns True if a match was found
        Returns False if a match was not found.
        
        Raises exception (EnvironmentError) on error
        """
        pass

    def search_set_stop(self, where): # real signature unknown; restored from __doc__
        """
        search_set_stop(where) Set where cursor is positioned on search match.
        
        search_set_stop() determines where the internal cursor will stop when
        a search condition is met. The possible values are:
        
        AUSEARCH_STOP_EVENT:
        This one repositions the cursors to the first field of the first
        record of the event con- taining the items searched for.
        
        AUSEARCH_STOP_RECORD:
        This one repositions the cursors to the first field of the record
        containing the items searched for.
        
        AUSEARCH_STOP_FIELD:
        This one simply stops on the current field when the evaluation of the
        rules becomes true.
        
        No Return value, raises exception (ValueError) on error.
        """
        pass

    def __init__(self, source_type, source): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class NoParser(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



