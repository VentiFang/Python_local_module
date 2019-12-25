# encoding: utf-8
# module twisted.test.raiser
# from F:\Python\Python36\lib\site-packages\twisted\test\raiser.cp36-win_amd64.pyd
# by generator 1.147
"""
A trivial extension that just raises an exception.
See L{twisted.test.test_failure.test_failureConstructionWithMungedStackSucceeds}.
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

# functions

def raiseException(*args, **kwargs): # real signature unknown
    """ Raise L{RaiserException}. """
    pass

# classes

class RaiserException(Exception):
    """ A speficic exception only used to be identified in tests. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000022CDE92C470>'

__spec__ = None # (!) real value is "ModuleSpec(name='twisted.test.raiser', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000022CDE92C470>, origin='F:\\\\Python\\\\Python36\\\\lib\\\\site-packages\\\\twisted\\\\test\\\\raiser.cp36-win_amd64.pyd')"

__test__ = {}

