# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib64/python2.6/site-packages/PyQt4/QtCore.so
# by generator 1.136
# no doc

# imports
import sip as __sip


from QObject import QObject

class QAbstractEventDispatcher(QObject):
    # no doc
    def aboutToBlock(self, *args, **kwargs): # real signature unknown
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

    def awake(self, *args, **kwargs): # real signature unknown
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

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def closingDown(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def flush(self, *args, **kwargs): # real signature unknown
        pass

    def hasPendingEvents(self, *args, **kwargs): # real signature unknown
        pass

    def instance(self, *args, **kwargs): # real signature unknown
        pass

    def interrupt(self, *args, **kwargs): # real signature unknown
        pass

    def processEvents(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def registeredTimers(self, *args, **kwargs): # real signature unknown
        pass

    def registerSocketNotifier(self, *args, **kwargs): # real signature unknown
        pass

    def registerTimer(self, *args, **kwargs): # real signature unknown
        pass

    def startingUp(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def unregisterSocketNotifier(self, *args, **kwargs): # real signature unknown
        pass

    def unregisterTimer(self, *args, **kwargs): # real signature unknown
        pass

    def unregisterTimers(self, *args, **kwargs): # real signature unknown
        pass

    def wakeUp(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


