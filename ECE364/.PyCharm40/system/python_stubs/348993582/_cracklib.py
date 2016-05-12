# encoding: utf-8
# module _cracklib
# from /usr/lib64/python2.6/site-packages/_cracklibmodule.so
# by generator 1.136
"""
Python bindings for cracklib.

This module enables the use of cracklib features from within a Python
program or interpreter.
"""
# no imports

# functions

def FascistCheck(*args, **kwargs): # real signature unknown
    """
    arguments: passwd, dictpath (optional)
    
      passwd - password to be checked for weakness
      dictpath - full path name to the cracklib dictionary database
    
    if dictpath is not specified the default dictionary database
    will be used.
    
    return value: the same password passed as first argument.
    
    if password is weak, exception ValueError is raised with argument
    set to the reason of weakness.
    """
    pass

# no classes
