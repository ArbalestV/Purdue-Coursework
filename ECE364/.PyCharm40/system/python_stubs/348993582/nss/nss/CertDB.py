# encoding: utf-8
# module nss.nss
# from /usr/lib64/python2.6/site-packages/nss/nss.so
# by generator 1.136
""" This module implements the NSS functions """
# no imports

from object import object

class CertDB(object):
    """ An object representing a Certificate Database """
    def find_crl_by_cert(self, cert, type=None): # real signature unknown; restored from __doc__
        """
        find_crl_by_cert(cert, type=SEC_CRL_TYPE) -> SignedCRL object
        
        :Parameters:
            cert : Certificate object
                certificate used to lookup the CRL.
            type : int
                revocation list type
                
                may be one of:
                  - SEC_CRL_TYPE
                  - SEC_KRL_TYPE
        
        Returns a SignedCRL object found in the database given a certificate and revocation list type.
        """
        return SignedCRL

    def find_crl_by_name(self, name, type=None): # real signature unknown; restored from __doc__
        """
        find_crl_by_name(name, type=SEC_CRL_TYPE) -> SignedCRL object
        
        :Parameters:
            name : string
                name to lookup
            type : int
                revocation list type
                
                may be one of:
                  - SEC_CRL_TYPE
                  - SEC_KRL_TYPE
        
        Returns a SignedCRL object found in the database given a name and revocation list type.
        """
        return SignedCRL

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


