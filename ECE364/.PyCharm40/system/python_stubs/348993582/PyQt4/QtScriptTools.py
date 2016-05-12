# encoding: utf-8
# module PyQt4.QtScriptTools
# from /usr/lib64/python2.6/site-packages/PyQt4/QtScriptTools.so
# by generator 1.136
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


# no functions
# classes

class QScriptEngineDebugger(__PyQt4_QtCore.QObject):
    # no doc
    def action(self, *args, **kwargs): # real signature unknown
        pass

    def attachTo(self, *args, **kwargs): # real signature unknown
        pass

    def autoShowStandardWindow(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def createStandardMenu(self, *args, **kwargs): # real signature unknown
        pass

    def createStandardToolBar(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def detach(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def evaluationResumed(self, *args, **kwargs): # real signature unknown
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

    def evaluationSuspended(self, *args, **kwargs): # real signature unknown
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

    def setAutoShowStandardWindow(self, *args, **kwargs): # real signature unknown
        pass

    def standardWindow(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def widget(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    BreakpointsWidget = 6
    ClearConsoleAction = 10
    ClearDebugOutputAction = 8
    ClearErrorLogAction = 9
    CodeFinderWidget = 5
    CodeWidget = 4
    ConsoleWidget = 0
    ContinueAction = 1
    DebugOutputWidget = 7
    ErrorLogWidget = 8
    FindInScriptAction = 11
    FindNextInScriptAction = 12
    FindPreviousInScriptAction = 13
    GoToLineAction = 14
    InterruptAction = 0
    LocalsWidget = 3
    RunToCursorAction = 5
    RunToNewScriptAction = 6
    ScriptsWidget = 2
    StackWidget = 1
    StepIntoAction = 2
    StepOutAction = 4
    StepOverAction = 3
    ToggleBreakpointAction = 7


