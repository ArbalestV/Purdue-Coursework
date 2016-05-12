# encoding: utf-8
# module PyQt4.Qt
# from /usr/lib64/python2.6/site-packages/PyQt4/Qt.so
# by generator 1.136
# no doc

# imports
from PyQt4.phonon import Phonon

from PyQt4.QtAssistant import QAssistantClient

from PyQt4.QtCore import (QAbstractEventDispatcher, QAbstractFileEngine, 
    QAbstractFileEngineHandler, QAbstractFileEngineIterator, 
    QAbstractItemModel, QAbstractListModel, QAbstractTableModel, QBasicTimer, 
    QBitArray, QBuffer, QByteArray, QByteArrayMatcher, QChar, QChildEvent, 
    QCoreApplication, QCryptographicHash, QDataStream, QDate, QDateTime, QDir, 
    QDirIterator, QDynamicPropertyChangeEvent, QEvent, QEventLoop, 
    QFSFileEngine, QFile, QFileInfo, QFileSystemWatcher, QGenericArgument, 
    QGenericReturnArgument, QIODevice, QLatin1Char, QLatin1String, QLibrary, 
    QLibraryInfo, QLine, QLineF, QLocale, QMetaClassInfo, QMetaEnum, 
    QMetaMethod, QMetaObject, QMetaProperty, QMetaType, QMimeData, 
    QModelIndex, QMutex, QMutexLocker, QObject, QObjectCleanupHandler, 
    QPersistentModelIndex, QPluginLoader, QPoint, QPointF, QProcess, 
    QReadLocker, QReadWriteLock, QRect, QRectF, QRegExp, QResource, QRunnable, 
    QSemaphore, QSettings, QSharedMemory, QSignalMapper, QSize, QSizeF, 
    QSocketNotifier, QString, QStringList, QStringMatcher, QStringRef, 
    QSysInfo, QSystemLocale, QSystemSemaphore, QT_TRANSLATE_NOOP, QT_TR_NOOP, 
    QT_TR_NOOP_UTF8, QTemporaryFile, QTextBoundaryFinder, QTextCodec, 
    QTextDecoder, QTextEncoder, QTextStream, QTextStreamManipulator, QThread, 
    QThreadPool, QTime, QTimeLine, QTimer, QTimerEvent, QTranslator, QUrl, 
    QUuid, QVariant, QWaitCondition, QWriteLocker, QXmlStreamAttribute, 
    QXmlStreamAttributes, QXmlStreamEntityDeclaration, 
    QXmlStreamEntityResolver, QXmlStreamNamespaceDeclaration, 
    QXmlStreamNotationDeclaration, QXmlStreamReader, QXmlStreamWriter, Q_ARG, 
    Q_ENUMS, Q_FLAGS, Q_RETURN_ARG, Qt, QtCriticalMsg, QtDebugMsg, QtFatalMsg, 
    QtMsgType, QtSystemMsg, QtWarningMsg, SIGNAL, SLOT, bom, center, dec, 
    endl, fixed, flush, forcepoint, forcesign, left, lowercasebase, 
    lowercasedigits, noforcepoint, noforcesign, noshowbase, pyqtProperty, 
    pyqtRemoveInputHook, pyqtRestoreInputHook, pyqtSignal, pyqtSignature, 
    pyqtSlot, pyqtWrapperType, qAbs, qAddPostRoutine, qChecksum, qCompress, 
    qCritical, qDebug, qErrnoWarning, qFatal, qFuzzyCompare, qInf, 
    qInstallMsgHandler, qIsFinite, qIsInf, qIsNaN, qIsNull, qQNaN, 
    qRegisterResourceData, qRemovePostRoutine, qRound, qRound64, qSNaN, 
    qSetFieldWidth, qSetPadChar, qSetRealNumberPrecision, qSharedBuild, qSwap, 
    qUncompress, qUnregisterResourceData, qVersion, qWarning, qrand, qsrand, 
    reset, right, scientific, showbase, uppercasebase, uppercasedigits, ws)

from PyQt4.QtDesigner import (QAbstractExtensionFactory, 
    QAbstractExtensionManager, QAbstractFormBuilder, 
    QDesignerActionEditorInterface, QDesignerContainerExtension, 
    QDesignerCustomWidgetCollectionInterface, QDesignerCustomWidgetInterface, 
    QDesignerFormEditorInterface, QDesignerFormWindowCursorInterface, 
    QDesignerFormWindowInterface, QDesignerFormWindowManagerInterface, 
    QDesignerMemberSheetExtension, QDesignerObjectInspectorInterface, 
    QDesignerPropertyEditorInterface, QDesignerPropertySheetExtension, 
    QDesignerTaskMenuExtension, QDesignerWidgetBoxInterface, 
    QExtensionFactory, QExtensionManager, QFormBuilder, 
    QPyDesignerContainerExtension, QPyDesignerCustomWidgetCollectionPlugin, 
    QPyDesignerCustomWidgetPlugin, QPyDesignerMemberSheetExtension, 
    QPyDesignerPropertySheetExtension, QPyDesignerTaskMenuExtension)

from PyQt4.QtGui import (Display, QAbstractButton, QAbstractGraphicsShapeItem, 
    QAbstractItemDelegate, QAbstractItemView, QAbstractPrintDialog, 
    QAbstractProxyModel, QAbstractScrollArea, QAbstractSlider, 
    QAbstractSpinBox, QAbstractTextDocumentLayout, QAction, QActionEvent, 
    QActionGroup, QApplication, QBitmap, QBoxLayout, QBrush, QButtonGroup, 
    QCalendarWidget, QCheckBox, QClipboard, QCloseEvent, QColor, QColorDialog, 
    QColumnView, QComboBox, QCommandLinkButton, QCompleter, QConicalGradient, 
    QContextMenuEvent, QCursor, QDataWidgetMapper, QDateEdit, QDateTimeEdit, 
    QDesktopServices, QDesktopWidget, QDial, QDialog, QDialogButtonBox, 
    QDirModel, QDockWidget, QDoubleSpinBox, QDoubleValidator, QDrag, 
    QDragEnterEvent, QDragLeaveEvent, QDragMoveEvent, QDropEvent, 
    QErrorMessage, QFileDialog, QFileIconProvider, QFileOpenEvent, 
    QFileSystemModel, QFocusEvent, QFocusFrame, QFont, QFontComboBox, 
    QFontDatabase, QFontDialog, QFontInfo, QFontMetrics, QFontMetricsF, 
    QFormLayout, QFrame, QGradient, QGraphicsEllipseItem, QGraphicsGridLayout, 
    QGraphicsItem, QGraphicsItemAnimation, QGraphicsItemGroup, 
    QGraphicsLayout, QGraphicsLayoutItem, QGraphicsLineItem, 
    QGraphicsLinearLayout, QGraphicsPathItem, QGraphicsPixmapItem, 
    QGraphicsPolygonItem, QGraphicsProxyWidget, QGraphicsRectItem, 
    QGraphicsScene, QGraphicsSceneContextMenuEvent, 
    QGraphicsSceneDragDropEvent, QGraphicsSceneEvent, QGraphicsSceneHelpEvent, 
    QGraphicsSceneHoverEvent, QGraphicsSceneMouseEvent, 
    QGraphicsSceneMoveEvent, QGraphicsSceneResizeEvent, 
    QGraphicsSceneWheelEvent, QGraphicsSimpleTextItem, QGraphicsTextItem, 
    QGraphicsView, QGraphicsWidget, QGridLayout, QGroupBox, QHBoxLayout, 
    QHeaderView, QHelpEvent, QHideEvent, QHoverEvent, QIcon, QIconDragEvent, 
    QIconEngine, QIconEngineV2, QImage, QImageIOHandler, QImageReader, 
    QImageWriter, QInputContext, QInputContextFactory, QInputDialog, 
    QInputEvent, QInputMethodEvent, QIntValidator, QItemDelegate, 
    QItemEditorCreatorBase, QItemEditorFactory, QItemSelection, 
    QItemSelectionModel, QItemSelectionRange, QKeyEvent, QKeySequence, 
    QLCDNumber, QLabel, QLayout, QLayoutItem, QLineEdit, QLinearGradient, 
    QListView, QListWidget, QListWidgetItem, QMainWindow, QMatrix, QMdiArea, 
    QMdiSubWindow, QMenu, QMenuBar, QMessageBox, QMimeSource, QMouseEvent, 
    QMoveEvent, QMovie, QPageSetupDialog, QPaintDevice, QPaintEngine, 
    QPaintEngineState, QPaintEvent, QPainter, QPainterPath, 
    QPainterPathStroker, QPalette, QPen, QPicture, QPictureIO, QPixmap, 
    QPixmapCache, QPlainTextDocumentLayout, QPlainTextEdit, QPolygon, 
    QPolygonF, QPrintDialog, QPrintEngine, QPrintPreviewDialog, 
    QPrintPreviewWidget, QPrinter, QPrinterInfo, QProgressBar, 
    QProgressDialog, QProxyModel, QPushButton, QPyTextObject, QRadialGradient, 
    QRadioButton, QRegExpValidator, QRegion, QResizeEvent, QRubberBand, 
    QScrollArea, QScrollBar, QSessionManager, QShortcut, QShortcutEvent, 
    QShowEvent, QSizeGrip, QSizePolicy, QSlider, QSortFilterProxyModel, 
    QSound, QSpacerItem, QSpinBox, QSplashScreen, QSplitter, QSplitterHandle, 
    QStackedLayout, QStackedWidget, QStandardItem, QStandardItemModel, 
    QStatusBar, QStatusTipEvent, QStringListModel, QStyle, QStyleFactory, 
    QStyleHintReturn, QStyleHintReturnMask, QStyleHintReturnVariant, 
    QStyleOption, QStyleOptionButton, QStyleOptionComboBox, 
    QStyleOptionComplex, QStyleOptionDockWidget, QStyleOptionDockWidgetV2, 
    QStyleOptionFocusRect, QStyleOptionFrame, QStyleOptionFrameV2, 
    QStyleOptionFrameV3, QStyleOptionGraphicsItem, QStyleOptionGroupBox, 
    QStyleOptionHeader, QStyleOptionMenuItem, QStyleOptionProgressBar, 
    QStyleOptionProgressBarV2, QStyleOptionRubberBand, QStyleOptionSizeGrip, 
    QStyleOptionSlider, QStyleOptionSpinBox, QStyleOptionTab, 
    QStyleOptionTabBarBase, QStyleOptionTabBarBaseV2, QStyleOptionTabV2, 
    QStyleOptionTabV3, QStyleOptionTabWidgetFrame, QStyleOptionTitleBar, 
    QStyleOptionToolBar, QStyleOptionToolBox, QStyleOptionToolBoxV2, 
    QStyleOptionToolButton, QStyleOptionViewItem, QStyleOptionViewItemV2, 
    QStyleOptionViewItemV3, QStyleOptionViewItemV4, QStylePainter, 
    QStyledItemDelegate, QSyntaxHighlighter, QSystemTrayIcon, QTabBar, 
    QTabWidget, QTableView, QTableWidget, QTableWidgetItem, 
    QTableWidgetSelectionRange, QTabletEvent, QTextBlock, QTextBlockFormat, 
    QTextBlockGroup, QTextBlockUserData, QTextBrowser, QTextCharFormat, 
    QTextCursor, QTextDocument, QTextDocumentFragment, QTextDocumentWriter, 
    QTextEdit, QTextFormat, QTextFragment, QTextFrame, QTextFrameFormat, 
    QTextImageFormat, QTextInlineObject, QTextItem, QTextLayout, QTextLength, 
    QTextLine, QTextList, QTextListFormat, QTextObject, QTextObjectInterface, 
    QTextOption, QTextTable, QTextTableCell, QTextTableCellFormat, 
    QTextTableFormat, QTimeEdit, QToolBar, QToolBox, QToolButton, QToolTip, 
    QTransform, QTreeView, QTreeWidget, QTreeWidgetItem, 
    QTreeWidgetItemIterator, QUndoCommand, QUndoGroup, QUndoStack, QUndoView, 
    QVBoxLayout, QValidator, QWhatsThis, QWhatsThisClickedEvent, QWheelEvent, 
    QWidget, QWidgetAction, QWidgetItem, QWindowStateChangeEvent, QWizard, 
    QWizardPage, QWorkspace, QX11EmbedContainer, QX11EmbedWidget, QX11Info, 
    qAlpha, qApp, qBlue, qDrawPlainRect, qDrawShadeLine, qDrawShadePanel, 
    qDrawShadeRect, qDrawWinButton, qDrawWinPanel, qGray, qGreen, qIsGray, 
    qRed, qRgb, qRgba, qt_x11_wait_for_window_manager)

from PyQt4.QtHelp import (QHelpContentItem, QHelpContentModel, 
    QHelpContentWidget, QHelpEngine, QHelpEngineCore, QHelpIndexModel, 
    QHelpIndexWidget, QHelpSearchEngine, QHelpSearchQuery, 
    QHelpSearchQueryWidget, QHelpSearchResultWidget)

from PyQt4.QtNetwork import (QAbstractNetworkCache, QAbstractSocket, 
    QAuthenticator, QFtp, QHostAddress, QHostInfo, QHttp, QHttpHeader, 
    QHttpRequestHeader, QHttpResponseHeader, QLocalServer, QLocalSocket, 
    QNetworkAccessManager, QNetworkAddressEntry, QNetworkCacheMetaData, 
    QNetworkCookie, QNetworkCookieJar, QNetworkDiskCache, QNetworkInterface, 
    QNetworkProxy, QNetworkProxyFactory, QNetworkProxyQuery, QNetworkReply, 
    QNetworkRequest, QSsl, QSslCertificate, QSslCipher, QSslConfiguration, 
    QSslError, QSslKey, QSslSocket, QTcpServer, QTcpSocket, QUdpSocket, 
    QUrlInfo)

from PyQt4.QtOpenGL import (QGL, QGLColormap, QGLContext, QGLFormat, 
    QGLFramebufferObject, QGLPixelBuffer, QGLWidget)

from PyQt4.QtScript import (QScriptClass, QScriptClassPropertyIterator, 
    QScriptContext, QScriptContextInfo, QScriptEngine, QScriptEngineAgent, 
    QScriptString, QScriptSyntaxCheckResult, QScriptValue, 
    QScriptValueIterator, qScriptConnect, qScriptDisconnect)

from PyQt4.QtScriptTools import QScriptEngineDebugger

from PyQt4.QtSql import (QSql, QSqlDatabase, QSqlDriver, 
    QSqlDriverCreatorBase, QSqlError, QSqlField, QSqlIndex, QSqlQuery, 
    QSqlQueryModel, QSqlRecord, QSqlRelation, QSqlRelationalDelegate, 
    QSqlRelationalTableModel, QSqlResult, QSqlTableModel)

from PyQt4.QtSvg import (QGraphicsSvgItem, QSvgGenerator, QSvgRenderer, 
    QSvgWidget)

from PyQt4.QtTest import QTest

from PyQt4.QtXml import (QDomAttr, QDomCDATASection, QDomCharacterData, 
    QDomComment, QDomDocument, QDomDocumentFragment, QDomDocumentType, 
    QDomElement, QDomEntity, QDomEntityReference, QDomImplementation, 
    QDomNamedNodeMap, QDomNode, QDomNodeList, QDomNotation, 
    QDomProcessingInstruction, QDomText, QXmlAttributes, QXmlContentHandler, 
    QXmlDTDHandler, QXmlDeclHandler, QXmlDefaultHandler, QXmlEntityResolver, 
    QXmlErrorHandler, QXmlInputSource, QXmlLexicalHandler, QXmlLocator, 
    QXmlNamespaceSupport, QXmlParseException, QXmlReader, QXmlSimpleReader)

from PyQt4.QtXmlPatterns import (QAbstractMessageHandler, 
    QAbstractUriResolver, QAbstractXmlNodeModel, QAbstractXmlReceiver, 
    QSimpleXmlNodeModel, QSourceLocation, QXmlFormatter, QXmlItem, QXmlName, 
    QXmlNamePool, QXmlNodeModelIndex, QXmlQuery, QXmlResultItems, 
    QXmlSerializer)


# Variables with simple values

PYQT_VERSION = 263682

PYQT_VERSION_STR = '4.6.2'

QT_VERSION = 263682

QT_VERSION_STR = '4.6.2'

# functions

def bin(*args, **kwargs): # real signature unknown
    pass

def hex(*args, **kwargs): # real signature unknown
    pass

def oct(*args, **kwargs): # real signature unknown
    pass

# no classes
# variables with complex values


