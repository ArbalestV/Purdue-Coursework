# encoding: utf-8
# module nss.nss
# from /usr/lib64/python2.6/site-packages/nss/nss.so
# by generator 1.136
""" This module implements the NSS functions """
# no imports

from object import object

class RSAGenParams(object):
    """
    RSAGenParams(key_size=1024, public_exponent=0x10001)
    
    :Parameters:
        key_size : integer
            RSA key size in bits.
        public_exponent : integer
            public exponent.
    
    An object representing RSAGenParams.
    """
    def __init__(self, key_size=1024, public_exponent=0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    key_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """key size in bits (integer)"""

    public_exponent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """public exponent (integer)"""



