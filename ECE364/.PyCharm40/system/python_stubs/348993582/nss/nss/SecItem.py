# encoding: utf-8
# module nss.nss
# from /usr/lib64/python2.6/site-packages/nss/nss.so
# by generator 1.136
""" This module implements the NSS functions """
# no imports

from object import object

class SecItem(object):
    """
    SecItem(data=None, type=siBuffer)
    
    :Parameters:
        data : any read buffer compatible object (e.g. buffer or string)
            raw data to initialize from
        type : int
            SECItemType constant (e.g. si*)
    
    Encoded data. Used internally by NSS
    """
    def der_to_hex(self, octets_per_line=0, separator=None): # real signature unknown; restored from __doc__
        """
        der_to_hex(octets_per_line=0, separator=':') -> string or list of strings
        
        :Parameters:
            octets_per_line : integer
                Number of octets formatted on one line, if 0 then
                return a single string instead of an array of lines
            separator : string
                String used to seperate each octet
                If None it will be as if the empty string had been
                passed and no separator will be used.
        
        Interpret the SecItem as containing DER encoded data consisting
        of a <type,length,value> triplet (e.g. TLV). This function skips
        the type and length components and returns the value component as
        a hexadecimal string or a list of hexidecimal strings with a
        maximum of octets_per_line in each list element. See data_to_hex()
        for a more detailed explanation.
        """
        return ""

    def get_oid_sequence(self, sec_item, repr_kind=None): # real signature unknown; restored from __doc__
        """
        get_oid_sequence(sec_item, repr_kind=AsString) -> (obj, ...)
        
        :Parameters:
            sec_item : SecItem object
                A SecItem containing a DER encoded sequence of OID's
            repr_kind : RepresentationKind constant
                Specifies what the contents of the returned tuple will be.
                May be one of:
        
                AsObject
                    Each extended key usage will be a SecItem object embedding
                    the OID in DER format.
                AsString
                    Each extended key usage will be a descriptive string.
                    (e.g. "TLS Web Server Authentication Certificate")
                AsDottedDecimal
                    Each extended key usage will be OID rendered as a dotted decimal string.
                    (e.g. "OID.1.3.6.1.5.5.7.3.1")
                AsEnum
                    Each extended key usage will be OID tag enumeration constant (int).
                    (e.g. nss.SEC_OID_EXT_KEY_USAGE_SERVER_AUTH)
        
        Return a tuple of OID's according the representation kind.
        """
        pass

    def to_hex(self, octets_per_line=0, separator=None): # real signature unknown; restored from __doc__
        """
        to_hex(octets_per_line=0, separator=':') -> string or list of strings
        
        :Parameters:
            octets_per_line : integer
                Number of octets formatted on one line, if 0 then
                return a single string instead of an array of lines
            separator : string
                String used to seperate each octet
                If None it will be as if the empty string had been
                passed and no separator will be used.
        
        Equivalent to calling data_to_hex(sec_item)
        """
        return ""

    def __cmp__(self, y): # real signature unknown; restored from __doc__
        """ x.__cmp__(y) <==> cmp(x,y) """
        pass

    def __getitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __getslice__(self, i, j): # real signature unknown; restored from __doc__
        """
        x.__getslice__(i, j) <==> x[i:j]
                   
                   Use of negative indices is not supported.
        """
        pass

    def __init__(self, data=None, type=None): # real signature unknown; restored from __doc__
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
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

    data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """contents of SecItem buffer"""

    len = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """number of octets in SecItem buffer"""

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the SecItem type (si* constant)"""



