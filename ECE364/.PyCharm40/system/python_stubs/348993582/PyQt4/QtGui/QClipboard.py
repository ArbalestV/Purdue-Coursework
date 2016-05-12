# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib64/python2.6/site-packages/PyQt4/QtGui.so
# by generator 1.136
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QClipboard(__PyQt4_QtCore.QObject):
    # no doc
    def changed(self, *args, **kwargs): # real signature unknown
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

    def clear(self, *args, **kwargs): # real signature unknown
        pass

    def dataChanged(self, *args, **kwargs): # real signature unknown
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

    def findBufferChanged(self, *args, **kwargs): # real signature unknown
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

    def image(self, *args, **kwargs): # real signature unknown
        pass

    def mimeData(self, *args, **kwargs): # real signature unknown
        pass

    def ownsClipboard(self, *args, **kwargs): # real signature unknown
        pass

    def ownsFindBuffer(self, *args, **kwargs): # real signature unknown
        pass

    def ownsSelection(self, *args, **kwargs): # real signature unknown
        pass

    def pixmap(self, *args, **kwargs): # real signature unknown
        pass

    def selectionChanged(self, *args, **kwargs): # real signature unknown
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

    def setImage(self, *args, **kwargs): # real signature unknown
        pass

    def setMimeData(self, *args, **kwargs): # real signature unknown
        pass

    def setPixmap(self, *args, **kwargs): # real signature unknown
        pass

    def setText(self, *args, **kwargs): # real signature unknown
        pass

    def supportsFindBuffer(self, *args, **kwargs): # real signature unknown
        pass

    def supportsSelection(self, *args, **kwargs): # real signature unknown
        pass

    def text(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    Clipboard = 0
    FindBuffer = 2
    Selection = 1


