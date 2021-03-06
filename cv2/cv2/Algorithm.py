# encoding: utf-8
# module cv2.cv2
# from F:\Python\Python36\lib\site-packages\cv2\cv2.cp36-win_amd64.pyd
# by generator 1.147
""" Python wrapper for OpenCV. """

# imports
import cv2.cv2 as  # F:\Python\Python36\lib\site-packages\cv2\cv2.cp36-win_amd64.pyd
import cv2.Error as Error # <module 'cv2.Error'>
import cv2.cuda as cuda # <module 'cv2.cuda'>
import cv2.detail as detail # <module 'cv2.detail'>
import cv2.dnn as dnn # <module 'cv2.dnn'>
import cv2.fisheye as fisheye # <module 'cv2.fisheye'>
import cv2.flann as flann # <module 'cv2.flann'>
import cv2.instr as instr # <module 'cv2.instr'>
import cv2.ipp as ipp # <module 'cv2.ipp'>
import cv2.ml as ml # <module 'cv2.ml'>
import cv2.ocl as ocl # <module 'cv2.ocl'>
import cv2.ogl as ogl # <module 'cv2.ogl'>
import cv2.samples as samples # <module 'cv2.samples'>
import cv2.utils as utils # <module 'cv2.utils'>
import cv2.videoio_registry as videoio_registry # <module 'cv2.videoio_registry'>
import cv2 as __cv2


from .object import object

class Algorithm(object):
    # no doc
    def clear(self): # real signature unknown; restored from __doc__
        """
        clear() -> None
        .   @brief Clears the algorithm state
        """
        pass

    def empty(self): # real signature unknown; restored from __doc__
        """
        empty() -> retval
        .   @brief Returns true if the Algorithm is empty (e.g. in the very beginning or after unsuccessful read
        """
        pass

    def getDefaultName(self): # real signature unknown; restored from __doc__
        """
        getDefaultName() -> retval
        .   Returns the algorithm string identifier.
        .   This string is used as top level xml/yml node tag when the object is saved to a file or string.
        """
        pass

    def read(self, fn): # real signature unknown; restored from __doc__
        """
        read(fn) -> None
        .   @brief Reads algorithm parameters from a file storage
        """
        pass

    def save(self, filename): # real signature unknown; restored from __doc__
        """
        save(filename) -> None
        .   Saves the algorithm to a file.
        .   In order to make this method work, the derived class must implement Algorithm::write(FileStorage& fs).
        """
        pass

    def write(self, fs, name=None): # real signature unknown; restored from __doc__
        """
        write(fs[, name]) -> None
        .   @brief simplified API for language bindings
        .   * @overload
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass


