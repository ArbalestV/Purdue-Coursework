# encoding: utf-8
# module nss.nss
# from /usr/lib64/python2.6/site-packages/nss/nss.so
# by generator 1.136
""" This module implements the NSS functions """
# no imports

from object import object

class AVA(object):
    """
    An object representing an AVA (attribute value assertion).
    
    AVA(type, value)
    
    :Parameters:
         type : may be one of integer, string, SecItem
             What kind of attribute is being created. May be
             one of:
    
             * integer: A SEC OID enumeration constant (i.e. SEC_OID_*)
               for example SEC_OID_AVA_COMMON_NAME.
             * string: A string either as the ava name, for example 'cn'
               or as the dotted decimal representation, for example
               'OID.2.5.4.3'. Case is not significant for either form.
             * SecItem: A SecItem object encapsulating the OID in 
               DER format.
         value : string
             The value of the AVA, must be a string.
    
    RDN's (Relative Distinguished Name) are composed from AVA's.
    An `RDN` is a sequence of AVA's.
    
    An example of an AVA is "CN=www.redhat.com" where CN is the X500
    directory abbrevation for "Common Name".
    
    An AVA is composed of two items:
    
    type
        Specifies the attribute (e.g. CN). AVA types are specified by
        predefined OID's (Object Identifiers). For example the OID of CN
        is 2.5.4.3 ({joint-iso-itu-t(2) ds(5) attributeType(4) commonName(3)})
        OID's in NSS are encapsulated in a SecItem as a DER encoded OID.
        Because DER encoded OID's are less than ideal mechanisms by which
        to specify an item NSS has mapped each OID to a integral enumerated
        constant called an OID tag (i.e. SEC_OID_*). Many of the NSS API's
        will accept an OID tag number instead of DER encoded OID in a SecItem.
        One can easily convert between DER encoded OID's, tags, and their
        string representation in dotted-decimal format. The enumerated OID
        constants are the most efficient in most cases.
    value
        The value of the attribute (e.g. 'www.redhat.com').
    
    Examples::
    
        The AVA cn=www.redhat.com can be created in any of the follow ways:
    
        ava = nss.AVA('cn', 'www.redhat.com')
        ava = nss.AVA(nss.SEC_OID_AVA_COMMON_NAME, 'www.redhat.com')
        ava = nss.AVA('2.5.4.3', 'www.redhat.com')
        ava = nss.AVA('OID.2.5.4.3', 'www.redhat.com')
    """
    def __cmp__(self, y): # real signature unknown; restored from __doc__
        """ x.__cmp__(y) <==> cmp(x,y) """
        pass

    def __init__(self, attribute_value_assertion): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    oid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The OID (e.g. type) of the AVA as a SecItem"""

    oid_tag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The OID tag enumerated constant (i.e. SEC_OID_AVA_*) of the AVA's type"""

    value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The value of the AVA as a SecItem"""

    value_str = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The value of the AVA as a UTF-8 encoded string"""



