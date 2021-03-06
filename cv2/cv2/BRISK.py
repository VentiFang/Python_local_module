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


class BRISK(__cv2.Feature2D):
    # no doc
    def create(self, thresh=None, octaves=None, patternScale=None): # real signature unknown; restored from __doc__
        """
        create([, thresh[, octaves[, patternScale]]]) -> retval
        .   @brief The BRISK constructor
        .   
        .   @param thresh AGAST detection threshold score.
        .   @param octaves detection octaves. Use 0 to do single scale.
        .   @param patternScale apply this scale to the pattern used for sampling the neighbourhood of a
        .   keypoint.
        
        
        
        create(radiusList, numberList[, dMax[, dMin[, indexChange]]]) -> retval
        .   @brief The BRISK constructor for a custom pattern
        .   
        .   @param radiusList defines the radii (in pixels) where the samples around a keypoint are taken (for
        .   keypoint scale 1).
        .   @param numberList defines the number of sampling points on the sampling circle. Must be the same
        .   size as radiusList..
        .   @param dMax threshold for the short pairings used for descriptor formation (in pixels for keypoint
        .   scale 1).
        .   @param dMin threshold for the long pairings used for orientation determination (in pixels for
        .   keypoint scale 1).
        .   @param indexChange index remapping of the bits.
        
        
        
        create(thresh, octaves, radiusList, numberList[, dMax[, dMin[, indexChange]]]) -> retval
        .   @brief The BRISK constructor for a custom pattern, detection threshold and octaves
        .   
        .   @param thresh AGAST detection threshold score.
        .   @param octaves detection octaves. Use 0 to do single scale.
        .   @param radiusList defines the radii (in pixels) where the samples around a keypoint are taken (for
        .   keypoint scale 1).
        .   @param numberList defines the number of sampling points on the sampling circle. Must be the same
        .   size as radiusList..
        .   @param dMax threshold for the short pairings used for descriptor formation (in pixels for keypoint
        .   scale 1).
        .   @param dMin threshold for the long pairings used for orientation determination (in pixels for
        .   keypoint scale 1).
        .   @param indexChange index remapping of the bits.
        """
        pass

    def getDefaultName(self): # real signature unknown; restored from __doc__
        """
        getDefaultName() -> retval
        .
        """
        pass

    def getOctaves(self): # real signature unknown; restored from __doc__
        """
        getOctaves() -> retval
        .
        """
        pass

    def getThreshold(self): # real signature unknown; restored from __doc__
        """
        getThreshold() -> retval
        .
        """
        pass

    def setOctaves(self, octaves): # real signature unknown; restored from __doc__
        """
        setOctaves(octaves) -> None
        .   @brief Set detection octaves.
        .   @param octaves detection octaves. Use 0 to do single scale.
        """
        pass

    def setThreshold(self, threshold): # real signature unknown; restored from __doc__
        """
        setThreshold(threshold) -> None
        .   @brief Set detection threshold.
        .   @param threshold AGAST detection threshold score.
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


