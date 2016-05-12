# encoding: utf-8
# module nss.nss
# from /usr/lib64/python2.6/site-packages/nss/nss.so
# by generator 1.136
""" This module implements the NSS functions """
# no imports

from object import object

class RDN(object):
    """
    An object representing an X501 Relative Distinguished Name (e.g. RDN).
    
    RDN objects contain an ordered list of `AVA` objects. 
    
    Examples::
    
        RDN()
        RDN(nss.AVA('cn', 'www.redhat.com'))
        RDN([ava0, ava1])
    
    The RDN object constructor may be invoked with zero or more
    `AVA` objects, or you may optionally pass a list or tuple of `AVA`
    objects.
    
    RDN objects contain an ordered list of `AVA` objects. The
    RDN object has both sequence and mapping behaviors with respect to
    the AVA's they contain. Thus you can index an AVA by position, by
    name, or by SecItem (if it's an OID). You can iterate over the list,
    get it's length or take a slice.
    
    If you index by string the string may be either a canonical name for
    the AVA type (e.g. 'cn') or the dotted-decimal notation for the OID
    (e.g. 2.5.4.3). There may be multiple AVA's in a RDN whose type matches
    (e.g. OU=engineering+OU=boston). It is not common to have more than
    one AVA in a RDN with the same type. However because of the possiblity
    of being multi-valued when indexing by type a list is always returned
    containing the matching AVA's. Thus::
    
        rdn = nss.RDN(nss.AVA('OU', 'engineering'))
        rdn['ou']
            returns [AVA('OU=engineering')
    
        rdn = nss.RDN(nss.AVA('OU', 'engineering'), nss.AVA('OU', 'boston'))
        rdn['ou']
            returns [AVA('OU=boston'), AVA('OU=engineering')]
    
    Examples::
    
        rdn = nss.RDN(nss.AVA('cn', 'www.redhat.com'))
        str(rdn)
           returns 'CN=www.redhat.com'
        rdn[0]
           returns an `AVA` object with the value C=US
        rdn['cn']
            returns a list comprised of an `AVA` object with the value CN=www.redhat.com
        rdn['2.5.4.3']
            returns a list comprised of an `AVA` object with the value CN=www.redhat.com
            because 2.5.4.3 is the dotted-decimal OID for common name (i.e. cn)
        rdn.has_key('cn')
            returns True because the RDN has a common name RDN
        rdn.has_key('2.5.4.3')
            returns True because the RDN has a common name AVA
            because 2.5.4.3 is the dotted-decimal OID for common name (i.e. cn)
        len(rdn)
           returns 1 because there is one `AVA` object in it
        list(rdn)
           returns a list of each `AVA` object in it
    """
    def has_key(self, arg): # real signature unknown; restored from __doc__
        """
        has_key(arg) -> bool
        
        :Parameters:
            arg : string or integer
                canonical name (e.g. 'cn') or oid dotted-decimal or
                SEC_OID_* enumeration constant
        
        return True if RDN has an AVA whose oid can be identified by arg.
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


