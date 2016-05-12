# encoding: utf-8
# module PyQt4.QtXmlPatterns
# from /usr/lib64/python2.6/site-packages/PyQt4/QtXmlPatterns.so
# by generator 1.136
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore


# no functions
# classes

class QAbstractMessageHandler(__PyQt4_QtCore.QObject):
    # no doc
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def handleMessage(self, *args, **kwargs): # real signature unknown
        pass

    def message(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class QAbstractUriResolver(__PyQt4_QtCore.QObject):
    # no doc
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def resolve(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class QAbstractXmlNodeModel(): # skipped bases: <type 'sip.simplewrapper'>
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

    def kind(self, *args, **kwargs): # real signature unknown
        pass

    def name(self, *args, **kwargs): # real signature unknown
        pass

    def namespaceBindings(self, *args, **kwargs): # real signature unknown
        pass

    def nextFromSimpleAxis(self, *args, **kwargs): # real signature unknown
        pass

    def nodesByIdref(self, *args, **kwargs): # real signature unknown
        pass

    def root(self, *args, **kwargs): # real signature unknown
        pass

    def stringValue(self, *args, **kwargs): # real signature unknown
        pass

    def typedValue(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    FirstChild = 1
    NextSibling = 3
    Parent = 0
    PreviousSibling = 2


class QAbstractXmlReceiver(): # skipped bases: <type 'sip.simplewrapper'>
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

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QSimpleXmlNodeModel(QAbstractXmlNodeModel):
    # no doc
    def attributes(self, *args, **kwargs): # real signature unknown
        pass

    def baseUri(self, *args, **kwargs): # real signature unknown
        pass

    def createIndex(self, *args, **kwargs): # real signature unknown
        pass

    def elementById(self, *args, **kwargs): # real signature unknown
        pass

    def namePool(self, *args, **kwargs): # real signature unknown
        pass

    def namespaceBindings(self, *args, **kwargs): # real signature unknown
        pass

    def nextFromSimpleAxis(self, *args, **kwargs): # real signature unknown
        pass

    def nodesByIdref(self, *args, **kwargs): # real signature unknown
        pass

    def stringValue(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class QSourceLocation(): # skipped bases: <type 'sip.simplewrapper'>
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

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __hash__(self): # real signature unknown; restored from __doc__
        """ x.__hash__() <==> hash(x) """
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


class QXmlItem(): # skipped bases: <type 'sip.simplewrapper'>
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

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QXmlName(): # skipped bases: <type 'sip.simplewrapper'>
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

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __hash__(self): # real signature unknown; restored from __doc__
        """ x.__hash__() <==> hash(x) """
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



class QXmlNamePool(): # skipped bases: <type 'sip.simplewrapper'>
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QXmlNodeModelIndex(): # skipped bases: <type 'sip.simplewrapper'>
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

    def __eq__(self, y): # real signature unknown; restored from __doc__
        """ x.__eq__(y) <==> x==y """
        pass

    def __ge__(self, y): # real signature unknown; restored from __doc__
        """ x.__ge__(y) <==> x>=y """
        pass

    def __gt__(self, y): # real signature unknown; restored from __doc__
        """ x.__gt__(y) <==> x>y """
        pass

    def __hash__(self): # real signature unknown; restored from __doc__
        """ x.__hash__() <==> hash(x) """
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


    Attribute = 1
    Comment = 2
    Document = 4
    Element = 8
    Follows = 1
    Is = 0
    Namespace = 16
    Precedes = -1
    ProcessingInstruction = 32
    Text = 64


class QXmlQuery(): # skipped bases: <type 'sip.simplewrapper'>
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

    def networkAccessManager(self, *args, **kwargs): # real signature unknown
        pass

    def queryLanguage(self, *args, **kwargs): # real signature unknown
        pass

    def setFocus(self, *args, **kwargs): # real signature unknown
        pass

    def setInitialTemplateName(self, *args, **kwargs): # real signature unknown
        pass

    def setMessageHandler(self, *args, **kwargs): # real signature unknown
        pass

    def setNetworkAccessManager(self, *args, **kwargs): # real signature unknown
        pass

    def setQuery(self, *args, **kwargs): # real signature unknown
        pass

    def setUriResolver(self, *args, **kwargs): # real signature unknown
        pass

    def uriResolver(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    XQuery10 = 1
    XSLT20 = 2


class QXmlResultItems(): # skipped bases: <type 'sip.simplewrapper'>
    # no doc
    def current(self, *args, **kwargs): # real signature unknown
        pass

    def hasError(self, *args, **kwargs): # real signature unknown
        pass

    def next(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



