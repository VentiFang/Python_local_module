# encoding: utf-8
# module PyQt5.QtCore
# from F:\Python\Python36\lib\site-packages\PyQt5\QtCore.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import sip as __sip


from .QObject import QObject

class QLibrary(QObject):
    """
    QLibrary(parent: QObject = None)
    QLibrary(str, parent: QObject = None)
    QLibrary(str, int, parent: QObject = None)
    QLibrary(str, str, parent: QObject = None)
    """
    def childEvent(self, *args, **kwargs): # real signature unknown
        pass

    def connectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def customEvent(self, *args, **kwargs): # real signature unknown
        pass

    def disconnectNotify(self, *args, **kwargs): # real signature unknown
        pass

    def errorString(self): # real signature unknown; restored from __doc__
        """ errorString(self) -> str """
        return ""

    def fileName(self): # real signature unknown; restored from __doc__
        """ fileName(self) -> str """
        return ""

    def isLibrary(self, p_str): # real signature unknown; restored from __doc__
        """ isLibrary(str) -> bool """
        return False

    def isLoaded(self): # real signature unknown; restored from __doc__
        """ isLoaded(self) -> bool """
        return False

    def isSignalConnected(self, *args, **kwargs): # real signature unknown
        pass

    def load(self): # real signature unknown; restored from __doc__
        """ load(self) -> bool """
        return False

    def loadHints(self): # real signature unknown; restored from __doc__
        """ loadHints(self) -> QLibrary.LoadHints """
        pass

    def receivers(self, *args, **kwargs): # real signature unknown
        pass

    def resolve(self, p_str, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        resolve(self, str) -> sip.voidptr
        resolve(str, str) -> sip.voidptr
        resolve(str, int, str) -> sip.voidptr
        resolve(str, str, str) -> sip.voidptr
        """
        pass

    def sender(self, *args, **kwargs): # real signature unknown
        pass

    def senderSignalIndex(self, *args, **kwargs): # real signature unknown
        pass

    def setFileName(self, p_str): # real signature unknown; restored from __doc__
        """ setFileName(self, str) """
        pass

    def setFileNameAndVersion(self, p_str, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        """
        setFileNameAndVersion(self, str, int)
        setFileNameAndVersion(self, str, str)
        """
        pass

    def setLoadHints(self, Union, QLibrary_LoadHints=None, QLibrary_LoadHint=None): # real signature unknown; restored from __doc__
        """ setLoadHints(self, Union[QLibrary.LoadHints, QLibrary.LoadHint]) """
        pass

    def timerEvent(self, *args, **kwargs): # real signature unknown
        pass

    def unload(self): # real signature unknown; restored from __doc__
        """ unload(self) -> bool """
        return False

    def __init__(self, *__args): # real signature unknown; restored from __doc__ with multiple overloads
        pass

    DeepBindHint = 16
    ExportExternalSymbolsHint = 2
    LoadArchiveMemberHint = 4
    PreventUnloadHint = 8
    ResolveAllSymbolsHint = 1


