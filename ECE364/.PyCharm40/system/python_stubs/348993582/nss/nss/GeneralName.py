# encoding: utf-8
# module nss.nss
# from /usr/lib64/python2.6/site-packages/nss/nss.so
# by generator 1.136
""" This module implements the NSS functions """
# no imports

from object import object

class GeneralName(object):
    """ An object representing a GeneralName or list of GeneralNames. """
    def get_name(self, repr_kind=None): # real signature unknown; restored from __doc__
        """
        get_name(repr_kind=AsString) -> 
        
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
        
        Returns the value of the GeneralName according to the representation type parameter.
        """
        pass

    def __getitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    type_enum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the general name type enumerated constant"""

    type_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the general name type enumerated constant as a string"""

    type_string = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the type of the general name as a string (e.g. "URI")"""



