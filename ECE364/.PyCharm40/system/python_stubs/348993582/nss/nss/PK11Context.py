# encoding: utf-8
# module nss.nss
# from /usr/lib64/python2.6/site-packages/nss/nss.so
# by generator 1.136
""" This module implements the NSS functions """
# no imports

from object import object

class PK11Context(object):
    """  """
    def cipher_op(self, data): # real signature unknown; restored from __doc__
        """
        cipher_op(data) -> data
        :Parameters:
            data : any read buffer compatible object (e.g. buffer or string)
                raw data to compute digest from
        
        Execute a digest/signature operation.
        """
        pass

    def clone_context(self, context): # real signature unknown; restored from __doc__
        """
        clone_context(context) -> PK11Context
        
        :Parameters:
            context : PK11Context object
                The PK11Context to be cloned
        
        Create a new PK11Context which is clone of the supplied context.
        """
        return PK11Context

    def digest_begin(self): # real signature unknown; restored from __doc__
        """
        digest_begin()
        
        Start a new digesting or Mac'ing operation on this context.
        """
        pass

    def digest_final(self): # real signature unknown; restored from __doc__
        """
        digest_final() -> data
        
        Completes the multi-part cryptographic operation in progress
        on this context and returns any final data which may have been
        pending in the context (i.e. the output data is flushed from the
        context). If there was no final data the returned
        data buffer will have a length of zero.
        """
        pass

    def digest_key(self, sym_key): # real signature unknown; restored from __doc__
        """
        digest_key(sym_key)
        
        :Parameters:
            sym_key : PK11SymKey object
                symmetric key
        
        Continues a multiple-part message-digesting operation by digesting the
        value of a secret key.
        """
        pass

    def digest_op(self, data): # real signature unknown; restored from __doc__
        """
        digest_op(data)
        :Parameters:
            data : any read buffer compatible object (e.g. buffer or string)
                raw data to compute digest from
        
        Execute a digest/signature operation.
        """
        pass

    def finalize(self): # real signature unknown; restored from __doc__
        """
        finalize()
        
        Clean up cipher operation so that any pending multi-part
        operations have been flushed. Any pending output which would
        have been available as a result of the flush is discarded.
        The context is left in a state available for reuse.
        
        WARNING: Currently context reuse only works for digest contexts
        not encryption/decryption contexts
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


