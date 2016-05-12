# encoding: utf-8
# module PyQt4.QtGui
# from /usr/lib64/python2.6/site-packages/PyQt4/QtGui.so
# by generator 1.136
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


class QCompleter(__PyQt4_QtCore.QObject):
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

    def caseSensitivity(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def complete(self, *args, **kwargs): # real signature unknown
        pass

    def completionColumn(self, *args, **kwargs): # real signature unknown
        pass

    def completionCount(self, *args, **kwargs): # real signature unknown
        pass

    def completionMode(self, *args, **kwargs): # real signature unknown
        pass

    def completionModel(self, *args, **kwargs): # real signature unknown
        pass

    def completionPrefix(self, *args, **kwargs): # real signature unknown
        pass

    def completionRole(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def currentCompletion(self, *args, **kwargs): # real signature unknown
        pass

    def currentIndex(self, *args, **kwargs): # real signature unknown
        pass

    def currentRow(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, *args, **kwargs): # real signature unknown
        pass

    def eventFilter(self, *args, **kwargs): # real signature unknown
        pass

    def highlighted(self, *args, **kwargs): # real signature unknown
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

    def model(self, *args, **kwargs): # real signature unknown
        pass

    def modelSorting(self, *args, **kwargs): # real signature unknown
        pass

    def pathFromIndex(self, *args, **kwargs): # real signature unknown
        pass

    def popup(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def setCaseSensitivity(self, *args, **kwargs): # real signature unknown
        pass

    def setCompletionColumn(self, *args, **kwargs): # real signature unknown
        pass

    def setCompletionMode(self, *args, **kwargs): # real signature unknown
        pass

    def setCompletionPrefix(self, *args, **kwargs): # real signature unknown
        pass

    def setCompletionRole(self, *args, **kwargs): # real signature unknown
        pass

    def setCurrentRow(self, *args, **kwargs): # real signature unknown
        pass

    def setModel(self, *args, **kwargs): # real signature unknown
        pass

    def setModelSorting(self, *args, **kwargs): # real signature unknown
        pass

    def setPopup(self, *args, **kwargs): # real signature unknown
        pass

    def setWidget(self, *args, **kwargs): # real signature unknown
        pass

    def setWrapAround(self, *args, **kwargs): # real signature unknown
        pass

    def splitPath(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def widget(self, *args, **kwargs): # real signature unknown
        pass

    def wrapAround(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    CaseInsensitivelySortedModel = 2
    CaseSensitivelySortedModel = 1
    InlineCompletion = 2
    PopupCompletion = 0
    UnfilteredPopupCompletion = 1
    UnsortedModel = 0


