# encoding: utf-8
# module rhsm._certificate
# from /usr/lib64/python2.6/site-packages/rhsm/_certificate.so
# by generator 1.136
# no doc
# no imports

# functions

def load(*args, **kwargs): # real signature unknown
    """ load a certificate from a file """
    pass

# classes

class X509(object):
    """ X509 Certificate """
    def as_pem(self, *args, **kwargs): # real signature unknown
        """ return the pem representation of this certificate """
        pass

    def get_all_extensions(self, *args, **kwargs): # real signature unknown
        """ get a dict of oid: value """
        pass

    def get_extension(self, *args, **kwargs): # real signature unknown
        """ get the string representation of an extension by oid """
        pass

    def get_issuer(self, *args, **kwargs): # real signature unknown
        """ get the certificate's issuer """
        pass

    def get_not_after(self, *args, **kwargs): # real signature unknown
        """ get the certificate's end time """
        pass

    def get_not_before(self, *args, **kwargs): # real signature unknown
        """ get the certificate's start time """
        pass

    def get_serial_number(self, *args, **kwargs): # real signature unknown
        """ get the certificate's serial number """
        pass

    def get_subject(self, *args, **kwargs): # real signature unknown
        """ get the certificate's subject """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


