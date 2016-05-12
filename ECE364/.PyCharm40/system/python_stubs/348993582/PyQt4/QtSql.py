# encoding: utf-8
# module PyQt4.QtSql
# from /usr/lib64/python2.6/site-packages/PyQt4/QtSql.so
# by generator 1.136
# no doc

# imports
import PyQt4.QtCore as __PyQt4_QtCore
import PyQt4.QtGui as __PyQt4_QtGui


# no functions
# classes

class QSql(): # skipped bases: <type 'sip.wrapper'>
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    AfterLastRow = -2
    AllTables = 255
    BeforeFirstRow = -1
    Binary = 4
    HighPrecision = 0
    In = 1
    InOut = 3
    LowPrecisionDouble = 4
    LowPrecisionInt32 = 1
    LowPrecisionInt64 = 2
    Out = 2
    SystemTables = 2
    Tables = 1
    Views = 4


class QSqlDatabase(): # skipped bases: <type 'sip.simplewrapper'>
    # no doc
    def addDatabase(self, *args, **kwargs): # real signature unknown
        pass

    def cloneDatabase(self, *args, **kwargs): # real signature unknown
        pass

    def close(self, *args, **kwargs): # real signature unknown
        pass

    def commit(self, *args, **kwargs): # real signature unknown
        pass

    def connectionName(self, *args, **kwargs): # real signature unknown
        pass

    def connectionNames(self, *args, **kwargs): # real signature unknown
        pass

    def connectOptions(self, *args, **kwargs): # real signature unknown
        pass

    def contains(self, *args, **kwargs): # real signature unknown
        pass

    def database(self, *args, **kwargs): # real signature unknown
        pass

    def databaseName(self, *args, **kwargs): # real signature unknown
        pass

    def driver(self, *args, **kwargs): # real signature unknown
        pass

    def driverName(self, *args, **kwargs): # real signature unknown
        pass

    def drivers(self, *args, **kwargs): # real signature unknown
        pass

    def exec_(self, *args, **kwargs): # real signature unknown
        pass

    def hostName(self, *args, **kwargs): # real signature unknown
        pass

    def isDriverAvailable(self, *args, **kwargs): # real signature unknown
        pass

    def isOpen(self, *args, **kwargs): # real signature unknown
        pass

    def isOpenError(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        pass

    def lastError(self, *args, **kwargs): # real signature unknown
        pass

    def open(self, *args, **kwargs): # real signature unknown
        pass

    def password(self, *args, **kwargs): # real signature unknown
        pass

    def port(self, *args, **kwargs): # real signature unknown
        pass

    def primaryIndex(self, *args, **kwargs): # real signature unknown
        pass

    def record(self, *args, **kwargs): # real signature unknown
        pass

    def registerSqlDriver(self, *args, **kwargs): # real signature unknown
        pass

    def removeDatabase(self, *args, **kwargs): # real signature unknown
        pass

    def rollback(self, *args, **kwargs): # real signature unknown
        pass

    def setConnectOptions(self, *args, **kwargs): # real signature unknown
        pass

    def setDatabaseName(self, *args, **kwargs): # real signature unknown
        pass

    def setHostName(self, *args, **kwargs): # real signature unknown
        pass

    def setPassword(self, *args, **kwargs): # real signature unknown
        pass

    def setPort(self, *args, **kwargs): # real signature unknown
        pass

    def setUserName(self, *args, **kwargs): # real signature unknown
        pass

    def tables(self, *args, **kwargs): # real signature unknown
        pass

    def transaction(self, *args, **kwargs): # real signature unknown
        pass

    def userName(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QSqlDriver(__PyQt4_QtCore.QObject):
    # no doc
    def beginTransaction(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def close(self, *args, **kwargs): # real signature unknown
        pass

    def commitTransaction(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def createResult(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def escapeIdentifier(self, *args, **kwargs): # real signature unknown
        pass

    def formatValue(self, *args, **kwargs): # real signature unknown
        pass

    def handle(self, *args, **kwargs): # real signature unknown
        pass

    def hasFeature(self, *args, **kwargs): # real signature unknown
        pass

    def isOpen(self, *args, **kwargs): # real signature unknown
        pass

    def isOpenError(self, *args, **kwargs): # real signature unknown
        pass

    def lastError(self, *args, **kwargs): # real signature unknown
        pass

    def notification(self, *args, **kwargs): # real signature unknown
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

    def open(self, *args, **kwargs): # real signature unknown
        pass

    def primaryIndex(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def record(self, *args, **kwargs): # real signature unknown
        pass

    def rollbackTransaction(self, *args, **kwargs): # real signature unknown
        pass

    def setLastError(self, *args, **kwargs): # real signature unknown
        pass

    def setOpen(self, *args, **kwargs): # real signature unknown
        pass

    def setOpenError(self, *args, **kwargs): # real signature unknown
        pass

    def sqlStatement(self, *args, **kwargs): # real signature unknown
        pass

    def subscribedToNotifications(self, *args, **kwargs): # real signature unknown
        pass

    def subscribedToNotificationsImplementation(self, *args, **kwargs): # real signature unknown
        pass

    def subscribeToNotification(self, *args, **kwargs): # real signature unknown
        pass

    def subscribeToNotificationImplementation(self, *args, **kwargs): # real signature unknown
        pass

    def tables(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def unsubscribeFromNotification(self, *args, **kwargs): # real signature unknown
        pass

    def unsubscribeFromNotificationImplementation(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    BatchOperations = 8
    BLOB = 2
    DeleteStatement = 4
    EventNotifications = 11
    FieldName = 0
    FinishQuery = 12
    InsertStatement = 3
    LastInsertId = 7
    LowPrecisionNumbers = 10
    MultipleResultSets = 13
    NamedPlaceholders = 5
    PositionalPlaceholders = 6
    PreparedQueries = 4
    QuerySize = 1
    SelectStatement = 1
    SimpleLocking = 9
    TableName = 1
    Transactions = 0
    Unicode = 3
    UpdateStatement = 2
    WhereStatement = 0


class QSqlDriverCreatorBase(): # skipped bases: <type 'sip.wrapper'>
    # no doc
    def createObject(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QSqlError(): # skipped bases: <type 'sip.simplewrapper'>
    # no doc
    def databaseText(self, *args, **kwargs): # real signature unknown
        pass

    def driverText(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        pass

    def number(self, *args, **kwargs): # real signature unknown
        pass

    def setDatabaseText(self, *args, **kwargs): # real signature unknown
        pass

    def setDriverText(self, *args, **kwargs): # real signature unknown
        pass

    def setNumber(self, *args, **kwargs): # real signature unknown
        pass

    def setType(self, *args, **kwargs): # real signature unknown
        pass

    def text(self, *args, **kwargs): # real signature unknown
        pass

    def type(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    ConnectionError = 1
    NoError = 0
    StatementError = 2
    TransactionError = 3
    UnknownError = 4


class QSqlField(): # skipped bases: <type 'sip.simplewrapper'>
    # no doc
    def clear(self, *args, **kwargs): # real signature unknown
        pass

    def defaultValue(self, *args, **kwargs): # real signature unknown
        pass

    def isAutoValue(self, *args, **kwargs): # real signature unknown
        pass

    def isGenerated(self, *args, **kwargs): # real signature unknown
        pass

    def isNull(self, *args, **kwargs): # real signature unknown
        pass

    def isReadOnly(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        pass

    def length(self, *args, **kwargs): # real signature unknown
        pass

    def name(self, *args, **kwargs): # real signature unknown
        pass

    def precision(self, *args, **kwargs): # real signature unknown
        pass

    def requiredStatus(self, *args, **kwargs): # real signature unknown
        pass

    def setAutoValue(self, *args, **kwargs): # real signature unknown
        pass

    def setDefaultValue(self, *args, **kwargs): # real signature unknown
        pass

    def setGenerated(self, *args, **kwargs): # real signature unknown
        pass

    def setLength(self, *args, **kwargs): # real signature unknown
        pass

    def setName(self, *args, **kwargs): # real signature unknown
        pass

    def setPrecision(self, *args, **kwargs): # real signature unknown
        pass

    def setReadOnly(self, *args, **kwargs): # real signature unknown
        pass

    def setRequired(self, *args, **kwargs): # real signature unknown
        pass

    def setRequiredStatus(self, *args, **kwargs): # real signature unknown
        pass

    def setSqlType(self, *args, **kwargs): # real signature unknown
        pass

    def setType(self, *args, **kwargs): # real signature unknown
        pass

    def setValue(self, *args, **kwargs): # real signature unknown
        pass

    def type(self, *args, **kwargs): # real signature unknown
        pass

    def typeID(self, *args, **kwargs): # real signature unknown
        pass

    def value(self, *args, **kwargs): # real signature unknown
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


    Optional = 0
    Required = 1
    Unknown = -1


class QSqlRecord(): # skipped bases: <type 'sip.simplewrapper'>
    # no doc
    def append(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self, *args, **kwargs): # real signature unknown
        pass

    def clearValues(self, *args, **kwargs): # real signature unknown
        pass

    def contains(self, *args, **kwargs): # real signature unknown
        pass

    def count(self, *args, **kwargs): # real signature unknown
        pass

    def field(self, *args, **kwargs): # real signature unknown
        pass

    def fieldName(self, *args, **kwargs): # real signature unknown
        pass

    def indexOf(self, *args, **kwargs): # real signature unknown
        pass

    def insert(self, *args, **kwargs): # real signature unknown
        pass

    def isEmpty(self, *args, **kwargs): # real signature unknown
        pass

    def isGenerated(self, *args, **kwargs): # real signature unknown
        pass

    def isNull(self, *args, **kwargs): # real signature unknown
        pass

    def remove(self, *args, **kwargs): # real signature unknown
        pass

    def replace(self, *args, **kwargs): # real signature unknown
        pass

    def setGenerated(self, *args, **kwargs): # real signature unknown
        pass

    def setNull(self, *args, **kwargs): # real signature unknown
        pass

    def setValue(self, *args, **kwargs): # real signature unknown
        pass

    def value(self, *args, **kwargs): # real signature unknown
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



class QSqlIndex(QSqlRecord):
    # no doc
    def append(self, *args, **kwargs): # real signature unknown
        pass

    def cursorName(self, *args, **kwargs): # real signature unknown
        pass

    def isDescending(self, *args, **kwargs): # real signature unknown
        pass

    def name(self, *args, **kwargs): # real signature unknown
        pass

    def setCursorName(self, *args, **kwargs): # real signature unknown
        pass

    def setDescending(self, *args, **kwargs): # real signature unknown
        pass

    def setName(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class QSqlQuery(): # skipped bases: <type 'sip.simplewrapper'>
    # no doc
    def addBindValue(self, *args, **kwargs): # real signature unknown
        pass

    def at(self, *args, **kwargs): # real signature unknown
        pass

    def bindValue(self, *args, **kwargs): # real signature unknown
        pass

    def boundValue(self, *args, **kwargs): # real signature unknown
        pass

    def boundValues(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self, *args, **kwargs): # real signature unknown
        pass

    def driver(self, *args, **kwargs): # real signature unknown
        pass

    def execBatch(self, *args, **kwargs): # real signature unknown
        pass

    def executedQuery(self, *args, **kwargs): # real signature unknown
        pass

    def exec_(self, *args, **kwargs): # real signature unknown
        pass

    def finish(self, *args, **kwargs): # real signature unknown
        pass

    def first(self, *args, **kwargs): # real signature unknown
        pass

    def isActive(self, *args, **kwargs): # real signature unknown
        pass

    def isForwardOnly(self, *args, **kwargs): # real signature unknown
        pass

    def isNull(self, *args, **kwargs): # real signature unknown
        pass

    def isSelect(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        pass

    def last(self, *args, **kwargs): # real signature unknown
        pass

    def lastError(self, *args, **kwargs): # real signature unknown
        pass

    def lastInsertId(self, *args, **kwargs): # real signature unknown
        pass

    def lastQuery(self, *args, **kwargs): # real signature unknown
        pass

    def next(self, *args, **kwargs): # real signature unknown
        pass

    def nextResult(self, *args, **kwargs): # real signature unknown
        pass

    def numericalPrecisionPolicy(self, *args, **kwargs): # real signature unknown
        pass

    def numRowsAffected(self, *args, **kwargs): # real signature unknown
        pass

    def prepare(self, *args, **kwargs): # real signature unknown
        pass

    def previous(self, *args, **kwargs): # real signature unknown
        pass

    def record(self, *args, **kwargs): # real signature unknown
        pass

    def result(self, *args, **kwargs): # real signature unknown
        pass

    def seek(self, *args, **kwargs): # real signature unknown
        pass

    def setForwardOnly(self, *args, **kwargs): # real signature unknown
        pass

    def setNumericalPrecisionPolicy(self, *args, **kwargs): # real signature unknown
        pass

    def size(self, *args, **kwargs): # real signature unknown
        pass

    def value(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    ValuesAsColumns = 1
    ValuesAsRows = 0


class QSqlQueryModel(__PyQt4_QtCore.QAbstractTableModel):
    # no doc
    def beginInsertColumns(self, *args, **kwargs): # real signature unknown
        pass

    def beginInsertRows(self, *args, **kwargs): # real signature unknown
        pass

    def beginRemoveColumns(self, *args, **kwargs): # real signature unknown
        pass

    def beginRemoveRows(self, *args, **kwargs): # real signature unknown
        pass

    def canFetchMore(self, *args, **kwargs): # real signature unknown
        pass

    def changePersistentIndex(self, *args, **kwargs): # real signature unknown
        pass

    def changePersistentIndexList(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self, *args, **kwargs): # real signature unknown
        pass

    def columnCount(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def createIndex(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def data(self, *args, **kwargs): # real signature unknown
        pass

    def decodeData(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def encodeData(self, *args, **kwargs): # real signature unknown
        pass

    def endInsertColumns(self, *args, **kwargs): # real signature unknown
        pass

    def endInsertRows(self, *args, **kwargs): # real signature unknown
        pass

    def endRemoveColumns(self, *args, **kwargs): # real signature unknown
        pass

    def endRemoveRows(self, *args, **kwargs): # real signature unknown
        pass

    def fetchMore(self, *args, **kwargs): # real signature unknown
        pass

    def headerData(self, *args, **kwargs): # real signature unknown
        pass

    def indexInQuery(self, *args, **kwargs): # real signature unknown
        pass

    def insertColumns(self, *args, **kwargs): # real signature unknown
        pass

    def lastError(self, *args, **kwargs): # real signature unknown
        pass

    def persistentIndexList(self, *args, **kwargs): # real signature unknown
        pass

    def query(self, *args, **kwargs): # real signature unknown
        pass

    def queryChange(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def record(self, *args, **kwargs): # real signature unknown
        pass

    def removeColumns(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self, *args, **kwargs): # real signature unknown
        pass

    def rowCount(self, *args, **kwargs): # real signature unknown
        pass

    def setHeaderData(self, *args, **kwargs): # real signature unknown
        pass

    def setLastError(self, *args, **kwargs): # real signature unknown
        pass

    def setQuery(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class QSqlRelation(): # skipped bases: <type 'sip.simplewrapper'>
    # no doc
    def displayColumn(self, *args, **kwargs): # real signature unknown
        pass

    def indexColumn(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        pass

    def tableName(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class QSqlRelationalDelegate(__PyQt4_QtGui.QItemDelegate):
    # no doc
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def createEditor(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def drawBackground(self, *args, **kwargs): # real signature unknown
        pass

    def drawCheck(self, *args, **kwargs): # real signature unknown
        pass

    def drawDecoration(self, *args, **kwargs): # real signature unknown
        pass

    def drawDisplay(self, *args, **kwargs): # real signature unknown
        pass

    def drawFocus(self, *args, **kwargs): # real signature unknown
        pass

    def editorEvent(self, *args, **kwargs): # real signature unknown
        pass

    def eventFilter(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def setEditorData(self, *args, **kwargs): # real signature unknown
        pass

    def setModelData(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class QSqlTableModel(QSqlQueryModel):
    # no doc
    def beforeDelete(self, *args, **kwargs): # real signature unknown
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

    def beforeInsert(self, *args, **kwargs): # real signature unknown
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

    def beforeUpdate(self, *args, **kwargs): # real signature unknown
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

    def beginInsertColumns(self, *args, **kwargs): # real signature unknown
        pass

    def beginInsertRows(self, *args, **kwargs): # real signature unknown
        pass

    def beginRemoveColumns(self, *args, **kwargs): # real signature unknown
        pass

    def beginRemoveRows(self, *args, **kwargs): # real signature unknown
        pass

    def changePersistentIndex(self, *args, **kwargs): # real signature unknown
        pass

    def changePersistentIndexList(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def createIndex(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def data(self, *args, **kwargs): # real signature unknown
        pass

    def database(self, *args, **kwargs): # real signature unknown
        pass

    def decodeData(self, *args, **kwargs): # real signature unknown
        pass

    def deleteRowFromTable(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def editStrategy(self, *args, **kwargs): # real signature unknown
        pass

    def encodeData(self, *args, **kwargs): # real signature unknown
        pass

    def endInsertColumns(self, *args, **kwargs): # real signature unknown
        pass

    def endInsertRows(self, *args, **kwargs): # real signature unknown
        pass

    def endRemoveColumns(self, *args, **kwargs): # real signature unknown
        pass

    def endRemoveRows(self, *args, **kwargs): # real signature unknown
        pass

    def fieldIndex(self, *args, **kwargs): # real signature unknown
        pass

    def filter(self, *args, **kwargs): # real signature unknown
        pass

    def flags(self, *args, **kwargs): # real signature unknown
        pass

    def headerData(self, *args, **kwargs): # real signature unknown
        pass

    def indexInQuery(self, *args, **kwargs): # real signature unknown
        pass

    def insertRecord(self, *args, **kwargs): # real signature unknown
        pass

    def insertRowIntoTable(self, *args, **kwargs): # real signature unknown
        pass

    def insertRows(self, *args, **kwargs): # real signature unknown
        pass

    def isDirty(self, *args, **kwargs): # real signature unknown
        pass

    def orderByClause(self, *args, **kwargs): # real signature unknown
        pass

    def persistentIndexList(self, *args, **kwargs): # real signature unknown
        pass

    def primaryKey(self, *args, **kwargs): # real signature unknown
        pass

    def primeInsert(self, *args, **kwargs): # real signature unknown
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

    def queryChange(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def removeColumns(self, *args, **kwargs): # real signature unknown
        pass

    def removeRows(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self, *args, **kwargs): # real signature unknown
        pass

    def revert(self, *args, **kwargs): # real signature unknown
        pass

    def revertAll(self, *args, **kwargs): # real signature unknown
        pass

    def revertRow(self, *args, **kwargs): # real signature unknown
        pass

    def rowCount(self, *args, **kwargs): # real signature unknown
        pass

    def select(self, *args, **kwargs): # real signature unknown
        pass

    def selectStatement(self, *args, **kwargs): # real signature unknown
        pass

    def setData(self, *args, **kwargs): # real signature unknown
        pass

    def setEditStrategy(self, *args, **kwargs): # real signature unknown
        pass

    def setFilter(self, *args, **kwargs): # real signature unknown
        pass

    def setLastError(self, *args, **kwargs): # real signature unknown
        pass

    def setPrimaryKey(self, *args, **kwargs): # real signature unknown
        pass

    def setQuery(self, *args, **kwargs): # real signature unknown
        pass

    def setRecord(self, *args, **kwargs): # real signature unknown
        pass

    def setSort(self, *args, **kwargs): # real signature unknown
        pass

    def setTable(self, *args, **kwargs): # real signature unknown
        pass

    def sort(self, *args, **kwargs): # real signature unknown
        pass

    def submit(self, *args, **kwargs): # real signature unknown
        pass

    def submitAll(self, *args, **kwargs): # real signature unknown
        pass

    def tableName(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateRowInTable(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    OnFieldChange = 0
    OnManualSubmit = 2
    OnRowChange = 1


class QSqlRelationalTableModel(QSqlTableModel):
    # no doc
    def beginInsertColumns(self, *args, **kwargs): # real signature unknown
        pass

    def beginInsertRows(self, *args, **kwargs): # real signature unknown
        pass

    def beginRemoveColumns(self, *args, **kwargs): # real signature unknown
        pass

    def beginRemoveRows(self, *args, **kwargs): # real signature unknown
        pass

    def changePersistentIndex(self, *args, **kwargs): # real signature unknown
        pass

    def changePersistentIndexList(self, *args, **kwargs): # real signature unknown
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def createIndex(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def data(self, *args, **kwargs): # real signature unknown
        pass

    def decodeData(self, *args, **kwargs): # real signature unknown
        pass

    def deleteRowFromTable(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def encodeData(self, *args, **kwargs): # real signature unknown
        pass

    def endInsertColumns(self, *args, **kwargs): # real signature unknown
        pass

    def endInsertRows(self, *args, **kwargs): # real signature unknown
        pass

    def endRemoveColumns(self, *args, **kwargs): # real signature unknown
        pass

    def endRemoveRows(self, *args, **kwargs): # real signature unknown
        pass

    def indexInQuery(self, *args, **kwargs): # real signature unknown
        pass

    def insertRowIntoTable(self, *args, **kwargs): # real signature unknown
        pass

    def orderByClause(self, *args, **kwargs): # real signature unknown
        pass

    def persistentIndexList(self, *args, **kwargs): # real signature unknown
        pass

    def queryChange(self, *args, **kwargs): # real signature unknown
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def relation(self, *args, **kwargs): # real signature unknown
        pass

    def relationModel(self, *args, **kwargs): # real signature unknown
        pass

    def removeColumns(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self, *args, **kwargs): # real signature unknown
        pass

    def revertRow(self, *args, **kwargs): # real signature unknown
        pass

    def select(self, *args, **kwargs): # real signature unknown
        pass

    def selectStatement(self, *args, **kwargs): # real signature unknown
        pass

    def setData(self, *args, **kwargs): # real signature unknown
        pass

    def setLastError(self, *args, **kwargs): # real signature unknown
        pass

    def setPrimaryKey(self, *args, **kwargs): # real signature unknown
        pass

    def setQuery(self, *args, **kwargs): # real signature unknown
        pass

    def setRelation(self, *args, **kwargs): # real signature unknown
        pass

    def setTable(self, *args, **kwargs): # real signature unknown
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def updateRowInTable(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class QSqlResult(): # skipped bases: <type 'sip.wrapper'>
    # no doc
    def addBindValue(self, *args, **kwargs): # real signature unknown
        pass

    def at(self, *args, **kwargs): # real signature unknown
        pass

    def bindingSyntax(self, *args, **kwargs): # real signature unknown
        pass

    def bindValue(self, *args, **kwargs): # real signature unknown
        pass

    def bindValueType(self, *args, **kwargs): # real signature unknown
        pass

    def boundValue(self, *args, **kwargs): # real signature unknown
        pass

    def boundValueCount(self, *args, **kwargs): # real signature unknown
        pass

    def boundValueName(self, *args, **kwargs): # real signature unknown
        pass

    def boundValues(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self, *args, **kwargs): # real signature unknown
        pass

    def data(self, *args, **kwargs): # real signature unknown
        pass

    def driver(self, *args, **kwargs): # real signature unknown
        pass

    def executedQuery(self, *args, **kwargs): # real signature unknown
        pass

    def exec_(self, *args, **kwargs): # real signature unknown
        pass

    def fetch(self, *args, **kwargs): # real signature unknown
        pass

    def fetchFirst(self, *args, **kwargs): # real signature unknown
        pass

    def fetchLast(self, *args, **kwargs): # real signature unknown
        pass

    def fetchNext(self, *args, **kwargs): # real signature unknown
        pass

    def fetchPrevious(self, *args, **kwargs): # real signature unknown
        pass

    def handle(self, *args, **kwargs): # real signature unknown
        pass

    def hasOutValues(self, *args, **kwargs): # real signature unknown
        pass

    def isActive(self, *args, **kwargs): # real signature unknown
        pass

    def isForwardOnly(self, *args, **kwargs): # real signature unknown
        pass

    def isNull(self, *args, **kwargs): # real signature unknown
        pass

    def isSelect(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        pass

    def lastError(self, *args, **kwargs): # real signature unknown
        pass

    def lastInsertId(self, *args, **kwargs): # real signature unknown
        pass

    def lastQuery(self, *args, **kwargs): # real signature unknown
        pass

    def numRowsAffected(self, *args, **kwargs): # real signature unknown
        pass

    def prepare(self, *args, **kwargs): # real signature unknown
        pass

    def record(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self, *args, **kwargs): # real signature unknown
        pass

    def savePrepare(self, *args, **kwargs): # real signature unknown
        pass

    def setActive(self, *args, **kwargs): # real signature unknown
        pass

    def setAt(self, *args, **kwargs): # real signature unknown
        pass

    def setForwardOnly(self, *args, **kwargs): # real signature unknown
        pass

    def setLastError(self, *args, **kwargs): # real signature unknown
        pass

    def setQuery(self, *args, **kwargs): # real signature unknown
        pass

    def setSelect(self, *args, **kwargs): # real signature unknown
        pass

    def size(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    NamedBinding = 1
    PositionalBinding = 0


