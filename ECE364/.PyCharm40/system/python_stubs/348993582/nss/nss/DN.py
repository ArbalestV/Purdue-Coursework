# encoding: utf-8
# module nss.nss
# from /usr/lib64/python2.6/site-packages/nss/nss.so
# by generator 1.136
""" This module implements the NSS functions """
# no imports

from object import object

class DN(object):
    """
    An object representing an X501 Distinguished Name (e.g DN).
    
    DN objects contain an ordered list of `RDN` objects.
    
    The DN object constructor may be invoked with a string
    representing an X500 name. Zero or more `RDN` objects, or you may
    optionally pass a list or tuple of `RDN` objects.
    
    Examples::
    
        DN()
        DN('CN=www.redhat.com,OU=Web Operations,O=Red Hat Inc,L=Raleigh,ST=North Carolina,C=US')
        DN(rdn0, ...)
        DN([rdn0, rdn1])
    
    **The string representation of a Distinguished Name (DN) has reverse
    ordering from it's sequential components.**
    
    The ordering is a requirement of the relevant RFC's. When a
    Distinguished Name is rendered as a string it is ordered from most
    specific to least specific. However it's components (RDN's) as a
    sequence are ordered from least specific to most specific.
    
    DN objects contain an ordered list of `RDN` objects. The
    DN object has both sequence and mapping behaviors with respect to
    the RDN's they contain. Thus you can index an RDN by position, by
    name, or by SecItem (if it's an OID). You can iterate over the list,
    get it's length or take a slice.
    
    If you index by string the string may be either a canonical name for
    the RDN type (e.g. 'cn') or the dotted-decimal notation for the OID
    (e.g. 2.5.4.3). There may be multiple RDN's in a DN whose type matches
    (e.g. OU=engineering, OU=boston). It is not common to have more than
    one RDN in a DN with the same type. However because of the possiblity
    of being multi-valued when indexing by type a list is always returned
    containing the matching RDN's. Thus::
    
        dn = nss.DN('OU=engineering')
        dn['ou']
            returns [RDN('OU=engineering')
    
        dn = nss.DN('OU=engineering, OU=boston')
        dn['ou']
            returns [RDN('OU=boston'), RDN('OU=engineering')]
            Note the reverse ordering between string representation and RDN sequencing
    
    Note, if you use properties to access the RDN values (e.g. name.common_name,
    name.org_unit_name) the string value is returned or None if not found.
    If the item was multi-valued then the most appropriate item will be selected
    and returned as a string value.
    
    Note it is not possible to index by oid tag
    (e.g. nss.SEC_OID_AVA_COMMON_NAME) because oid tags are integers and
    it's impossible to distinguish between an integer representing the
    n'th member of the sequence and the integer representing the oid
    tag. In this case positional indexing wins (e.g. rdn[0] means the
    first element).
    
    Examples::
    
        subject_name = 'CN=www.redhat.com,OU=Web Operations,O=Red Hat Inc,L=Raleigh,ST=North Carolina,C=US'
        name = nss.DN(subject_name)
        str(name)
           returns 'CN=www.redhat.com,OU=Web Operations,O=Red Hat Inc,L=Raleigh,ST=North Carolina,C=US'
        name[0]
           returns an `RDN` object with the value C=US
        name['cn']
            returns a list comprised of an `RDN` object with the value CN=www.redhat.com
        name['2.5.4.3']
            returns a list comprised of an `RDN` object with the value CN=www.redhat.com
            because 2.5.4.3 is the dotted-decimal OID for common name (i.e. cn)
        name.common_name
            returns the string www.redhat.com
            common_name is easy shorthand property, it only retuns a single string
            value or None, if it was multi-valued the most appropriate item is selected.
        name.has_key('cn')
            returns True because the DN has a common name RDN
        name.has_key('2.5.4.3')
            returns True because the DN has a common name RDN
            because 2.5.4.3 is the dotted-decimal OID for common name (i.e. cn)
    
        cn_rdn = nss.RDN(nss.AVA('cn', 'www.redhat.com'))
        ou_rdn = nss.RDN(nss.AVA('ou', 'Web Operations'))
        name = nss.DN(cn_rdn)
        name
           is a DN with one RDN (e.g. CN=www.redhat.com)
        len(name)
           returns 1 because there is one RDN in it
        name.add_rdn(ou_rdn)
        name
           name is now a DN with two RDN's (e.g. OU=Web Operations,CN=www.redhat.com)
        len(name)
           returns 2 because there are now two RDN's in it
        list(name)
           returns a list with the two RDN's in it
        name[:]
           same as list(name)
        for rdn in name:
           iterate over each RDN in name
        name = nss.DN(cn_rdn, ou_rdn)
            This is an alternate way to build the above DN
    """
    def add_rdn(self, rdn): # real signature unknown; restored from __doc__
        """
        add_rdn(rdn) 
        
        :Parameters:
            rdn : RDN object
                The rnd to add to the name
        
        Adds a RDN to the name.
        """
        pass

    def has_key(self, arg): # real signature unknown; restored from __doc__
        """
        has_key(arg) -> bool
        
        :Parameters:
            arg : string or integer
                canonical name (e.g. 'cn') or oid dotted-decimal or
                SEC_OID_* enumeration constant
        
        return True if Name has an AVA whose oid can be identified by arg.
        """
        return False

    def __cmp__(self, y): # real signature unknown; restored from __doc__
        """ x.__cmp__(y) <==> cmp(x,y) """
        pass

    def __getitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
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

    cert_uid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the certificate uid member (i.e. UID) as a string. Returns None if not found."""

    common_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the common name member (i.e. CN) as a string. Returns None if not found."""

    country_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the country name member (i.e. C) as a string. Returns None if not found."""

    dc_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the domain component name member (i.e. DC) as a string. Returns None if not found."""

    email_address = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the email address member as a string. Returns None if not found."""

    locality_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the locality name member (i.e. L) as a string. Returns None if not found."""

    org_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the organization name member (i.e. O) as a string. Returns None if not found."""

    org_unit_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the organizational unit name member (i.e. OU) as a string. Returns None if not found."""

    state_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the state name member (i.e. ST) as a string. Returns None if not found."""



