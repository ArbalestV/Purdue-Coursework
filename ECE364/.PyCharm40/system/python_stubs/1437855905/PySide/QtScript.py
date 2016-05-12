# encoding: utf-8
# module PySide.QtScript
# from /opt/python3/current/lib/python3.4/site-packages/PySide/QtScript.so
# by generator 1.136
# no doc

# imports
import PySide.QtCore as __PySide_QtCore
import Shiboken as __Shiboken


# no functions
# classes

class QScriptable(__Shiboken.Object):
    # no doc
    def argument(self, *args, **kwargs): # real signature unknown
        pass

    def argumentCount(self, *args, **kwargs): # real signature unknown
        pass

    def context(self, *args, **kwargs): # real signature unknown
        pass

    def engine(self, *args, **kwargs): # real signature unknown
        pass

    def thisObject(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class QScriptClass(__Shiboken.Object):
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

    def setProperty(self, *args, **kwargs): # real signature unknown
        pass

    def supportsExtension(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    Callable = None # (!) real value is ''
    Extension = None # (!) real value is ''
    HandlesReadAccess = None # (!) real value is ''
    HandlesWriteAccess = None # (!) real value is ''
    HasInstance = None # (!) real value is ''
    QueryFlag = None # (!) real value is ''


class QScriptClassPropertyIterator(__Shiboken.Object):
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

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class QScriptContext(__Shiboken.Object):
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

    def popScope(self, *args, **kwargs): # real signature unknown
        pass

    def pushScope(self, *args, **kwargs): # real signature unknown
        pass

    def returnValue(self, *args, **kwargs): # real signature unknown
        pass

    def scopeChain(self, *args, **kwargs): # real signature unknown
        pass

    def setActivationObject(self, *args, **kwargs): # real signature unknown
        pass

    def setReturnValue(self, *args, **kwargs): # real signature unknown
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

    Error = None # (!) real value is ''
    ExceptionState = None # (!) real value is ''
    ExecutionState = None # (!) real value is ''
    NormalState = None # (!) real value is ''
    RangeError = None # (!) real value is ''
    ReferenceError = None # (!) real value is ''
    SyntaxError = None # (!) real value is ''
    TypeError = None # (!) real value is ''
    UnknownError = None # (!) real value is ''
    URIError = None # (!) real value is ''


class QScriptContextInfo(__Shiboken.Object):
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

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lshift__(self, *args, **kwargs): # real signature unknown
        """ Return self<<value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, *args, **kwargs): # real signature unknown
        """ Return self>>value. """
        pass

    FunctionType = None # (!) real value is ''
    NativeFunction = None # (!) real value is ''
    QtFunction = None # (!) real value is ''
    QtPropertyFunction = None # (!) real value is ''
    ScriptFunction = None # (!) real value is ''
    __hash__ = None


class QScriptEngine(__PySide_QtCore.QObject):
    # no doc
    def abortEvaluation(self, *args, **kwargs): # real signature unknown
        pass

    def agent(self, *args, **kwargs): # real signature unknown
        pass

    def availableExtensions(self, *args, **kwargs): # real signature unknown
        pass

    def canEvaluate(self, *args, **kwargs): # real signature unknown
        pass

    def clearExceptions(self, *args, **kwargs): # real signature unknown
        pass

    def collectGarbage(self, *args, **kwargs): # real signature unknown
        pass

    def currentContext(self, *args, **kwargs): # real signature unknown
        pass

    def defaultPrototype(self, *args, **kwargs): # real signature unknown
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

    def newActivationObject(self, *args, **kwargs): # real signature unknown
        pass

    def newArray(self, *args, **kwargs): # real signature unknown
        pass

    def newDate(self, *args, **kwargs): # real signature unknown
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

    def objectById(self, *args, **kwargs): # real signature unknown
        pass

    def popContext(self, *args, **kwargs): # real signature unknown
        pass

    def processEventsInterval(self, *args, **kwargs): # real signature unknown
        pass

    def pushContext(self, *args, **kwargs): # real signature unknown
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
        """ Signal """
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

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    AutoCreateDynamicProperties = None # (!) real value is ''
    AutoOwnership = None # (!) real value is ''
    ExcludeChildObjects = None # (!) real value is ''
    ExcludeDeleteLater = None # (!) real value is ''
    ExcludeSuperClassContents = None # (!) real value is ''
    ExcludeSuperClassMethods = None # (!) real value is ''
    ExcludeSuperClassProperties = None # (!) real value is ''
    PreferExistingWrapperObject = None # (!) real value is ''
    QObjectWrapOption = None # (!) real value is ''
    QObjectWrapOptions = None # (!) real value is ''
    QtOwnership = None # (!) real value is ''
    ScriptOwnership = None # (!) real value is ''
    SkipMethodsInEnumeration = None # (!) real value is ''
    staticMetaObject = None # (!) real value is ''
    ValueOwnership = None # (!) real value is ''


class QScriptEngineAgent(__Shiboken.Object):
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

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    DebuggerInvocationRequest = None # (!) real value is ''
    Extension = None # (!) real value is ''


class QScriptExtensionInterface(__PySide_QtCore.QFactoryInterface):
    # no doc
    def initialize(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class QScriptExtensionPlugin(__PySide_QtCore.QObject, QScriptExtensionInterface):
    # no doc
    def initialize(self, *args, **kwargs): # real signature unknown
        pass

    def keys(self, *args, **kwargs): # real signature unknown
        pass

    def setupPackage(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    staticMetaObject = None # (!) real value is ''


class QScriptString(__Shiboken.Object):
    # no doc
    def isValid(self, *args, **kwargs): # real signature unknown
        pass

    def toArrayIndex(self, *args, **kwargs): # real signature unknown
        pass

    def toString(self, *args, **kwargs): # real signature unknown
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    __hash__ = None


class QScriptValue(__Shiboken.Object):
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

    def objectId(self, *args, **kwargs): # real signature unknown
        pass

    def property(self, *args, **kwargs): # real signature unknown
        pass

    def propertyFlags(self, *args, **kwargs): # real signature unknown
        pass

    def prototype(self, *args, **kwargs): # real signature unknown
        pass

    def scope(self, *args, **kwargs): # real signature unknown
        pass

    def scriptClass(self, *args, **kwargs): # real signature unknown
        pass

    def setData(self, *args, **kwargs): # real signature unknown
        pass

    def setProperty(self, *args, **kwargs): # real signature unknown
        pass

    def setPrototype(self, *args, **kwargs): # real signature unknown
        pass

    def setScope(self, *args, **kwargs): # real signature unknown
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

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    KeepExistingFlags = None # (!) real value is ''
    NullValue = None # (!) real value is ''
    PropertyFlag = None # (!) real value is ''
    PropertyFlags = None # (!) real value is ''
    PropertyGetter = None # (!) real value is ''
    PropertySetter = None # (!) real value is ''
    QObjectMember = None # (!) real value is ''
    ReadOnly = None # (!) real value is ''
    ResolveFlag = None # (!) real value is ''
    ResolveFlags = None # (!) real value is ''
    ResolveFull = None # (!) real value is ''
    ResolveLocal = None # (!) real value is ''
    ResolvePrototype = None # (!) real value is ''
    ResolveScope = None # (!) real value is ''
    SkipInEnumeration = None # (!) real value is ''
    SpecialValue = None # (!) real value is ''
    UndefinedValue = None # (!) real value is ''
    Undeletable = None # (!) real value is ''
    UserRange = None # (!) real value is ''


class QScriptValueIterator(__Shiboken.Object):
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

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __next__(self, *args, **kwargs): # real signature unknown
        """ Implement next(self). """
        pass


# variables with complex values

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

