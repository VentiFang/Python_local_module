# encoding: utf-8
# module types
# from F:\Python\Python36\lib\site-packages\win32\types.cp36-win_amd64.pyd
# by generator 1.147
""" Define names for built-in types that aren't directly accessible as a builtin. """

# imports
import functools as _functools # F:\Python\Python36\lib\functools.py
import collections.abc as _collections_abc # F:\Python\Python36\lib\collections\abc.py

# Variables with simple values

__cached__ = 'F:\\Python\\Python36\\lib\\__pycache__\\types.cpython-36.pyc'

# functions

def coroutine(func): # reliably restored by inspect
    """ Convert regular generator function to a coroutine. """
    pass

def new_class(name, bases='()', kwds=None, exec_body=None): # reliably restored by inspect
    """ Create a class object dynamically using the appropriate metaclass. """
    pass

def prepare_class(name, bases='()', kwds=None): # reliably restored by inspect
    """
    Call the __prepare__ method of the appropriate metaclass.
    
        Returns (metaclass, namespace, kwds) as a 3-tuple
    
        *metaclass* is the appropriate metaclass
        *namespace* is the prepared class namespace
        *kwds* is an updated copy of the passed in kwds argument with any
        'metaclass' entry removed. If no kwds argument is passed in, this will
        be an empty dict.
    """
    pass

def _calculate_meta(meta, bases): # reliably restored by inspect
    """ Calculate the most derived metaclass. """
    pass

# classes

class AsyncGeneratorType(object):
    # no doc
    def aclose(self): # real signature unknown; restored from __doc__
        """ aclose() -> raise GeneratorExit inside generator. """
        pass

    def asend(self, v): # real signature unknown; restored from __doc__
        """ asend(v) -> send 'v' in generator. """
        pass

    def athrow(self, typ, val=None, tb=None): # real signature unknown; restored from __doc__
        """ athrow(typ[,val[,tb]]) -> raise exception in generator. """
        pass

    def __aiter__(self, *args, **kwargs): # real signature unknown
        """ Return an awaitable, that resolves in asynchronous iterator. """
        pass

    def __anext__(self, *args, **kwargs): # real signature unknown
        """ Return a value or raise StopAsyncIteration. """
        pass

    def __del__(self, *args, **kwargs): # real signature unknown
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    ag_await = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """object being awaited on, or None"""

    ag_code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ag_frame = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ag_running = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __name__ = 'async_generator'
    __qualname__ = 'async_generator'


class BuiltinMethodType(object):
    def __call__(self, *args, **kwargs): # real signature unknown
        """ Call self as a function. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    __self__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __name__ = 'builtin_function_or_method'
    __qualname__ = 'builtin_function_or_method'
    __text_signature__ = None


BuiltinFunctionType = BuiltinMethodType


class CodeType(object):
    """
    code(argcount, kwonlyargcount, nlocals, stacksize, flags, codestring,
          constants, names, varnames, filename, name, firstlineno,
          lnotab[, freevars[, cellvars]])
    
    Create a code object.  Not for the faint of heart.
    """
    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        pass

    co_argcount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    co_cellvars = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    co_code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    co_consts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    co_filename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    co_firstlineno = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    co_flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    co_freevars = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    co_kwonlyargcount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    co_lnotab = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    co_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    co_names = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    co_nlocals = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    co_stacksize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    co_varnames = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class CoroutineType(object):
    # no doc
    def close(self): # real signature unknown; restored from __doc__
        """ close() -> raise GeneratorExit inside coroutine. """
        pass

    def send(self, arg): # real signature unknown; restored from __doc__
        """
        send(arg) -> send 'arg' into coroutine,
        return next iterated value or raise StopIteration.
        """
        pass

    def throw(self, typ, val=None, tb=None): # real signature unknown; restored from __doc__
        """
        throw(typ[,val[,tb]]) -> raise exception in coroutine,
        return next iterated value or raise StopIteration.
        """
        pass

    def __await__(self, *args, **kwargs): # real signature unknown
        """ Return an iterator to be used in await expression. """
        pass

    def __del__(self, *args, **kwargs): # real signature unknown
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    cr_await = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """object being awaited on, or None"""

    cr_code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    cr_frame = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    cr_running = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __name__ = 'coroutine'
    __qualname__ = 'coroutine'


class DynamicClassAttribute(object):
    """
    Route attribute access on a class to __getattr__.
    
        This is a descriptor, used to define attributes that act differently when
        accessed through an instance and through a class.  Instance access remains
        normal, but access to an attribute through a class will be routed to the
        class's __getattr__ method; this is done by raising AttributeError.
    
        This allows one to have properties active on an instance, and have virtual
        attributes on the class with the same name (see Enum for an example).
    """
    def deleter(self, fdel): # reliably restored by inspect
        # no doc
        pass

    def getter(self, fget): # reliably restored by inspect
        # no doc
        pass

    def setter(self, fset): # reliably restored by inspect
        # no doc
        pass

    def __delete__(self, instance): # reliably restored by inspect
        # no doc
        pass

    def __get__(self, instance, ownerclass=None): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, fget=None, fset=None, fdel=None, doc=None): # reliably restored by inspect
        # no doc
        pass

    def __set__(self, instance, value): # reliably restored by inspect
        # no doc
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'types\', \'__doc__\': "Route attribute access on a class to __getattr__.\\n\\n    This is a descriptor, used to define attributes that act differently when\\n    accessed through an instance and through a class.  Instance access remains\\n    normal, but access to an attribute through a class will be routed to the\\n    class\'s __getattr__ method; this is done by raising AttributeError.\\n\\n    This allows one to have properties active on an instance, and have virtual\\n    attributes on the class with the same name (see Enum for an example).\\n\\n    ", \'__init__\': <function DynamicClassAttribute.__init__ at 0x000001C5B9B8FF28>, \'__get__\': <function DynamicClassAttribute.__get__ at 0x000001C5B9B97048>, \'__set__\': <function DynamicClassAttribute.__set__ at 0x000001C5B9B970D0>, \'__delete__\': <function DynamicClassAttribute.__delete__ at 0x000001C5B9B97158>, \'getter\': <function DynamicClassAttribute.getter at 0x000001C5B9B971E0>, \'setter\': <function DynamicClassAttribute.setter at 0x000001C5B9B97268>, \'deleter\': <function DynamicClassAttribute.deleter at 0x000001C5B9B972F0>, \'__dict__\': <attribute \'__dict__\' of \'DynamicClassAttribute\' objects>, \'__weakref__\': <attribute \'__weakref__\' of \'DynamicClassAttribute\' objects>})'


class FrameType(object):
    # no doc
    def clear(self): # real signature unknown; restored from __doc__
        """ F.clear(): clear most references held by the frame """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __sizeof__(self): # real signature unknown; restored from __doc__
        """ F.__sizeof__() -> size of F in memory, in bytes """
        pass

    f_back = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    f_builtins = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    f_code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    f_globals = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    f_lasti = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    f_lineno = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    f_locals = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    f_trace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class LambdaType(object):
    """
    function(code, globals[, name[, argdefs[, closure]]])
    
    Create a function object from a code object and a dictionary.
    The optional name string overrides the name from the code object.
    The optional argdefs tuple specifies the default argument values.
    The optional closure tuple supplies the bindings for free variables.
    """
    def __call__(self, *args, **kwargs): # real signature unknown
        """ Call self as a function. """
        pass

    def __get__(self, *args, **kwargs): # real signature unknown
        """ Return an attribute of instance, which is of type owner. """
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

    __annotations__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __closure__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __code__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __defaults__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __globals__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __kwdefaults__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'__repr__': <slot wrapper '__repr__' of 'function' objects>, '__call__': <slot wrapper '__call__' of 'function' objects>, '__get__': <slot wrapper '__get__' of 'function' objects>, '__new__': <built-in method __new__ of type object at 0x0000000063E98A00>, '__closure__': <member '__closure__' of 'function' objects>, '__doc__': <member '__doc__' of 'function' objects>, '__globals__': <member '__globals__' of 'function' objects>, '__module__': <member '__module__' of 'function' objects>, '__code__': <attribute '__code__' of 'function' objects>, '__defaults__': <attribute '__defaults__' of 'function' objects>, '__kwdefaults__': <attribute '__kwdefaults__' of 'function' objects>, '__annotations__': <attribute '__annotations__' of 'function' objects>, '__dict__': <attribute '__dict__' of 'function' objects>, '__name__': <attribute '__name__' of 'function' objects>, '__qualname__': <attribute '__qualname__' of 'function' objects>})"
    __name__ = 'function'
    __qualname__ = 'function'


FunctionType = LambdaType


class GeneratorType(object):
    # no doc
    def close(self): # real signature unknown; restored from __doc__
        """ close() -> raise GeneratorExit inside generator. """
        pass

    def send(self, arg): # real signature unknown; restored from __doc__
        """
        send(arg) -> send 'arg' into generator,
        return next yielded value or raise StopIteration.
        """
        pass

    def throw(self, typ, val=None, tb=None): # real signature unknown; restored from __doc__
        """
        throw(typ[,val[,tb]]) -> raise exception in generator,
        return next yielded value or raise StopIteration.
        """
        pass

    def __del__(self, *args, **kwargs): # real signature unknown
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    def __next__(self, *args, **kwargs): # real signature unknown
        """ Implement next(self). """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    gi_code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    gi_frame = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    gi_running = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    gi_yieldfrom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """object being iterated by yield from, or None"""


    __name__ = 'generator'
    __qualname__ = 'generator'


class GetSetDescriptorType(object):
    def __delete__(self, *args, **kwargs): # real signature unknown
        """ Delete an attribute of instance. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __get__(self, *args, **kwargs): # real signature unknown
        """ Return an attribute of instance, which is of type owner. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __set__(self, *args, **kwargs): # real signature unknown
        """ Set an attribute of instance to value. """
        pass

    __objclass__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __name__ = 'getset_descriptor'
    __qualname__ = 'getset_descriptor'


class MappingProxyType(object):
    # no doc
    def copy(self): # real signature unknown; restored from __doc__
        """ D.copy() -> a shallow copy of D """
        pass

    def get(self, k, d=None): # real signature unknown; restored from __doc__
        """ D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None. """
        pass

    def items(self): # real signature unknown; restored from __doc__
        """ D.items() -> list of D's (key, value) pairs, as 2-tuples """
        return []

    def keys(self): # real signature unknown; restored from __doc__
        """ D.keys() -> list of D's keys """
        return []

    def values(self): # real signature unknown; restored from __doc__
        """ D.values() -> list of D's values """
        return []

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return key in self. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    __hash__ = None


class MemberDescriptorType(object):
    def __delete__(self, *args, **kwargs): # real signature unknown
        """ Delete an attribute of instance. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __get__(self, *args, **kwargs): # real signature unknown
        """ Return an attribute of instance, which is of type owner. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __set__(self, *args, **kwargs): # real signature unknown
        """ Set an attribute of instance to value. """
        pass

    __objclass__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __name__ = 'member_descriptor'
    __qualname__ = 'member_descriptor'


class MethodType(object):
    """
    method(function, instance)
    
    Create a bound instance method object.
    """
    def __call__(self, *args, **kwargs): # real signature unknown
        """ Call self as a function. """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __get__(self, *args, **kwargs): # real signature unknown
        """ Return an attribute of instance, which is of type owner. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    __func__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the function (or other callable) implementing a method"""

    __self__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the instance to which a method is bound"""



class ModuleType(object):
    """
    module(name[, doc])
    
    Create a module object.
    The name must be a string; the optional doc argument can have any type.
    """
    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __dir__(self): # real signature unknown; restored from __doc__
        """
        __dir__() -> list
        specialized dir() implementation
        """
        return []

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
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

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    __dict__ = None # (!) real value is "mappingproxy({'__repr__': <slot wrapper '__repr__' of 'module' objects>, '__getattribute__': <slot wrapper '__getattribute__' of 'module' objects>, '__setattr__': <slot wrapper '__setattr__' of 'module' objects>, '__delattr__': <slot wrapper '__delattr__' of 'module' objects>, '__init__': <slot wrapper '__init__' of 'module' objects>, '__new__': <built-in method __new__ of type object at 0x0000000063E99FE0>, '__dir__': <method '__dir__' of 'module' objects>, '__dict__': <member '__dict__' of 'module' objects>, '__doc__': 'module(name[, doc])\\n\\nCreate a module object.\\nThe name must be a string; the optional doc argument can have any type.'})"


class SimpleNamespace(object):
    """
    A simple attribute-based namespace.
    
    SimpleNamespace(**kwargs)
    """
    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, **kwargs): # real signature unknown; restored from __doc__
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Return state information for pickling """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    __dict__ = None # (!) real value is "mappingproxy({'__repr__': <slot wrapper '__repr__' of 'types.SimpleNamespace' objects>, '__getattribute__': <slot wrapper '__getattribute__' of 'types.SimpleNamespace' objects>, '__setattr__': <slot wrapper '__setattr__' of 'types.SimpleNamespace' objects>, '__delattr__': <slot wrapper '__delattr__' of 'types.SimpleNamespace' objects>, '__lt__': <slot wrapper '__lt__' of 'types.SimpleNamespace' objects>, '__le__': <slot wrapper '__le__' of 'types.SimpleNamespace' objects>, '__eq__': <slot wrapper '__eq__' of 'types.SimpleNamespace' objects>, '__ne__': <slot wrapper '__ne__' of 'types.SimpleNamespace' objects>, '__gt__': <slot wrapper '__gt__' of 'types.SimpleNamespace' objects>, '__ge__': <slot wrapper '__ge__' of 'types.SimpleNamespace' objects>, '__init__': <slot wrapper '__init__' of 'types.SimpleNamespace' objects>, '__new__': <built-in method __new__ of type object at 0x0000000063E9A300>, '__reduce__': <method '__reduce__' of 'types.SimpleNamespace' objects>, '__dict__': <member '__dict__' of 'types.SimpleNamespace' objects>, '__doc__': 'A simple attribute-based namespace.\\n\\nSimpleNamespace(**kwargs)', '__hash__': None})"
    __hash__ = None


class TracebackType(object):
    # no doc
    def __dir__(self, *args, **kwargs): # real signature unknown
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    tb_frame = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tb_lasti = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tb_lineno = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tb_next = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class _GeneratorWrapper(object):
    # no doc
    def close(self): # reliably restored by inspect
        # no doc
        pass

    def send(self, val): # reliably restored by inspect
        # no doc
        pass

    def throw(self, tp, *rest): # reliably restored by inspect
        # no doc
        pass

    def __await__(self): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, gen): # reliably restored by inspect
        # no doc
        pass

    def __iter__(self): # reliably restored by inspect
        # no doc
        pass

    def __next__(self): # reliably restored by inspect
        # no doc
        pass

    cr_await = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    cr_code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    cr_frame = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    cr_running = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    gi_code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    gi_frame = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    gi_running = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    gi_yieldfrom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'types', '__init__': <function _GeneratorWrapper.__init__ at 0x000001C5B9CFD7B8>, 'send': <function _GeneratorWrapper.send at 0x000001C5B9CFD840>, 'throw': <function _GeneratorWrapper.throw at 0x000001C5B9CFD8C8>, 'close': <function _GeneratorWrapper.close at 0x000001C5B9CFD950>, 'gi_code': <property object at 0x000001C5B9B9D778>, 'gi_frame': <property object at 0x000001C5B9B9D7C8>, 'gi_running': <property object at 0x000001C5B9B9DE58>, 'gi_yieldfrom': <property object at 0x000001C5B9B9DEA8>, 'cr_code': <property object at 0x000001C5B9B9D778>, 'cr_frame': <property object at 0x000001C5B9B9D7C8>, 'cr_running': <property object at 0x000001C5B9B9DE58>, 'cr_await': <property object at 0x000001C5B9B9DEA8>, '__next__': <function _GeneratorWrapper.__next__ at 0x000001C5B9CFDBF8>, '__iter__': <function _GeneratorWrapper.__iter__ at 0x000001C5B9CFDC80>, '__await__': <function _GeneratorWrapper.__iter__ at 0x000001C5B9CFDC80>, '__dict__': <attribute '__dict__' of '_GeneratorWrapper' objects>, '__weakref__': <attribute '__weakref__' of '_GeneratorWrapper' objects>, '__doc__': None})"


# variables with complex values

_ag = None # (!) real value is '<async_generator object _ag at 0x000001C5B9B89458>'

__all__ = [
    'FunctionType',
    'LambdaType',
    'CodeType',
    'MappingProxyType',
    'SimpleNamespace',
    'GeneratorType',
    'CoroutineType',
    'AsyncGeneratorType',
    'MethodType',
    'BuiltinFunctionType',
    'BuiltinMethodType',
    'ModuleType',
    'TracebackType',
    'FrameType',
    'GetSetDescriptorType',
    'MemberDescriptorType',
    'new_class',
    'prepare_class',
    'DynamicClassAttribute',
    'coroutine',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.SourceFileLoader object at 0x000001C5B9B8B860>'

__spec__ = None # (!) real value is "ModuleSpec(name='types', loader=<_frozen_importlib_external.SourceFileLoader object at 0x000001C5B9B8B860>, origin='F:\\\\Python\\\\Python36\\\\lib\\\\types.py')"

