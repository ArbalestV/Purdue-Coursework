# encoding: utf-8
# module PyQt4.QtNetwork
# from /usr/lib64/python2.6/site-packages/PyQt4/QtNetwork.so
# by generator 1.136
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QNetworkReply(__PyQt4_QtCore.QIODevice):
    # no doc
    def abort(self, *args, **kwargs): # real signature unknown
        pass

    def attribute(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def close(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def downloadProgress(self, *args, **kwargs): # real signature unknown
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

    def finished(self, *args, **kwargs): # real signature unknown
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

    def hasRawHeader(self, *args, **kwargs): # real signature unknown
        pass

    def header(self, *args, **kwargs): # real signature unknown
        pass

    def ignoreSslErrors(self, *args, **kwargs): # real signature unknown
        pass

    def isSequential(self, *args, **kwargs): # real signature unknown
        pass

    def manager(self, *args, **kwargs): # real signature unknown
        pass

    def metaDataChanged(self, *args, **kwargs): # real signature unknown
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

    def operation(self, *args, **kwargs): # real signature unknown
        pass

    def rawHeader(self, *args, **kwargs): # real signature unknown
        pass

    def rawHeaderList(self, *args, **kwargs): # real signature unknown
        pass

    def readBufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def readData(self, *args, **kwargs): # real signature unknown
        pass

    def readLineData(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def request(self, *args, **kwargs): # real signature unknown
        pass

    def setAttribute(self, *args, **kwargs): # real signature unknown
        pass

    def setError(self, *args, **kwargs): # real signature unknown
        pass

    def setErrorString(self, *args, **kwargs): # real signature unknown
        pass

    def setHeader(self, *args, **kwargs): # real signature unknown
        pass

    def setOpenMode(self, *args, **kwargs): # real signature unknown
        pass

    def setOperation(self, *args, **kwargs): # real signature unknown
        pass

    def setRawHeader(self, *args, **kwargs): # real signature unknown
        pass

    def setReadBufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def setRequest(self, *args, **kwargs): # real signature unknown
        pass

    def setSslConfiguration(self, *args, **kwargs): # real signature unknown
        pass

    def setUrl(self, *args, **kwargs): # real signature unknown
        pass

    def sslConfiguration(self, *args, **kwargs): # real signature unknown
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

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def uploadProgress(self, *args, **kwargs): # real signature unknown
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

    def url(self, *args, **kwargs): # real signature unknown
        pass

    def writeData(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    AuthenticationRequiredError = 204
    ConnectionRefusedError = 1
    ContentAccessDenied = 201
    ContentNotFoundError = 203
    ContentOperationNotPermittedError = 202
    HostNotFoundError = 3
    NoError = 0
    OperationCanceledError = 5
    ProtocolFailure = 399
    ProtocolInvalidOperationError = 302
    ProtocolUnknownError = 301
    ProxyAuthenticationRequiredError = 105
    ProxyConnectionClosedError = 102
    ProxyConnectionRefusedError = 101
    ProxyNotFoundError = 103
    ProxyTimeoutError = 104
    RemoteHostClosedError = 2
    SslHandshakeFailedError = 6
    TimeoutError = 4
    UnknownContentError = 299
    UnknownNetworkError = 99
    UnknownProxyError = 199


