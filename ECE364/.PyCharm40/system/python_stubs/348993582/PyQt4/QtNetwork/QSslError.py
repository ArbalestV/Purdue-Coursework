# encoding: utf-8
# module PyQt4.QtNetwork
# from /usr/lib64/python2.6/site-packages/PyQt4/QtNetwork.so
# by generator 1.136
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QSslError(): # skipped bases: <type 'sip.simplewrapper'>
    # no doc
    def certificate(self, *args, **kwargs): # real signature unknown
        pass

    def error(self, *args, **kwargs): # real signature unknown
        pass

    def errorString(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, y): # real signature unknown; restored from __doc__
        """ x.__le__(y) <==> x<=y """
        pass

    def __lt__(self, y): # real signature unknown; restored from __doc__
        """ x.__lt__(y) <==> x<y """
        pass

    def __ne__(self, y): # real signature unknown; restored from __doc__
        """ x.__ne__(y) <==> x!=y """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    AuthorityIssuerSerialNumberMismatch = 20
    CertificateExpired = 6
    CertificateNotYetValid = 5
    CertificateRejected = 18
    CertificateRevoked = 13
    CertificateSignatureFailed = 4
    CertificateUntrusted = 17
    HostNameMismatch = 22
    InvalidCaCertificate = 14
    InvalidNotAfterField = 8
    InvalidNotBeforeField = 7
    InvalidPurpose = 16
    NoError = 0
    NoPeerCertificate = 21
    NoSslSupport = 23
    PathLengthExceeded = 15
    SelfSignedCertificate = 9
    SelfSignedCertificateInChain = 10
    SubjectIssuerMismatch = 19
    UnableToDecodeIssuerPublicKey = 3
    UnableToDecryptCertificateSignature = 2
    UnableToGetIssuerCertificate = 1
    UnableToGetLocalIssuerCertificate = 11
    UnableToVerifyFirstCertificate = 12
    UnspecifiedError = -1


