# encoding: utf-8
# module PyQt4.QtScript
# from /usr/lib64/python2.6/site-packages/PyQt4/QtScript.so
# by generator 1.136
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


# functions

def qScriptConnect(*args, **kwargs): # real signature unknown
    pass

def qScriptDisconnect(*args, **kwargs): # real signature unknown
    pass

# classes

class QScriptClass(): # skipped bases: <type 'sip.simplewrapper'>
    # no doc
    def engine(self, *args, **kwargs): # real signature unknown
        pass

    def extension(self, *args, **kwargs): # real signature unknown
        pass

    def name(self, *args, **kwargs): # real signature unknown
        pass

    def newIterator(self, *args, **kwargs): # real signature unknown
        pass

    def property(self, *args, **kwargs): # real signature unknown
        pass

    def propertyFlags(self, *args, **kwargs): # real signature unknown
        pass

    def prototype(self, *args, **kwargs): # real signature unknown
        pass

    def queryProperty(self, *args, **kwargs): # real signature unknown
        pass

    def setProperty(self, *args, **kwargs): # real signature unknown
        pass

    def supportsExtension(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    Callable = 0
    HandlesReadAccess = 1
    HandlesWriteAccess = 2
    HasInstance = 1


class QScriptClassPropertyIterator(): # skipped bases: <type 'sip.simplewrapper'>
    # no doc
    def flags(self, *args, **kwargs): # real signature unknown
        pass

    def hasNext(self, *args, **kwargs): # real signature unknown
        pass

    def hasPrevious(self, *args, **kwargs): # real signature unknown
        pass

    def id(self, *args, **kwargs): # real signature unknown
        pass

    def name(self, *args, **kwargs): # real signature unknown
        pass

    def next(self, *args, **kwargs): # real signature unknown
        pass

    def object(self, *args, **kwargs): # real signature unknown
        pass

    def previous(self, *args, **kwargs): # real signature unknown
        pass

    def toBack(self, *args, **kwargs): # real signature unknown
        pass

    def toFront(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QScriptContext(): # skipped bases: <type 'sip.simplewrapper'>
    # no doc
    def activationObject(self, *args, **kwargs): # real signature unknown
        pass

    def argument(self, *args, **kwargs): # real signature unknown
        pass

    def argumentCount(self, *args, **kwargs): # real signature unknown
        pass

    def argumentsObject(self, *args, **kwargs): # real signature unknown
        pass

    def backtrace(self, *args, **kwargs): # real signature unknown
        pass

    def callee(self, *args, **kwargs): # real signature unknown
        pass

    def engine(self, *args, **kwargs): # real signature unknown
        pass

    def isCalledAsConstructor(self, *args, **kwargs): # real signature unknown
        pass

    def parentContext(self, *args, **kwargs): # real signature unknown
        pass

    def setActivationObject(self, *args, **kwargs): # real signature unknown
        pass

    def setThisObject(self, *args, **kwargs): # real signature unknown
        pass

    def state(self, *args, **kwargs): # real signature unknown
        pass

    def thisObject(self, *args, **kwargs): # real signature unknown
        pass

    def throwError(self, *args, **kwargs): # real signature unknown
        pass

    def throwValue(self, *args, **kwargs): # real signature unknown
        pass

    def toString(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    ExceptionState = 1
    NormalState = 0
    RangeError = 4
    ReferenceError = 1
    SyntaxError = 2
    TypeError = 3
    UnknownError = 0
    URIError = 5


class QScriptContextInfo(): # skipped bases: <type 'sip.simplewrapper'>
    # no doc
    def columnNumber(self, *args, **kwargs): # real signature unknown
        pass

    def fileName(self, *args, **kwargs): # real signature unknown
        pass

    def functionEndLineNumber(self, *args, **kwargs): # real signature unknown
        pass

    def functionMetaIndex(self, *args, **kwargs): # real signature unknown
        pass

    def functionName(self, *args, **kwargs): # real signature unknown
        pass

    def functionParameterNames(self, *args, **kwargs): # real signature unknown
        pass

    def functionStartLineNumber(self, *args, **kwargs): # real signature unknown
        pass

    def functionType(self, *args, **kwargs): # real signature unknown
        pass

    def isNull(self, *args, **kwargs): # real signature unknown
        pass

    def lineNumber(self, *args, **kwargs): # real signature unknown
        pass

    def scriptId(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, y): # real signature unknown; restored from __doc__
        """ x.__le__(y) <==> x<=y """
        pass

    def __lt__(self, y): # real signature unknown; restored from __doc__
        """ x.__lt__(y) <==> x<y """
        pass

    def __ne__(self, y): # real signature unknown; restored from __doc__
        """ x.__ne__(y) <==> x!=y """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    NativeFunction = 3
    QtFunction = 1
    QtPropertyFunction = 2
    ScriptFunction = 0


class QScriptEngine(__PyQt4_QtCore.QObject):
    # no doc
    def abortEvaluation(self, *args, **kwargs): # real signature unknown
        pass

    def agent(self, *args, **kwargs): # real signature unknown
        pass

    def availableExtensions(self, *args, **kwargs): # real signature unknown
        pass

    def canEvaluate(self, *args, **kwargs): # real signature unknown
        pass

    def checkSyntax(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clearExceptions(self, *args, **kwargs): # real signature unknown
        pass

    def collectGarbage(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def currentContext(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def defaultPrototype(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def evaluate(self, *args, **kwargs): # real signature unknown
        pass

    def globalObject(self, *args, **kwargs): # real signature unknown
        pass

    def hasUncaughtException(self, *args, **kwargs): # real signature unknown
        pass

    def importedExtensions(self, *args, **kwargs): # real signature unknown
        pass

    def importExtension(self, *args, **kwargs): # real signature unknown
        pass

    def installTranslatorFunctions(self, *args, **kwargs): # real signature unknown
        pass

    def isEvaluating(self, *args, **kwargs): # real signature unknown
        pass

    def newArray(self, *args, **kwargs): # real signature unknown
        pass

    def newDate(self, *args, **kwargs): # real signature unknown
        pass

    def newFunction(self, *args, **kwargs): # real signature unknown
        pass

    def newObject(self, *args, **kwargs): # real signature unknown
        pass

    def newQMetaObject(self, *args, **kwargs): # real signature unknown
        pass

    def newQObject(self, *args, **kwargs): # real signature unknown
        pass

    def newRegExp(self, *args, **kwargs): # real signature unknown
        pass

    def newVariant(self, *args, **kwargs): # real signature unknown
        pass

    def nullValue(self, *args, **kwargs): # real signature unknown
        pass

    def processEventsInterval(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def setAgent(self, *args, **kwargs): # real signature unknown
        pass

    def setDefaultPrototype(self, *args, **kwargs): # real signature unknown
        pass

    def setGlobalObject(self, *args, **kwargs): # real signature unknown
        pass

    def setProcessEventsInterval(self, *args, **kwargs): # real signature unknown
        pass

    def signalHandlerException(self, *args, **kwargs): # real signature unknown
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

    def toObject(self, *args, **kwargs): # real signature unknown
        pass

    def toStringHandle(self, *args, **kwargs): # real signature unknown
        pass

    def uncaughtException(self, *args, **kwargs): # real signature unknown
        pass

    def uncaughtExceptionBacktrace(self, *args, **kwargs): # real signature unknown
        pass

    def uncaughtExceptionLineNumber(self, *args, **kwargs): # real signature unknown
        pass

    def undefinedValue(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    AutoCreateDynamicProperties = 256
    AutoOwnership = 2
    ExcludeChildObjects = 1
    ExcludeDeleteLater = 16
    ExcludeSuperClassContents = 6
    ExcludeSuperClassMethods = 2
    ExcludeSuperClassProperties = 4
    PreferExistingWrapperObject = 512
    QtOwnership = 0
    ScriptOwnership = 1
    SkipMethodsInEnumeration = 8


class QScriptEngineAgent(): # skipped bases: <type 'sip.simplewrapper'>
    # no doc
    def contextPop(self, *args, **kwargs): # real signature unknown
        pass

    def contextPush(self, *args, **kwargs): # real signature unknown
        pass

    def engine(self, *args, **kwargs): # real signature unknown
        pass

    def exceptionCatch(self, *args, **kwargs): # real signature unknown
        pass

    def exceptionThrow(self, *args, **kwargs): # real signature unknown
        pass

    def extension(self, *args, **kwargs): # real signature unknown
        pass

    def functionEntry(self, *args, **kwargs): # real signature unknown
        pass

    def functionExit(self, *args, **kwargs): # real signature unknown
        pass

    def positionChange(self, *args, **kwargs): # real signature unknown
        pass

    def scriptLoad(self, *args, **kwargs): # real signature unknown
        pass

    def scriptUnload(self, *args, **kwargs): # real signature unknown
        pass

    def supportsExtension(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    DebuggerInvocationRequest = 0


class QScriptString(): # skipped bases: <type 'sip.simplewrapper'>
    # no doc
    def isValid(self, *args, **kwargs): # real signature unknown
        pass

    def toString(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, y): # real signature unknown; restored from __doc__
        """ x.__le__(y) <==> x<=y """
        pass

    def __lt__(self, y): # real signature unknown; restored from __doc__
        """ x.__lt__(y) <==> x<y """
        pass

    def __ne__(self, y): # real signature unknown; restored from __doc__
        """ x.__ne__(y) <==> x!=y """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QScriptSyntaxCheckResult(): # skipped bases: <type 'sip.simplewrapper'>
    # no doc
    def errorColumnNumber(self, *args, **kwargs): # real signature unknown
        pass

    def errorLineNumber(self, *args, **kwargs): # real signature unknown
        pass

    def errorMessage(self, *args, **kwargs): # real signature unknown
        pass

    def state(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    Error = 0
    Intermediate = 1
    Valid = 2


class QScriptValue(): # skipped bases: <type 'sip.simplewrapper'>
    # no doc
    def call(self, *args, **kwargs): # real signature unknown
        pass

    def construct(self, *args, **kwargs): # real signature unknown
        pass

    def data(self, *args, **kwargs): # real signature unknown
        pass

    def engine(self, *args, **kwargs): # real signature unknown
        pass

    def equals(self, *args, **kwargs): # real signature unknown
        pass

    def instanceOf(self, *args, **kwargs): # real signature unknown
        pass

    def isArray(self, *args, **kwargs): # real signature unknown
        pass

    def isBool(self, *args, **kwargs): # real signature unknown
        pass

    def isBoolean(self, *args, **kwargs): # real signature unknown
        pass

    def isDate(self, *args, **kwargs): # real signature unknown
        pass

    def isError(self, *args, **kwargs): # real signature unknown
        pass

    def isFunction(self, *args, **kwargs): # real signature unknown
        pass

    def isNull(self, *args, **kwargs): # real signature unknown
        pass

    def isNumber(self, *args, **kwargs): # real signature unknown
        pass

    def isObject(self, *args, **kwargs): # real signature unknown
        pass

    def isQMetaObject(self, *args, **kwargs): # real signature unknown
        pass

    def isQObject(self, *args, **kwargs): # real signature unknown
        pass

    def isRegExp(self, *args, **kwargs): # real signature unknown
        pass

    def isString(self, *args, **kwargs): # real signature unknown
        pass

    def isUndefined(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        pass

    def isVariant(self, *args, **kwargs): # real signature unknown
        pass

    def lessThan(self, *args, **kwargs): # real signature unknown
        pass

    def property(self, *args, **kwargs): # real signature unknown
        pass

    def propertyFlags(self, *args, **kwargs): # real signature unknown
        pass

    def prototype(self, *args, **kwargs): # real signature unknown
        pass

    def scriptClass(self, *args, **kwargs): # real signature unknown
        pass

    def setData(self, *args, **kwargs): # real signature unknown
        pass

    def setProperty(self, *args, **kwargs): # real signature unknown
        pass

    def setPrototype(self, *args, **kwargs): # real signature unknown
        pass

    def setScriptClass(self, *args, **kwargs): # real signature unknown
        pass

    def strictlyEquals(self, *args, **kwargs): # real signature unknown
        pass

    def toBool(self, *args, **kwargs): # real signature unknown
        pass

    def toBoolean(self, *args, **kwargs): # real signature unknown
        pass

    def toDateTime(self, *args, **kwargs): # real signature unknown
        pass

    def toInt32(self, *args, **kwargs): # real signature unknown
        pass

    def toInteger(self, *args, **kwargs): # real signature unknown
        pass

    def toNumber(self, *args, **kwargs): # real signature unknown
        pass

    def toObject(self, *args, **kwargs): # real signature unknown
        pass

    def toQMetaObject(self, *args, **kwargs): # real signature unknown
        pass

    def toQObject(self, *args, **kwargs): # real signature unknown
        pass

    def toRegExp(self, *args, **kwargs): # real signature unknown
        pass

    def toString(self, *args, **kwargs): # real signature unknown
        pass

    def toUInt16(self, *args, **kwargs): # real signature unknown
        pass

    def toUInt32(self, *args, **kwargs): # real signature unknown
        pass

    def toVariant(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    KeepExistingFlags = 2048
    NullValue = 0
    PropertyGetter = 8
    PropertySetter = 16
    QObjectMember = 32
    ReadOnly = 1
    ResolveFull = 3
    ResolveLocal = 0
    ResolvePrototype = 1
    ResolveScope = 2
    SkipInEnumeration = 4
    UndefinedValue = 1
    Undeletable = 2
    UserRange = -16777216


class QScriptValueIterator(): # skipped bases: <type 'sip.simplewrapper'>
    # no doc
    def flags(self, *args, **kwargs): # real signature unknown
        pass

    def hasNext(self, *args, **kwargs): # real signature unknown
        pass

    def hasPrevious(self, *args, **kwargs): # real signature unknown
        pass

    def name(self, *args, **kwargs): # real signature unknown
        pass

    def next(self, *args, **kwargs): # real signature unknown
        pass

    def previous(self, *args, **kwargs): # real signature unknown
        pass

    def remove(self, *args, **kwargs): # real signature unknown
        pass

    def scriptName(self, *args, **kwargs): # real signature unknown
        pass

    def setValue(self, *args, **kwargs): # real signature unknown
        pass

    def toBack(self, *args, **kwargs): # real signature unknown
        pass

    def toFront(self, *args, **kwargs): # real signature unknown
        pass

    def value(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



