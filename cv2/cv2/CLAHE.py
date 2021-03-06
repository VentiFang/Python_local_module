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


class CLAHE(__cv2.Algorithm):
    # no doc
    def apply(self, src, dst=None): # real signature unknown; restored from __doc__
        """
        apply(src[, dst]) -> dst
        .   @brief Equalizes the histogram of a grayscale image using Contrast Limited Adaptive Histogram Equalization.
        .   
        .   @param src Source image of type CV_8UC1 or CV_16UC1.
        .   @param dst Destination image.
        """
        pass

    def collectGarbage(self): # real signature unknown; restored from __doc__
        """
        collectGarbage() -> None
        .
        """
        pass

    def getClipLimit(self): # real signature unknown; restored from __doc__
        """
        getClipLimit() -> retval
        .
        """
        pass

    def getTilesGridSize(self): # real signature unknown; restored from __doc__
        """
        getTilesGridSize() -> retval
        .
        """
        pass

    def setClipLimit(self, clipLimit): # real signature unknown; restored from __doc__
        """
        setClipLimit(clipLimit) -> None
        .   @brief Sets threshold for contrast limiting.
        .   
        .   @param clipLimit threshold value.
        """
        pass

    def setTilesGridSize(self, tileGridSize): # real signature unknown; restored from __doc__
        """
        setTilesGridSize(tileGridSize) -> None
        .   @brief Sets size of grid for histogram equalization. Input image will be divided into
        .   equally sized rectangular tiles.
        .   
        .   @param tileGridSize defines the number of tiles in row and column.
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


