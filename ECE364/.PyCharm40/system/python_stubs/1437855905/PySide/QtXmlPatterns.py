# encoding: utf-8
# module PySide.QtXmlPatterns
# from /opt/python3/current/lib/python3.4/site-packages/PySide/QtXmlPatterns.so
# by generator 1.136
# no doc

# imports
import PySide.QtCore as __PySide_QtCore
import Shiboken as __Shiboken


# no functions
# classes

class QAbstractMessageHandler(__PySide_QtCore.QObject):
    # no doc
    def handleMessage(self, *args, **kwargs): # real signature unknown
        pass

    def message(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    staticMetaObject = None # (!) real value is ''


class QAbstractUriResolver(__PySide_QtCore.QObject):
    # no doc
    def resolve(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    staticMetaObject = None # (!) real value is ''


class QAbstractXmlNodeModel(__Shiboken.Object):
    # no doc
    def attributes(self, *args, **kwargs): # real signature unknown
        pass

    def baseUri(self, *args, **kwargs): # real signature unknown
        pass

    def compareOrder(self, *args, **kwargs): # real signature unknown
        pass

    def createIndex(self, *args, **kwargs): # real signature unknown
        pass

    def documentUri(self, *args, **kwargs): # real signature unknown
        pass

    def elementById(self, *args, **kwargs): # real signature unknown
        pass

    def isDeepEqual(self, *args, **kwargs): # real signature unknown
        pass

    def kind(self, *args, **kwargs): # real signature unknown
        pass

    def name(self, *args, **kwargs): # real signature unknown
        pass

    def namespaceBindings(self, *args, **kwargs): # real signature unknown
        pass

    def namespaceForPrefix(self, *args, **kwargs): # real signature unknown
        pass

    def nextFromSimpleAxis(self, *args, **kwargs): # real signature unknown
        pass

    def nodesByIdref(self, *args, **kwargs): # real signature unknown
        pass

    def root(self, *args, **kwargs): # real signature unknown
        pass

    def sendNamespaces(self, *args, **kwargs): # real signature unknown
        pass

    def sourceLocation(self, *args, **kwargs): # real signature unknown
        pass

    def stringValue(self, *args, **kwargs): # real signature unknown
        pass

    def typedValue(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    FirstChild = None # (!) real value is ''
    InheritNamespaces = None # (!) real value is ''
    NextSibling = None # (!) real value is ''
    NodeCopySetting = None # (!) real value is ''
    Parent = None # (!) real value is ''
    PreserveNamespaces = None # (!) real value is ''
    PreviousSibling = None # (!) real value is ''
    SimpleAxis = None # (!) real value is ''


class QAbstractXmlReceiver(__Shiboken.Object):
    # no doc
    def atomicValue(self, *args, **kwargs): # real signature unknown
        pass

    def attribute(self, *args, **kwargs): # real signature unknown
        pass

    def characters(self, *args, **kwargs): # real signature unknown
        pass

    def comment(self, *args, **kwargs): # real signature unknown
        pass

    def endDocument(self, *args, **kwargs): # real signature unknown
        pass

    def endElement(self, *args, **kwargs): # real signature unknown
        pass

    def endOfSequence(self, *args, **kwargs): # real signature unknown
        pass

    def namespaceBinding(self, *args, **kwargs): # real signature unknown
        pass

    def processingInstruction(self, *args, **kwargs): # real signature unknown
        pass

    def startDocument(self, *args, **kwargs): # real signature unknown
        pass

    def startElement(self, *args, **kwargs): # real signature unknown
        pass

    def startOfSequence(self, *args, **kwargs): # real signature unknown
        pass

    def whitespaceOnly(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class QSourceLocation(__Shiboken.Object):
    # no doc
    def column(self, *args, **kwargs): # real signature unknown
        pass

    def isNull(self, *args, **kwargs): # real signature unknown
        pass

    def line(self, *args, **kwargs): # real signature unknown
        pass

    def setColumn(self, *args, **kwargs): # real signature unknown
        pass

    def setLine(self, *args, **kwargs): # real signature unknown
        pass

    def setUri(self, *args, **kwargs): # real signature unknown
        pass

    def uri(self, *args, **kwargs): # real signature unknown
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

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    __hash__ = None


class QXmlSerializer(QAbstractXmlReceiver):
    # no doc
    def atomicValue(self, *args, **kwargs): # real signature unknown
        pass

    def attribute(self, *args, **kwargs): # real signature unknown
        pass

    def characters(self, *args, **kwargs): # real signature unknown
        pass

    def codec(self, *args, **kwargs): # real signature unknown
        pass

    def comment(self, *args, **kwargs): # real signature unknown
        pass

    def endDocument(self, *args, **kwargs): # real signature unknown
        pass

    def endElement(self, *args, **kwargs): # real signature unknown
        pass

    def endOfSequence(self, *args, **kwargs): # real signature unknown
        pass

    def namespaceBinding(self, *args, **kwargs): # real signature unknown
        pass

    def outputDevice(self, *args, **kwargs): # real signature unknown
        pass

    def processingInstruction(self, *args, **kwargs): # real signature unknown
        pass

    def setCodec(self, *args, **kwargs): # real signature unknown
        pass

    def startDocument(self, *args, **kwargs): # real signature unknown
        pass

    def startElement(self, *args, **kwargs): # real signature unknown
        pass

    def startOfSequence(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class QXmlFormatter(QXmlSerializer):
    # no doc
    def atomicValue(self, *args, **kwargs): # real signature unknown
        pass

    def attribute(self, *args, **kwargs): # real signature unknown
        pass

    def characters(self, *args, **kwargs): # real signature unknown
        pass

    def comment(self, *args, **kwargs): # real signature unknown
        pass

    def endDocument(self, *args, **kwargs): # real signature unknown
        pass

    def endElement(self, *args, **kwargs): # real signature unknown
        pass

    def endOfSequence(self, *args, **kwargs): # real signature unknown
        pass

    def indentationDepth(self, *args, **kwargs): # real signature unknown
        pass

    def processingInstruction(self, *args, **kwargs): # real signature unknown
        pass

    def setIndentationDepth(self, *args, **kwargs): # real signature unknown
        pass

    def startDocument(self, *args, **kwargs): # real signature unknown
        pass

    def startElement(self, *args, **kwargs): # real signature unknown
        pass

    def startOfSequence(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class QXmlItem(__Shiboken.Object):
    # no doc
    def isAtomicValue(self, *args, **kwargs): # real signature unknown
        pass

    def isNode(self, *args, **kwargs): # real signature unknown
        pass

    def isNull(self, *args, **kwargs): # real signature unknown
        pass

    def toAtomicValue(self, *args, **kwargs): # real signature unknown
        pass

    def toNodeModelIndex(self, *args, **kwargs): # real signature unknown
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class QXmlName(__Shiboken.Object):
    # no doc
    def fromClarkName(self, *args, **kwargs): # real signature unknown
        pass

    def isNCName(self, *args, **kwargs): # real signature unknown
        pass

    def isNull(self, *args, **kwargs): # real signature unknown
        pass

    def localName(self, *args, **kwargs): # real signature unknown
        pass

    def namespaceUri(self, *args, **kwargs): # real signature unknown
        pass

    def prefix(self, *args, **kwargs): # real signature unknown
        pass

    def toClarkName(self, *args, **kwargs): # real signature unknown
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


class QXmlNamePool(__Shiboken.Object):
    # no doc
    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class QXmlNodeModelIndex(__Shiboken.Object):
    # no doc
    def additionalData(self, *args, **kwargs): # real signature unknown
        pass

    def data(self, *args, **kwargs): # real signature unknown
        pass

    def internalPointer(self, *args, **kwargs): # real signature unknown
        pass

    def isNull(self, *args, **kwargs): # real signature unknown
        pass

    def model(self, *args, **kwargs): # real signature unknown
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

    Attribute = None # (!) real value is ''
    Comment = None # (!) real value is ''
    Document = None # (!) real value is ''
    DocumentOrder = None # (!) real value is ''
    Element = None # (!) real value is ''
    Follows = None # (!) real value is ''
    Is = None # (!) real value is ''
    Namespace = None # (!) real value is ''
    NodeKind = None # (!) real value is ''
    Precedes = None # (!) real value is ''
    ProcessingInstruction = None # (!) real value is ''
    Text = None # (!) real value is ''
    __hash__ = None


class QXmlQuery(__Shiboken.Object):
    # no doc
    def bindVariable(self, *args, **kwargs): # real signature unknown
        pass

    def evaluateTo(self, *args, **kwargs): # real signature unknown
        pass

    def initialTemplateName(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        pass

    def messageHandler(self, *args, **kwargs): # real signature unknown
        pass

    def namePool(self, *args, **kwargs): # real signature unknown
        pass

    def queryLanguage(self, *args, **kwargs): # real signature unknown
        pass

    def setFocus(self, *args, **kwargs): # real signature unknown
        pass

    def setInitialTemplateName(self, *args, **kwargs): # real signature unknown
        pass

    def setMessageHandler(self, *args, **kwargs): # real signature unknown
        pass

    def setQuery(self, *args, **kwargs): # real signature unknown
        pass

    def setUriResolver(self, *args, **kwargs): # real signature unknown
        pass

    def uriResolver(self, *args, **kwargs): # real signature unknown
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    QueryLanguage = None # (!) real value is ''
    XmlSchema11IdentityConstraintField = None # (!) real value is ''
    XmlSchema11IdentityConstraintSelector = None # (!) real value is ''
    XPath20 = None # (!) real value is ''
    XQuery10 = None # (!) real value is ''
    XSLT20 = None # (!) real value is ''


class QXmlResultItems(__Shiboken.Object):
    # no doc
    def current(self, *args, **kwargs): # real signature unknown
        pass

    def hasError(self, *args, **kwargs): # real signature unknown
        pass

    def next(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class QXmlSchema(__Shiboken.Object):
    # no doc
    def documentUri(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        pass

    def load(self, *args, **kwargs): # real signature unknown
        pass

    def messageHandler(self, *args, **kwargs): # real signature unknown
        pass

    def namePool(self, *args, **kwargs): # real signature unknown
        pass

    def setMessageHandler(self, *args, **kwargs): # real signature unknown
        pass

    def setUriResolver(self, *args, **kwargs): # real signature unknown
        pass

    def uriResolver(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class QXmlSchemaValidator(__Shiboken.Object):
    # no doc
    def messageHandler(self, *args, **kwargs): # real signature unknown
        pass

    def namePool(self, *args, **kwargs): # real signature unknown
        pass

    def schema(self, *args, **kwargs): # real signature unknown
        pass

    def setMessageHandler(self, *args, **kwargs): # real signature unknown
        pass

    def setSchema(self, *args, **kwargs): # real signature unknown
        pass

    def setUriResolver(self, *args, **kwargs): # real signature unknown
        pass

    def uriResolver(self, *args, **kwargs): # real signature unknown
        pass

    def validate(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


# variables with complex values

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

