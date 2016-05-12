# encoding: utf-8
# module PyQt4.QtNetwork
# from /usr/lib64/python2.6/site-packages/PyQt4/QtNetwork.so
# by generator 1.136
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QHttp(__PyQt4_QtCore.QObject):
    # no doc
    def abort(self, *args, **kwargs): # real signature unknown
        pass

    def authenticationRequired(self, *args, **kwargs): # real signature unknown
        """
        pyqtSignal(*types, name=str) -> signal attribute
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively each
        type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        """
        pass

    def bytesAvailable(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clearPendingRequests(self, *args, **kwargs): # real signature unknown
        pass

    def close(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def currentDestinationDevice(self, *args, **kwargs): # real signature unknown
        pass

    def currentId(self, *args, **kwargs): # real signature unknown
        pass

    def currentRequest(self, *args, **kwargs): # real signature unknown
        pass

    def currentSourceDevice(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def dataReadProgress(self, *args, **kwargs): # real signature unknown
        """
        pyqtSignal(*types, name=str) -> signal attribute
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively each
        type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        """
        pass

    def dataSendProgress(self, *args, **kwargs): # real signature unknown
        """
        pyqtSignal(*types, name=str) -> signal attribute
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively each
        type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        """
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def done(self, *args, **kwargs): # real signature unknown
        """
        pyqtSignal(*types, name=str) -> signal attribute
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively each
        type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        """
        pass

    def error(self, *args, **kwargs): # real signature unknown
        pass

    def errorString(self, *args, **kwargs): # real signature unknown
        pass

    def get(self, *args, **kwargs): # real signature unknown
        pass

    def hasPendingRequests(self, *args, **kwargs): # real signature unknown
        pass

    def head(self, *args, **kwargs): # real signature unknown
        pass

    def ignoreSslErrors(self, *args, **kwargs): # real signature unknown
        pass

    def lastResponse(self, *args, **kwargs): # real signature unknown
        pass

    def post(self, *args, **kwargs): # real signature unknown
        pass

    def proxyAuthenticationRequired(self, *args, **kwargs): # real signature unknown
        """
        pyqtSignal(*types, name=str) -> signal attribute
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively each
        type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        """
        pass

    def read(self, *args, **kwargs): # real signature unknown
        pass

    def readAll(self, *args, **kwargs): # real signature unknown
        pass

    def readyRead(self, *args, **kwargs): # real signature unknown
        """
        pyqtSignal(*types, name=str) -> signal attribute
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively each
        type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def request(self, *args, **kwargs): # real signature unknown
        pass

    def requestFinished(self, *args, **kwargs): # real signature unknown
        """
        pyqtSignal(*types, name=str) -> signal attribute
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively each
        type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        """
        pass

    def requestStarted(self, *args, **kwargs): # real signature unknown
        """
        pyqtSignal(*types, name=str) -> signal attribute
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively each
        type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        """
        pass

    def responseHeaderReceived(self, *args, **kwargs): # real signature unknown
        """
        pyqtSignal(*types, name=str) -> signal attribute
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively each
        type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        """
        pass

    def setHost(self, *args, **kwargs): # real signature unknown
        pass

    def setProxy(self, *args, **kwargs): # real signature unknown
        pass

    def setSocket(self, *args, **kwargs): # real signature unknown
        pass

    def setUser(self, *args, **kwargs): # real signature unknown
        pass

    def sslErrors(self, *args, **kwargs): # real signature unknown
        """
        pyqtSignal(*types, name=str) -> signal attribute
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively each
        type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        """
        pass

    def state(self, *args, **kwargs): # real signature unknown
        pass

    def stateChanged(self, *args, **kwargs): # real signature unknown
        """
        pyqtSignal(*types, name=str) -> signal attribute
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively each
        type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    Aborted = 7
    AuthenticationRequiredError = 8
    Closing = 6
    Connected = 5
    Connecting = 2
    ConnectionModeHttp = 0
    ConnectionModeHttps = 1
    ConnectionRefused = 3
    HostLookup = 1
    HostNotFound = 2
    InvalidResponseHeader = 5
    NoError = 0
    ProxyAuthenticationRequiredError = 9
    Reading = 4
    Sending = 3
    Unconnected = 0
    UnexpectedClose = 4
    UnknownError = 1
    WrongContentLength = 6


