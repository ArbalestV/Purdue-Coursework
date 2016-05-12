# encoding: utf-8
# module cryptsetup
# from /usr/lib64/python2.6/site-packages/cryptsetup.so
# by generator 1.136
""" CryptSetup pythonized API. """
# no imports

# no functions
# classes

class CryptSetup(object):
    """
    CryptSetup object
    
    constructor takes two arguments:
      __init__(yesDialog, logFunc)
    
      yesDialog - python function with func(text) signature, which asks the user question text and returns 1 of the answer was positive or 0 if not
      logFunc   - python function with func(level, text) signature to log stuff somewhere
    """
    def askyes(self, *args, **kwargs): # real signature unknown
        """
        Logs a string using the configured log CB
        
          log(int level, message)
        """
        pass

    def isLuks(self, device): # real signature unknown; restored from __doc__
        """
        Is the device LUKS?
        
          isLuks(device)
        
          return value:
           0   - device is LUKS
          -22  - device is not LUKS
        """
        pass

    def log(self, *args, **kwargs): # real signature unknown
        """
        Asks a question using the configured dialog CB
        
          int askyes(message)
        """
        pass

    def luksClose(self, name): # real signature unknown; restored from __doc__
        """
        Close LUKS device and remove it from devmapper
        
          luksClose(name)
        
          the mapping name which should be removed from devmapper.
        """
        pass

    def luksFormat(self, device, cipher=None, keysize=256, keyfile=None): # real signature unknown; restored from __doc__
        """
        Format device to enable LUKS
        
          luksFormat(device, cipher = 'aes-cbc-essiv:sha256', keysize = 256, keyfile = None)
        
          device - which device?
          cipher - text string to specify cipher (cipher-mode-iv:hash_for_iv. probably aes-cbc-essiv:sha256 or aes-xts-plain)
          keysize - key size in bits, cipher must support this
          keyfile - filename which contains the key for encrypting this device. If None, cryptsetup will ask for one.
        """
        pass

    def luksOpen(self, device, name, keyfile): # real signature unknown; restored from __doc__
        """
        Open LUKS device and add it do devmapper
        
          luksOpen(device, name, keyfile)
        
          device - which device?
          name - what mapping name should be created
          keyfile - filename which contains the key for encrypting this device. '-' means standard input
        """
        pass

    def luksStatus(self, name): # real signature unknown; restored from __doc__
        """
        What is the status of Luks subsystem?
        
          luksStatus(name)
        
          return value:
          - dictionary with luks status
          - or number <=0 if the device is not active
        """
        pass

    def luksUUID(self, device): # real signature unknown; restored from __doc__
        """
        Get UUID of the LUKS device
        
          luksUUID(device)
        """
        pass

    def __init__(self, yesDialog, logFunc): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    cmdLineLogCB = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """logging callback"""

    yesDialogCB = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """confirmation dialog callback"""



