# encoding: utf-8
# module nss.nss
# from /usr/lib64/python2.6/site-packages/nss/nss.so
# by generator 1.136
""" This module implements the NSS functions """
# no imports

from object import object

class PK11SymKey(object):
    """ Holds a hash, encryption or signing context for multi-part operations. """
    def derive(self, mechanism, sec_param, target, operation, key_size): # real signature unknown; restored from __doc__
        """
        derive(mechanism, sec_param, target, operation, key_size) -> PK11SymKey
        
        :Parameters:
            mechanism : int
                key mechanism enumeration constant (CKM_*)
            sec_param : SecItem object or None
                mechanism parameters or None.
            target : int
                key mechanism enumeration constant (CKM_*)
            operation : int
                type of operation. A (CKA_*) constant
                (e.g. CKA_ENCRYPT, CKA_DECRYPT, CKA_SIGN, CKA_VERIFY, CKA_DIGEST)
            key_size : int
                key size.
        
        Derive a new key from this key.
        Return a key which can do exactly one operation, it is
        ephemeral (session key).
        """
        return PK11SymKey

    def unwrap_sym_key(self, mechanism, sec_param, wrapped_key, target, operation, key_size): # real signature unknown; restored from __doc__
        """
        unwrap_sym_key(mechanism, sec_param, wrapped_key, target, operation, key_size) -> PK11SymKey
        
        :Parameters:
            mechanism : int
                key mechanism enumeration constant (CKM_*)
            sec_param : SecItem object or None
                mechanism parameters or None.
            wrapped_key : SecItem object
                the symmetric key to unwrap
            target : int
                key mechanism enumeration constant (CKM_*)
            operation : int
                type of operation. A (CKA_*) constant
                (e.g. CKA_ENCRYPT, CKA_DECRYPT, CKA_SIGN, CKA_VERIFY, CKA_DIGEST)
            key_size : int
                key size.
        
        Unwrap (decrypt) the supplied wrapped key.
        Return the unwrapped key as a PK11SymKey.
        """
        return PK11SymKey

    def wrap_sym_key(self, mechanism, sec_param, sym_key): # real signature unknown; restored from __doc__
        """
        wrap_sym_key(mechanism, sec_param, sym_key) -> SecItem
        
        :Parameters:
            mechanism : int
                key mechanism enumeration constant (CKM_*)
            sec_param : SecItem object or None
                mechanism parameters or None.
            sym_key : PK11SymKey object
                the symmetric key to wrap
        
        Wrap (encrypt) the supplied sym_key using the mechanism
        and parameter. Return the wrapped key as a SecItem.
        """
        return SecItem

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    key_data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """key data"""

    key_length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """key length"""

    mechanism = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """CK_MECHANISM_TYPE mechanism"""

    slot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """slot"""



