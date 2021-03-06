# encoding: utf-8
# module PyQt5.QtSensors
# from F:\Python\Python36\lib\site-packages\PyQt5\QtSensors.pyd
# by generator 1.147
# no doc

# imports
import PyQt5.QtCore as __PyQt5_QtCore
import sip as __sip


from .QSensor import QSensor

class QAccelerometer(QSensor):
    """ QAccelerometer(parent: QObject = None) """
    def accelerationMode(self): # real signature unknown; restored from __doc__
        """ accelerationMode(self) -> QAccelerometer.AccelerationMode """
        pass

    def accelerationModeChanged(self, QAccelerometer_AccelerationMode): # real signature unknown; restored from __doc__
        """ accelerationModeChanged(self, QAccelerometer.AccelerationMode) [signal] """
        pass

    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def reading(self): # real signature unknown; restored from __doc__
        """ reading(self) -> QAccelerometerReading """
        return QAccelerometerReading

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setAccelerationMode(self, QAccelerometer_AccelerationMode): # real signature unknown; restored from __doc__
        """ setAccelerationMode(self, QAccelerometer.AccelerationMode) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, parent=None): # real signature unknown; restored from __doc__
        pass

    Combined = 0
    Gravity = 1
    User = 2


