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


class AlignMTB(__cv2.AlignExposures):
    # no doc
    def calculateShift(self, img0, img1): # real signature unknown; restored from __doc__
        """
        calculateShift(img0, img1) -> retval
        .   @brief Calculates shift between two images, i. e. how to shift the second image to correspond it with the
        .   first.
        .   
        .   @param img0 first image
        .   @param img1 second image
        """
        pass

    def computeBitmaps(self, img, tb=None, eb=None): # real signature unknown; restored from __doc__
        """
        computeBitmaps(img[, tb[, eb]]) -> tb, eb
        .   @brief Computes median threshold and exclude bitmaps of given image.
        .   
        .   @param img input image
        .   @param tb median threshold bitmap
        .   @param eb exclude bitmap
        """
        pass

    def getCut(self): # real signature unknown; restored from __doc__
        """
        getCut() -> retval
        .
        """
        pass

    def getExcludeRange(self): # real signature unknown; restored from __doc__
        """
        getExcludeRange() -> retval
        .
        """
        pass

    def getMaxBits(self): # real signature unknown; restored from __doc__
        """
        getMaxBits() -> retval
        .
        """
        pass

    def process(self, src, dst, times, response): # real signature unknown; restored from __doc__
        """
        process(src, dst, times, response) -> None
        .   
        
        
        
        process(src, dst) -> None
        .   @brief Short version of process, that doesn't take extra arguments.
        .   
        .   @param src vector of input images
        .   @param dst vector of aligned images
        """
        pass

    def setCut(self, value): # real signature unknown; restored from __doc__
        """
        setCut(value) -> None
        .
        """
        pass

    def setExcludeRange(self, exclude_range): # real signature unknown; restored from __doc__
        """
        setExcludeRange(exclude_range) -> None
        .
        """
        pass

    def setMaxBits(self, max_bits): # real signature unknown; restored from __doc__
        """
        setMaxBits(max_bits) -> None
        .
        """
        pass

    def shiftMat(self, src, shift, dst=None): # real signature unknown; restored from __doc__
        """
        shiftMat(src, shift[, dst]) -> dst
        .   @brief Helper function, that shift Mat filling new regions with zeros.
        .   
        .   @param src input image
        .   @param dst result image
        .   @param shift shift value
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


