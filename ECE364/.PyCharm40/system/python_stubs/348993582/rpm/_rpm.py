# encoding: utf-8
# module rpm._rpm
# from /usr/lib64/python2.6/site-packages/rpm/_rpmmodule.so
# by generator 1.136
# no doc
# no imports

# Variables with simple values

HEADERCONV_COMPRESSFILELIST = 1
HEADERCONV_EXPANDFILELIST = 0

HEADERCONV_RETROFIT_V3 = 2

RPMCALLBACK_CPIO_ERROR = 16384

RPMCALLBACK_INST_CLOSE_FILE = 8

RPMCALLBACK_INST_OPEN_FILE = 4

RPMCALLBACK_INST_PROGRESS = 1
RPMCALLBACK_INST_START = 2

RPMCALLBACK_REPACKAGE_PROGRESS = 1024
RPMCALLBACK_REPACKAGE_START = 2048
RPMCALLBACK_REPACKAGE_STOP = 4096

RPMCALLBACK_SCRIPT_ERROR = 32768

RPMCALLBACK_TRANS_PROGRESS = 16
RPMCALLBACK_TRANS_START = 32
RPMCALLBACK_TRANS_STOP = 64

RPMCALLBACK_UNINST_PROGRESS = 128
RPMCALLBACK_UNINST_START = 256
RPMCALLBACK_UNINST_STOP = 512

RPMCALLBACK_UNKNOWN = 0

RPMCALLBACK_UNPACK_ERROR = 8192

RPMDBI_LABEL = 2
RPMDBI_PACKAGES = 0

RPMDEP_SENSE_CONFLICTS = 1
RPMDEP_SENSE_REQUIRES = 0

RPMFILE_CONFIG = 1
RPMFILE_DOC = 2
RPMFILE_EXCLUDE = 512
RPMFILE_GHOST = 64
RPMFILE_LICENSE = 128
RPMFILE_MISSINGOK = 8
RPMFILE_NOREPLACE = 16
RPMFILE_PUBKEY = 2048
RPMFILE_README = 256

RPMFILE_STATE_NETSHARED = 3
RPMFILE_STATE_NORMAL = 0
RPMFILE_STATE_NOTINSTALLED = 2
RPMFILE_STATE_REPLACED = 1
RPMFILE_STATE_WRONGCOLOR = 4

RPMFILE_UNPATCHED = 1024

RPMLOG_ALERT = 1
RPMLOG_CRIT = 2
RPMLOG_DEBUG = 7
RPMLOG_EMERG = 0
RPMLOG_ERR = 3
RPMLOG_INFO = 6
RPMLOG_NOTICE = 5
RPMLOG_WARNING = 4

RPMMIRE_DEFAULT = 0
RPMMIRE_GLOB = 3
RPMMIRE_REGEX = 2
RPMMIRE_STRCMP = 1

RPMPROB_BADARCH = 0
RPMPROB_BADOS = 1
RPMPROB_BADRELOCATE = 3
RPMPROB_CONFLICT = 5
RPMPROB_DISKNODES = 10
RPMPROB_DISKSPACE = 9

RPMPROB_FILE_CONFLICT = 7

RPMPROB_FILTER_DISKNODES = 256
RPMPROB_FILTER_DISKSPACE = 128
RPMPROB_FILTER_FORCERELOCATE = 8
RPMPROB_FILTER_IGNOREARCH = 2
RPMPROB_FILTER_IGNOREOS = 1
RPMPROB_FILTER_OLDPACKAGE = 64
RPMPROB_FILTER_REPLACENEWFILES = 16
RPMPROB_FILTER_REPLACEOLDFILES = 32
RPMPROB_FILTER_REPLACEPKG = 4

RPMPROB_NEW_FILE_CONFLICT = 6

RPMPROB_OLDPACKAGE = 8

RPMPROB_PKG_INSTALLED = 2

RPMPROB_REQUIRES = 4

RPMRC_FAIL = 2
RPMRC_NOKEY = 4
RPMRC_NOTFOUND = 1
RPMRC_NOTTRUSTED = 3
RPMRC_OK = 0

RPMSENSE_ANY = 0
RPMSENSE_CONFIG = 268435456
RPMSENSE_EQUAL = 8

RPMSENSE_FIND_PROVIDES = 32768
RPMSENSE_FIND_REQUIRES = 16384

RPMSENSE_GREATER = 4
RPMSENSE_INTERP = 256
RPMSENSE_KEYRING = 67108864
RPMSENSE_LESS = 2
RPMSENSE_PATCHES = 134217728
RPMSENSE_PREREQ = 64
RPMSENSE_RPMLIB = 16777216

RPMSENSE_SCRIPT_BUILD = 2097152
RPMSENSE_SCRIPT_CLEAN = 8388608
RPMSENSE_SCRIPT_INSTALL = 4194304
RPMSENSE_SCRIPT_POST = 1024
RPMSENSE_SCRIPT_POSTUN = 4096
RPMSENSE_SCRIPT_PRE = 512
RPMSENSE_SCRIPT_PREP = 1048576
RPMSENSE_SCRIPT_PREUN = 2048
RPMSENSE_SCRIPT_VERIFY = 8192

RPMSENSE_TRIGGERIN = 65536
RPMSENSE_TRIGGERPOSTUN = 262144
RPMSENSE_TRIGGERPREIN = 33554432
RPMSENSE_TRIGGERUN = 131072

RPMTAG_ARCH = 1022
RPMTAG_ARCHIVESIZE = 1046
RPMTAG_BASENAMES = 1117
RPMTAG_BUGURL = 5012
RPMTAG_BUILDARCHS = 1089
RPMTAG_BUILDHOST = 1007
RPMTAG_BUILDTIME = 1006
RPMTAG_C = 1054
RPMTAG_CAPABILITY = 1105
RPMTAG_CHANGELOGNAME = 1081
RPMTAG_CHANGELOGTEXT = 1082
RPMTAG_CHANGELOGTIME = 1080
RPMTAG_CLASSDICT = 1142
RPMTAG_CONFLICTFLAGS = 1053
RPMTAG_CONFLICTNAME = 1054
RPMTAG_CONFLICTS = 1054
RPMTAG_CONFLICTVERSION = 1055
RPMTAG_COOKIE = 1094
RPMTAG_DBINSTANCE = 1195
RPMTAG_DEPENDSDICT = 1145
RPMTAG_DESCRIPTION = 1005
RPMTAG_DIRINDEXES = 1116
RPMTAG_DIRNAMES = 1118
RPMTAG_DISTRIBUTION = 1010
RPMTAG_DISTTAG = 1155
RPMTAG_DISTURL = 1123
RPMTAG_DSAHEADER = 267
RPMTAG_E = 1003
RPMTAG_EPOCH = 1003
RPMTAG_EPOCHNUM = 5019
RPMTAG_EVR = 5013
RPMTAG_EXCLUDEARCH = 1059
RPMTAG_EXCLUDEOS = 1060
RPMTAG_EXCLUSIVEARCH = 1061
RPMTAG_EXCLUSIVEOS = 1062
RPMTAG_FILECAPS = 5010
RPMTAG_FILECLASS = 1141
RPMTAG_FILECOLORS = 1140
RPMTAG_FILECONTEXTS = 1147
RPMTAG_FILEDEPENDSN = 1144
RPMTAG_FILEDEPENDSX = 1143
RPMTAG_FILEDEVICES = 1095
RPMTAG_FILEDIGESTALGO = 5011
RPMTAG_FILEDIGESTS = 1035
RPMTAG_FILEFLAGS = 1037
RPMTAG_FILEGROUPNAME = 1040
RPMTAG_FILEINODES = 1096
RPMTAG_FILELANGS = 1097
RPMTAG_FILELINKTOS = 1036
RPMTAG_FILEMD5S = 1035
RPMTAG_FILEMODES = 1030
RPMTAG_FILEMTIMES = 1034
RPMTAG_FILENAMES = 5000
RPMTAG_FILEPROVIDE = 5001
RPMTAG_FILERDEVS = 1033
RPMTAG_FILEREQUIRE = 5002
RPMTAG_FILESIZES = 1028
RPMTAG_FILESTATES = 1029
RPMTAG_FILEUSERNAME = 1039
RPMTAG_FILEVERIFYFLAGS = 1045
RPMTAG_FSCONTEXTS = 1148
RPMTAG_FSNAMES = 5003
RPMTAG_FSSIZES = 5004
RPMTAG_GIF = 1012
RPMTAG_GROUP = 1016
RPMTAG_HDRID = 269
RPMTAG_HEADERCOLOR = 5017
RPMTAG_HEADERI18NTABLE = 100
RPMTAG_HEADERIMAGE = 61
RPMTAG_HEADERIMMUTABLE = 63
RPMTAG_HEADERREGIONS = 64
RPMTAG_HEADERSIGNATURES = 62
RPMTAG_ICON = 1043
RPMTAG_INSTALLCOLOR = 1127
RPMTAG_INSTALLTID = 1128
RPMTAG_INSTALLTIME = 1008
RPMTAG_INSTPREFIXES = 1099
RPMTAG_LICENSE = 1014
RPMTAG_LONGARCHIVESIZE = 271
RPMTAG_LONGFILESIZES = 5008
RPMTAG_LONGSIGSIZE = 270
RPMTAG_LONGSIZE = 5009
RPMTAG_N = 1000
RPMTAG_NAME = 1000
RPMTAG_NEVR = 5015
RPMTAG_NEVRA = 5016
RPMTAG_NOPATCH = 1052
RPMTAG_NOSOURCE = 1051

RPMTAG_NOT_FOUND = -1

RPMTAG_NVR = 5014
RPMTAG_NVRA = 1196
RPMTAG_O = 1090
RPMTAG_OBSOLETEFLAGS = 1114
RPMTAG_OBSOLETENAME = 1090
RPMTAG_OBSOLETES = 1090
RPMTAG_OBSOLETEVERSION = 1115
RPMTAG_OLDFILENAMES = 1027
RPMTAG_OPTFLAGS = 1122
RPMTAG_ORIGBASENAMES = 1120
RPMTAG_ORIGDIRINDEXES = 1119
RPMTAG_ORIGDIRNAMES = 1121
RPMTAG_ORIGFILENAMES = 5007
RPMTAG_OS = 1021
RPMTAG_P = 1047
RPMTAG_PACKAGER = 1015
RPMTAG_PATCH = 1019
RPMTAG_PATCHESFLAGS = 1134
RPMTAG_PATCHESNAME = 1133
RPMTAG_PATCHESVERSION = 1135
RPMTAG_PAYLOADCOMPRESSOR = 1125
RPMTAG_PAYLOADFLAGS = 1126
RPMTAG_PAYLOADFORMAT = 1124
RPMTAG_PKGID = 261
RPMTAG_PLATFORM = 1132
RPMTAG_POLICIES = 1150
RPMTAG_POSTIN = 1024
RPMTAG_POSTINPROG = 1086
RPMTAG_POSTTRANS = 1152
RPMTAG_POSTTRANSPROG = 1154
RPMTAG_POSTUN = 1026
RPMTAG_POSTUNPROG = 1088
RPMTAG_PREFIXES = 1098
RPMTAG_PREIN = 1023
RPMTAG_PREINPROG = 1085
RPMTAG_PRETRANS = 1151
RPMTAG_PRETRANSPROG = 1153
RPMTAG_PREUN = 1025
RPMTAG_PREUNPROG = 1087
RPMTAG_PROVIDEFLAGS = 1112
RPMTAG_PROVIDENAME = 1047
RPMTAG_PROVIDES = 1047
RPMTAG_PROVIDEVERSION = 1113
RPMTAG_PUBKEYS = 266
RPMTAG_R = 1002
RPMTAG_RECONTEXTS = 1149
RPMTAG_RELEASE = 1002
RPMTAG_REMOVETID = 1129
RPMTAG_REQUIREFLAGS = 1048
RPMTAG_REQUIRENAME = 1049
RPMTAG_REQUIRES = 1049
RPMTAG_REQUIREVERSION = 1050
RPMTAG_RHNPLATFORM = 1131
RPMTAG_RPMVERSION = 1064
RPMTAG_RSAHEADER = 268
RPMTAG_SHA1HEADER = 269
RPMTAG_SIGGPG = 262
RPMTAG_SIGMD5 = 261
RPMTAG_SIGPGP = 259
RPMTAG_SIGSIZE = 257
RPMTAG_SIZE = 1009
RPMTAG_SOURCE = 1018
RPMTAG_SOURCEPACKAGE = 1106
RPMTAG_SOURCEPKGID = 1146
RPMTAG_SOURCERPM = 1044
RPMTAG_SUMMARY = 1004
RPMTAG_TRIGGERCONDS = 5005
RPMTAG_TRIGGERFLAGS = 1068
RPMTAG_TRIGGERINDEX = 1069
RPMTAG_TRIGGERNAME = 1066
RPMTAG_TRIGGERSCRIPTPROG = 1092
RPMTAG_TRIGGERSCRIPTS = 1065
RPMTAG_TRIGGERTYPE = 5006
RPMTAG_TRIGGERVERSION = 1067
RPMTAG_URL = 1020
RPMTAG_V = 1001
RPMTAG_VENDOR = 1011
RPMTAG_VERBOSE = 5018
RPMTAG_VERIFYSCRIPT = 1079
RPMTAG_VERIFYSCRIPTPROG = 1091
RPMTAG_VERSION = 1001
RPMTAG_XPM = 1013

RPMTRANS_FLAG_ADDINDEPS = 536870912
RPMTRANS_FLAG_ALLFILES = 64

RPMTRANS_FLAG_BUILD_PROBS = 2

RPMTRANS_FLAG_JUSTDB = 8
RPMTRANS_FLAG_KEEPOBSOLETE = 128
RPMTRANS_FLAG_NOCONFIGS = 1073741824
RPMTRANS_FLAG_NOCONTEXTS = 256
RPMTRANS_FLAG_NODOCS = 32
RPMTRANS_FLAG_NOFILEDIGEST = 134217728
RPMTRANS_FLAG_NOMD5 = 134217728
RPMTRANS_FLAG_NOPOST = 262144
RPMTRANS_FLAG_NOPOSTUN = 4194304
RPMTRANS_FLAG_NOPRE = 131072
RPMTRANS_FLAG_NOPREUN = 2097152
RPMTRANS_FLAG_NOSCRIPTS = 4
RPMTRANS_FLAG_NOSUGGEST = 268435456
RPMTRANS_FLAG_NOTRIGGERIN = 524288
RPMTRANS_FLAG_NOTRIGGERPOSTUN = 8388608
RPMTRANS_FLAG_NOTRIGGERPREIN = 65536
RPMTRANS_FLAG_NOTRIGGERS = 16
RPMTRANS_FLAG_NOTRIGGERUN = 1048576
RPMTRANS_FLAG_REPACKAGE = 1024
RPMTRANS_FLAG_REVERSE = 32768
RPMTRANS_FLAG_TEST = 1

RPMVSF_DEFAULT = 0
RPMVSF_NEEDPAYLOAD = 2
RPMVSF_NODSA = 262144
RPMVSF_NODSAHEADER = 1024
RPMVSF_NOHDRCHK = 1
RPMVSF_NOMD5 = 131072
RPMVSF_NOMD5HEADER = 512
RPMVSF_NORSA = 524288
RPMVSF_NORSAHEADER = 2048
RPMVSF_NOSHA1 = 65536
RPMVSF_NOSHA1HEADER = 256

TR_ADDED = 1
TR_REMOVED = 2

VERIFY_DIGEST = 524288
VERIFY_SIGNATURE = 1048576

_RPMVSF_NODIGESTS = 197376
_RPMVSF_NOHEADER = 3840
_RPMVSF_NOPAYLOAD = 983040
_RPMVSF_NOSIGNATURES = 789504

# functions

def addMacro(*args, **kwargs): # real signature unknown
    pass

def archscore(*args, **kwargs): # real signature unknown
    pass

def checkSignals(*args, **kwargs): # real signature unknown
    pass

def delMacro(*args, **kwargs): # real signature unknown
    pass

def expandMacro(*args, **kwargs): # real signature unknown
    pass

def labelCompare(*args, **kwargs): # real signature unknown
    pass

def log(*args, **kwargs): # real signature unknown
    pass

def mergeHeaderListFromFD(*args, **kwargs): # real signature unknown
    pass

def reloadConfig(*args, **kwargs): # real signature unknown
    pass

def setEpochPromote(*args, **kwargs): # real signature unknown
    pass

def setLogFile(*args, **kwargs): # real signature unknown
    pass

def setStats(*args, **kwargs): # real signature unknown
    pass

def setVerbosity(*args, **kwargs): # real signature unknown
    pass

def signalCaught(*args, **kwargs): # real signature unknown
    pass

def versionCompare(*args, **kwargs): # real signature unknown
    pass

# classes

class ds(object):
    # no doc
    def BT(self, *args, **kwargs): # real signature unknown
        """ ds.BT -> BT	- Return build time. """
        pass

    def Color(self, *args, **kwargs): # real signature unknown
        """ ds.Color -> Color	- Return current Color. """
        pass

    def Compare(self, *args, **kwargs): # real signature unknown
        pass

    def Count(self, *args, **kwargs): # real signature unknown
        """ ds.Count -> Count	- Return no. of elements. """
        pass

    def DNEVR(self, *args, **kwargs): # real signature unknown
        """ ds.DNEVR -> DNEVR	- Return current DNEVR. """
        pass

    def EVR(self, *args, **kwargs): # real signature unknown
        """ ds.EVR -> EVR		- Return current EVR. """
        pass

    def Find(self, *args, **kwargs): # real signature unknown
        pass

    def Flags(self, *args, **kwargs): # real signature unknown
        """ ds.Flags -> Flags	- Return current Flags. """
        pass

    def Ix(self, *args, **kwargs): # real signature unknown
        """ ds.Ix -> Ix		- Return current element index. """
        pass

    def Merge(self, *args, **kwargs): # real signature unknown
        pass

    def N(self, *args, **kwargs): # real signature unknown
        """ ds.N -> N		- Return current N. """
        pass

    def next(self): # real signature unknown; restored from __doc__
        """ x.next() -> the next value, or raise StopIteration """
        pass

    def Notify(self, *args, **kwargs): # real signature unknown
        pass

    def Refs(self, *args, **kwargs): # real signature unknown
        """ ds.Refs -> Refs	- Return current Refs. """
        pass

    def Rpmlib(self, *args, **kwargs): # real signature unknown
        """ ds.Rpmlib -> nds       - Return internal rpmlib dependency set. """
        pass

    def Search(self, element): # real signature unknown; restored from __doc__
        """
        ds.Search(element) -> matching ds index (-1 on failure)
        - Check that element dependency range overlaps some member of ds.
        The current index in ds is positioned at overlapping member upon success.
        """
        pass

    def SetNoPromote(self, *args, **kwargs): # real signature unknown
        pass

    def Sort(self, *args, **kwargs): # real signature unknown
        pass

    def TagN(self, *args, **kwargs): # real signature unknown
        """ ds.TagN -> TagN	- Return current TagN. """
        pass

    def __delattr__(self, name): # real signature unknown; restored from __doc__
        """ x.__delattr__('name') <==> del x.name """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __getitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self): # real signature unknown; restored from __doc__
        """ x.__iter__() <==> iter(x) """
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __setattr__(self, name, value): # real signature unknown; restored from __doc__
        """ x.__setattr__('name', value) <==> x.name = value """
        pass


class error(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class fd(object):
    # no doc
    def close(self, *args, **kwargs): # real signature unknown
        pass

    def fileno(self, *args, **kwargs): # real signature unknown
        pass

    def flush(self, *args, **kwargs): # real signature unknown
        pass

    def isatty(self, *args, **kwargs): # real signature unknown
        pass

    def read(self, *args, **kwargs): # real signature unknown
        pass

    def seek(self, *args, **kwargs): # real signature unknown
        pass

    def tell(self, *args, **kwargs): # real signature unknown
        pass

    def write(self, *args, **kwargs): # real signature unknown
        pass

    def __delattr__(self, name): # real signature unknown; restored from __doc__
        """ x.__delattr__('name') <==> del x.name """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __setattr__(self, name, value): # real signature unknown; restored from __doc__
        """ x.__setattr__('name', value) <==> x.name = value """
        pass

    closed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class fi(object):
    # no doc
    def BN(self, *args, **kwargs): # real signature unknown
        pass

    def DC(self, *args, **kwargs): # real signature unknown
        pass

    def Digest(self, *args, **kwargs): # real signature unknown
        pass

    def DN(self, *args, **kwargs): # real signature unknown
        pass

    def DX(self, *args, **kwargs): # real signature unknown
        pass

    def FC(self, *args, **kwargs): # real signature unknown
        pass

    def FClass(self, *args, **kwargs): # real signature unknown
        pass

    def FColor(self, *args, **kwargs): # real signature unknown
        pass

    def FFlags(self, *args, **kwargs): # real signature unknown
        pass

    def FGroup(self, *args, **kwargs): # real signature unknown
        pass

    def FLink(self, *args, **kwargs): # real signature unknown
        pass

    def FMode(self, *args, **kwargs): # real signature unknown
        pass

    def FMtime(self, *args, **kwargs): # real signature unknown
        pass

    def FN(self, *args, **kwargs): # real signature unknown
        pass

    def FRdev(self, *args, **kwargs): # real signature unknown
        pass

    def FSize(self, *args, **kwargs): # real signature unknown
        pass

    def FState(self, *args, **kwargs): # real signature unknown
        pass

    def FUser(self, *args, **kwargs): # real signature unknown
        pass

    def FX(self, *args, **kwargs): # real signature unknown
        pass

    def MD5(self, *args, **kwargs): # real signature unknown
        pass

    def next(self): # real signature unknown; restored from __doc__
        """ x.next() -> the next value, or raise StopIteration """
        pass

    def VFlags(self, *args, **kwargs): # real signature unknown
        pass

    def __delattr__(self, name): # real signature unknown; restored from __doc__
        """ x.__delattr__('name') <==> del x.name """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __getitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self): # real signature unknown; restored from __doc__
        """ x.__iter__() <==> iter(x) """
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __setattr__(self, name, value): # real signature unknown; restored from __doc__
        """ x.__setattr__('name', value) <==> x.name = value """
        pass


class hdr(object):
    # no doc
    def compressFilelist(self, *args, **kwargs): # real signature unknown
        pass

    def convert(self, *args, **kwargs): # real signature unknown
        pass

    def dsFromHeader(self, *args, **kwargs): # real signature unknown
        pass

    def dsOfHeader(self, *args, **kwargs): # real signature unknown
        pass

    def expandFilelist(self, *args, **kwargs): # real signature unknown
        pass

    def fiFromHeader(self, *args, **kwargs): # real signature unknown
        pass

    def format(self, *args, **kwargs): # real signature unknown
        pass

    def fullFilelist(self, *args, **kwargs): # real signature unknown
        pass

    def isSource(self, *args, **kwargs): # real signature unknown
        pass

    def keys(self, *args, **kwargs): # real signature unknown
        pass

    def next(self): # real signature unknown; restored from __doc__
        """ x.next() -> the next value, or raise StopIteration """
        pass

    def sprintf(self, *args, **kwargs): # real signature unknown
        pass

    def unload(self, *args, **kwargs): # real signature unknown
        pass

    def write(self, *args, **kwargs): # real signature unknown
        pass

    def __contains__(self, y): # real signature unknown; restored from __doc__
        """ x.__contains__(y) <==> y in x """
        pass

    def __delattr__(self, name): # real signature unknown; restored from __doc__
        """ x.__delattr__('name') <==> del x.name """
        pass

    def __delitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__delitem__(y) <==> del x[y] """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __getitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __hash__(self): # real signature unknown; restored from __doc__
        """ x.__hash__() <==> hash(x) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self): # real signature unknown; restored from __doc__
        """ x.__iter__() <==> iter(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __setattr__(self, name, value): # real signature unknown; restored from __doc__
        """ x.__setattr__('name', value) <==> x.name = value """
        pass

    def __setitem__(self, i, y): # real signature unknown; restored from __doc__
        """ x.__setitem__(i, y) <==> x[i]=y """
        pass


class keyring(object):
    # no doc
    def addKey(self, *args, **kwargs): # real signature unknown
        pass

    def __delattr__(self, name): # real signature unknown; restored from __doc__
        """ x.__delattr__('name') <==> del x.name """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __setattr__(self, name, value): # real signature unknown; restored from __doc__
        """ x.__setattr__('name', value) <==> x.name = value """
        pass


class mi(object):
    # no doc
    def count(self, *args, **kwargs): # real signature unknown
        pass

    def instance(self, *args, **kwargs): # real signature unknown
        pass

    def next(self): # real signature unknown; restored from __doc__
        """ x.next() -> the next value, or raise StopIteration """
        pass

    def pattern(self, TagN, mire_type, pattern): # real signature unknown; restored from __doc__
        """
        mi.pattern(TagN, mire_type, pattern)
        - Set a secondary match pattern on tags from retrieved header.
        """
        pass

    def __delattr__(self, name): # real signature unknown; restored from __doc__
        """ x.__delattr__('name') <==> del x.name """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self): # real signature unknown; restored from __doc__
        """ x.__iter__() <==> iter(x) """
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
        pass

    def __nonzero__(self): # real signature unknown; restored from __doc__
        """ x.__nonzero__() <==> x != 0 """
        pass

    def __setattr__(self, name, value): # real signature unknown; restored from __doc__
        """ x.__setattr__('name', value) <==> x.name = value """
        pass


class prob(object):
    # no doc
    def __delattr__(self, name): # real signature unknown; restored from __doc__
        """ x.__delattr__('name') <==> del x.name """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __setattr__(self, name, value): # real signature unknown; restored from __doc__
        """ x.__setattr__('name', value) <==> x.name = value """
        pass

    def __str__(self): # real signature unknown; restored from __doc__
        """ x.__str__() <==> str(x) """
        pass

    altNEVR = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    key = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pkgNEVR = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _num = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _str = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class pubkey(object):
    # no doc
    def base64(self, *args, **kwargs): # real signature unknown
        pass

    def __delattr__(self, name): # real signature unknown; restored from __doc__
        """ x.__delattr__('name') <==> del x.name """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __setattr__(self, name, value): # real signature unknown; restored from __doc__
        """ x.__setattr__('name', value) <==> x.name = value """
        pass


class te(object):
    # no doc
    def A(self): # real signature unknown; restored from __doc__
        """
        te.A() -> A
        - Return element arch.
        """
        pass

    def Color(self, *args, **kwargs): # real signature unknown
        pass

    def DBOffset(self, *args, **kwargs): # real signature unknown
        pass

    def Degree(self, *args, **kwargs): # real signature unknown
        pass

    def Depth(self, *args, **kwargs): # real signature unknown
        pass

    def DS(self, TagN): # real signature unknown; restored from __doc__
        """
        te.DS(TagN) -> DS
        - Return the TagN dependency set (or None). TagN is one of
        	'Providename', 'Requirename', 'Obsoletename', 'Conflictname'
        """
        pass

    def E(self): # real signature unknown; restored from __doc__
        """
        te.E() -> E
        - Return element epoch.
        """
        pass

    def FI(self, TagN): # real signature unknown; restored from __doc__
        """
        te.FI(TagN) -> FI
        - Return the TagN dependency set (or None). TagN must be 'Basenames'.
        """
        pass

    def Key(self, *args, **kwargs): # real signature unknown
        pass

    def N(self): # real signature unknown; restored from __doc__
        """
        te.N() -> N
        - Return element name.
        """
        pass

    def NEVR(self): # real signature unknown; restored from __doc__
        """
        te.NEVR() -> NEVR
        - Return element name-[epoch:]version-release.
        """
        pass

    def NEVRA(self): # real signature unknown; restored from __doc__
        """
        te.NEVRA() -> NEVRA
        - Return element name-[epoch:]version-release.arch
        """
        pass

    def Npreds(self, *args, **kwargs): # real signature unknown
        pass

    def O(self): # real signature unknown; restored from __doc__
        """
        te.O() -> O
        - Return element os.
        """
        pass

    def Parent(self, *args, **kwargs): # real signature unknown
        pass

    def PkgFileSize(self, *args, **kwargs): # real signature unknown
        pass

    def R(self): # real signature unknown; restored from __doc__
        """
        te.R() -> R
        - Return element release.
        """
        pass

    def Tree(self, *args, **kwargs): # real signature unknown
        pass

    def Type(self): # real signature unknown; restored from __doc__
        """
        te.Type() -> Type
        - Return element type (rpm.TR_ADDED | rpm.TR_REMOVED).
        """
        pass

    def V(self): # real signature unknown; restored from __doc__
        """
        te.V() -> V
        - Return element version.
        """
        pass

    def __delattr__(self, name): # real signature unknown; restored from __doc__
        """ x.__delattr__('name') <==> del x.name """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __setattr__(self, name, value): # real signature unknown; restored from __doc__
        """ x.__setattr__('name', value) <==> x.name = value """
        pass


class ts(object):
    # no doc
    def addErase(self, *args, **kwargs): # real signature unknown
        pass

    def addInstall(self, *args, **kwargs): # real signature unknown
        pass

    def check(self, *args, **kwargs): # real signature unknown
        pass

    def clean(self, *args, **kwargs): # real signature unknown
        pass

    def closeDB(self): # real signature unknown; restored from __doc__
        """
        ts.closeDB() -> None
        - Close the default transaction rpmdb.
          Note: ts.closeDB() disables lazy opens, and should hardly ever be used.
        """
        pass

    def dbMatch(self, TagN=None, key=None, len=None): # real signature unknown; restored from __doc__
        """
        ts.dbMatch([TagN, [key, [len]]]) -> mi
        - Create a match iterator for the default transaction rpmdb.
        """
        return mi

    def getKeyring(self, *args, **kwargs): # real signature unknown
        pass

    def hdrCheck(self, *args, **kwargs): # real signature unknown
        pass

    def hdrFromFdno(self, fdno): # real signature unknown; restored from __doc__
        """
        ts.hdrFromFdno(fdno) -> hdr
        - Read a package header from a file descriptor.
        """
        return hdr

    def initDB(self): # real signature unknown; restored from __doc__
        """
        ts.initDB() -> None
        - Initialize the default transaction rpmdb.
         Note: ts.initDB() is seldom needed anymore.
        """
        pass

    def next(self): # real signature unknown; restored from __doc__
        """ x.next() -> the next value, or raise StopIteration """
        pass

    def openDB(self): # real signature unknown; restored from __doc__
        """
        ts.openDB() -> None
        - Open the default transaction rpmdb.
          Note: The transaction rpmdb is lazily opened, so ts.openDB() is seldom needed.
        """
        pass

    def order(self, *args, **kwargs): # real signature unknown
        pass

    def pgpImportPubkey(self, *args, **kwargs): # real signature unknown
        pass

    def pgpPrtPkts(self, *args, **kwargs): # real signature unknown
        pass

    def problems(self): # real signature unknown; restored from __doc__
        """
        ts.problems() -> ps
        - Return current problem set.
        """
        pass

    def rebuildDB(self): # real signature unknown; restored from __doc__
        """
        ts.rebuildDB() -> None
        - Rebuild the default transaction rpmdb.
        """
        pass

    def run(self, callback, data): # real signature unknown; restored from __doc__
        """
        ts.run(callback, data) -> (problems)
        - Run a transaction set, returning list of problems found.
          Note: The callback may not be None.
        """
        pass

    def setKeyring(self, *args, **kwargs): # real signature unknown
        pass

    def verifyDB(self): # real signature unknown; restored from __doc__
        """
        ts.verifyDB() -> None
        - Verify the default transaction rpmdb.
        """
        pass

    def __delattr__(self, name): # real signature unknown; restored from __doc__
        """ x.__delattr__('name') <==> del x.name """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self): # real signature unknown; restored from __doc__
        """ x.__iter__() <==> iter(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __setattr__(self, name, value): # real signature unknown; restored from __doc__
        """ x.__setattr__('name', value) <==> x.name = value """
        pass

    rootDir = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    scriptFd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _prefcolor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _vsflags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



# variables with complex values

tagnames = {
    61: 'HEADERIMAGE',
    62: 'HEADERSIGNATURES',
    63: 'HEADERIMMUTABLE',
    64: 'HEADERREGIONS',
    100: 'HEADERI18NTABLE',
    257: 'SIGSIZE',
    259: 'SIGPGP',
    261: 'SIGMD5',
    262: 'SIGGPG',
    266: 'PUBKEYS',
    267: 'DSAHEADER',
    268: 'RSAHEADER',
    269: 'SHA1HEADER',
    270: 'LONGSIGSIZE',
    271: 'LONGARCHIVESIZE',
    1000: 'NAME',
    1001: 'VERSION',
    1002: 'RELEASE',
    1003: 'EPOCH',
    1004: 'SUMMARY',
    1005: 'DESCRIPTION',
    1006: 'BUILDTIME',
    1007: 'BUILDHOST',
    1008: 'INSTALLTIME',
    1009: 'SIZE',
    1010: 'DISTRIBUTION',
    1011: 'VENDOR',
    1012: 'GIF',
    1013: 'XPM',
    1014: 'LICENSE',
    1015: 'PACKAGER',
    1016: 'GROUP',
    1018: 'SOURCE',
    1019: 'PATCH',
    1020: 'URL',
    1021: 'OS',
    1022: 'ARCH',
    1023: 'PREIN',
    1024: 'POSTIN',
    1025: 'PREUN',
    1026: 'POSTUN',
    1027: 'OLDFILENAMES',
    1028: 'FILESIZES',
    1029: 'FILESTATES',
    1030: 'FILEMODES',
    1033: 'FILERDEVS',
    1034: 'FILEMTIMES',
    1035: 'FILEMD5S',
    1036: 'FILELINKTOS',
    1037: 'FILEFLAGS',
    1039: 'FILEUSERNAME',
    1040: 'FILEGROUPNAME',
    1043: 'ICON',
    1044: 'SOURCERPM',
    1045: 'FILEVERIFYFLAGS',
    1046: 'ARCHIVESIZE',
    1047: 'PROVIDES',
    1048: 'REQUIREFLAGS',
    1049: 'REQUIRES',
    1050: 'REQUIREVERSION',
    1051: 'NOSOURCE',
    1052: 'NOPATCH',
    1053: 'CONFLICTFLAGS',
    1054: 'CONFLICTS',
    1055: 'CONFLICTVERSION',
    1059: 'EXCLUDEARCH',
    1060: 'EXCLUDEOS',
    1061: 'EXCLUSIVEARCH',
    1062: 'EXCLUSIVEOS',
    1064: 'RPMVERSION',
    1065: 'TRIGGERSCRIPTS',
    1066: 'TRIGGERNAME',
    1067: 'TRIGGERVERSION',
    1068: 'TRIGGERFLAGS',
    1069: 'TRIGGERINDEX',
    1079: 'VERIFYSCRIPT',
    1080: 'CHANGELOGTIME',
    1081: 'CHANGELOGNAME',
    1082: 'CHANGELOGTEXT',
    1085: 'PREINPROG',
    1086: 'POSTINPROG',
    1087: 'PREUNPROG',
    1088: 'POSTUNPROG',
    1089: 'BUILDARCHS',
    1090: 'OBSOLETES',
    1091: 'VERIFYSCRIPTPROG',
    1092: 'TRIGGERSCRIPTPROG',
    1094: 'COOKIE',
    1095: 'FILEDEVICES',
    1096: 'FILEINODES',
    1097: 'FILELANGS',
    1098: 'PREFIXES',
    1099: 'INSTPREFIXES',
    1105: 'CAPABILITY',
    1106: 'SOURCEPACKAGE',
    1112: 'PROVIDEFLAGS',
    1113: 'PROVIDEVERSION',
    1114: 'OBSOLETEFLAGS',
    1115: 'OBSOLETEVERSION',
    1116: 'DIRINDEXES',
    1117: 'BASENAMES',
    1118: 'DIRNAMES',
    1119: 'ORIGDIRINDEXES',
    1120: 'ORIGBASENAMES',
    1121: 'ORIGDIRNAMES',
    1122: 'OPTFLAGS',
    1123: 'DISTURL',
    1124: 'PAYLOADFORMAT',
    1125: 'PAYLOADCOMPRESSOR',
    1126: 'PAYLOADFLAGS',
    1127: 'INSTALLCOLOR',
    1128: 'INSTALLTID',
    1129: 'REMOVETID',
    1131: 'RHNPLATFORM',
    1132: 'PLATFORM',
    1133: 'PATCHESNAME',
    1134: 'PATCHESFLAGS',
    1135: 'PATCHESVERSION',
    1140: 'FILECOLORS',
    1141: 'FILECLASS',
    1142: 'CLASSDICT',
    1143: 'FILEDEPENDSX',
    1144: 'FILEDEPENDSN',
    1145: 'DEPENDSDICT',
    1146: 'SOURCEPKGID',
    1147: 'FILECONTEXTS',
    1148: 'FSCONTEXTS',
    1149: 'RECONTEXTS',
    1150: 'POLICIES',
    1151: 'PRETRANS',
    1152: 'POSTTRANS',
    1153: 'PRETRANSPROG',
    1154: 'POSTTRANSPROG',
    1155: 'DISTTAG',
    1195: 'DBINSTANCE',
    1196: 'NVRA',
    5000: 'FILENAMES',
    5001: 'FILEPROVIDE',
    5002: 'FILEREQUIRE',
    5003: 'FSNAMES',
    5004: 'FSSIZES',
    5005: 'TRIGGERCONDS',
    5006: 'TRIGGERTYPE',
    5007: 'ORIGFILENAMES',
    5008: 'LONGFILESIZES',
    5009: 'LONGSIZE',
    5010: 'FILECAPS',
    5011: 'FILEDIGESTALGO',
    5012: 'BUGURL',
    5013: 'EVR',
    5014: 'NVR',
    5015: 'NEVR',
    5016: 'NEVRA',
    5017: 'HEADERCOLOR',
    5018: 'VERBOSE',
    5019: 'EPOCHNUM',
}

