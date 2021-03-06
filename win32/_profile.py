# encoding: utf-8
# module win32._profile
# from F:\Python\Python36\lib\site-packages\win32\_profile.cp36-win_amd64.pyd
# by generator 1.147
""" Interface to the User Profile Api. """
# no imports

# Variables with simple values

PI_APPLYPOLICY = 2
PI_NOUI = 1

PT_MANDATORY = 4
PT_ROAMING = 2
PT_TEMPORARY = 1

# functions

def CreateEnvironmentBlock(*args, **kwargs): # real signature unknown
    """ Retrieves environment variables for a user """
    pass

def DeleteProfile(*args, **kwargs): # real signature unknown
    """ Remove a user's profile """
    pass

def ExpandEnvironmentStringsForUser(*args, **kwargs): # real signature unknown
    """ Replaces environment variables in a string with per-user values """
    pass

def GetAllUsersProfileDirectory(*args, **kwargs): # real signature unknown
    """ Retrieve All Users profile directory """
    pass

def GetDefaultUserProfileDirectory(*args, **kwargs): # real signature unknown
    """ Retrieve profile path for Default user """
    pass

def GetEnvironmentStrings(*args, **kwargs): # real signature unknown
    """ Retrieves environment variables for current process """
    pass

def GetProfilesDirectory(*args, **kwargs): # real signature unknown
    """ Retrieves directory where user profiles are stored """
    pass

def GetProfileType(*args, **kwargs): # real signature unknown
    """ Returns type of current user's profile """
    pass

def GetUserProfileDirectory(*args, **kwargs): # real signature unknown
    """ Returns profile directory for a logon token """
    pass

def LoadUserProfile(*args, **kwargs): # real signature unknown
    """ Load user settings for a login token """
    pass

def UnloadUserProfile(*args, **kwargs): # real signature unknown
    """ Unload profile loaded by LoadUserProfile """
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001B725B665C0>'

__spec__ = None # (!) real value is "ModuleSpec(name='win32._profile', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001B725B665C0>, origin='F:\\\\Python\\\\Python36\\\\lib\\\\site-packages\\\\win32\\\\_profile.cp36-win_amd64.pyd')"

