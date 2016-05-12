# encoding: utf-8
# module _fileio
# from /usr/lib64/python2.6/lib-dynload/_fileio.so
# by generator 1.136
""" Fast implementation of io.FileIO. """
# no imports

# no functions
# classes

class _FileIO(object):
    """
    file(name: str[, mode: str]) -> file IO object
    
    Open a file.  The mode can be 'r', 'w' or 'a' for reading (default),
    writing or appending.  The file will be created if it doesn't exist
    when opened for writing or appending; it will be truncated when
    opened for writing.  Add a '+' to the mode to allow simultaneous
    reading and writing.
    """
    def close(self): # real signature unknown; restored from __doc__
        """
        close() -> None.  Close the file.
        
        A closed file cannot be used for further I/O operations.  close() may be
        called more than once without error.  Changes the fileno to -1.
        """
        pass

    def fileno(self): # real signature unknown; restored from __doc__
        """
        fileno() -> int. "file descriptor".
        
        This is needed for lower-level file interfaces, such the fcntl module.
        """
        pass

    def isatty(self): # real signature unknown; restored from __doc__
        """ isatty() -> bool.  True if the file is connected to a tty device. """
        pass

    def read(self, size=-1): # known case of _fileio._FileIO.read
        """
        read(size: int) -> bytes.  read at most size bytes, returned as bytes.
        
        Only makes one system call, so less data may be returned than requested
        In non-blocking mode, returns None if no data is available.
        On end-of-file, returns ''.
        """
        return ""

    def readable(self): # real signature unknown; restored from __doc__
        """ readable() -> bool.  True if file was opened in a read mode. """
        pass

    def readall(self): # real signature unknown; restored from __doc__
        """
        readall() -> bytes.  read all data from the file, returned as bytes.
        
        In non-blocking mode, returns as much as is immediately available,
        or None if no data is available.  On end-of-file, returns ''.
        """
        pass

    def readinto(self): # real signature unknown; restored from __doc__
        """ readinto() -> Undocumented.  Don't use this; it may go away. """
        pass

    def seek(self, offset, whence=None): # real signature unknown; restored from __doc__
        """
        seek(offset: int[, whence: int]) -> None.  Move to new file position.
        
        Argument offset is a byte count.  Optional argument whence defaults to
        0 (offset from start of file, offset should be >= 0); other values are 1
        (move relative to current position, positive or negative), and 2 (move
        relative to end of file, usually negative, although many platforms allow
        seeking beyond the end of a file).
        Note that not all file objects are seekable.
        """
        pass

    def seekable(self): # real signature unknown; restored from __doc__
        """ seekable() -> bool.  True if file supports random-access. """
        pass

    def tell(self): # real signature unknown; restored from __doc__
        """ tell() -> int.  Current file position """
        pass

    def truncate(self, size=None): # real signature unknown; restored from __doc__
        """
        truncate([size: int]) -> None.  Truncate the file to at most size bytes.
        
        Size defaults to the current file position, as returned by tell().The current file position is changed to the value of size.
        """
        pass

    def writable(self): # real signature unknown; restored from __doc__
        """ writable() -> bool.  True if file was opened in a write mode. """
        pass

    def write(self, b): # real signature unknown; restored from __doc__
        """
        write(b: bytes) -> int.  Write bytes b to file, return number written.
        
        Only makes one system call, so not all of the data may be written.
        The number of bytes actually written is returned.
        """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    closed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if the file is closed"""

    closefd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if the file descriptor will be closed"""

    mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """String giving the file mode"""



