# encoding: utf-8
# module ORBit.CORBA
# from /usr/lib64/python2.6/site-packages/gtk-2.0/gnomevfs/gnomevfsbonobo.so
# by generator 1.136
# no doc

# imports
from CORBA import (Any, BAD_CONTEXT, BAD_INV_ORDER, BAD_OPERATION, BAD_PARAM, 
    BAD_TYPECODE, CODESET_INCOMPATIBLE, COMM_FAILURE, DATA_CONVERSION, 
    Exception, FREE_MEM, IMP_LIMIT, INITIALIZE, INTERNAL, INTF_REPOS, 
    INVALID_TRANSACTION, INV_FLAG, INV_IDENT, INV_OBJREF, INV_POLICY, MARSHAL, 
    NO_IMPLEMENT, NO_MEMORY, NO_PERMISSION, NO_RESOURCES, NO_RESPONSE, 
    OBJECT_NOT_EXIST, OBJ_ADAPTER, ORB, Object, PERSIST_STORE, Policy, 
    SystemException, TRANSACTION_REQUIRED, TRANSACTION_ROLLEDBACK, TRANSIENT, 
    TypeCode, UNKNOWN, UserException, fixed)

import CORBA as __CORBA


# Variables with simple values

ADD_OVERRIDE = 1

ATTR_NORMAL = 0
ATTR_READONLY = 1

COMPLETED_MAYBE = 2
COMPLETED_NO = 1
COMPLETED_YES = 0

dk_AbstractInterface = 24
dk_Alias = 9
dk_all = 1
dk_Array = 16
dk_Attribute = 2
dk_Component = 26
dk_Constant = 3
dk_Consumes = 32
dk_Emits = 30
dk_Enum = 12
dk_Event = 35
dk_Exception = 4
dk_Factory = 28
dk_Finder = 29
dk_Fixed = 19
dk_Home = 27
dk_Interface = 5
dk_LocalInterface = 25
dk_Module = 6
dk_Native = 23
dk_none = 0
dk_Operation = 7
dk_Primitive = 13
dk_Provides = 33
dk_Publishes = 31
dk_Repository = 17
dk_Sequence = 15
dk_String = 14
dk_Struct = 10
dk_Typedef = 8
dk_Union = 11
dk_Uses = 34
dk_Value = 20
dk_ValueBox = 21
dk_ValueMember = 22
dk_Wstring = 18

FALSE = False

NO_EXCEPTION = 0

OP_NORMAL = 0
OP_ONEWAY = 1

PARAM_IN = 0
PARAM_INOUT = 2
PARAM_OUT = 1

pk_any = 11
pk_boolean = 8
pk_char = 9
pk_double = 7
pk_float = 6
pk_long = 3
pk_longdouble = 18
pk_longlong = 16
pk_null = 0
pk_objref = 15
pk_octet = 10
pk_Principal = 13
pk_short = 2
pk_string = 14
pk_TypeCode = 12
pk_ulong = 5
pk_ulonglong = 17
pk_ushort = 4

pk_value_base = 21

pk_void = 1
pk_wchar = 19
pk_wstring = 20

SET_OVERRIDE = 0

SYSTEM_EXCEPTION = 2

tk_abstract_interface = 32

tk_alias = 21
tk_any = 11
tk_array = 20
tk_boolean = 8
tk_char = 9
tk_component = 34
tk_double = 7
tk_enum = 17
tk_event = 36
tk_except = 22
tk_fixed = 28
tk_float = 6
tk_home = 35

tk_local_interface = 33

tk_long = 3
tk_longdouble = 25
tk_longlong = 23
tk_native = 31
tk_null = 0
tk_objref = 14
tk_octet = 10
tk_Principal = 13
tk_sequence = 19
tk_short = 2
tk_string = 18
tk_struct = 15
tk_TypeCode = 12
tk_ulong = 5
tk_ulonglong = 24
tk_union = 16
tk_ushort = 4
tk_value = 29

tk_value_box = 30

tk_void = 1
tk_wchar = 26
tk_wstring = 27

TRUE = True

USER_EXCEPTION = 1

# functions

def ORB_init(*args, **kwargs): # real signature unknown
    pass

# classes

class AttributeDescription(__CORBA.Struct):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __typecode__ = None # (!) real value is ''


class AttributeMode(__CORBA.Enum):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __enum_values__ = (
        0,
        1,
    )
    __typecode__ = None # (!) real value is ''


class completion_status(__CORBA.Enum):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __enum_values__ = (
        0,
        1,
        2,
    )
    __typecode__ = None # (!) real value is ''


class ConstantDescription(__CORBA.Struct):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __typecode__ = None # (!) real value is ''


class DefinitionKind(__CORBA.Enum):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __enum_values__ = (
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
        21,
        22,
        23,
        24,
        25,
        26,
        27,
        28,
        29,
        30,
        31,
        32,
        33,
        34,
        35,
    )
    __typecode__ = None # (!) real value is ''


class ExceptionDescription(__CORBA.Struct):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __typecode__ = None # (!) real value is ''


class exception_type(__CORBA.Enum):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __enum_values__ = (
        0,
        1,
        2,
    )
    __typecode__ = None # (!) real value is ''


class Initializer(__CORBA.Struct):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __typecode__ = None # (!) real value is ''


class InterfaceDescription(__CORBA.Struct):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __typecode__ = None # (!) real value is ''


class ModuleDescription(__CORBA.Struct):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __typecode__ = None # (!) real value is ''


class NamedValue(__CORBA.Struct):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __typecode__ = None # (!) real value is ''


class OperationDescription(__CORBA.Struct):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __typecode__ = None # (!) real value is ''


class OperationMode(__CORBA.Enum):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __enum_values__ = (
        0,
        1,
    )
    __typecode__ = None # (!) real value is ''


class ParameterDescription(__CORBA.Struct):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __typecode__ = None # (!) real value is ''


class ParameterMode(__CORBA.Enum):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __enum_values__ = (
        0,
        1,
        2,
    )
    __typecode__ = None # (!) real value is ''


class PolicyError(__CORBA.UserException):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __typecode__ = None # (!) real value is ''


class PrimitiveKind(__CORBA.Enum):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __enum_values__ = (
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
        21,
    )
    __typecode__ = None # (!) real value is ''


class ServiceDetail(__CORBA.Struct):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __typecode__ = None # (!) real value is ''


class ServiceInformation(__CORBA.Struct):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __typecode__ = None # (!) real value is ''


class SetOverrideType(__CORBA.Enum):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __enum_values__ = (
        0,
        1,
    )
    __typecode__ = None # (!) real value is ''


class StructMember(__CORBA.Struct):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __typecode__ = None # (!) real value is ''


class TCKind(__CORBA.Enum):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __enum_values__ = (
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
        21,
        22,
        23,
        24,
        25,
        26,
        27,
        28,
        29,
        30,
        31,
        32,
        33,
        34,
        35,
        36,
    )
    __typecode__ = None # (!) real value is ''


class TypeDescription(__CORBA.Struct):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __typecode__ = None # (!) real value is ''


class UnionMember(__CORBA.Struct):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __typecode__ = None # (!) real value is ''


class ValueDescription(__CORBA.Struct):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __typecode__ = None # (!) real value is ''


class ValueMember(__CORBA.Struct):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''
    __typecode__ = None # (!) real value is ''


# variables with complex values

TC_any = None # (!) real value is ''

TC_boolean = None # (!) real value is ''

TC_char = None # (!) real value is ''

TC_double = None # (!) real value is ''

TC_float = None # (!) real value is ''

TC_long = None # (!) real value is ''

TC_longdouble = None # (!) real value is ''

TC_longlong = None # (!) real value is ''

TC_null = None # (!) real value is ''

TC_Object = None # (!) real value is ''

TC_octet = None # (!) real value is ''

TC_short = None # (!) real value is ''

TC_string = None # (!) real value is ''

TC_TypeCode = None # (!) real value is ''

TC_ulong = None # (!) real value is ''

TC_ulonglong = None # (!) real value is ''

TC_ushort = None # (!) real value is ''

TC_void = None # (!) real value is ''

TC_wchar = None # (!) real value is ''

TC_wstring = None # (!) real value is ''

