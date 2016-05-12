# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib64/python2.6/site-packages/PyQt4/QtCore.so
# by generator 1.136
# no doc

# imports
import sip as __sip


from QObject import QObject

class QTimeLine(QObject):
    # no doc
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def currentFrame(self, *args, **kwargs): # real signature unknown
        pass

    def currentTime(self, *args, **kwargs): # real signature unknown
        pass

    def currentValue(self, *args, **kwargs): # real signature unknown
        pass

    def curveShape(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def direction(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def duration(self, *args, **kwargs): # real signature unknown
        pass

    def endFrame(self, *args, **kwargs): # real signature unknown
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

    def frameForTime(self, *args, **kwargs): # real signature unknown
        pass

    def loopCount(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def resume(self, *args, **kwargs): # real signature unknown
        pass

    def setCurrentTime(self, *args, **kwargs): # real signature unknown
        pass

    def setCurveShape(self, *args, **kwargs): # real signature unknown
        pass

    def setDirection(self, *args, **kwargs): # real signature unknown
        pass

    def setDuration(self, *args, **kwargs): # real signature unknown
        pass

    def setEndFrame(self, *args, **kwargs): # real signature unknown
        pass

    def setFrameRange(self, *args, **kwargs): # real signature unknown
        pass

    def setLoopCount(self, *args, **kwargs): # real signature unknown
        pass

    def setPaused(self, *args, **kwargs): # real signature unknown
        pass

    def setStartFrame(self, *args, **kwargs): # real signature unknown
        pass

    def setUpdateInterval(self, *args, **kwargs): # real signature unknown
        pass

    def start(self, *args, **kwargs): # real signature unknown
        pass

    def startFrame(self, *args, **kwargs): # real signature unknown
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

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def toggleDirection(self, *args, **kwargs): # real signature unknown
        pass

    def updateInterval(self, *args, **kwargs): # real signature unknown
        pass

    def valueChanged(self, *args, **kwargs): # real signature unknown
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

    def valueForTime(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    Backward = 1
    CosineCurve = 5
    EaseInCurve = 0
    EaseInOutCurve = 2
    EaseOutCurve = 1
    Forward = 0
    LinearCurve = 3
    NotRunning = 0
    Paused = 1
    Running = 2
    SineCurve = 4


