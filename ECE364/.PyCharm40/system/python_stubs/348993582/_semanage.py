# encoding: utf-8
# module _semanage
# from /usr/lib64/python2.6/site-packages/_semanage.so
# by generator 1.136
# no doc
# no imports

# Variables with simple values

SEMANAGE_CAN_READ = 1
SEMANAGE_CAN_WRITE = 2

SEMANAGE_CON_DIRECT = 1
SEMANAGE_CON_INVALID = 0

SEMANAGE_CON_POLSERV_LOCAL = 2
SEMANAGE_CON_POLSERV_REMOTE = 3

SEMANAGE_FCONTEXT_ALL = 0
SEMANAGE_FCONTEXT_BLOCK = 4
SEMANAGE_FCONTEXT_CHAR = 3
SEMANAGE_FCONTEXT_DIR = 2
SEMANAGE_FCONTEXT_LINK = 6
SEMANAGE_FCONTEXT_PIPE = 7
SEMANAGE_FCONTEXT_REG = 1
SEMANAGE_FCONTEXT_SOCK = 5

SEMANAGE_MSG_ERR = 1
SEMANAGE_MSG_INFO = 3
SEMANAGE_MSG_WARN = 2

SEMANAGE_PROTO_IP4 = 0
SEMANAGE_PROTO_IP6 = 1
SEMANAGE_PROTO_TCP = 1
SEMANAGE_PROTO_UDP = 0

# functions

def semanage_access_check(*args, **kwargs): # real signature unknown
    pass

def semanage_begin_transaction(*args, **kwargs): # real signature unknown
    pass

def semanage_bool_clone(*args, **kwargs): # real signature unknown
    pass

def semanage_bool_compare(*args, **kwargs): # real signature unknown
    pass

def semanage_bool_compare2(*args, **kwargs): # real signature unknown
    pass

def semanage_bool_count(*args, **kwargs): # real signature unknown
    pass

def semanage_bool_count_active(*args, **kwargs): # real signature unknown
    pass

def semanage_bool_count_local(*args, **kwargs): # real signature unknown
    pass

def semanage_bool_create(*args, **kwargs): # real signature unknown
    pass

def semanage_bool_del_local(*args, **kwargs): # real signature unknown
    pass

def semanage_bool_exists(*args, **kwargs): # real signature unknown
    pass

def semanage_bool_exists_active(*args, **kwargs): # real signature unknown
    pass

def semanage_bool_exists_local(*args, **kwargs): # real signature unknown
    pass

def semanage_bool_free(*args, **kwargs): # real signature unknown
    pass

def semanage_bool_get_name(*args, **kwargs): # real signature unknown
    pass

def semanage_bool_get_value(*args, **kwargs): # real signature unknown
    pass

def semanage_bool_iterate(*args, **kwargs): # real signature unknown
    pass

def semanage_bool_iterate_active(*args, **kwargs): # real signature unknown
    pass

def semanage_bool_iterate_local(*args, **kwargs): # real signature unknown
    pass

def semanage_bool_key_create(*args, **kwargs): # real signature unknown
    pass

def semanage_bool_key_extract(*args, **kwargs): # real signature unknown
    pass

def semanage_bool_key_free(*args, **kwargs): # real signature unknown
    pass

def semanage_bool_list(*args, **kwargs): # real signature unknown
    pass

def semanage_bool_list_active(*args, **kwargs): # real signature unknown
    pass

def semanage_bool_list_local(*args, **kwargs): # real signature unknown
    pass

def semanage_bool_modify_local(*args, **kwargs): # real signature unknown
    pass

def semanage_bool_query(*args, **kwargs): # real signature unknown
    pass

def semanage_bool_query_active(*args, **kwargs): # real signature unknown
    pass

def semanage_bool_query_local(*args, **kwargs): # real signature unknown
    pass

def semanage_bool_set_active(*args, **kwargs): # real signature unknown
    pass

def semanage_bool_set_name(*args, **kwargs): # real signature unknown
    pass

def semanage_bool_set_value(*args, **kwargs): # real signature unknown
    pass

def semanage_commit(*args, **kwargs): # real signature unknown
    pass

def semanage_connect(*args, **kwargs): # real signature unknown
    pass

def semanage_context_clone(*args, **kwargs): # real signature unknown
    pass

def semanage_context_create(*args, **kwargs): # real signature unknown
    pass

def semanage_context_free(*args, **kwargs): # real signature unknown
    pass

def semanage_context_from_string(*args, **kwargs): # real signature unknown
    pass

def semanage_context_get_mls(*args, **kwargs): # real signature unknown
    pass

def semanage_context_get_role(*args, **kwargs): # real signature unknown
    pass

def semanage_context_get_type(*args, **kwargs): # real signature unknown
    pass

def semanage_context_get_user(*args, **kwargs): # real signature unknown
    pass

def semanage_context_set_mls(*args, **kwargs): # real signature unknown
    pass

def semanage_context_set_role(*args, **kwargs): # real signature unknown
    pass

def semanage_context_set_type(*args, **kwargs): # real signature unknown
    pass

def semanage_context_set_user(*args, **kwargs): # real signature unknown
    pass

def semanage_context_to_string(*args, **kwargs): # real signature unknown
    pass

def semanage_disconnect(*args, **kwargs): # real signature unknown
    pass

def semanage_fcontext_clone(*args, **kwargs): # real signature unknown
    pass

def semanage_fcontext_compare(*args, **kwargs): # real signature unknown
    pass

def semanage_fcontext_compare2(*args, **kwargs): # real signature unknown
    pass

def semanage_fcontext_count(*args, **kwargs): # real signature unknown
    pass

def semanage_fcontext_count_local(*args, **kwargs): # real signature unknown
    pass

def semanage_fcontext_create(*args, **kwargs): # real signature unknown
    pass

def semanage_fcontext_del_local(*args, **kwargs): # real signature unknown
    pass

def semanage_fcontext_exists(*args, **kwargs): # real signature unknown
    pass

def semanage_fcontext_exists_local(*args, **kwargs): # real signature unknown
    pass

def semanage_fcontext_free(*args, **kwargs): # real signature unknown
    pass

def semanage_fcontext_get_con(*args, **kwargs): # real signature unknown
    pass

def semanage_fcontext_get_expr(*args, **kwargs): # real signature unknown
    pass

def semanage_fcontext_get_type(*args, **kwargs): # real signature unknown
    pass

def semanage_fcontext_get_type_str(*args, **kwargs): # real signature unknown
    pass

def semanage_fcontext_iterate(*args, **kwargs): # real signature unknown
    pass

def semanage_fcontext_iterate_local(*args, **kwargs): # real signature unknown
    pass

def semanage_fcontext_key_create(*args, **kwargs): # real signature unknown
    pass

def semanage_fcontext_key_extract(*args, **kwargs): # real signature unknown
    pass

def semanage_fcontext_key_free(*args, **kwargs): # real signature unknown
    pass

def semanage_fcontext_list(*args, **kwargs): # real signature unknown
    pass

def semanage_fcontext_list_local(*args, **kwargs): # real signature unknown
    pass

def semanage_fcontext_modify_local(*args, **kwargs): # real signature unknown
    pass

def semanage_fcontext_query(*args, **kwargs): # real signature unknown
    pass

def semanage_fcontext_query_local(*args, **kwargs): # real signature unknown
    pass

def semanage_fcontext_set_con(*args, **kwargs): # real signature unknown
    pass

def semanage_fcontext_set_expr(*args, **kwargs): # real signature unknown
    pass

def semanage_fcontext_set_type(*args, **kwargs): # real signature unknown
    pass

def semanage_get_disable_dontaudit(*args, **kwargs): # real signature unknown
    pass

def semanage_handle_create(*args, **kwargs): # real signature unknown
    pass

def semanage_handle_destroy(*args, **kwargs): # real signature unknown
    pass

def semanage_iface_clone(*args, **kwargs): # real signature unknown
    pass

def semanage_iface_compare(*args, **kwargs): # real signature unknown
    pass

def semanage_iface_compare2(*args, **kwargs): # real signature unknown
    pass

def semanage_iface_count(*args, **kwargs): # real signature unknown
    pass

def semanage_iface_count_local(*args, **kwargs): # real signature unknown
    pass

def semanage_iface_create(*args, **kwargs): # real signature unknown
    pass

def semanage_iface_del_local(*args, **kwargs): # real signature unknown
    pass

def semanage_iface_exists(*args, **kwargs): # real signature unknown
    pass

def semanage_iface_exists_local(*args, **kwargs): # real signature unknown
    pass

def semanage_iface_free(*args, **kwargs): # real signature unknown
    pass

def semanage_iface_get_ifcon(*args, **kwargs): # real signature unknown
    pass

def semanage_iface_get_msgcon(*args, **kwargs): # real signature unknown
    pass

def semanage_iface_get_name(*args, **kwargs): # real signature unknown
    pass

def semanage_iface_iterate(*args, **kwargs): # real signature unknown
    pass

def semanage_iface_iterate_local(*args, **kwargs): # real signature unknown
    pass

def semanage_iface_key_create(*args, **kwargs): # real signature unknown
    pass

def semanage_iface_key_extract(*args, **kwargs): # real signature unknown
    pass

def semanage_iface_key_free(*args, **kwargs): # real signature unknown
    pass

def semanage_iface_list(*args, **kwargs): # real signature unknown
    pass

def semanage_iface_list_local(*args, **kwargs): # real signature unknown
    pass

def semanage_iface_modify_local(*args, **kwargs): # real signature unknown
    pass

def semanage_iface_query(*args, **kwargs): # real signature unknown
    pass

def semanage_iface_query_local(*args, **kwargs): # real signature unknown
    pass

def semanage_iface_set_ifcon(*args, **kwargs): # real signature unknown
    pass

def semanage_iface_set_msgcon(*args, **kwargs): # real signature unknown
    pass

def semanage_iface_set_name(*args, **kwargs): # real signature unknown
    pass

def semanage_is_connected(*args, **kwargs): # real signature unknown
    pass

def semanage_is_managed(*args, **kwargs): # real signature unknown
    pass

def semanage_mls_enabled(*args, **kwargs): # real signature unknown
    pass

def semanage_module_disable(*args, **kwargs): # real signature unknown
    pass

def semanage_module_enable(*args, **kwargs): # real signature unknown
    pass

def semanage_module_get_enabled(*args, **kwargs): # real signature unknown
    pass

def semanage_module_get_name(*args, **kwargs): # real signature unknown
    pass

def semanage_module_get_version(*args, **kwargs): # real signature unknown
    pass

def semanage_module_info_datum_destroy(*args, **kwargs): # real signature unknown
    pass

def semanage_module_install(*args, **kwargs): # real signature unknown
    pass

def semanage_module_install_base(*args, **kwargs): # real signature unknown
    pass

def semanage_module_install_base_file(*args, **kwargs): # real signature unknown
    pass

def semanage_module_install_file(*args, **kwargs): # real signature unknown
    pass

def semanage_module_list(*args, **kwargs): # real signature unknown
    pass

def semanage_module_list_nth(*args, **kwargs): # real signature unknown
    pass

def semanage_module_remove(*args, **kwargs): # real signature unknown
    pass

def semanage_module_upgrade(*args, **kwargs): # real signature unknown
    pass

def semanage_module_upgrade_file(*args, **kwargs): # real signature unknown
    pass

def semanage_msg_get_channel(*args, **kwargs): # real signature unknown
    pass

def semanage_msg_get_fname(*args, **kwargs): # real signature unknown
    pass

def semanage_msg_get_level(*args, **kwargs): # real signature unknown
    pass

def semanage_msg_set_callback(*args, **kwargs): # real signature unknown
    pass

def semanage_node_clone(*args, **kwargs): # real signature unknown
    pass

def semanage_node_compare(*args, **kwargs): # real signature unknown
    pass

def semanage_node_compare2(*args, **kwargs): # real signature unknown
    pass

def semanage_node_count(*args, **kwargs): # real signature unknown
    pass

def semanage_node_count_local(*args, **kwargs): # real signature unknown
    pass

def semanage_node_create(*args, **kwargs): # real signature unknown
    pass

def semanage_node_del_local(*args, **kwargs): # real signature unknown
    pass

def semanage_node_exists(*args, **kwargs): # real signature unknown
    pass

def semanage_node_exists_local(*args, **kwargs): # real signature unknown
    pass

def semanage_node_free(*args, **kwargs): # real signature unknown
    pass

def semanage_node_get_addr(*args, **kwargs): # real signature unknown
    pass

def semanage_node_get_addr_bytes(*args, **kwargs): # real signature unknown
    pass

def semanage_node_get_con(*args, **kwargs): # real signature unknown
    pass

def semanage_node_get_mask(*args, **kwargs): # real signature unknown
    pass

def semanage_node_get_mask_bytes(*args, **kwargs): # real signature unknown
    pass

def semanage_node_get_proto(*args, **kwargs): # real signature unknown
    pass

def semanage_node_get_proto_str(*args, **kwargs): # real signature unknown
    pass

def semanage_node_iterate(*args, **kwargs): # real signature unknown
    pass

def semanage_node_iterate_local(*args, **kwargs): # real signature unknown
    pass

def semanage_node_key_create(*args, **kwargs): # real signature unknown
    pass

def semanage_node_key_extract(*args, **kwargs): # real signature unknown
    pass

def semanage_node_key_free(*args, **kwargs): # real signature unknown
    pass

def semanage_node_list(*args, **kwargs): # real signature unknown
    pass

def semanage_node_list_local(*args, **kwargs): # real signature unknown
    pass

def semanage_node_modify_local(*args, **kwargs): # real signature unknown
    pass

def semanage_node_query(*args, **kwargs): # real signature unknown
    pass

def semanage_node_query_local(*args, **kwargs): # real signature unknown
    pass

def semanage_node_set_addr(*args, **kwargs): # real signature unknown
    pass

def semanage_node_set_addr_bytes(*args, **kwargs): # real signature unknown
    pass

def semanage_node_set_con(*args, **kwargs): # real signature unknown
    pass

def semanage_node_set_mask(*args, **kwargs): # real signature unknown
    pass

def semanage_node_set_mask_bytes(*args, **kwargs): # real signature unknown
    pass

def semanage_node_set_proto(*args, **kwargs): # real signature unknown
    pass

def semanage_port_clone(*args, **kwargs): # real signature unknown
    pass

def semanage_port_compare(*args, **kwargs): # real signature unknown
    pass

def semanage_port_compare2(*args, **kwargs): # real signature unknown
    pass

def semanage_port_count(*args, **kwargs): # real signature unknown
    pass

def semanage_port_count_local(*args, **kwargs): # real signature unknown
    pass

def semanage_port_create(*args, **kwargs): # real signature unknown
    pass

def semanage_port_del_local(*args, **kwargs): # real signature unknown
    pass

def semanage_port_exists(*args, **kwargs): # real signature unknown
    pass

def semanage_port_exists_local(*args, **kwargs): # real signature unknown
    pass

def semanage_port_free(*args, **kwargs): # real signature unknown
    pass

def semanage_port_get_con(*args, **kwargs): # real signature unknown
    pass

def semanage_port_get_high(*args, **kwargs): # real signature unknown
    pass

def semanage_port_get_low(*args, **kwargs): # real signature unknown
    pass

def semanage_port_get_proto(*args, **kwargs): # real signature unknown
    pass

def semanage_port_get_proto_str(*args, **kwargs): # real signature unknown
    pass

def semanage_port_iterate(*args, **kwargs): # real signature unknown
    pass

def semanage_port_iterate_local(*args, **kwargs): # real signature unknown
    pass

def semanage_port_key_create(*args, **kwargs): # real signature unknown
    pass

def semanage_port_key_extract(*args, **kwargs): # real signature unknown
    pass

def semanage_port_key_free(*args, **kwargs): # real signature unknown
    pass

def semanage_port_list(*args, **kwargs): # real signature unknown
    pass

def semanage_port_list_local(*args, **kwargs): # real signature unknown
    pass

def semanage_port_modify_local(*args, **kwargs): # real signature unknown
    pass

def semanage_port_query(*args, **kwargs): # real signature unknown
    pass

def semanage_port_query_local(*args, **kwargs): # real signature unknown
    pass

def semanage_port_set_con(*args, **kwargs): # real signature unknown
    pass

def semanage_port_set_port(*args, **kwargs): # real signature unknown
    pass

def semanage_port_set_proto(*args, **kwargs): # real signature unknown
    pass

def semanage_port_set_range(*args, **kwargs): # real signature unknown
    pass

def semanage_reload_policy(*args, **kwargs): # real signature unknown
    pass

def semanage_select_store(*args, **kwargs): # real signature unknown
    pass

def semanage_set_check_contexts(*args, **kwargs): # real signature unknown
    pass

def semanage_set_create_store(*args, **kwargs): # real signature unknown
    pass

def semanage_set_disable_dontaudit(*args, **kwargs): # real signature unknown
    pass

def semanage_set_rebuild(*args, **kwargs): # real signature unknown
    pass

def semanage_set_reload(*args, **kwargs): # real signature unknown
    pass

def semanage_seuser_clone(*args, **kwargs): # real signature unknown
    pass

def semanage_seuser_compare(*args, **kwargs): # real signature unknown
    pass

def semanage_seuser_compare2(*args, **kwargs): # real signature unknown
    pass

def semanage_seuser_count(*args, **kwargs): # real signature unknown
    pass

def semanage_seuser_count_local(*args, **kwargs): # real signature unknown
    pass

def semanage_seuser_create(*args, **kwargs): # real signature unknown
    pass

def semanage_seuser_del_local(*args, **kwargs): # real signature unknown
    pass

def semanage_seuser_exists(*args, **kwargs): # real signature unknown
    pass

def semanage_seuser_exists_local(*args, **kwargs): # real signature unknown
    pass

def semanage_seuser_free(*args, **kwargs): # real signature unknown
    pass

def semanage_seuser_get_mlsrange(*args, **kwargs): # real signature unknown
    pass

def semanage_seuser_get_name(*args, **kwargs): # real signature unknown
    pass

def semanage_seuser_get_sename(*args, **kwargs): # real signature unknown
    pass

def semanage_seuser_iterate(*args, **kwargs): # real signature unknown
    pass

def semanage_seuser_iterate_local(*args, **kwargs): # real signature unknown
    pass

def semanage_seuser_key_create(*args, **kwargs): # real signature unknown
    pass

def semanage_seuser_key_extract(*args, **kwargs): # real signature unknown
    pass

def semanage_seuser_key_free(*args, **kwargs): # real signature unknown
    pass

def semanage_seuser_list(*args, **kwargs): # real signature unknown
    pass

def semanage_seuser_list_local(*args, **kwargs): # real signature unknown
    pass

def semanage_seuser_modify_local(*args, **kwargs): # real signature unknown
    pass

def semanage_seuser_query(*args, **kwargs): # real signature unknown
    pass

def semanage_seuser_query_local(*args, **kwargs): # real signature unknown
    pass

def semanage_seuser_set_mlsrange(*args, **kwargs): # real signature unknown
    pass

def semanage_seuser_set_name(*args, **kwargs): # real signature unknown
    pass

def semanage_seuser_set_sename(*args, **kwargs): # real signature unknown
    pass

def semanage_user_add_role(*args, **kwargs): # real signature unknown
    pass

def semanage_user_clone(*args, **kwargs): # real signature unknown
    pass

def semanage_user_compare(*args, **kwargs): # real signature unknown
    pass

def semanage_user_compare2(*args, **kwargs): # real signature unknown
    pass

def semanage_user_count(*args, **kwargs): # real signature unknown
    pass

def semanage_user_count_local(*args, **kwargs): # real signature unknown
    pass

def semanage_user_create(*args, **kwargs): # real signature unknown
    pass

def semanage_user_del_local(*args, **kwargs): # real signature unknown
    pass

def semanage_user_del_role(*args, **kwargs): # real signature unknown
    pass

def semanage_user_exists(*args, **kwargs): # real signature unknown
    pass

def semanage_user_exists_local(*args, **kwargs): # real signature unknown
    pass

def semanage_user_free(*args, **kwargs): # real signature unknown
    pass

def semanage_user_get_mlslevel(*args, **kwargs): # real signature unknown
    pass

def semanage_user_get_mlsrange(*args, **kwargs): # real signature unknown
    pass

def semanage_user_get_name(*args, **kwargs): # real signature unknown
    pass

def semanage_user_get_num_roles(*args, **kwargs): # real signature unknown
    pass

def semanage_user_get_prefix(*args, **kwargs): # real signature unknown
    pass

def semanage_user_get_roles(*args, **kwargs): # real signature unknown
    pass

def semanage_user_has_role(*args, **kwargs): # real signature unknown
    pass

def semanage_user_iterate(*args, **kwargs): # real signature unknown
    pass

def semanage_user_iterate_local(*args, **kwargs): # real signature unknown
    pass

def semanage_user_key_create(*args, **kwargs): # real signature unknown
    pass

def semanage_user_key_extract(*args, **kwargs): # real signature unknown
    pass

def semanage_user_key_free(*args, **kwargs): # real signature unknown
    pass

def semanage_user_list(*args, **kwargs): # real signature unknown
    pass

def semanage_user_list_local(*args, **kwargs): # real signature unknown
    pass

def semanage_user_modify_local(*args, **kwargs): # real signature unknown
    pass

def semanage_user_query(*args, **kwargs): # real signature unknown
    pass

def semanage_user_query_local(*args, **kwargs): # real signature unknown
    pass

def semanage_user_set_mlslevel(*args, **kwargs): # real signature unknown
    pass

def semanage_user_set_mlsrange(*args, **kwargs): # real signature unknown
    pass

def semanage_user_set_name(*args, **kwargs): # real signature unknown
    pass

def semanage_user_set_prefix(*args, **kwargs): # real signature unknown
    pass

def semanage_user_set_roles(*args, **kwargs): # real signature unknown
    pass

def SWIG_PyInstanceMethod_New(*args, **kwargs): # real signature unknown
    pass

# no classes
