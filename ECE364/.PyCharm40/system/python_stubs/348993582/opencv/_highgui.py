# encoding: utf-8
# module opencv._highgui
# from /usr/lib64/python2.6/site-packages/opencv/_highgui.so
# by generator 1.136
# no doc
# no imports

# Variables with simple values

CV_CAP_ANY = 0
CV_CAP_CMU1394 = 300
CV_CAP_DC1394 = 300
CV_CAP_DSHOW = 700
CV_CAP_FIREWARE = 300
CV_CAP_FIREWIRE = 300
CV_CAP_IEEE1394 = 300
CV_CAP_MIL = 100

CV_CAP_PROP_BRIGHTNESS = 10
CV_CAP_PROP_CONTRAST = 11

CV_CAP_PROP_CONVERT_RGB = 16

CV_CAP_PROP_EXPOSURE = 15
CV_CAP_PROP_FORMAT = 8
CV_CAP_PROP_FOURCC = 6
CV_CAP_PROP_FPS = 5

CV_CAP_PROP_FRAME_COUNT = 7
CV_CAP_PROP_FRAME_HEIGHT = 4
CV_CAP_PROP_FRAME_WIDTH = 3

CV_CAP_PROP_GAIN = 14
CV_CAP_PROP_HUE = 13
CV_CAP_PROP_MODE = 9

CV_CAP_PROP_POS_AVI_RATIO = 2

CV_CAP_PROP_POS_FRAMES = 1
CV_CAP_PROP_POS_MSEC = 0

CV_CAP_PROP_RECTIFICATION = 18
CV_CAP_PROP_SATURATION = 12

CV_CAP_PROP_WHITE_BALANCE = 17

CV_CAP_QT = 500
CV_CAP_STEREO = 400
CV_CAP_TYZX = 400
CV_CAP_UNICAP = 600
CV_CAP_V4L = 200
CV_CAP_V4L2 = 200
CV_CAP_VFW = 200

CV_CVTIMG_FLIP = 1

CV_CVTIMG_SWAP_RB = 2

CV_EVENT_FLAG_ALTKEY = 32
CV_EVENT_FLAG_CTRLKEY = 8
CV_EVENT_FLAG_LBUTTON = 1
CV_EVENT_FLAG_MBUTTON = 4
CV_EVENT_FLAG_RBUTTON = 2
CV_EVENT_FLAG_SHIFTKEY = 16

CV_EVENT_LBUTTONDBLCLK = 7
CV_EVENT_LBUTTONDOWN = 1
CV_EVENT_LBUTTONUP = 4
CV_EVENT_MBUTTONDBLCLK = 9
CV_EVENT_MBUTTONDOWN = 3
CV_EVENT_MBUTTONUP = 6
CV_EVENT_MOUSEMOVE = 0
CV_EVENT_RBUTTONDBLCLK = 8
CV_EVENT_RBUTTONDOWN = 2
CV_EVENT_RBUTTONUP = 5

CV_FOURCC_PROMPT = -1

CV_IMWRITE_JPEG_QUALITY = 1

CV_IMWRITE_PNG_COMPRESSION = 16

CV_IMWRITE_PXM_BINARY = 32

CV_LOAD_IMAGE_ANYCOLOR = 4
CV_LOAD_IMAGE_ANYDEPTH = 2
CV_LOAD_IMAGE_COLOR = 1
CV_LOAD_IMAGE_GRAYSCALE = 0
CV_LOAD_IMAGE_UNCHANGED = -1

CV_TYZX_COLOR = 402
CV_TYZX_LEFT = 400
CV_TYZX_RIGHT = 401
CV_TYZX_Z = 403

CV_WINDOW_AUTOSIZE = 1

HG_AUTOSIZE = 1

# functions

def CvCapture_swigregister(*args, **kwargs): # real signature unknown
    pass

def cvConvertImage(CvArr_src, CvArr_dst, int_flags=0): # real signature unknown; restored from __doc__
    """ cvConvertImage(CvArr src, CvArr dst, int flags = 0) """
    pass

def cvCreateCameraCapture(int_index): # real signature unknown; restored from __doc__
    """ cvCreateCameraCapture(int index) -> CvCapture """
    pass

def cvCreateFileCapture(char_filename): # real signature unknown; restored from __doc__
    """ cvCreateFileCapture(char filename) -> CvCapture """
    pass

def cvCreateTrackbar(char_trackbar_name, char_window_name, int_value, int_count, CvTrackbarCallback_on_change): # real signature unknown; restored from __doc__
    """
    cvCreateTrackbar(char trackbar_name, char window_name, int value, int count, 
        CvTrackbarCallback on_change) -> int
    """
    return 0

def cvCreateTrackbar2(char_trackbar_name, char_window_name, int_value, int_count, CvTrackbarCallback2_on_change, void_userdata=None): # real signature unknown; restored from __doc__
    """
    cvCreateTrackbar2(char trackbar_name, char window_name, int value, int count, 
        CvTrackbarCallback2 on_change, void userdata = None) -> int
    """
    return 0

def cvCreateVideoWriter(char_filename, int_fourcc, double_fps, CvSize_frame_size, int_is_color=1): # real signature unknown; restored from __doc__
    """
    cvCreateVideoWriter(char filename, int fourcc, double fps, CvSize frame_size, 
        int is_color = 1) -> CvVideoWriter
    """
    pass

def cvDecodeImage(CvMat_buf, int_iscolor=1): # real signature unknown; restored from __doc__
    """ cvDecodeImage(CvMat buf, int iscolor = 1) """
    pass

def cvDecodeImageM(CvMat_buf, int_iscolor=1): # real signature unknown; restored from __doc__
    """ cvDecodeImageM(CvMat buf, int iscolor = 1) -> CvMat """
    pass

def cvDestroyAllWindows(): # real signature unknown; restored from __doc__
    """ cvDestroyAllWindows() """
    pass

def cvDestroyWindow(char_name): # real signature unknown; restored from __doc__
    """ cvDestroyWindow(char name) """
    pass

def cvEncodeImage(char_ext, CvArr_image, int_params=None): # real signature unknown; restored from __doc__
    """ cvEncodeImage(char ext, CvArr image, int params = None) -> CvMat """
    pass

def cvGetCaptureDomain(CvCapture_capture): # real signature unknown; restored from __doc__
    """ cvGetCaptureDomain(CvCapture capture) -> int """
    return 0

def cvGetCaptureProperty(CvCapture_capture, int_property_id): # real signature unknown; restored from __doc__
    """ cvGetCaptureProperty(CvCapture capture, int property_id) -> double """
    return 0.0

def cvGetTrackbarPos(char_trackbar_name, char_window_name): # real signature unknown; restored from __doc__
    """ cvGetTrackbarPos(char trackbar_name, char window_name) -> int """
    return 0

def cvGetWindowHandle(char_name): # real signature unknown; restored from __doc__
    """ cvGetWindowHandle(char name) -> void """
    pass

def cvGetWindowName(void_window_handle): # real signature unknown; restored from __doc__
    """ cvGetWindowName(void window_handle) -> char """
    return ""

def cvGrabFrame(CvCapture_capture): # real signature unknown; restored from __doc__
    """ cvGrabFrame(CvCapture capture) -> int """
    return 0

def cvInitSystem(int_argc, char_argv): # real signature unknown; restored from __doc__
    """ cvInitSystem(int argc, char argv) -> int """
    return 0

def cvLoadImage(char_filename, int_iscolor=1): # real signature unknown; restored from __doc__
    """
    cvLoadImage(char filename, int iscolor = 1) -> CvMat
    cvLoadImage(char filename) -> CvMat
    """
    pass

def cvLoadImageM(char_filename, int_iscolor=1): # real signature unknown; restored from __doc__
    """ cvLoadImageM(char filename, int iscolor = 1) -> CvMat """
    pass

def cvMoveWindow(char_name, int_x, int_y): # real signature unknown; restored from __doc__
    """ cvMoveWindow(char name, int x, int y) """
    pass

def cvNamedWindow(char_name, int_flags=1): # real signature unknown; restored from __doc__
    """ cvNamedWindow(char name, int flags = 1) -> int """
    return 0

def cvQueryFrame(CvCapture_capture): # real signature unknown; restored from __doc__
    """ cvQueryFrame(CvCapture capture) -> CvMat """
    pass

def cvQueryFrame__Deprecated(CvCapture_capture): # real signature unknown; restored from __doc__
    """ cvQueryFrame__Deprecated(CvCapture capture) """
    pass

def cvResizeWindow(char_name, int_width, int_height): # real signature unknown; restored from __doc__
    """ cvResizeWindow(char name, int width, int height) """
    pass

def cvRetrieveFrame(CvCapture_capture): # real signature unknown; restored from __doc__
    """ cvRetrieveFrame(CvCapture capture) -> CvMat """
    pass

def cvRetrieveFrame__Deprecated(CvCapture_capture, int_streamIdx=0): # real signature unknown; restored from __doc__
    """ cvRetrieveFrame__Deprecated(CvCapture capture, int streamIdx = 0) """
    pass

def CvRNG_Wrapper_ptr(*args, **kwargs): # real signature unknown
    pass

def CvRNG_Wrapper_ref(*args, **kwargs): # real signature unknown
    pass

def CvRNG_Wrapper_swigregister(*args, **kwargs): # real signature unknown
    pass

def CvRNG_Wrapper___eq__(*args, **kwargs): # real signature unknown
    pass

def CvRNG_Wrapper___ne__(*args, **kwargs): # real signature unknown
    pass

def cvSaveImage(char_filename, CvArr_image, int_params=None): # real signature unknown; restored from __doc__
    """ cvSaveImage(char filename, CvArr image, int params = None) -> int """
    return 0

def cvSetCaptureProperty(CvCapture_capture, int_property_id, double_value): # real signature unknown; restored from __doc__
    """ cvSetCaptureProperty(CvCapture capture, int property_id, double value) -> int """
    return 0

def cvSetMouseCallback(*args, **kwargs): # real signature unknown
    pass

def cvSetMouseCallbackOld(char_window_name, CvMouseCallback_on_mouse, void_param=None): # real signature unknown; restored from __doc__
    """ cvSetMouseCallbackOld(char window_name, CvMouseCallback on_mouse, void param = None) """
    pass

def cvSetTrackbarPos(char_trackbar_name, char_window_name, int_pos): # real signature unknown; restored from __doc__
    """ cvSetTrackbarPos(char trackbar_name, char window_name, int pos) """
    pass

def cvShowImage(char_name, CvArr_image): # real signature unknown; restored from __doc__
    """ cvShowImage(char name, CvArr image) """
    pass

def cvStartWindowThread(): # real signature unknown; restored from __doc__
    """ cvStartWindowThread() -> int """
    return 0

def CvSubdiv2DEdge_Wrapper_ptr(*args, **kwargs): # real signature unknown
    pass

def CvSubdiv2DEdge_Wrapper_ref(*args, **kwargs): # real signature unknown
    pass

def CvSubdiv2DEdge_Wrapper_swigregister(*args, **kwargs): # real signature unknown
    pass

def CvSubdiv2DEdge_Wrapper___eq__(*args, **kwargs): # real signature unknown
    pass

def CvSubdiv2DEdge_Wrapper___ne__(*args, **kwargs): # real signature unknown
    pass

def CvVideoWriter_swigregister(*args, **kwargs): # real signature unknown
    pass

def CvvImage_Bpp(CvvImage_self): # real signature unknown; restored from __doc__
    """ CvvImage_Bpp(CvvImage self) -> int """
    return 0

def CvvImage_CopyOf(CvvImage_self, img): # real signature unknown; restored from __doc__
    """
    CopyOf(CvvImage image, int desired_color = -1)
    CopyOf(CvvImage image)
    CopyOf( img, int desired_color = -1)
    CvvImage_CopyOf(CvvImage self,  img)
    """
    pass

def CvvImage_Create(CvvImage_self, int_width, int_height, int_bits_per_pixel): # real signature unknown; restored from __doc__
    """
    Create(int width, int height, int bits_per_pixel, int image_origin = 0) -> bool
    CvvImage_Create(CvvImage self, int width, int height, int bits_per_pixel) -> bool
    """
    return False

def CvvImage_Destroy(CvvImage_self): # real signature unknown; restored from __doc__
    """ CvvImage_Destroy(CvvImage self) """
    pass

def CvvImage_Fill(CvvImage_self, int_color): # real signature unknown; restored from __doc__
    """ CvvImage_Fill(CvvImage self, int color) """
    pass

def CvvImage_GetImage(CvvImage_self): # real signature unknown; restored from __doc__
    """ CvvImage_GetImage(CvvImage self) """
    pass

def CvvImage_Height(CvvImage_self): # real signature unknown; restored from __doc__
    """ CvvImage_Height(CvvImage self) -> int """
    return 0

def CvvImage_Load(CvvImage_self, char_filename): # real signature unknown; restored from __doc__
    """
    Load(char filename, int desired_color = 1) -> bool
    CvvImage_Load(CvvImage self, char filename) -> bool
    """
    return False

def CvvImage_LoadRect(CvvImage_self, char_filename, int_desired_color, CvRect_r): # real signature unknown; restored from __doc__
    """ CvvImage_LoadRect(CvvImage self, char filename, int desired_color, CvRect r) -> bool """
    return False

def CvvImage_Save(CvvImage_self, char_filename): # real signature unknown; restored from __doc__
    """ CvvImage_Save(CvvImage self, char filename) -> bool """
    return False

def CvvImage_Show(CvvImage_self, char_window): # real signature unknown; restored from __doc__
    """ CvvImage_Show(CvvImage self, char window) """
    pass

def CvvImage_swigregister(*args, **kwargs): # real signature unknown
    pass

def CvvImage_Width(CvvImage_self): # real signature unknown; restored from __doc__
    """ CvvImage_Width(CvvImage self) -> int """
    return 0

def cvWaitKey(*args, **kwargs): # real signature unknown
    pass

def cvWaitKeyC(int_delay=0): # real signature unknown; restored from __doc__
    """ cvWaitKeyC(int delay = 0) -> int """
    return 0

def cvWriteFrame(CvVideoWriter_writer, image): # real signature unknown; restored from __doc__
    """ cvWriteFrame(CvVideoWriter writer,  image) -> int """
    return 0

def CV_FOURCC(char_c1, char_c2, char_c3, char_c4): # real signature unknown; restored from __doc__
    """ CV_FOURCC(char c1, char c2, char c3, char c4) -> int """
    return 0

def delete_CvCapture(CvCapture_self): # real signature unknown; restored from __doc__
    """ delete_CvCapture(CvCapture self) """
    pass

def delete_CvRNG_Wrapper(CvRNG_Wrapper_self): # real signature unknown; restored from __doc__
    """ delete_CvRNG_Wrapper(CvRNG_Wrapper self) """
    pass

def delete_CvSubdiv2DEdge_Wrapper(CvSubdiv2DEdge_Wrapper_self): # real signature unknown; restored from __doc__
    """ delete_CvSubdiv2DEdge_Wrapper(CvSubdiv2DEdge_Wrapper self) """
    pass

def delete_CvVideoWriter(CvVideoWriter_self): # real signature unknown; restored from __doc__
    """ delete_CvVideoWriter(CvVideoWriter self) """
    pass

def delete_CvvImage(CvvImage_self): # real signature unknown; restored from __doc__
    """ delete_CvvImage(CvvImage self) """
    pass

def new_CvRNG_Wrapper(*args, **kwargs): # real signature unknown
    pass

def new_CvSubdiv2DEdge_Wrapper(*args, **kwargs): # real signature unknown
    pass

def new_CvvImage(): # real signature unknown; restored from __doc__
    """ new_CvvImage() -> CvvImage """
    pass

def SWIG_PyInstanceMethod_New(*args, **kwargs): # real signature unknown
    pass

# no classes
