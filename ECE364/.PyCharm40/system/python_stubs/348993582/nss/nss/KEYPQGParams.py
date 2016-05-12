# encoding: utf-8
# module nss.nss
# from /usr/lib64/python2.6/site-packages/nss/nss.so
# by generator 1.136
""" This module implements the NSS functions """
# no imports

from object import object

class KEYPQGParams(object):
    """
    KEYPQGParams(prime=None, subprime=None, base=None)
    
    :Parameters:
        prime : SecItem or str or any buffer compatible object or None
            prime (also known as p)
        subprime : SecItem or str or any buffer compatible object or None
            subprime (also known as q)
        base : SecItem or str or any buffer compatible object or None
            base (also known as g)
    
    An object representing DSA key parameters
        - prime (also known as p)
        - subprime (also known as q)
        - base (also known as g)
    
    If no parameters are passed the default PQG the KeyPQGParams will
    be intialized to default values. If you pass any initialization
    parameters then they must all be passed.
    """
    def format(self, level=0, indent='    '): # real signature unknown; restored from __doc__
        """
        format(level=0, indent='    ') -> string)
        
        :Parameters:
            level : integer
                Initial indentation level, all subsequent indents are relative
                to this starting level.
            indent : string
                string replicated once for each indent level then prepended to output line
        
        This is equivalent to:
        indented_format(obj.format_lines()) on an object providing a format_lines() method.
        """
        return ""

    def format_lines(self, level=0): # real signature unknown; restored from __doc__
        """
        format_lines(level=0) -> [(level, string),...]
        
        :Parameters:
            level : integer
                Initial indentation level, all subsequent indents are relative
                to this starting level.
        
        Formats the object into a sequence of lines with indent level
        information.  The return value is a list where each list item is a
        tuple.  The first item in the tuple is an integer
        representing the indentation level for that line. Any remaining items
        in the tuple are strings to be output on that line.
        
        The output of this function can be formatted into a single string by
        calling `indented_format()`, e.g.:
        
            print indented_format(obj.format_lines())
        
        The reason this function returns a tuple as opposed to an single
        indented string is to support other text formatting systems such as
        GUI's with indentation controls.  See `indented_format()` for a
        complete explanation.
        """
        pass

    def __init__(self, prime=None, subprime=None, base=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    base = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """key base value, also known as g"""

    prime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """key prime value, also known as p"""

    subprime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """key subprime value, also known as q"""



