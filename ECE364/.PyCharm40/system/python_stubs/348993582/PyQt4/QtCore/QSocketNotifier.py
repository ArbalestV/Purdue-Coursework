# encoding: utf-8
# module PyQt4.QtCore
# from /usr/lib64/python2.6/site-packages/PyQt4/QtCore.so
# by generator 1.136
# no doc

# imports
import sip as __sip


from QObject import QObject

class QSocketNotifier(QObject):
    # no doc
    def activated(self, *args, **kwargs): # real signature unknown
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

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, *args, **kwargs): # real signature unknown
        pass

    def isEnabled(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def setEnabled(self, *args, **kwargs): # real signature unknown
        pass

    def socket(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def type(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    Exception = 2
    Read = 0
    Write = 1


