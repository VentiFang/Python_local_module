# encoding: utf-8
# module _hashlib
# from (pre-generated)
# by generator 1.147
# no doc
# no imports

# functions

def new(*args, **kwargs): # real signature unknown
    """
    Return a new hash object using the named algorithm.
    An optional string argument may be provided and will be
    automatically hashed.
    
    The MD5 and SHA1 algorithms are always supported.
    """
    pass

def openssl_md5(*args, **kwargs): # real signature unknown
    """ Returns a md5 hash object; optionally initialized with a string """
    pass

def openssl_sha1(*args, **kwargs): # real signature unknown
    """ Returns a sha1 hash object; optionally initialized with a string """
    pass

def openssl_sha224(*args, **kwargs): # real signature unknown
    """ Returns a sha224 hash object; optionally initialized with a string """
    pass

def openssl_sha256(*args, **kwargs): # real signature unknown
    """ Returns a sha256 hash object; optionally initialized with a string """
    pass

def openssl_sha384(*args, **kwargs): # real signature unknown
    """ Returns a sha384 hash object; optionally initialized with a string """
    pass

def openssl_sha512(*args, **kwargs): # real signature unknown
    """ Returns a sha512 hash object; optionally initialized with a string """
    pass

def pbkdf2_hmac(hash_name, password, salt, iterations, dklen=None): # real signature unknown; restored from __doc__
    """
    pbkdf2_hmac(hash_name, password, salt, iterations, dklen=None) -> key
    
    Password based key derivation function 2 (PKCS #5 v2.0) with HMAC as
    pseudorandom function.
    """
    pass

# classes

class HASH(object):
    """
    A hash represents the object used to calculate a checksum of a
    string of information.
    
    Methods:
    
    update() -- updates the current digest with an additional string
    digest() -- return the current digest value
    hexdigest() -- return the current digest as a string of hexadecimal digits
    copy() -- return a copy of the current hash object
    
    Attributes:
    
    name -- the hash algorithm being used by this object
    digest_size -- number of bytes in this hashes output
    """
    def copy(self, *args, **kwargs): # real signature unknown
        """ Return a copy of the hash object. """
        pass

    def digest(self, *args, **kwargs): # real signature unknown
        """ Return the digest value as a bytes object. """
        pass

    def hexdigest(self, *args, **kwargs): # real signature unknown
        """ Return the digest value as a string of hexadecimal digits. """
        pass

    def update(self, *args, **kwargs): # real signature unknown
        """ Update this hash object's state with the provided string. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    block_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    digest_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """algorithm name."""



# variables with complex values

openssl_md_meth_names = None # (!) real value is "frozenset({'MD5', 'SHA224', 'whirlpool', 'sha256', 'md5', 'MD4', 'sha512', 'SHA512', 'md4', 'sha384', 'SHA256', 'sha', 'sha224', 'SHA384', 'DSA-SHA', 'ecdsa-with-SHA1', 'dsaWithSHA', 'sha1', 'ripemd160', 'RIPEMD160', 'dsaEncryption', 'DSA', 'SHA', 'SHA1'})"

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000002CAE2BFE358>'

__spec__ = None # (!) real value is "ModuleSpec(name='_hashlib', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000002CAE2BFE358>, origin='C:\\\\BuildAgent\\\\system\\\\.persistent_cache\\\\pythons\\\\python36\\\\DLLs\\\\_hashlib.pyd')"

