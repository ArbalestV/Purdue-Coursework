# encoding: utf-8
# module PySide.QtNetwork
# from /opt/python3/current/lib/python3.4/site-packages/PySide/QtNetwork.so
# by generator 1.136
# no doc

# imports
import PySide.QtCore as __PySide_QtCore
import Shiboken as __Shiboken


class QLocalSocket(__PySide_QtCore.QIODevice):
    # no doc
    def abort(self, *args, **kwargs): # real signature unknown
        pass

    def bytesAvailable(self, *args, **kwargs): # real signature unknown
        pass

    def bytesToWrite(self, *args, **kwargs): # real signature unknown
        pass

    def canReadLine(self, *args, **kwargs): # real signature unknown
        pass

    def close(self, *args, **kwargs): # real signature unknown
        pass

    def connected(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def connectToServer(self, *args, **kwargs): # real signature unknown
        pass

    def disconnected(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def disconnectFromServer(self, *args, **kwargs): # real signature unknown
        pass

    def error(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def flush(self, *args, **kwargs): # real signature unknown
        pass

    def fullServerName(self, *args, **kwargs): # real signature unknown
        pass

    def isSequential(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        pass

    def readBufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def readData(self, *args, **kwargs): # real signature unknown
        pass

    def serverName(self, *args, **kwargs): # real signature unknown
        pass

    def setReadBufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def state(self, *args, **kwargs): # real signature unknown
        pass

    def stateChanged(self, *args, **kwargs): # real signature unknown
        """ Signal """
        pass

    def waitForBytesWritten(self, *args, **kwargs): # real signature unknown
        pass

    def waitForConnected(self, *args, **kwargs): # real signature unknown
        pass

    def waitForDisconnected(self, *args, **kwargs): # real signature unknown
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

    ClosingState = None # (!) real value is ''
    ConnectedState = None # (!) real value is ''
    ConnectingState = None # (!) real value is ''
    ConnectionError = None # (!) real value is ''
    ConnectionRefusedError = None # (!) real value is ''
    DatagramTooLargeError = None # (!) real value is ''
    LocalSocketError = None # (!) real value is ''
    LocalSocketState = None # (!) real value is ''
    PeerClosedError = None # (!) real value is ''
    ServerNotFoundError = None # (!) real value is ''
    SocketAccessError = None # (!) real value is ''
    SocketResourceError = None # (!) real value is ''
    SocketTimeoutError = None # (!) real value is ''
    staticMetaObject = None # (!) real value is ''
    UnconnectedState = None # (!) real value is ''
    UnknownSocketError = None # (!) real value is ''
    UnsupportedSocketOperationError = None # (!) real value is ''


