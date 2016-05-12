# encoding: utf-8
# module PySide.QtOpenGL
# from /opt/python3/current/lib/python3.4/site-packages/PySide/QtOpenGL.so
# by generator 1.136
# no doc

# imports
import PySide.QtCore as __PySide_QtCore
import PySide.QtGui as __PySide_QtGui
import Shiboken as __Shiboken


# no functions
# classes

class QGL(__Shiboken.Object):
    # no doc
    def setPreferredPaintEngine(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    AccumBuffer = None # (!) real value is ''
    AlphaChannel = None # (!) real value is ''
    ColorIndex = None # (!) real value is ''
    DepthBuffer = None # (!) real value is ''
    DirectRendering = None # (!) real value is ''
    DoubleBuffer = None # (!) real value is ''
    FormatOption = None # (!) real value is ''
    FormatOptions = None # (!) real value is ''
    HasOverlay = None # (!) real value is ''
    IndirectRendering = None # (!) real value is ''
    NoAccumBuffer = None # (!) real value is ''
    NoAlphaChannel = None # (!) real value is ''
    NoDepthBuffer = None # (!) real value is ''
    NoOverlay = None # (!) real value is ''
    NoSampleBuffers = None # (!) real value is ''
    NoStencilBuffer = None # (!) real value is ''
    NoStereoBuffers = None # (!) real value is ''
    Rgba = None # (!) real value is ''
    SampleBuffers = None # (!) real value is ''
    SingleBuffer = None # (!) real value is ''
    StencilBuffer = None # (!) real value is ''
    StereoBuffers = None # (!) real value is ''


class QGLColormap(__Shiboken.Object):
    # no doc
    def entryColor(self, *args, **kwargs): # real signature unknown
        pass

    def entryRgb(self, *args, **kwargs): # real signature unknown
        pass

    def find(self, *args, **kwargs): # real signature unknown
        pass

    def findNearest(self, *args, **kwargs): # real signature unknown
        pass

    def handle(self, *args, **kwargs): # real signature unknown
        pass

    def isEmpty(self, *args, **kwargs): # real signature unknown
        pass

    def setEntry(self, *args, **kwargs): # real signature unknown
        pass

    def setHandle(self, *args, **kwargs): # real signature unknown
        pass

    def size(self, *args, **kwargs): # real signature unknown
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class QGLContext(__Shiboken.Object):
    # no doc
    def areSharing(self, *args, **kwargs): # real signature unknown
        pass

    def bindTexture(self, *args, **kwargs): # real signature unknown
        pass

    def chooseContext(self, *args, **kwargs): # real signature unknown
        pass

    def chooseVisual(self, *args, **kwargs): # real signature unknown
        pass

    def colorIndex(self, *args, **kwargs): # real signature unknown
        pass

    def create(self, *args, **kwargs): # real signature unknown
        pass

    def currentContext(self, *args, **kwargs): # real signature unknown
        pass

    def deleteTexture(self, *args, **kwargs): # real signature unknown
        pass

    def device(self, *args, **kwargs): # real signature unknown
        pass

    def deviceIsPixmap(self, *args, **kwargs): # real signature unknown
        pass

    def doneCurrent(self, *args, **kwargs): # real signature unknown
        pass

    def drawTexture(self, *args, **kwargs): # real signature unknown
        pass

    def format(self, *args, **kwargs): # real signature unknown
        pass

    def getProcAddress(self, *args, **kwargs): # real signature unknown
        pass

    def initialized(self, *args, **kwargs): # real signature unknown
        pass

    def isSharing(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        pass

    def makeCurrent(self, *args, **kwargs): # real signature unknown
        pass

    def overlayTransparentColor(self, *args, **kwargs): # real signature unknown
        pass

    def requestedFormat(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self, *args, **kwargs): # real signature unknown
        pass

    def setDevice(self, *args, **kwargs): # real signature unknown
        pass

    def setFormat(self, *args, **kwargs): # real signature unknown
        pass

    def setInitialized(self, *args, **kwargs): # real signature unknown
        pass

    def setTextureCacheLimit(self, *args, **kwargs): # real signature unknown
        pass

    def setValid(self, *args, **kwargs): # real signature unknown
        pass

    def setWindowCreated(self, *args, **kwargs): # real signature unknown
        pass

    def swapBuffers(self, *args, **kwargs): # real signature unknown
        pass

    def textureCacheLimit(self, *args, **kwargs): # real signature unknown
        pass

    def tryVisual(self, *args, **kwargs): # real signature unknown
        pass

    def windowCreated(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    BindOption = None # (!) real value is ''
    BindOptions = None # (!) real value is ''
    CanFlipNativePixmapBindOption = None # (!) real value is ''
    DefaultBindOption = None # (!) real value is ''
    InternalBindOption = None # (!) real value is ''
    InvertedYBindOption = None # (!) real value is ''
    LinearFilteringBindOption = None # (!) real value is ''
    MemoryManagedBindOption = None # (!) real value is ''
    MipmapBindOption = None # (!) real value is ''
    NoBindOption = None # (!) real value is ''
    PremultipliedAlphaBindOption = None # (!) real value is ''


class QGLFormat(__Shiboken.Object):
    # no doc
    def accum(self, *args, **kwargs): # real signature unknown
        pass

    def accumBufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def alpha(self, *args, **kwargs): # real signature unknown
        pass

    def alphaBufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def blueBufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def defaultFormat(self, *args, **kwargs): # real signature unknown
        pass

    def defaultOverlayFormat(self, *args, **kwargs): # real signature unknown
        pass

    def depth(self, *args, **kwargs): # real signature unknown
        pass

    def depthBufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def directRendering(self, *args, **kwargs): # real signature unknown
        pass

    def doubleBuffer(self, *args, **kwargs): # real signature unknown
        pass

    def greenBufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def hasOpenGL(self, *args, **kwargs): # real signature unknown
        pass

    def hasOpenGLOverlays(self, *args, **kwargs): # real signature unknown
        pass

    def hasOverlay(self, *args, **kwargs): # real signature unknown
        pass

    def openGLVersionFlags(self, *args, **kwargs): # real signature unknown
        pass

    def plane(self, *args, **kwargs): # real signature unknown
        pass

    def redBufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def rgba(self, *args, **kwargs): # real signature unknown
        pass

    def sampleBuffers(self, *args, **kwargs): # real signature unknown
        pass

    def samples(self, *args, **kwargs): # real signature unknown
        pass

    def setAccum(self, *args, **kwargs): # real signature unknown
        pass

    def setAccumBufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def setAlpha(self, *args, **kwargs): # real signature unknown
        pass

    def setAlphaBufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def setBlueBufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def setDefaultFormat(self, *args, **kwargs): # real signature unknown
        pass

    def setDefaultOverlayFormat(self, *args, **kwargs): # real signature unknown
        pass

    def setDepth(self, *args, **kwargs): # real signature unknown
        pass

    def setDepthBufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def setDirectRendering(self, *args, **kwargs): # real signature unknown
        pass

    def setDoubleBuffer(self, *args, **kwargs): # real signature unknown
        pass

    def setGreenBufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def setOption(self, *args, **kwargs): # real signature unknown
        pass

    def setOverlay(self, *args, **kwargs): # real signature unknown
        pass

    def setPlane(self, *args, **kwargs): # real signature unknown
        pass

    def setRedBufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def setRgba(self, *args, **kwargs): # real signature unknown
        pass

    def setSampleBuffers(self, *args, **kwargs): # real signature unknown
        pass

    def setSamples(self, *args, **kwargs): # real signature unknown
        pass

    def setStencil(self, *args, **kwargs): # real signature unknown
        pass

    def setStencilBufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def setStereo(self, *args, **kwargs): # real signature unknown
        pass

    def setSwapInterval(self, *args, **kwargs): # real signature unknown
        pass

    def stencil(self, *args, **kwargs): # real signature unknown
        pass

    def stencilBufferSize(self, *args, **kwargs): # real signature unknown
        pass

    def stereo(self, *args, **kwargs): # real signature unknown
        pass

    def swapInterval(self, *args, **kwargs): # real signature unknown
        pass

    def testOption(self, *args, **kwargs): # real signature unknown
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

    OpenGLVersionFlag = None # (!) real value is ''
    OpenGLVersionFlags = None # (!) real value is ''
    OpenGL_ES_CommonLite_Version_1_0 = None # (!) real value is ''
    OpenGL_ES_CommonLite_Version_1_1 = None # (!) real value is ''
    OpenGL_ES_Common_Version_1_0 = None # (!) real value is ''
    OpenGL_ES_Common_Version_1_1 = None # (!) real value is ''
    OpenGL_ES_Version_2_0 = None # (!) real value is ''
    OpenGL_Version_1_1 = None # (!) real value is ''
    OpenGL_Version_1_2 = None # (!) real value is ''
    OpenGL_Version_1_3 = None # (!) real value is ''
    OpenGL_Version_1_4 = None # (!) real value is ''
    OpenGL_Version_1_5 = None # (!) real value is ''
    OpenGL_Version_2_0 = None # (!) real value is ''
    OpenGL_Version_2_1 = None # (!) real value is ''
    OpenGL_Version_3_0 = None # (!) real value is ''
    OpenGL_Version_3_1 = None # (!) real value is ''
    OpenGL_Version_3_2 = None # (!) real value is ''
    OpenGL_Version_3_3 = None # (!) real value is ''
    OpenGL_Version_4_0 = None # (!) real value is ''
    OpenGL_Version_None = None # (!) real value is ''
    __hash__ = None


class QGLFramebufferObject(__PySide_QtGui.QPaintDevice):
    # no doc
    def attachment(self, *args, **kwargs): # real signature unknown
        pass

    def bind(self, *args, **kwargs): # real signature unknown
        pass

    def blitFramebuffer(self, *args, **kwargs): # real signature unknown
        pass

    def devType(self, *args, **kwargs): # real signature unknown
        pass

    def drawTexture(self, *args, **kwargs): # real signature unknown
        pass

    def format(self, *args, **kwargs): # real signature unknown
        pass

    def handle(self, *args, **kwargs): # real signature unknown
        pass

    def hasOpenGLFramebufferBlit(self, *args, **kwargs): # real signature unknown
        pass

    def hasOpenGLFramebufferObjects(self, *args, **kwargs): # real signature unknown
        pass

    def isBound(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        pass

    def metric(self, *args, **kwargs): # real signature unknown
        pass

    def paintEngine(self, *args, **kwargs): # real signature unknown
        pass

    def release(self, *args, **kwargs): # real signature unknown
        pass

    def size(self, *args, **kwargs): # real signature unknown
        pass

    def texture(self, *args, **kwargs): # real signature unknown
        pass

    def toImage(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    Attachment = None # (!) real value is ''
    CombinedDepthStencil = None # (!) real value is ''
    Depth = None # (!) real value is ''
    NoAttachment = None # (!) real value is ''


class QGLFramebufferObjectFormat(__Shiboken.Object):
    # no doc
    def attachment(self, *args, **kwargs): # real signature unknown
        pass

    def internalTextureFormat(self, *args, **kwargs): # real signature unknown
        pass

    def samples(self, *args, **kwargs): # real signature unknown
        pass

    def setAttachment(self, *args, **kwargs): # real signature unknown
        pass

    def setInternalTextureFormat(self, *args, **kwargs): # real signature unknown
        pass

    def setSamples(self, *args, **kwargs): # real signature unknown
        pass

    def setTextureTarget(self, *args, **kwargs): # real signature unknown
        pass

    def textureTarget(self, *args, **kwargs): # real signature unknown
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


class QGLPixelBuffer(__PySide_QtGui.QPaintDevice):
    # no doc
    def bindTexture(self, *args, **kwargs): # real signature unknown
        pass

    def bindToDynamicTexture(self, *args, **kwargs): # real signature unknown
        pass

    def deleteTexture(self, *args, **kwargs): # real signature unknown
        pass

    def devType(self, *args, **kwargs): # real signature unknown
        pass

    def doneCurrent(self, *args, **kwargs): # real signature unknown
        pass

    def drawTexture(self, *args, **kwargs): # real signature unknown
        pass

    def format(self, *args, **kwargs): # real signature unknown
        pass

    def generateDynamicTexture(self, *args, **kwargs): # real signature unknown
        pass

    def handle(self, *args, **kwargs): # real signature unknown
        pass

    def hasOpenGLPbuffers(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        pass

    def makeCurrent(self, *args, **kwargs): # real signature unknown
        pass

    def metric(self, *args, **kwargs): # real signature unknown
        pass

    def paintEngine(self, *args, **kwargs): # real signature unknown
        pass

    def releaseFromDynamicTexture(self, *args, **kwargs): # real signature unknown
        pass

    def size(self, *args, **kwargs): # real signature unknown
        pass

    def toImage(self, *args, **kwargs): # real signature unknown
        pass

    def updateDynamicTexture(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class QGLShader(__PySide_QtCore.QObject):
    # no doc
    def compileSourceCode(self, *args, **kwargs): # real signature unknown
        pass

    def compileSourceFile(self, *args, **kwargs): # real signature unknown
        pass

    def isCompiled(self, *args, **kwargs): # real signature unknown
        pass

    def log(self, *args, **kwargs): # real signature unknown
        pass

    def shaderId(self, *args, **kwargs): # real signature unknown
        pass

    def shaderType(self, *args, **kwargs): # real signature unknown
        pass

    def sourceCode(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    Fragment = None # (!) real value is ''
    ShaderType = None # (!) real value is ''
    ShaderTypeBit = None # (!) real value is ''
    staticMetaObject = None # (!) real value is ''
    Vertex = None # (!) real value is ''


class QGLShaderProgram(__PySide_QtCore.QObject):
    # no doc
    def addShader(self, *args, **kwargs): # real signature unknown
        pass

    def addShaderFromSourceCode(self, *args, **kwargs): # real signature unknown
        pass

    def addShaderFromSourceFile(self, *args, **kwargs): # real signature unknown
        pass

    def attributeLocation(self, *args, **kwargs): # real signature unknown
        pass

    def bind(self, *args, **kwargs): # real signature unknown
        pass

    def bindAttributeLocation(self, *args, **kwargs): # real signature unknown
        pass

    def disableAttributeArray(self, *args, **kwargs): # real signature unknown
        pass

    def enableAttributeArray(self, *args, **kwargs): # real signature unknown
        pass

    def hasOpenGLShaderPrograms(self, *args, **kwargs): # real signature unknown
        pass

    def isLinked(self, *args, **kwargs): # real signature unknown
        pass

    def link(self, *args, **kwargs): # real signature unknown
        pass

    def log(self, *args, **kwargs): # real signature unknown
        pass

    def programId(self, *args, **kwargs): # real signature unknown
        pass

    def release(self, *args, **kwargs): # real signature unknown
        pass

    def removeAllShaders(self, *args, **kwargs): # real signature unknown
        pass

    def removeShader(self, *args, **kwargs): # real signature unknown
        pass

    def setAttributeArray2D(self, *args, **kwargs): # real signature unknown
        pass

    def setAttributeArray3D(self, *args, **kwargs): # real signature unknown
        pass

    def setAttributeArray4D(self, *args, **kwargs): # real signature unknown
        pass

    def setAttributeValue(self, *args, **kwargs): # real signature unknown
        pass

    def setUniformValue(self, *args, **kwargs): # real signature unknown
        pass

    def setUniformValueArray2D(self, *args, **kwargs): # real signature unknown
        pass

    def setUniformValueArray2x2(self, *args, **kwargs): # real signature unknown
        pass

    def setUniformValueArray2x3(self, *args, **kwargs): # real signature unknown
        pass

    def setUniformValueArray2x4(self, *args, **kwargs): # real signature unknown
        pass

    def setUniformValueArray3D(self, *args, **kwargs): # real signature unknown
        pass

    def setUniformValueArray3x2(self, *args, **kwargs): # real signature unknown
        pass

    def setUniformValueArray3x3(self, *args, **kwargs): # real signature unknown
        pass

    def setUniformValueArray3x4(self, *args, **kwargs): # real signature unknown
        pass

    def setUniformValueArray4D(self, *args, **kwargs): # real signature unknown
        pass

    def setUniformValueArray4x2(self, *args, **kwargs): # real signature unknown
        pass

    def setUniformValueArray4x3(self, *args, **kwargs): # real signature unknown
        pass

    def setUniformValueArray4x4(self, *args, **kwargs): # real signature unknown
        pass

    def setUniformValueArrayInt(self, *args, **kwargs): # real signature unknown
        pass

    def setUniformValueArrayUint(self, *args, **kwargs): # real signature unknown
        pass

    def shaders(self, *args, **kwargs): # real signature unknown
        pass

    def uniformLocation(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    staticMetaObject = None # (!) real value is ''


class QGLWidget(__PySide_QtGui.QWidget):
    # no doc
    def autoBufferSwap(self, *args, **kwargs): # real signature unknown
        pass

    def bindTexture(self, *args, **kwargs): # real signature unknown
        pass

    def colormap(self, *args, **kwargs): # real signature unknown
        pass

    def context(self, *args, **kwargs): # real signature unknown
        pass

    def convertToGLFormat(self, *args, **kwargs): # real signature unknown
        pass

    def deleteTexture(self, *args, **kwargs): # real signature unknown
        pass

    def doneCurrent(self, *args, **kwargs): # real signature unknown
        pass

    def doubleBuffer(self, *args, **kwargs): # real signature unknown
        pass

    def drawTexture(self, *args, **kwargs): # real signature unknown
        pass

    def event(self, *args, **kwargs): # real signature unknown
        pass

    def format(self, *args, **kwargs): # real signature unknown
        pass

    def glDraw(self, *args, **kwargs): # real signature unknown
        pass

    def glInit(self, *args, **kwargs): # real signature unknown
        pass

    def grabFrameBuffer(self, *args, **kwargs): # real signature unknown
        pass

    def initializeGL(self, *args, **kwargs): # real signature unknown
        pass

    def initializeOverlayGL(self, *args, **kwargs): # real signature unknown
        pass

    def isSharing(self, *args, **kwargs): # real signature unknown
        pass

    def isValid(self, *args, **kwargs): # real signature unknown
        pass

    def makeCurrent(self, *args, **kwargs): # real signature unknown
        pass

    def makeOverlayCurrent(self, *args, **kwargs): # real signature unknown
        pass

    def overlayContext(self, *args, **kwargs): # real signature unknown
        pass

    def paintEngine(self, *args, **kwargs): # real signature unknown
        pass

    def paintEvent(self, *args, **kwargs): # real signature unknown
        pass

    def paintGL(self, *args, **kwargs): # real signature unknown
        pass

    def paintOverlayGL(self, *args, **kwargs): # real signature unknown
        pass

    def qglClearColor(self, *args, **kwargs): # real signature unknown
        pass

    def qglColor(self, *args, **kwargs): # real signature unknown
        pass

    def renderPixmap(self, *args, **kwargs): # real signature unknown
        pass

    def renderText(self, *args, **kwargs): # real signature unknown
        pass

    def resizeEvent(self, *args, **kwargs): # real signature unknown
        pass

    def resizeGL(self, *args, **kwargs): # real signature unknown
        pass

    def resizeOverlayGL(self, *args, **kwargs): # real signature unknown
        pass

    def setAutoBufferSwap(self, *args, **kwargs): # real signature unknown
        pass

    def setColormap(self, *args, **kwargs): # real signature unknown
        pass

    def setMouseTracking(self, *args, **kwargs): # real signature unknown
        pass

    def swapBuffers(self, *args, **kwargs): # real signature unknown
        pass

    def updateGL(self, *args, **kwargs): # real signature unknown
        pass

    def updateOverlayGL(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    staticMetaObject = None # (!) real value is ''


# variables with complex values

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

