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


class AKAZE(__cv2.Feature2D):
    # no doc
    def create(self, descriptor_type=None, descriptor_size=None, descriptor_channels=None, threshold=None, nOctaves=None, nOctaveLayers=None, diffusivity=None): # real signature unknown; restored from __doc__
        """
        create([, descriptor_type[, descriptor_size[, descriptor_channels[, threshold[, nOctaves[, nOctaveLayers[, diffusivity]]]]]]]) -> retval
        .   @brief The AKAZE constructor
        .   
        .   @param descriptor_type Type of the extracted descriptor: DESCRIPTOR_KAZE,
        .   DESCRIPTOR_KAZE_UPRIGHT, DESCRIPTOR_MLDB or DESCRIPTOR_MLDB_UPRIGHT.
        .   @param descriptor_size Size of the descriptor in bits. 0 -\> Full size
        .   @param descriptor_channels Number of channels in the descriptor (1, 2, 3)
        .   @param threshold Detector response threshold to accept point
        .   @param nOctaves Maximum octave evolution of the image
        .   @param nOctaveLayers Default number of sublevels per scale level
        .   @param diffusivity Diffusivity type. DIFF_PM_G1, DIFF_PM_G2, DIFF_WEICKERT or
        .   DIFF_CHARBONNIER
        """
        pass

    def getDefaultName(self): # real signature unknown; restored from __doc__
        """
        getDefaultName() -> retval
        .
        """
        pass

    def getDescriptorChannels(self): # real signature unknown; restored from __doc__
        """
        getDescriptorChannels() -> retval
        .
        """
        pass

    def getDescriptorSize(self): # real signature unknown; restored from __doc__
        """
        getDescriptorSize() -> retval
        .
        """
        pass

    def getDescriptorType(self): # real signature unknown; restored from __doc__
        """
        getDescriptorType() -> retval
        .
        """
        pass

    def getDiffusivity(self): # real signature unknown; restored from __doc__
        """
        getDiffusivity() -> retval
        .
        """
        pass

    def getNOctaveLayers(self): # real signature unknown; restored from __doc__
        """
        getNOctaveLayers() -> retval
        .
        """
        pass

    def getNOctaves(self): # real signature unknown; restored from __doc__
        """
        getNOctaves() -> retval
        .
        """
        pass

    def getThreshold(self): # real signature unknown; restored from __doc__
        """
        getThreshold() -> retval
        .
        """
        pass

    def setDescriptorChannels(self, dch): # real signature unknown; restored from __doc__
        """
        setDescriptorChannels(dch) -> None
        .
        """
        pass

    def setDescriptorSize(self, dsize): # real signature unknown; restored from __doc__
        """
        setDescriptorSize(dsize) -> None
        .
        """
        pass

    def setDescriptorType(self, dtype): # real signature unknown; restored from __doc__
        """
        setDescriptorType(dtype) -> None
        .
        """
        pass

    def setDiffusivity(self, diff): # real signature unknown; restored from __doc__
        """
        setDiffusivity(diff) -> None
        .
        """
        pass

    def setNOctaveLayers(self, octaveLayers): # real signature unknown; restored from __doc__
        """
        setNOctaveLayers(octaveLayers) -> None
        .
        """
        pass

    def setNOctaves(self, octaves): # real signature unknown; restored from __doc__
        """
        setNOctaves(octaves) -> None
        .
        """
        pass

    def setThreshold(self, threshold): # real signature unknown; restored from __doc__
        """
        setThreshold(threshold) -> None
        .
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


