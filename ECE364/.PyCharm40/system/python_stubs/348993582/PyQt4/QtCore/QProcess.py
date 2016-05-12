# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib64/python2.6/site-packages/PyQt4/QtCore.so
# by generator 1.136
# no doc

# imports
import sip as __sip


from QIODevice import QIODevice

class QProcess(QIODevice):
    # no doc
    def atEnd(self, *args, **kwargs): # real signature unknown
        pass

    def bytesAvailable(self, *args, **kwargs): # real signature unknown
        pass

    def bytesToWrite(self, *args, **kwargs): # real signature unknown
        pass

    def canReadLine(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def close(self, *args, **kwargs): # real signature unknown
        pass

    def closeReadChannel(self, *args, **kwargs): # real signature unknown
        pass

    def closeWriteChannel(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def environment(self, *args, **kwargs): # real signature unknown
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

    def execute(self, *args, **kwargs): # real signature unknown
        pass

    def exitCode(self, *args, **kwargs): # real signature unknown
        pass

    def exitStatus(self, *args, **kwargs): # real signature unknown
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

    def isSequential(self, *args, **kwargs): # real signature unknown
        pass

    def kill(self, *args, **kwargs): # real signature unknown
        pass

    def pid(self, *args, **kwargs): # real signature unknown
        pass

    def processChannelMode(self, *args, **kwargs): # real signature unknown
        pass

    def readAllStandardError(self, *args, **kwargs): # real signature unknown
        pass

    def readAllStandardOutput(self, *args, **kwargs): # real signature unknown
        pass

    def readChannel(self, *args, **kwargs): # real signature unknown
        pass

    def readChannelMode(self, *args, **kwargs): # real signature unknown
        pass

    def readData(self, *args, **kwargs): # real signature unknown
        pass

    def readLineData(self, *args, **kwargs): # real signature unknown
        pass

    def readyReadStandardError(self, *args, **kwargs): # real signature unknown
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

    def readyReadStandardOutput(self, *args, **kwargs): # real signature unknown
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

    def setEnvironment(self, *args, **kwargs): # real signature unknown
        pass

    def setErrorString(self, *args, **kwargs): # real signature unknown
        pass

    def setOpenMode(self, *args, **kwargs): # real signature unknown
        pass

    def setProcessChannelMode(self, *args, **kwargs): # real signature unknown
        pass

    def setProcessState(self, *args, **kwargs): # real signature unknown
        pass

    def setReadChannel(self, *args, **kwargs): # real signature unknown
        pass

    def setReadChannelMode(self, *args, **kwargs): # real signature unknown
        pass

    def setStandardErrorFile(self, *args, **kwargs): # real signature unknown
        pass

    def setStandardInputFile(self, *args, **kwargs): # real signature unknown
        pass

    def setStandardOutputFile(self, *args, **kwargs): # real signature unknown
        pass

    def setStandardOutputProcess(self, *args, **kwargs): # real signature unknown
        pass

    def setupChildProcess(self, *args, **kwargs): # real signature unknown
        pass

    def setWorkingDirectory(self, *args, **kwargs): # real signature unknown
        pass

    def start(self, *args, **kwargs): # real signature unknown
        pass

    def startDetached(self, *args, **kwargs): # real signature unknown
        pass

    def started(self, *args, **kwargs): # real signature unknown
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

    def systemEnvironment(self, *args, **kwargs): # real signature unknown
        pass

    def terminate(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def waitForBytesWritten(self, *args, **kwargs): # real signature unknown
        pass

    def waitForFinished(self, *args, **kwargs): # real signature unknown
        pass

    def waitForReadyRead(self, *args, **kwargs): # real signature unknown
        pass

    def waitForStarted(self, *args, **kwargs): # real signature unknown
        pass

    def workingDirectory(self, *args, **kwargs): # real signature unknown
        pass

    def writeData(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    Crashed = 1
    CrashExit = 1
    FailedToStart = 0
    ForwardedChannels = 2
    MergedChannels = 1
    NormalExit = 0
    NotRunning = 0
    ReadError = 3
    Running = 2
    SeparateChannels = 0
    StandardError = 1
    StandardOutput = 0
    Starting = 1
    Timedout = 2
    UnknownError = 5
    WriteError = 4


