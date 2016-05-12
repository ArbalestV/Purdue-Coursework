# encoding: utf-8
# module CORBA calls itself ORBit.CORBA
# from /usr/lib64/python2.6/site-packages/gtk-2.0/bonobo/_bonobo.so
# by generator 1.136
# no doc

# imports
from ORBit.CORBA import (ADD_OVERRIDE, ATTR_NORMAL, ATTR_READONLY, 
    AttributeDescription, AttributeMode, COMPLETED_MAYBE, COMPLETED_NO, 
    COMPLETED_YES, ConstantDescription, DefinitionKind, ExceptionDescription, 
    Initializer, InterfaceDescription, ModuleDescription, NO_EXCEPTION, 
    NamedValue, OP_NORMAL, OP_ONEWAY, ORB_init, OperationDescription, 
    OperationMode, PARAM_IN, PARAM_INOUT, PARAM_OUT, ParameterDescription, 
    ParameterMode, PolicyError, PrimitiveKind, SET_OVERRIDE, SYSTEM_EXCEPTION, 
    ServiceDetail, ServiceInformation, SetOverrideType, StructMember, TCKind, 
    TypeDescription, USER_EXCEPTION, UnionMember, ValueDescription, 
    ValueMember, completion_status, dk_AbstractInterface, dk_Alias, dk_Array, 
    dk_Attribute, dk_Component, dk_Constant, dk_Consumes, dk_Emits, dk_Enum, 
    dk_Event, dk_Exception, dk_Factory, dk_Finder, dk_Fixed, dk_Home, 
    dk_Interface, dk_LocalInterface, dk_Module, dk_Native, dk_Operation, 
    dk_Primitive, dk_Provides, dk_Publishes, dk_Repository, dk_Sequence, 
    dk_String, dk_Struct, dk_Typedef, dk_Union, dk_Uses, dk_Value, 
    dk_ValueBox, dk_ValueMember, dk_Wstring, dk_all, dk_none, exception_type, 
    pk_Principal, pk_TypeCode, pk_any, pk_boolean, pk_char, pk_double, 
    pk_float, pk_long, pk_longdouble, pk_longlong, pk_null, pk_objref, 
    pk_octet, pk_short, pk_string, pk_ulong, pk_ulonglong, pk_ushort, 
    pk_value_base, pk_void, pk_wchar, pk_wstring, tk_Principal, tk_TypeCode, 
    tk_abstract_interface, tk_alias, tk_any, tk_array, tk_boolean, tk_char, 
    tk_component, tk_double, tk_enum, tk_event, tk_except, tk_fixed, tk_float, 
    tk_home, tk_local_interface, tk_long, tk_longdouble, tk_longlong, 
    tk_native, tk_null, tk_objref, tk_octet, tk_sequence, tk_short, tk_string, 
    tk_struct, tk_ulong, tk_ulonglong, tk_union, tk_ushort, tk_value, 
    tk_value_box, tk_void, tk_wchar, tk_wstring)


from object import object

class Object(object):
    # no doc
    def _duplicate(self): # real signature unknown; restored from __doc__
        """ _duplicate() -> CORBA.Object """
        pass

    def _get_orbit_object_refcount(self): # real signature unknown; restored from __doc__
        """ _get_orbit_object_refcount() -> integer """
        return 0

    def _hash(self, maximum): # real signature unknown; restored from __doc__
        """ _hash(maximum) -> int """
        return 0

    def _is_a(self, type_id): # real signature unknown; restored from __doc__
        """ _is_a(type_id) -> boolean """
        return False

    def _is_equivalent(self, other): # real signature unknown; restored from __doc__
        """ _is_equivalent(other) -> boolean """
        return False

    def _is_nil(self): # real signature unknown; restored from __doc__
        """ _is_nil() -> boolean """
        return False

    def _narrow(self, stub): # real signature unknown; restored from __doc__
        """ _narrow(stub) -> object """
        return object()

    def _non_existent(self): # real signature unknown; restored from __doc__
        """ _non_existent() -> boolean """
        return False

    def __cmp__(self, y): # real signature unknown; restored from __doc__
        """ x.__cmp__(y) <==> cmp(x,y) """
        pass

    def __hash__(self): # real signature unknown; restored from __doc__
        """ x.__hash__() <==> hash(x) """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __repr__(self): # real signature unknown; restored from __doc__
        """ x.__repr__() <==> repr(x) """
        pass

    __typecode__ = None # (!) real value is ''


