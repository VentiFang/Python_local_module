# encoding: utf-8
# module twisted.internet.iocpreactor.iocpsupport
# from F:\Python\Python36\lib\site-packages\twisted\internet\iocpreactor\iocpsupport.cp36-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import socket as socket # F:\Python\Python36\lib\socket.py

# Variables with simple values

have_connectex = True

# functions

def accept(*args, **kwargs): # real signature unknown
    """ CAUTION: unlike system AcceptEx(), this function returns 0 on success """
    pass

def connect(*args, **kwargs): # real signature unknown
    """ CAUTION: unlike system ConnectEx(), this function returns 0 on success """
    pass

def get_accept_addrs(*args, **kwargs): # real signature unknown
    pass

def makesockaddr(*args, **kwargs): # real signature unknown
    pass

def maxAddrLen(*args, **kwargs): # real signature unknown
    pass

def recv(*args, **kwargs): # real signature unknown
    pass

def recvfrom(*args, **kwargs): # real signature unknown
    pass

def send(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_CompletionPort(*args, **kwargs): # real signature unknown
    pass

# classes

class CompletionPort(object):
    # no doc
    def addHandle(self, *args, **kwargs): # real signature unknown
        pass

    def getEvent(self, *args, **kwargs): # real signature unknown
        pass

    def postEvent(self, *args, **kwargs): # real signature unknown
        pass

    def __del__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass


class Event(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'iocpsupport', '__init__': <cyfunction Event.__init__ at 0x00000234B9F339A0>, '__dict__': <attribute '__dict__' of 'Event' objects>, '__weakref__': <attribute '__weakref__' of 'Event' objects>, '__doc__': None})"


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x00000234BA78A208>'

__spec__ = None # (!) real value is "ModuleSpec(name='twisted.internet.iocpreactor.iocpsupport', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x00000234BA78A208>, origin='F:\\\\Python\\\\Python36\\\\lib\\\\site-packages\\\\twisted\\\\internet\\\\iocpreactor\\\\iocpsupport.cp36-win_amd64.pyd')"

__test__ = {}

