# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib64/python2.6/site-packages/PyQt4/QtGui.so
# by generator 1.136
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QMovie(__PyQt4_QtCore.QObject):
    # no doc
    def backgroundColor(self, *args, **kwargs): # real signature unknown
        pass

    def cacheMode(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def currentFrameNumber(self, *args, **kwargs): # real signature unknown
        pass

    def currentImage(self, *args, **kwargs): # real signature unknown
        pass

    def currentPixmap(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def device(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
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

    def fileName(self, *args, **kwargs): # real signature unknown
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

    def format(self, *args, **kwargs): # real signature unknown
        pass

    def frameChanged(self, *args, **kwargs): # real signature unknown
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

    def frameCount(self, *args, **kwargs): # real signature unknown
        pass

    def frameRect(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        pass

    def jumpToFrame(self, *args, **kwargs): # real signature unknown
        pass

    def jumpToNextFrame(self, *args, **kwargs): # real signature unknown
        pass

    def loopCount(self, *args, **kwargs): # real signature unknown
        pass

    def nextFrameDelay(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def resized(self, *args, **kwargs): # real signature unknown
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

    def scaledSize(self, *args, **kwargs): # real signature unknown
        pass

    def setBackgroundColor(self, *args, **kwargs): # real signature unknown
        pass

    def setCacheMode(self, *args, **kwargs): # real signature unknown
        pass

    def setDevice(self, *args, **kwargs): # real signature unknown
        pass

    def setFileName(self, *args, **kwargs): # real signature unknown
        pass

    def setFormat(self, *args, **kwargs): # real signature unknown
        pass

    def setPaused(self, *args, **kwargs): # real signature unknown
        pass

    def setScaledSize(self, *args, **kwargs): # real signature unknown
        pass

    def setSpeed(self, *args, **kwargs): # real signature unknown
        pass

    def speed(self, *args, **kwargs): # real signature unknown
        pass

    def start(self, *args, **kwargs): # real signature unknown
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

    def stop(self, *args, **kwargs): # real signature unknown
        pass

    def supportedFormats(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updated(self, *args, **kwargs): # real signature unknown
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

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    CacheAll = 1
    CacheNone = 0
    NotRunning = 0
    Paused = 1
    Running = 2


