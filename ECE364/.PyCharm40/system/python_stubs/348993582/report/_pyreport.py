# encoding: utf-8
# module report._pyreport
# from /usr/lib64/python2.6/site-packages/report/_pyreport.so
# by generator 1.136
# no doc
# no imports

# Variables with simple values

CD_FLAG_BIN = 1
CD_FLAG_ISEDITABLE = 4
CD_FLAG_ISNOTEDITABLE = 8
CD_FLAG_TXT = 2

DD_FAIL_QUIETLY_EACCES = 2
DD_FAIL_QUIETLY_ENOENT = 1

DD_LOAD_TEXT_RETURN_NULL_ON_FAILURE = 16

DD_OPEN_READONLY = 8

LIBREPORT_ANALYZE = 4

LIBREPORT_DEL_DIR = 64

LIBREPORT_GETPID = 2
LIBREPORT_NOWAIT = 0

LIBREPORT_RELOAD_DATA = 32

LIBREPORT_RUN_CLI = 128
LIBREPORT_RUN_NEWT = 256

LIBREPORT_WAIT = 1

# functions

def dd_create(*args, **kwargs): # real signature unknown
    pass

def dd_opendir(*args, **kwargs): # real signature unknown
    pass

def delete_dump_dir(*args, **kwargs): # real signature unknown
    pass

def report_problem(*args, **kwargs): # real signature unknown
    pass

def report_problem_in_dir(*args, **kwargs): # real signature unknown
    pass

def report_problem_in_memory(*args, **kwargs): # real signature unknown
    pass

# classes

class dump_dir(object):
    # no doc
    def close(self, *args, **kwargs): # real signature unknown
        pass

    def delete(self, *args, **kwargs): # real signature unknown
        pass

    def delete_item(self, *args, **kwargs): # real signature unknown
        pass

    def exist(self, *args, **kwargs): # real signature unknown
        pass

    def load_text(self, *args, **kwargs): # real signature unknown
        pass

    def save_binary(self, *args, **kwargs): # real signature unknown
        pass

    def save_text(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __nonzero__(self): # real signature unknown; restored from __doc__
        """ x.__nonzero__() <==> x != 0 """
        pass

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class error(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class problem_data(object):
    # no doc
    def add(self, *args, **kwargs): # real signature unknown
        pass

    def add_basics(self, *args, **kwargs): # real signature unknown
        pass

    def create_dump_dir(self, *args, **kwargs): # real signature unknown
        pass

    def get(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class run_event_state(object):
    # no doc
    def run_event_on_dir_name(self, *args, **kwargs): # real signature unknown
        pass

    def run_event_on_problem_data(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    logging_callback = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    post_run_callback = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



