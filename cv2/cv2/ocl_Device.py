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

class ocl_Device(object):
    # no doc
    def addressBits(self): # real signature unknown; restored from __doc__
        """
        addressBits() -> retval
        .
        """
        pass

    def available(self): # real signature unknown; restored from __doc__
        """
        available() -> retval
        .
        """
        pass

    def compilerAvailable(self): # real signature unknown; restored from __doc__
        """
        compilerAvailable() -> retval
        .
        """
        pass

    def deviceVersionMajor(self): # real signature unknown; restored from __doc__
        """
        deviceVersionMajor() -> retval
        .
        """
        pass

    def deviceVersionMinor(self): # real signature unknown; restored from __doc__
        """
        deviceVersionMinor() -> retval
        .
        """
        pass

    def doubleFPConfig(self): # real signature unknown; restored from __doc__
        """
        doubleFPConfig() -> retval
        .
        """
        pass

    def driverVersion(self): # real signature unknown; restored from __doc__
        """
        driverVersion() -> retval
        .
        """
        pass

    def endianLittle(self): # real signature unknown; restored from __doc__
        """
        endianLittle() -> retval
        .
        """
        pass

    def errorCorrectionSupport(self): # real signature unknown; restored from __doc__
        """
        errorCorrectionSupport() -> retval
        .
        """
        pass

    def executionCapabilities(self): # real signature unknown; restored from __doc__
        """
        executionCapabilities() -> retval
        .
        """
        pass

    def extensions(self): # real signature unknown; restored from __doc__
        """
        extensions() -> retval
        .
        """
        pass

    def getDefault(self): # real signature unknown; restored from __doc__
        """
        getDefault() -> retval
        .
        """
        pass

    def globalMemCacheLineSize(self): # real signature unknown; restored from __doc__
        """
        globalMemCacheLineSize() -> retval
        .
        """
        pass

    def globalMemCacheSize(self): # real signature unknown; restored from __doc__
        """
        globalMemCacheSize() -> retval
        .
        """
        pass

    def globalMemCacheType(self): # real signature unknown; restored from __doc__
        """
        globalMemCacheType() -> retval
        .
        """
        pass

    def globalMemSize(self): # real signature unknown; restored from __doc__
        """
        globalMemSize() -> retval
        .
        """
        pass

    def halfFPConfig(self): # real signature unknown; restored from __doc__
        """
        halfFPConfig() -> retval
        .
        """
        pass

    def hostUnifiedMemory(self): # real signature unknown; restored from __doc__
        """
        hostUnifiedMemory() -> retval
        .
        """
        pass

    def image2DMaxHeight(self): # real signature unknown; restored from __doc__
        """
        image2DMaxHeight() -> retval
        .
        """
        pass

    def image2DMaxWidth(self): # real signature unknown; restored from __doc__
        """
        image2DMaxWidth() -> retval
        .
        """
        pass

    def image3DMaxDepth(self): # real signature unknown; restored from __doc__
        """
        image3DMaxDepth() -> retval
        .
        """
        pass

    def image3DMaxHeight(self): # real signature unknown; restored from __doc__
        """
        image3DMaxHeight() -> retval
        .
        """
        pass

    def image3DMaxWidth(self): # real signature unknown; restored from __doc__
        """
        image3DMaxWidth() -> retval
        .
        """
        pass

    def imageFromBufferSupport(self): # real signature unknown; restored from __doc__
        """
        imageFromBufferSupport() -> retval
        .
        """
        pass

    def imageMaxArraySize(self): # real signature unknown; restored from __doc__
        """
        imageMaxArraySize() -> retval
        .
        """
        pass

    def imageMaxBufferSize(self): # real signature unknown; restored from __doc__
        """
        imageMaxBufferSize() -> retval
        .
        """
        pass

    def imageSupport(self): # real signature unknown; restored from __doc__
        """
        imageSupport() -> retval
        .
        """
        pass

    def intelSubgroupsSupport(self): # real signature unknown; restored from __doc__
        """
        intelSubgroupsSupport() -> retval
        .
        """
        pass

    def isAMD(self): # real signature unknown; restored from __doc__
        """
        isAMD() -> retval
        .
        """
        pass

    def isExtensionSupported(self, extensionName): # real signature unknown; restored from __doc__
        """
        isExtensionSupported(extensionName) -> retval
        .
        """
        pass

    def isIntel(self): # real signature unknown; restored from __doc__
        """
        isIntel() -> retval
        .
        """
        pass

    def isNVidia(self): # real signature unknown; restored from __doc__
        """
        isNVidia() -> retval
        .
        """
        pass

    def linkerAvailable(self): # real signature unknown; restored from __doc__
        """
        linkerAvailable() -> retval
        .
        """
        pass

    def localMemSize(self): # real signature unknown; restored from __doc__
        """
        localMemSize() -> retval
        .
        """
        pass

    def localMemType(self): # real signature unknown; restored from __doc__
        """
        localMemType() -> retval
        .
        """
        pass

    def maxClockFrequency(self): # real signature unknown; restored from __doc__
        """
        maxClockFrequency() -> retval
        .
        """
        pass

    def maxComputeUnits(self): # real signature unknown; restored from __doc__
        """
        maxComputeUnits() -> retval
        .
        """
        pass

    def maxConstantArgs(self): # real signature unknown; restored from __doc__
        """
        maxConstantArgs() -> retval
        .
        """
        pass

    def maxConstantBufferSize(self): # real signature unknown; restored from __doc__
        """
        maxConstantBufferSize() -> retval
        .
        """
        pass

    def maxMemAllocSize(self): # real signature unknown; restored from __doc__
        """
        maxMemAllocSize() -> retval
        .
        """
        pass

    def maxParameterSize(self): # real signature unknown; restored from __doc__
        """
        maxParameterSize() -> retval
        .
        """
        pass

    def maxReadImageArgs(self): # real signature unknown; restored from __doc__
        """
        maxReadImageArgs() -> retval
        .
        """
        pass

    def maxSamplers(self): # real signature unknown; restored from __doc__
        """
        maxSamplers() -> retval
        .
        """
        pass

    def maxWorkGroupSize(self): # real signature unknown; restored from __doc__
        """
        maxWorkGroupSize() -> retval
        .
        """
        pass

    def maxWorkItemDims(self): # real signature unknown; restored from __doc__
        """
        maxWorkItemDims() -> retval
        .
        """
        pass

    def maxWriteImageArgs(self): # real signature unknown; restored from __doc__
        """
        maxWriteImageArgs() -> retval
        .
        """
        pass

    def memBaseAddrAlign(self): # real signature unknown; restored from __doc__
        """
        memBaseAddrAlign() -> retval
        .
        """
        pass

    def name(self): # real signature unknown; restored from __doc__
        """
        name() -> retval
        .
        """
        pass

    def nativeVectorWidthChar(self): # real signature unknown; restored from __doc__
        """
        nativeVectorWidthChar() -> retval
        .
        """
        pass

    def nativeVectorWidthDouble(self): # real signature unknown; restored from __doc__
        """
        nativeVectorWidthDouble() -> retval
        .
        """
        pass

    def nativeVectorWidthFloat(self): # real signature unknown; restored from __doc__
        """
        nativeVectorWidthFloat() -> retval
        .
        """
        pass

    def nativeVectorWidthHalf(self): # real signature unknown; restored from __doc__
        """
        nativeVectorWidthHalf() -> retval
        .
        """
        pass

    def nativeVectorWidthInt(self): # real signature unknown; restored from __doc__
        """
        nativeVectorWidthInt() -> retval
        .
        """
        pass

    def nativeVectorWidthLong(self): # real signature unknown; restored from __doc__
        """
        nativeVectorWidthLong() -> retval
        .
        """
        pass

    def nativeVectorWidthShort(self): # real signature unknown; restored from __doc__
        """
        nativeVectorWidthShort() -> retval
        .
        """
        pass

    def OpenCLVersion(self): # real signature unknown; restored from __doc__
        """
        OpenCLVersion() -> retval
        .
        """
        pass

    def OpenCL_C_Version(self): # real signature unknown; restored from __doc__
        """
        OpenCL_C_Version() -> retval
        .
        """
        pass

    def preferredVectorWidthChar(self): # real signature unknown; restored from __doc__
        """
        preferredVectorWidthChar() -> retval
        .
        """
        pass

    def preferredVectorWidthDouble(self): # real signature unknown; restored from __doc__
        """
        preferredVectorWidthDouble() -> retval
        .
        """
        pass

    def preferredVectorWidthFloat(self): # real signature unknown; restored from __doc__
        """
        preferredVectorWidthFloat() -> retval
        .
        """
        pass

    def preferredVectorWidthHalf(self): # real signature unknown; restored from __doc__
        """
        preferredVectorWidthHalf() -> retval
        .
        """
        pass

    def preferredVectorWidthInt(self): # real signature unknown; restored from __doc__
        """
        preferredVectorWidthInt() -> retval
        .
        """
        pass

    def preferredVectorWidthLong(self): # real signature unknown; restored from __doc__
        """
        preferredVectorWidthLong() -> retval
        .
        """
        pass

    def preferredVectorWidthShort(self): # real signature unknown; restored from __doc__
        """
        preferredVectorWidthShort() -> retval
        .
        """
        pass

    def printfBufferSize(self): # real signature unknown; restored from __doc__
        """
        printfBufferSize() -> retval
        .
        """
        pass

    def profilingTimerResolution(self): # real signature unknown; restored from __doc__
        """
        profilingTimerResolution() -> retval
        .
        """
        pass

    def singleFPConfig(self): # real signature unknown; restored from __doc__
        """
        singleFPConfig() -> retval
        .
        """
        pass

    def type(self): # real signature unknown; restored from __doc__
        """
        type() -> retval
        .
        """
        pass

    def vendorID(self): # real signature unknown; restored from __doc__
        """
        vendorID() -> retval
        .
        """
        pass

    def vendorName(self): # real signature unknown; restored from __doc__
        """
        vendorName() -> retval
        .
        """
        pass

    def version(self): # real signature unknown; restored from __doc__
        """
        version() -> retval
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


