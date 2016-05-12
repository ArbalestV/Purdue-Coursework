# encoding: utf-8
# module _bytesio
# from /usr/lib64/python2.6/lib-dynload/_bytesio.so
# by generator 1.136
# no doc
# no imports

# no functions
# classes

class _BytesIO(object):
    """
    BytesIO([buffer]) -> object
    
    Create a buffered I/O implementation using an in-memory bytes
    buffer, ready for reading and writing.
    """
    def close(self): # real signature unknown; restored from __doc__
        """ close() -> None.  Disable all I/O operations. """
        pass

    def flush(self): # real signature unknown; restored from __doc__
        """ flush() -> None.  Does nothing. """
        pass

    def getvalue(self): # real signature unknown; restored from __doc__
        """
        getvalue() -> bytes.
        
        Retrieve the entire contents of the BytesIO object.
        """
        pass

    def isatty(self): # real signature unknown; restored from __doc__
        """
        isatty() -> False.
        
        Always returns False since BytesIO objects are not connected
        to a tty-like device.
        """
        pass

    def next(self): # real signature unknown; restored from __doc__
        """ x.next() -> the next value, or raise StopIteration """
        pass

    def read(self, size=None): # real signature unknown; restored from __doc__
        """
        read([size]) -> read at most size bytes, returned as a string.
        
        If the size argument is negative, read until EOF is reached.
        Return an empty string at EOF.
        """
        pass

    def read1(self, size): # real signature unknown; restored from __doc__
        """
        read1(size) -> read at most size bytes, returned as a string.
        
        If the size argument is negative or omitted, read until EOF is reached.
        Return an empty string at EOF.
        """
        pass

    def readable(self, *args, **kwargs): # real signature unknown
        pass

    def readinto(self, bytearray): # real signature unknown; restored from __doc__
        """
        readinto(bytearray) -> int.  Read up to len(b) bytes into b.
        
        Returns number of bytes read (0 for EOF), or None if the object
        is set not to block as has no data to read.
        """
        pass

    def readline(self, size=None): # real signature unknown; restored from __doc__
        """
        readline([size]) -> next line from the file, as a string.
        
        Retain newline.  A non-negative size argument limits the maximum
        number of bytes to return (an incomplete line may be returned then).
        Return an empty string at EOF.
        """
        pass

    def readlines(self, size=None): # real signature unknown; restored from __doc__
        """
        readlines([size]) -> list of strings, each a line from the file.
        
        Call readline() repeatedly and return a list of the lines so read.
        The optional size argument, if given, is an approximate bound on the
        total number of bytes in the lines returned.
        """
        return []

    def seek(self, pos, whence=0): # real signature unknown; restored from __doc__
        """
        seek(pos, whence=0) -> int.  Change stream position.
        
        Seek to byte offset pos relative to position indicated by whence:
             0  Start of stream (the default).  pos should be >= 0;
             1  Current position - pos may be negative;
             2  End of stream - pos usually negative.
        Returns the new absolute position.
        """
        pass

    def seekable(self, *args, **kwargs): # real signature unknown
        pass

    def tell(self): # real signature unknown; restored from __doc__
        """ tell() -> current file position, an integer """
        pass

    def truncate(self, size=None): # real signature unknown; restored from __doc__
        """
        truncate([size]) -> int.  Truncate the file to at most size bytes.
        
        Size defaults to the current file position, as returned by tell().
        Returns the new size.  Imply an absolute seek to the position size.
        """
        pass

    def writable(self, *args, **kwargs): # real signature unknown
        pass

    def write(self, bytes): # real signature unknown; restored from __doc__
        """
        write(bytes) -> int.  Write bytes to file.
        
        Return the number of bytes written.
        """
        pass

    def writelines(self, sequence_of_strings): # real signature unknown; restored from __doc__
        """
        writelines(sequence_of_strings) -> None.  Write strings to the file.
        
        Note that newlines are not added.  The sequence can be any iterable
        object producing strings. This is equivalent to calling write() for
        each string.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self): # real signature unknown; restored from __doc__
        """ x.__iter__() <==> iter(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    closed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True if the file is closed."""



