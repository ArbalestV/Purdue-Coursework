# encoding: utf-8
# module gmenu
# from /usr/lib64/python2.6/site-packages/gmenu.so
# by generator 1.136
# no doc
# no imports

# Variables with simple values

FLAGS_INCLUDE_EXCLUDED = 1
FLAGS_INCLUDE_NODISPLAY = 4

FLAGS_NONE = 0

FLAGS_SHOW_ALL_SEPARATORS = 8

FLAGS_SHOW_EMPTY = 2

SORT_DISPLAY_NAME = 1

SORT_NAME = 0

TYPE_ALIAS = 5
TYPE_DIRECTORY = 1
TYPE_ENTRY = 2
TYPE_HEADER = 4
TYPE_INVALID = 0
TYPE_SEPARATOR = 3

# functions

def lookup_tree(*args, **kwargs): # real signature unknown
    pass

# classes

class Item(object):
    # no doc
    def get_parent(self, *args, **kwargs): # real signature unknown
        pass

    def get_type(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class Alias(Item):
    # no doc
    def get_directory(self, *args, **kwargs): # real signature unknown
        pass

    def get_item(self, *args, **kwargs): # real signature unknown
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class Directory(Item):
    # no doc
    def get_comment(self, *args, **kwargs): # real signature unknown
        pass

    def get_contents(self, *args, **kwargs): # real signature unknown
        pass

    def get_desktop_file_path(self, *args, **kwargs): # real signature unknown
        pass

    def get_icon(self, *args, **kwargs): # real signature unknown
        pass

    def get_menu_id(self, *args, **kwargs): # real signature unknown
        pass

    def get_name(self, *args, **kwargs): # real signature unknown
        pass

    def get_tree(self, *args, **kwargs): # real signature unknown
        pass

    def make_path(self, *args, **kwargs): # real signature unknown
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class Entry(Item):
    # no doc
    def get_comment(self, *args, **kwargs): # real signature unknown
        pass

    def get_desktop_file_id(self, *args, **kwargs): # real signature unknown
        pass

    def get_desktop_file_path(self, *args, **kwargs): # real signature unknown
        pass

    def get_display_name(self, *args, **kwargs): # real signature unknown
        pass

    def get_exec(self, *args, **kwargs): # real signature unknown
        pass

    def get_generic_name(self, *args, **kwargs): # real signature unknown
        pass

    def get_icon(self, *args, **kwargs): # real signature unknown
        pass

    def get_is_excluded(self, *args, **kwargs): # real signature unknown
        pass

    def get_is_nodisplay(self, *args, **kwargs): # real signature unknown
        pass

    def get_launch_in_terminal(self, *args, **kwargs): # real signature unknown
        pass

    def get_name(self, *args, **kwargs): # real signature unknown
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class Header(Item):
    # no doc
    def get_directory(self, *args, **kwargs): # real signature unknown
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class Separator(Item):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class Tree(object):
    # no doc
    def add_monitor(self, *args, **kwargs): # real signature unknown
        pass

    def get_directory_from_path(self, *args, **kwargs): # real signature unknown
        pass

    def get_menu_file(self, *args, **kwargs): # real signature unknown
        pass

    def get_root_directory(self, *args, **kwargs): # real signature unknown
        pass

    def get_sort_key(self, *args, **kwargs): # real signature unknown
        pass

    def remove_monitor(self, *args, **kwargs): # real signature unknown
        pass

    def set_sort_key(self, *args, **kwargs): # real signature unknown
        pass

    def __delattr__(self, name): # real signature unknown; restored from __doc__
        """ x.__delattr__('name') <==> del x.name """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __setattr__(self, name, value): # real signature unknown; restored from __doc__
        """ x.__setattr__('name', value) <==> x.name = value """
        pass


