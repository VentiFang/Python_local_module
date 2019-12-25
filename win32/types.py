# encoding: utf-8
# module win32.types
# from F:\Python\Python36\lib\site-packages\win32\types.cp36-win_amd64.pyd
# by generator 1.147
""" Module containing common objects and functions used by various Pywin32 modules """

# imports
import datetime as __datetime


# Variables with simple values

FALSE = False

TRUE = True

WAVE_FORMAT_PCM = 1

# functions

def ACL(*args, **kwargs): # real signature unknown
    pass

def CreateGuid(*args, **kwargs): # real signature unknown
    pass

def DosDateTimeToTime(*args, **kwargs): # real signature unknown
    pass

def HANDLE(*args, **kwargs): # real signature unknown
    pass

def HKEY(*args, **kwargs): # real signature unknown
    pass

def IID(*args, **kwargs): # real signature unknown
    pass

def IsTextUnicode(*args, **kwargs): # real signature unknown
    pass

def OVERLAPPED(*args, **kwargs): # real signature unknown
    pass

def SECURITY_ATTRIBUTES(*args, **kwargs): # real signature unknown
    pass

def SECURITY_DESCRIPTOR(*args, **kwargs): # real signature unknown
    pass

def SID(*args, **kwargs): # real signature unknown
    pass

def Time(*args, **kwargs): # real signature unknown
    pass

def Unicode(*args, **kwargs): # real signature unknown
    pass

def UnicodeFromRaw(*args, **kwargs): # real signature unknown
    pass

def WAVEFORMATEX(*args, **kwargs): # real signature unknown
    pass

# classes

class ACLType(object):
    # no doc
    def AddAccessAllowedAce(self, *args, **kwargs): # real signature unknown
        pass

    def AddAccessAllowedAceEx(self, *args, **kwargs): # real signature unknown
        pass

    def AddAccessAllowedObjectAce(self, *args, **kwargs): # real signature unknown
        pass

    def AddAccessDeniedAce(self, *args, **kwargs): # real signature unknown
        pass

    def AddAccessDeniedAceEx(self, *args, **kwargs): # real signature unknown
        pass

    def AddAccessDeniedObjectAce(self, *args, **kwargs): # real signature unknown
        pass

    def AddAuditAccessAce(self, *args, **kwargs): # real signature unknown
        pass

    def AddAuditAccessAceEx(self, *args, **kwargs): # real signature unknown
        pass

    def AddAuditAccessObjectAce(self, *args, **kwargs): # real signature unknown
        pass

    def AddMandatoryAce(self, *args, **kwargs): # real signature unknown
        pass

    def DeleteAce(self, *args, **kwargs): # real signature unknown
        pass

    def GetAce(self, *args, **kwargs): # real signature unknown
        pass

    def GetAceCount(self, *args, **kwargs): # real signature unknown
        pass

    def GetAclRevision(self, *args, **kwargs): # real signature unknown
        pass

    def GetAclSize(self, *args, **kwargs): # real signature unknown
        pass

    def GetAuditedPermissionsFromAcl(self, *args, **kwargs): # real signature unknown
        pass

    def GetEffectiveRightsFromAcl(self, *args, **kwargs): # real signature unknown
        pass

    def GetExplicitEntriesFromAcl(self, *args, **kwargs): # real signature unknown
        pass

    def Initialize(self, *args, **kwargs): # real signature unknown
        pass

    def IsValid(self, *args, **kwargs): # real signature unknown
        pass

    def SetEntriesInAcl(self, *args, **kwargs): # real signature unknown
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class com_error(Exception):
    # no doc
    def __init__(self, *args, **kw): # reliably restored by inspect
        # no doc
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class DEVMODEAType(object):
    # no doc
    def Clear(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    BitsPerPel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Color resolution in bits per pixel"""

    Collate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """DMCOLLATE_TRUE or DMCOLLATE_FALSE"""

    Color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """DMCOLOR_COLOR or DMCOLOR_MONOCHROME"""

    Copies = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Nbr of copies to print"""

    DefaultSource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """DMBIN_* constant, or can be a printer-specific value"""

    DeviceName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """String of at most 32 chars"""

    DisplayFixedOutput = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """DMDFO_DEFAULT, DMDFO_CENTER, DMDFO_STRETCH"""

    DisplayFlags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Combination of DM_GRAYSCALE and DM_INTERLACED"""

    DisplayFrequency = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Refresh rate"""

    DisplayOrientation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Display rotation: DMDO_DEFAULT,DMDO_90, DMDO_180, DMDO_270"""

    DitherType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Dithering options, win32con.DMDITHER_*"""

    DriverData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Driver data appended to end of structure"""

    DriverExtra = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of extra bytes allocated for driver data, can only be set when new object is created"""

    DriverVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Version nbr assigned to printer driver by vendor"""

    Duplex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """For printers that do two-sided printing: DMDUP_SIMPLEX, DMDUP_HORIZONTAL, DMDUP_VERTICAL"""

    Fields = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Bitmask of win32con.DM_* constants indicating which members are set"""

    FormName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Name of form as returned by EnumForms, at most 32 chars"""

    ICMIntent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Intent of ICM, one of win32con.DMICM_* values"""

    ICMMethod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates where ICM is performed, one of win32con.DMICMMETHOD_* values"""

    LogPixels = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Pixels per inch (only for display devices)"""

    MediaType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """win32con.DMMEDIA_*, can also be a printer-specific value greater then DMMEDIA_USER"""

    Nup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Controls printing of multiple logical pages per physical page, DMNUP_SYSTEM or DMNUP_ONEUP"""

    Orientation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Only applies to printers, DMORIENT_PORTRAIT or DMORIENT_LANDSCAPE"""

    PanningHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Not used, leave as 0"""

    PanningWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Not used, leave as 0"""

    PaperLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specified in 1/10 millimeters"""

    PaperSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Use 0 if PaperWidth and PaperLength are set, otherwise win32con.DMPAPER_* constant"""

    PaperWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specified in 1/10 millimeters"""

    PelsHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Pixel height of display"""

    PelsWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Pixel width of display"""

    Position_x = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Position of display relative to desktop"""

    Position_y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Position of display relative to desktop"""

    PrintQuality = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """DMRES_* constant, interpreted as DPI if positive"""

    Reserved1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Reserved, use only 0"""

    Reserved2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Reserved, use only 0"""

    Scale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specified as percentage, eg 50 means half size of original"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Size of structure"""

    SpecVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Should always be set to DM_SPECVERSION"""

    TTOption = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """TrueType options: DMTT_BITMAP, DMTT_DOWNLOAD, DMTT_DOWNLOAD_OUTLINE, DMTT_SUBDEV"""

    YResolution = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Vertical printer resolution in DPI - if this is set, PrintQuality indicates horizontal DPI"""



class DEVMODEWType(object):
    # no doc
    def Clear(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    BitsPerPel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Color resolution in bits per pixel"""

    Collate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """DMCOLLATE_TRUE or DMCOLLATE_FALSE"""

    Color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """DMCOLOR_COLOR or DMCOLOR_MONOCHROME"""

    Copies = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Nbr of copies to print"""

    DefaultSource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """DMBIN_* constant, or can be a printer-specific value"""

    DeviceName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """String of at most 32 chars"""

    DisplayFixedOutput = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """DMDFO_DEFAULT, DMDFO_CENTER, DMDFO_STRETCH"""

    DisplayFlags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Combination of DM_GRAYSCALE and DM_INTERLACED"""

    DisplayFrequency = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Refresh rate"""

    DisplayOrientation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Display rotation: DMDO_DEFAULT,DMDO_90, DMDO_180, DMDO_270"""

    DitherType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Dithering options, win32con.DMDITHER_*"""

    DriverData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Driver data appended to end of structure"""

    DriverExtra = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of extra bytes allocated for driver data, can only be set when new object is created"""

    DriverVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Version nbr assigned to printer driver by vendor"""

    Duplex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """For printers that do two-sided printing: DMDUP_SIMPLEX, DMDUP_HORIZONTAL, DMDUP_VERTICAL"""

    Fields = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Bitmask of win32con.DM_* constants indicating which members are set"""

    FormName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Name of form as returned by EnumForms, at most 32 chars"""

    ICMIntent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Intent of ICM, one of win32con.DMICM_* values"""

    ICMMethod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates where ICM is performed, one of win32con.DMICMMETHOD_* values"""

    LogPixels = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Pixels per inch (only for display devices)"""

    MediaType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """win32con.DMMEDIA_*, can also be a printer-specific value greater then DMMEDIA_USER"""

    Nup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Controls printing of multiple logical pages per physical page, DMNUP_SYSTEM or DMNUP_ONEUP"""

    Orientation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Only applies to printers, DMORIENT_PORTRAIT or DMORIENT_LANDSCAPE"""

    PanningHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Not used, leave as 0"""

    PanningWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Not used, leave as 0"""

    PaperLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specified in 1/10 millimeters"""

    PaperSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Use 0 if PaperWidth and PaperLength are set, otherwise win32con.DMPAPER_* constant"""

    PaperWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specified in 1/10 millimeters"""

    PelsHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Pixel height of display"""

    PelsWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Pixel width of display"""

    Position_x = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Position of display relative to desktop"""

    Position_y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Position of display relative to desktop"""

    PrintQuality = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """DMRES_* constant, interpreted as DPI if positive"""

    Reserved1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Reserved, use only 0"""

    Reserved2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Reserved, use only 0"""

    Scale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specified as percentage, eg 50 means half size of original"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Size of structure"""

    SpecVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Should always be set to DM_SPECVERSION"""

    TTOption = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """TrueType options: DMTT_BITMAP, DMTT_DOWNLOAD, DMTT_DOWNLOAD_OUTLINE, DMTT_SUBDEV"""

    YResolution = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Vertical printer resolution in DPI - if this is set, PrintQuality indicates horizontal DPI"""



DEVMODEType = DEVMODEWType


class error(Exception):
    # no doc
    def __init__(self, *args, **kw): # reliably restored by inspect
        # no doc
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class HANDLEType(object):
    # no doc
    def Close(self, *args, **kwargs): # real signature unknown
        pass

    def close(self, *args, **kwargs): # real signature unknown
        pass

    def Detach(self, *args, **kwargs): # real signature unknown
        pass

    def __abs__(self, *args, **kwargs): # real signature unknown
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __and__(self, *args, **kwargs): # real signature unknown
        """ Return self&value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(self, value). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __float__(self, *args, **kwargs): # real signature unknown
        """ float(self) """
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

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
        pass

    def __invert__(self, *args, **kwargs): # real signature unknown
        """ ~self """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lshift__(self, *args, **kwargs): # real signature unknown
        """ Return self<<value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __pow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(self, value, mod). """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rand__(self, *args, **kwargs): # real signature unknown
        """ Return value&self. """
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(value, self). """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    def __rpow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(value, self, mod). """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, *args, **kwargs): # real signature unknown
        """ Return self>>value. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rxor__(self, *args, **kwargs): # real signature unknown
        """ Return value^self. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __xor__(self, *args, **kwargs): # real signature unknown
        """ Return self^value. """
        pass

    handle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class IIDType(object):
    # no doc
    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
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

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass


class OVERLAPPEDType(object):
    # no doc
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

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    dword = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    hEvent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Internal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    InternalHigh = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    object = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    OffsetHigh = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class SECURITY_ATTRIBUTESType(object):
    """ A Python object, representing a SECURITY_ATTRIBUTES structure """
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

    bInheritHandle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    SECURITY_DESCRIPTOR = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class SECURITY_DESCRIPTORType(object):
    # no doc
    def GetLength(self, *args, **kwargs): # real signature unknown
        pass

    def GetSecurityDescriptorControl(self, *args, **kwargs): # real signature unknown
        pass

    def GetSecurityDescriptorDacl(self, *args, **kwargs): # real signature unknown
        pass

    def GetSecurityDescriptorGroup(self, *args, **kwargs): # real signature unknown
        pass

    def GetSecurityDescriptorOwner(self, *args, **kwargs): # real signature unknown
        pass

    def GetSecurityDescriptorSacl(self, *args, **kwargs): # real signature unknown
        pass

    def Initialize(self, *args, **kwargs): # real signature unknown
        pass

    def IsSelfRelative(self, *args, **kwargs): # real signature unknown
        pass

    def IsValid(self, *args, **kwargs): # real signature unknown
        pass

    def SetDacl(self, *args, **kwargs): # real signature unknown
        pass

    def SetSecurityDescriptorControl(self, *args, **kwargs): # real signature unknown
        pass

    def SetSecurityDescriptorDacl(self, *args, **kwargs): # real signature unknown
        pass

    def SetSecurityDescriptorGroup(self, *args, **kwargs): # real signature unknown
        pass

    def SetSecurityDescriptorOwner(self, *args, **kwargs): # real signature unknown
        pass

    def SetSecurityDescriptorSacl(self, *args, **kwargs): # real signature unknown
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


class SIDType(object):
    # no doc
    def GetLength(self, *args, **kwargs): # real signature unknown
        pass

    def GetSidIdentifierAuthority(self, *args, **kwargs): # real signature unknown
        pass

    def GetSubAuthority(self, *args, **kwargs): # real signature unknown
        pass

    def GetSubAuthorityCount(self, *args, **kwargs): # real signature unknown
        pass

    def Initialize(self, *args, **kwargs): # real signature unknown
        pass

    def IsValid(self, *args, **kwargs): # real signature unknown
        pass

    def SetSubAuthority(self, *args, **kwargs): # real signature unknown
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

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    __hash__ = None


class TimeType(__datetime.datetime):
    # no doc
    def Format(self, *args, **kwargs): # real signature unknown
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass


class UnicodeType(object):
    """
    str(object='') -> str
    str(bytes_or_buffer[, encoding[, errors]]) -> str
    
    Create a new string object from the given object. If encoding or
    errors is specified, then the object must expose a data buffer
    that will be decoded using the given encoding and error handler.
    Otherwise, returns the result of object.__str__() (if defined)
    or repr(object).
    encoding defaults to sys.getdefaultencoding().
    errors defaults to 'strict'.
    """
    def capitalize(self): # real signature unknown; restored from __doc__
        """
        S.capitalize() -> str
        
        Return a capitalized version of S, i.e. make the first character
        have upper case and the rest lower case.
        """
        return ""

    def casefold(self): # real signature unknown; restored from __doc__
        """
        S.casefold() -> str
        
        Return a version of S suitable for caseless comparisons.
        """
        return ""

    def center(self, width, fillchar=None): # real signature unknown; restored from __doc__
        """
        S.center(width[, fillchar]) -> str
        
        Return S centered in a string of length width. Padding is
        done using the specified fill character (default is a space)
        """
        return ""

    def count(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.count(sub[, start[, end]]) -> int
        
        Return the number of non-overlapping occurrences of substring sub in
        string S[start:end].  Optional arguments start and end are
        interpreted as in slice notation.
        """
        return 0

    def encode(self, encoding='utf-8', errors='strict'): # real signature unknown; restored from __doc__
        """
        S.encode(encoding='utf-8', errors='strict') -> bytes
        
        Encode S using the codec registered for encoding. Default encoding
        is 'utf-8'. errors may be given to set a different error
        handling scheme. Default is 'strict' meaning that encoding errors raise
        a UnicodeEncodeError. Other possible values are 'ignore', 'replace' and
        'xmlcharrefreplace' as well as any other name registered with
        codecs.register_error that can handle UnicodeEncodeErrors.
        """
        return b""

    def endswith(self, suffix, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.endswith(suffix[, start[, end]]) -> bool
        
        Return True if S ends with the specified suffix, False otherwise.
        With optional start, test S beginning at that position.
        With optional end, stop comparing S at that position.
        suffix can also be a tuple of strings to try.
        """
        return False

    def expandtabs(self, tabsize=8): # real signature unknown; restored from __doc__
        """
        S.expandtabs(tabsize=8) -> str
        
        Return a copy of S where all tab characters are expanded using spaces.
        If tabsize is not given, a tab size of 8 characters is assumed.
        """
        return ""

    def find(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.find(sub[, start[, end]]) -> int
        
        Return the lowest index in S where substring sub is found,
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Return -1 on failure.
        """
        return 0

    def format(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        S.format(*args, **kwargs) -> str
        
        Return a formatted version of S, using substitutions from args and kwargs.
        The substitutions are identified by braces ('{' and '}').
        """
        return ""

    def format_map(self, mapping): # real signature unknown; restored from __doc__
        """
        S.format_map(mapping) -> str
        
        Return a formatted version of S, using substitutions from mapping.
        The substitutions are identified by braces ('{' and '}').
        """
        return ""

    def index(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.index(sub[, start[, end]]) -> int
        
        Return the lowest index in S where substring sub is found, 
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Raises ValueError when the substring is not found.
        """
        return 0

    def isalnum(self): # real signature unknown; restored from __doc__
        """
        S.isalnum() -> bool
        
        Return True if all characters in S are alphanumeric
        and there is at least one character in S, False otherwise.
        """
        return False

    def isalpha(self): # real signature unknown; restored from __doc__
        """
        S.isalpha() -> bool
        
        Return True if all characters in S are alphabetic
        and there is at least one character in S, False otherwise.
        """
        return False

    def isdecimal(self): # real signature unknown; restored from __doc__
        """
        S.isdecimal() -> bool
        
        Return True if there are only decimal characters in S,
        False otherwise.
        """
        return False

    def isdigit(self): # real signature unknown; restored from __doc__
        """
        S.isdigit() -> bool
        
        Return True if all characters in S are digits
        and there is at least one character in S, False otherwise.
        """
        return False

    def isidentifier(self): # real signature unknown; restored from __doc__
        """
        S.isidentifier() -> bool
        
        Return True if S is a valid identifier according
        to the language definition.
        
        Use keyword.iskeyword() to test for reserved identifiers
        such as "def" and "class".
        """
        return False

    def islower(self): # real signature unknown; restored from __doc__
        """
        S.islower() -> bool
        
        Return True if all cased characters in S are lowercase and there is
        at least one cased character in S, False otherwise.
        """
        return False

    def isnumeric(self): # real signature unknown; restored from __doc__
        """
        S.isnumeric() -> bool
        
        Return True if there are only numeric characters in S,
        False otherwise.
        """
        return False

    def isprintable(self): # real signature unknown; restored from __doc__
        """
        S.isprintable() -> bool
        
        Return True if all characters in S are considered
        printable in repr() or S is empty, False otherwise.
        """
        return False

    def isspace(self): # real signature unknown; restored from __doc__
        """
        S.isspace() -> bool
        
        Return True if all characters in S are whitespace
        and there is at least one character in S, False otherwise.
        """
        return False

    def istitle(self): # real signature unknown; restored from __doc__
        """
        S.istitle() -> bool
        
        Return True if S is a titlecased string and there is at least one
        character in S, i.e. upper- and titlecase characters may only
        follow uncased characters and lowercase characters only cased ones.
        Return False otherwise.
        """
        return False

    def isupper(self): # real signature unknown; restored from __doc__
        """
        S.isupper() -> bool
        
        Return True if all cased characters in S are uppercase and there is
        at least one cased character in S, False otherwise.
        """
        return False

    def join(self, iterable): # real signature unknown; restored from __doc__
        """
        S.join(iterable) -> str
        
        Return a string which is the concatenation of the strings in the
        iterable.  The separator between elements is S.
        """
        return ""

    def ljust(self, width, fillchar=None): # real signature unknown; restored from __doc__
        """
        S.ljust(width[, fillchar]) -> str
        
        Return S left-justified in a Unicode string of length width. Padding is
        done using the specified fill character (default is a space).
        """
        return ""

    def lower(self): # real signature unknown; restored from __doc__
        """
        S.lower() -> str
        
        Return a copy of the string S converted to lowercase.
        """
        return ""

    def lstrip(self, chars=None): # real signature unknown; restored from __doc__
        """
        S.lstrip([chars]) -> str
        
        Return a copy of the string S with leading whitespace removed.
        If chars is given and not None, remove characters in chars instead.
        """
        return ""

    def maketrans(self, *args, **kwargs): # real signature unknown
        """
        Return a translation table usable for str.translate().
        
        If there is only one argument, it must be a dictionary mapping Unicode
        ordinals (integers) or characters to Unicode ordinals, strings or None.
        Character keys will be then converted to ordinals.
        If there are two arguments, they must be strings of equal length, and
        in the resulting dictionary, each character in x will be mapped to the
        character at the same position in y. If there is a third argument, it
        must be a string, whose characters will be mapped to None in the result.
        """
        pass

    def partition(self, sep): # real signature unknown; restored from __doc__
        """
        S.partition(sep) -> (head, sep, tail)
        
        Search for the separator sep in S, and return the part before it,
        the separator itself, and the part after it.  If the separator is not
        found, return S and two empty strings.
        """
        pass

    def replace(self, old, new, count=None): # real signature unknown; restored from __doc__
        """
        S.replace(old, new[, count]) -> str
        
        Return a copy of S with all occurrences of substring
        old replaced by new.  If the optional argument count is
        given, only the first count occurrences are replaced.
        """
        return ""

    def rfind(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.rfind(sub[, start[, end]]) -> int
        
        Return the highest index in S where substring sub is found,
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Return -1 on failure.
        """
        return 0

    def rindex(self, sub, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.rindex(sub[, start[, end]]) -> int
        
        Return the highest index in S where substring sub is found,
        such that sub is contained within S[start:end].  Optional
        arguments start and end are interpreted as in slice notation.
        
        Raises ValueError when the substring is not found.
        """
        return 0

    def rjust(self, width, fillchar=None): # real signature unknown; restored from __doc__
        """
        S.rjust(width[, fillchar]) -> str
        
        Return S right-justified in a string of length width. Padding is
        done using the specified fill character (default is a space).
        """
        return ""

    def rpartition(self, sep): # real signature unknown; restored from __doc__
        """
        S.rpartition(sep) -> (head, sep, tail)
        
        Search for the separator sep in S, starting at the end of S, and return
        the part before it, the separator itself, and the part after it.  If the
        separator is not found, return two empty strings and S.
        """
        pass

    def rsplit(self, sep=None, maxsplit=-1): # real signature unknown; restored from __doc__
        """
        S.rsplit(sep=None, maxsplit=-1) -> list of strings
        
        Return a list of the words in S, using sep as the
        delimiter string, starting at the end of the string and
        working to the front.  If maxsplit is given, at most maxsplit
        splits are done. If sep is not specified, any whitespace string
        is a separator.
        """
        return []

    def rstrip(self, chars=None): # real signature unknown; restored from __doc__
        """
        S.rstrip([chars]) -> str
        
        Return a copy of the string S with trailing whitespace removed.
        If chars is given and not None, remove characters in chars instead.
        """
        return ""

    def split(self, sep=None, maxsplit=-1): # real signature unknown; restored from __doc__
        """
        S.split(sep=None, maxsplit=-1) -> list of strings
        
        Return a list of the words in S, using sep as the
        delimiter string.  If maxsplit is given, at most maxsplit
        splits are done. If sep is not specified or is None, any
        whitespace string is a separator and empty strings are
        removed from the result.
        """
        return []

    def splitlines(self, keepends=None): # real signature unknown; restored from __doc__
        """
        S.splitlines([keepends]) -> list of strings
        
        Return a list of the lines in S, breaking at line boundaries.
        Line breaks are not included in the resulting list unless keepends
        is given and true.
        """
        return []

    def startswith(self, prefix, start=None, end=None): # real signature unknown; restored from __doc__
        """
        S.startswith(prefix[, start[, end]]) -> bool
        
        Return True if S starts with the specified prefix, False otherwise.
        With optional start, test S beginning at that position.
        With optional end, stop comparing S at that position.
        prefix can also be a tuple of strings to try.
        """
        return False

    def strip(self, chars=None): # real signature unknown; restored from __doc__
        """
        S.strip([chars]) -> str
        
        Return a copy of the string S with leading and trailing
        whitespace removed.
        If chars is given and not None, remove characters in chars instead.
        """
        return ""

    def swapcase(self): # real signature unknown; restored from __doc__
        """
        S.swapcase() -> str
        
        Return a copy of S with uppercase characters converted to lowercase
        and vice versa.
        """
        return ""

    def title(self): # real signature unknown; restored from __doc__
        """
        S.title() -> str
        
        Return a titlecased version of S, i.e. words start with title case
        characters, all remaining cased characters have lower case.
        """
        return ""

    def translate(self, table): # real signature unknown; restored from __doc__
        """
        S.translate(table) -> str
        
        Return a copy of the string S in which each character has been mapped
        through the given translation table. The table must implement
        lookup/indexing via __getitem__, for instance a dictionary or list,
        mapping Unicode ordinals to Unicode ordinals, strings, or None. If
        this operation raises LookupError, the character is left untouched.
        Characters mapped to None are deleted.
        """
        return ""

    def upper(self): # real signature unknown; restored from __doc__
        """
        S.upper() -> str
        
        Return a copy of S converted to uppercase.
        """
        return ""

    def zfill(self, width): # real signature unknown; restored from __doc__
        """
        S.zfill(width) -> str
        
        Pad a numeric string S with zeros on the left, to fill a field
        of the specified width. The string S is never truncated.
        """
        return ""

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return key in self. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __format__(self, format_spec): # real signature unknown; restored from __doc__
        """
        S.__format__(format_spec) -> str
        
        Return a formatted version of S as described by format_spec.
        """
        return ""

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __getnewargs__(self, *args, **kwargs): # real signature unknown
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

    def __mod__(self, *args, **kwargs): # real signature unknown
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
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

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __sizeof__(self): # real signature unknown; restored from __doc__
        """ S.__sizeof__() -> size of S in memory, in bytes """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass


class WAVEFORMATEXType(object):
    # no doc
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

    nAvgBytesPerSec = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Required average data-transfer rate, in bytes per second, for the format tag. If wFormatTag is WAVE_FORMAT_PCM, nAvgBytesPerSec should be equal to the product of nSamplesPerSec and nBlockAlign."""

    nBlockAlign = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Block alignment, in bytes. The block alignment is the minimum atomic unit of data for the wFormatTag format type. If wFormatTag is WAVE_FORMAT_PCM, nBlockAlign should be equal to the product of nChannels and wBitsPerSample divided by 8 (bits per byte)."""

    nChannels = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of channels"""

    nSamplesPerSec = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Sample rate in seconds"""

    wBitsPerSample = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Bits per sample for the wFormatTag format type. If wFormatTag is WAVE_FORMAT_PCM, then wBitsPerSample should be equal to 8 or 16."""

    wFormatTag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Format as an integer. WAVE_FORMAT_PCM (1) is very common."""



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x00000244ADE86588>'

__spec__ = None # (!) real value is "ModuleSpec(name='win32.types', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x00000244ADE86588>, origin='F:\\\\Python\\\\Python36\\\\lib\\\\site-packages\\\\win32\\\\types.cp36-win_amd64.pyd')"

