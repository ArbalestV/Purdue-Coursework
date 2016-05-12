# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib64/python2.6/site-packages/PyQt4/QtGui.so
# by generator 1.136
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QItemSelectionModel(__PyQt4_QtCore.QObject):
    # no doc
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self, *args, **kwargs): # real signature unknown
        pass

    def clearSelection(self, *args, **kwargs): # real signature unknown
        pass

    def columnIntersectsSelection(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def currentChanged(self, *args, **kwargs): # real signature unknown
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

    def currentColumnChanged(self, *args, **kwargs): # real signature unknown
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

    def currentIndex(self, *args, **kwargs): # real signature unknown
        pass

    def currentRowChanged(self, *args, **kwargs): # real signature unknown
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

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def emitSelectionChanged(self, *args, **kwargs): # real signature unknown
        pass

    def hasSelection(self, *args, **kwargs): # real signature unknown
        pass

    def isColumnSelected(self, *args, **kwargs): # real signature unknown
        pass

    def isRowSelected(self, *args, **kwargs): # real signature unknown
        pass

    def isSelected(self, *args, **kwargs): # real signature unknown
        pass

    def model(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self, *args, **kwargs): # real signature unknown
        pass

    def rowIntersectsSelection(self, *args, **kwargs): # real signature unknown
        pass

    def select(self, *args, **kwargs): # real signature unknown
        pass

    def selectedColumns(self, *args, **kwargs): # real signature unknown
        pass

    def selectedIndexes(self, *args, **kwargs): # real signature unknown
        pass

    def selectedRows(self, *args, **kwargs): # real signature unknown
        pass

    def selection(self, *args, **kwargs): # real signature unknown
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

    def setCurrentIndex(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    Clear = 1
    ClearAndSelect = 3
    Columns = 64
    Current = 16
    Deselect = 4
    NoUpdate = 0
    Rows = 32
    Select = 2
    SelectCurrent = 18
    Toggle = 8
    ToggleCurrent = 24


