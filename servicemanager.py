# encoding: utf-8
# module servicemanager
# from F:\Python\Python36\lib\site-packages\win32\servicemanager.pyd
# by generator 1.147
# no doc

# imports
from win32._servicemanager import (CoInitializeEx, CoUninitialize, Debugging, 
    Finalize, Initialize, LogErrorMsg, LogInfoMsg, LogMsg, LogWarningMsg, 
    PrepareToHostMultiple, PrepareToHostSingle, PumpWaitingMessages, 
    RegisterServiceCtrlHandler, RunningAsService, SetEventSourceName, 
    StartServiceCtrlDispatcher)


# Variables with simple values

COINIT_APARTMENTTHREADED = 2

COINIT_DISABLE_OLE1DDE = 4

COINIT_MULTITHREADED = 0

COINIT_SPEED_OVER_MEMORY = 8

EVENTLOG_AUDIT_FAILURE = 16
EVENTLOG_AUDIT_SUCCESS = 8

EVENTLOG_ERROR_TYPE = 1

EVENTLOG_INFORMATION_TYPE = 4

EVENTLOG_WARNING_TYPE = 2

PYS_SERVICE_STARTED = 1073745922
PYS_SERVICE_STARTING = 1073745920
PYS_SERVICE_STOPPED = 1073745924
PYS_SERVICE_STOPPING = 1073745923

__cached__ = 'F:\\Python\\Python36\\lib\\site-packages\\win32\\servicemanager\\__pycache__\\__init__.cpython-36.pyc'

# no functions
# classes

class startup_error(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.SourceFileLoader object at 0x000002B66ECAE9B0>'

__path__ = [
    'F:\\Python\\Python36\\lib\\site-packages\\win32\\servicemanager',
]

__spec__ = None # (!) real value is "ModuleSpec(name='servicemanager', loader=<_frozen_importlib_external.SourceFileLoader object at 0x000002B66ECAE9B0>, origin='F:\\\\Python\\\\Python36\\\\lib\\\\site-packages\\\\win32\\\\servicemanager\\\\__init__.py', submodule_search_locations=['F:\\\\Python\\\\Python36\\\\lib\\\\site-packages\\\\win32\\\\servicemanager'])"

