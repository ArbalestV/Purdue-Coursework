# encoding: utf-8
# module PySide.QtNetwork
# from /opt/python3/current/lib/python3.4/site-packages/PySide/QtNetwork.so
# by generator 1.136
# no doc

# imports
import PySide.QtCore as __PySide_QtCore
import Shiboken as __Shiboken


from .QTcpSocket import QTcpSocket

class QSslSocket(QTcpSocket):
    # no doc
    def abort(self, *args, **kwargs): # real signature unknown
        pass

    def addCaCertificate(self, *args, **kwargs): # real signature unknown
        pass

    def addCaCertificates(self, *args, **kwargs): # real signature unknown
        pass

    def addDefaultCaCertificate(self, *args, **kwargs): # real signature unknown
        pass

    def addDefaultCaCertificates(self, *args, **kwargs): # real signature unknown
        pass

    def atEnd(self, *args, **kwargs): # real signature unknown
        pass

    def bytesAvailable(self, *args, **kwargs): # real signature unknown
        pass

    def bytesToWrite(self, *args, **kwargs): # real signature unknown
        pass

    def caCertificates(self, *args, **kwargs): # real signature unknown
        pass

    def canReadLine(self, *args, **kwargs): # real signature unknown
        pass

    def ciphers(self, *args, **kwargs): # real signature unknown
        pass

    def close(self, *args, **kwargs): # real signature unknown
        pass

    def connectToHostEncrypted(self, *args, **kwargs): # real signature unknown
        pass

    def connectToHostImplementation(self, *args, **kwargs): # real signature unknown
        pass

    def defaultCaCertificates(self, *args, **kwargs): # real signature unknown
        pass

    def defaultCiphers(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectFromHostImplementation(self, *args, **kwargs): # real signature unknown
        pass

    def encrypted(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def encryptedBytesAvailable(self, *args, **kwargs): # real signature unknown
        pass

    def encryptedBytesToWrite(self, *args, **kwargs): # real signature unknown
        pass

    def encryptedBytesWritten(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def flush(self, *args, **kwargs): # real signature unknown
        pass

    def ignoreSslErrors(self, *args, **kwargs): # real signature unknown
        pass

    def isEncrypted(self, *args, **kwargs): # real signature unknown
        pass

    def localCertificate(self, *args, **kwargs): # real signature unknown
        pass

    def mode(self, *args, **kwargs): # real signature unknown
        pass

    def modeChanged(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def peerCertificate(self, *args, **kwargs): # real signature unknown
        pass

    def peerCertificateChain(self, *args, **kwargs): # real signature unknown
        pass

    def peerVerifyDepth(self, *args, **kwargs): # real signature unknown
        pass

    def peerVerifyError(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def peerVerifyMode(self, *args, **kwargs): # real signature unknown
        pass

    def privateKey(self, *args, **kwargs): # real signature unknown
        pass

    def protocol(self, *args, **kwargs): # real signature unknown
        pass

    def readData(self, *args, **kwargs): # real signature unknown
        pass

    def sessionCipher(self, *args, **kwargs): # real signature unknown
        pass

    def setCaCertificates(self, *args, **kwargs): # real signature unknown
        pass

    def setCiphers(self, *args, **kwargs): # real signature unknown
        pass

    def setDefaultCaCertificates(self, *args, **kwargs): # real signature unknown
        pass

    def setDefaultCiphers(self, *args, **kwargs): # real signature unknown
        pass

    def setLocalCertificate(self, *args, **kwargs): # real signature unknown
        pass

    def setPeerVerifyDepth(self, *args, **kwargs): # real signature unknown
        pass

    def setPeerVerifyMode(self, *args, **kwargs): # real signature unknown
        pass

    def setPrivateKey(self, *args, **kwargs): # real signature unknown
        pass

    def setProtocol(self, *args, **kwargs): # real signature unknown
        pass

    def setReadBufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def setSocketDescriptor(self, *args, **kwargs): # real signature unknown
        pass

    def setSocketOption(self, *args, **kwargs): # real signature unknown
        pass

    def setSslConfiguration(self, *args, **kwargs): # real signature unknown
        pass

    def socketOption(self, *args, **kwargs): # real signature unknown
        pass

    def sslConfiguration(self, *args, **kwargs): # real signature unknown
        pass

    def sslErrors(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def startClientEncryption(self, *args, **kwargs): # real signature unknown
        pass

    def startServerEncryption(self, *args, **kwargs): # real signature unknown
        pass

    def supportedCiphers(self, *args, **kwargs): # real signature unknown
        pass

    def supportsSsl(self, *args, **kwargs): # real signature unknown
        pass

    def systemCaCertificates(self, *args, **kwargs): # real signature unknown
        pass

    def waitForBytesWritten(self, *args, **kwargs): # real signature unknown
        pass

    def waitForConnected(self, *args, **kwargs): # real signature unknown
        pass

    def waitForDisconnected(self, *args, **kwargs): # real signature unknown
        pass

    def waitForEncrypted(self, *args, **kwargs): # real signature unknown
        pass

    def waitForReadyRead(self, *args, **kwargs): # real signature unknown
        pass

    def writeData(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    AutoVerifyPeer = None # (!) real value is ''
    PeerVerifyMode = None # (!) real value is ''
    QueryPeer = None # (!) real value is ''
    SslClientMode = None # (!) real value is ''
    SslMode = None # (!) real value is ''
    SslServerMode = None # (!) real value is ''
    staticMetaObject = None # (!) real value is ''
    UnencryptedMode = None # (!) real value is ''
    VerifyNone = None # (!) real value is ''
    VerifyPeer = None # (!) real value is ''


