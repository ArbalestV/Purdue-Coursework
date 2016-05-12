# encoding: utf-8
# module nss.nss
# from /usr/lib64/python2.6/site-packages/nss/nss.so
# by generator 1.136
""" This module implements the NSS functions """
# no imports

from object import object

class CRLDistributionPoint(object):
    """ An object representing a CRL Distribution Point """
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

    def get_general_names(self, repr_kind=None): # real signature unknown; restored from __doc__
        """
        get_general_names(repr_kind=AsString) -> (general_name, ...)
        
        :Parameters:
            repr_kind : RepresentationKind constant
                Specifies what the contents of the returned tuple will be.
                May be one of:
        
                AsObject
                    The general name as a nss.GeneralName object
                AsString
                    The general name as a string.
                    (e.g. "http://crl.geotrust.com/crls/secureca.crl")
                AsTypeString
                    The general name type as a string.
                     (e.g. "URI")
                AsTypeEnum
                    The general name type as a general name type enumerated constant.
                     (e.g. nss.certURI )
                AsLabeledString
                    The general name as a string with it's type prepended.
                    (e.g. "URI: http://crl.geotrust.com/crls/secureca.crl"
        
        Returns a tuple of general names in the CRL Distribution Point. If the
        distribution point type is not nss.generalName or the list was empty then
        the returned tuple will be empty.
        
        You may specify how the each member of the tuple is represented, by default
        it will be as a string.
        """
        pass

    def get_reasons(self, repr_kind=None): # real signature unknown; restored from __doc__
        """
        get_reasons(repr_kind=AsEnumDescription) -> (reason, ...)
        
        :Parameters:
            repr_kind : RepresentationKind constant
                Specifies what the contents of the returned tuple will be.
                May be one of:
        
                AsEnum
                    The enumerated constant.
                    (e.g. nss.crlEntryReasonCaCompromise)
                AsEnumDescription
                    A friendly human readable description of the enumerated constant as a string.
                     (e.g. "CA Compromise")
                AsIndex
                    The bit position within the bit string.
        
        Returns a tuple of reasons in the CRL Distribution Point. If no
        reasons were defined the returned tuple will be empty.
        
        You may specify how the each member of the tuple is represented, by default
        it will be as a string.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
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

    issuer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """returns the CRL Issuer as a GeneralName object if defined, returns None if not defined"""



