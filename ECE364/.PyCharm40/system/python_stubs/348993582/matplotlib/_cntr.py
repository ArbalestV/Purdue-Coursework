# encoding: utf-8
# module matplotlib._cntr
# from /usr/lib64/python2.6/site-packages/matplotlib/_cntr.so
# by generator 1.136
""" Contouring engine as an extension type (numpy). """
# no imports

# no functions
# classes

class Cntr(object):
    """ Contour engine """
    def trace(self, *args, **kwargs): # real signature unknown
        """
        Return a list of contour line segments or polygons.
        
            Required argument: level0, a contour level
            Optional argument: level1; if given, and if level1 > level0,
                then the contours will be polygons surrounding areas between
                the levels.
            Optional argument: points; if 0 (default), return a list of
                vector pairs; otherwise, return a list of lists of points.
            Optional argument: nchunk; approximate number of grid points
                per chunk. 0 (default) for no chunking.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


