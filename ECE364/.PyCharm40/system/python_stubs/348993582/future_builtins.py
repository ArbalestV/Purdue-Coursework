# encoding: utf-8
# module future_builtins
# from /usr/lib64/python2.6/lib-dynload/future_builtins.so
# by generator 1.136
"""
This module provides functions that will be builtins in Python 3.0,
but that conflict with builtins that already exist in Python 2.x.

Functions:

hex(arg) -- Returns the hexadecimal representation of an integer
oct(arg) -- Returns the octal representation of an integer

The typical usage of this module is to replace existing builtins in a
module's namespace:
 
from future_builtins import hex, oct
"""

# imports
from itertools import filter, map, zip


# functions

def ascii(p_object): # real signature unknown; restored from __doc__
    """
    ascii(object) -> string
    
    Return the same as repr().  In Python 3.x, the repr() result will
    contain printable characters unescaped, while the ascii() result
    will have such characters backslash-escaped.
    """
    return ""

def hex(number): # real signature unknown; restored from __doc__
    """
    hex(number) -> string
    
    Return the hexadecimal representation of an integer or long integer.
    """
    return ""

def oct(number): # real signature unknown; restored from __doc__
    """
    oct(number) -> string
    
    Return the octal representation of an integer or long integer.
    """
    return ""

# no classes
