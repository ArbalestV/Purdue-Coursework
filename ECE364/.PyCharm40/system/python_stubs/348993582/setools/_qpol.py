# encoding: utf-8
# module setools._qpol
# from /usr/lib64/python2.6/site-packages/setools/_qpol.so
# by generator 1.136
# no doc
# no imports

# Variables with simple values

IPPROTO_TCP = 6
IPPROTO_UDP = 17

QPOL_CAP_ATTRIB_NAMES = 0

QPOL_CAP_CONDITIONALS = 3

QPOL_CAP_LINE_NUMBERS = 2

QPOL_CAP_MLS = 4
QPOL_CAP_MODULES = 6
QPOL_CAP_NEVERALLOW = 9

QPOL_CAP_RULES_LOADED = 7

QPOL_CAP_SOURCE = 8

QPOL_CAP_SYN_RULES = 1

QPOL_CEXPR_OP_DOM = 3
QPOL_CEXPR_OP_DOMBY = 4
QPOL_CEXPR_OP_EQ = 1
QPOL_CEXPR_OP_INCOMP = 5
QPOL_CEXPR_OP_NEQ = 2

QPOL_CEXPR_SYM_H1H2 = 256
QPOL_CEXPR_SYM_H1L2 = 128
QPOL_CEXPR_SYM_L1H1 = 512
QPOL_CEXPR_SYM_L1H2 = 64
QPOL_CEXPR_SYM_L1L2 = 32
QPOL_CEXPR_SYM_L2H2 = 1024
QPOL_CEXPR_SYM_ROLE = 2
QPOL_CEXPR_SYM_TARGET = 8
QPOL_CEXPR_SYM_TYPE = 4
QPOL_CEXPR_SYM_USER = 1
QPOL_CEXPR_SYM_XTARGET = 16

QPOL_CEXPR_TYPE_AND = 2
QPOL_CEXPR_TYPE_ATTR = 4
QPOL_CEXPR_TYPE_NAMES = 5
QPOL_CEXPR_TYPE_NOT = 1
QPOL_CEXPR_TYPE_OR = 3

QPOL_CLASS_ALL = 0

QPOL_CLASS_BLK_FILE = 11

QPOL_CLASS_CHR_FILE = 10

QPOL_CLASS_DIR = 7

QPOL_CLASS_FIFO_FILE = 13

QPOL_CLASS_FILE = 6

QPOL_CLASS_LNK_FILE = 9

QPOL_CLASS_SOCK_FILE = 12

QPOL_COND_EXPR_AND = 4
QPOL_COND_EXPR_BOOL = 1
QPOL_COND_EXPR_EQ = 6
QPOL_COND_EXPR_NEQ = 7
QPOL_COND_EXPR_NOT = 2
QPOL_COND_EXPR_OR = 3
QPOL_COND_EXPR_XOR = 5

QPOL_FS_USE_GENFS = 4
QPOL_FS_USE_NONE = 5
QPOL_FS_USE_PSID = 6
QPOL_FS_USE_TASK = 3
QPOL_FS_USE_TRANS = 2
QPOL_FS_USE_XATTR = 1

QPOL_IPV4 = 0
QPOL_IPV6 = 1

QPOL_MODULE_BASE = 1
QPOL_MODULE_OTHER = 2
QPOL_MODULE_UNKNOWN = 0

QPOL_POLICY_KERNEL_BINARY = 1
QPOL_POLICY_KERNEL_SOURCE = 0

QPOL_POLICY_MODULE_BINARY = 2

QPOL_POLICY_OPTION_MATCH_SYSTEM = 4

QPOL_POLICY_OPTION_NO_NEVERALLOWS = 1
QPOL_POLICY_OPTION_NO_RULES = 2

QPOL_POLICY_UNKNOWN = -1

QPOL_RULE_ALLOW = 1
QPOL_RULE_AUDITALLOW = 2
QPOL_RULE_DONTAUDIT = 4
QPOL_RULE_NEVERALLOW = 128

QPOL_RULE_TYPE_CHANGE = 64
QPOL_RULE_TYPE_MEMBER = 32
QPOL_RULE_TYPE_TRANS = 16

# functions

def delete_qpol_avrule_t(*args, **kwargs): # real signature unknown
    pass

def delete_qpol_bool_t(*args, **kwargs): # real signature unknown
    pass

def delete_qpol_cat_t(*args, **kwargs): # real signature unknown
    pass

def delete_qpol_class_t(*args, **kwargs): # real signature unknown
    pass

def delete_qpol_common_t(*args, **kwargs): # real signature unknown
    pass

def delete_qpol_cond_expr_node_t(*args, **kwargs): # real signature unknown
    pass

def delete_qpol_cond_t(*args, **kwargs): # real signature unknown
    pass

def delete_qpol_constraint_expr_node_t(*args, **kwargs): # real signature unknown
    pass

def delete_qpol_constraint_t(*args, **kwargs): # real signature unknown
    pass

def delete_qpol_context_t(*args, **kwargs): # real signature unknown
    pass

def delete_qpol_fs_use_t(*args, **kwargs): # real signature unknown
    pass

def delete_qpol_genfscon_t(*args, **kwargs): # real signature unknown
    pass

def delete_qpol_isid_t(*args, **kwargs): # real signature unknown
    pass

def delete_qpol_iterator_t(*args, **kwargs): # real signature unknown
    pass

def delete_qpol_level_t(*args, **kwargs): # real signature unknown
    pass

def delete_qpol_mls_level_t(*args, **kwargs): # real signature unknown
    pass

def delete_qpol_mls_range_t(*args, **kwargs): # real signature unknown
    pass

def delete_qpol_module_t(*args, **kwargs): # real signature unknown
    pass

def delete_qpol_netifcon_t(*args, **kwargs): # real signature unknown
    pass

def delete_qpol_nodecon_t(*args, **kwargs): # real signature unknown
    pass

def delete_qpol_policy_t(*args, **kwargs): # real signature unknown
    pass

def delete_qpol_portcon_t(*args, **kwargs): # real signature unknown
    pass

def delete_qpol_range_trans_t(*args, **kwargs): # real signature unknown
    pass

def delete_qpol_role_allow_t(*args, **kwargs): # real signature unknown
    pass

def delete_qpol_role_t(*args, **kwargs): # real signature unknown
    pass

def delete_qpol_role_trans_t(*args, **kwargs): # real signature unknown
    pass

def delete_qpol_syn_avrule_t(*args, **kwargs): # real signature unknown
    pass

def delete_qpol_syn_terule_t(*args, **kwargs): # real signature unknown
    pass

def delete_qpol_terule_t(*args, **kwargs): # real signature unknown
    pass

def delete_qpol_type_set_t(*args, **kwargs): # real signature unknown
    pass

def delete_qpol_type_t(*args, **kwargs): # real signature unknown
    pass

def delete_qpol_user_t(*args, **kwargs): # real signature unknown
    pass

def delete_qpol_validatetrans_t(*args, **kwargs): # real signature unknown
    pass

def libqpol_get_version(*args, **kwargs): # real signature unknown
    pass

def new_qpol_avrule_t(*args, **kwargs): # real signature unknown
    pass

def new_qpol_bool_t(*args, **kwargs): # real signature unknown
    pass

def new_qpol_cat_t(*args, **kwargs): # real signature unknown
    pass

def new_qpol_class_t(*args, **kwargs): # real signature unknown
    pass

def new_qpol_common_t(*args, **kwargs): # real signature unknown
    pass

def new_qpol_cond_expr_node_t(*args, **kwargs): # real signature unknown
    pass

def new_qpol_cond_t(*args, **kwargs): # real signature unknown
    pass

def new_qpol_constraint_expr_node_t(*args, **kwargs): # real signature unknown
    pass

def new_qpol_constraint_t(*args, **kwargs): # real signature unknown
    pass

def new_qpol_context_t(*args, **kwargs): # real signature unknown
    pass

def new_qpol_fs_use_t(*args, **kwargs): # real signature unknown
    pass

def new_qpol_genfscon_t(*args, **kwargs): # real signature unknown
    pass

def new_qpol_isid_t(*args, **kwargs): # real signature unknown
    pass

def new_qpol_iterator_t(*args, **kwargs): # real signature unknown
    pass

def new_qpol_level_t(*args, **kwargs): # real signature unknown
    pass

def new_qpol_mls_level_t(*args, **kwargs): # real signature unknown
    pass

def new_qpol_mls_range_t(*args, **kwargs): # real signature unknown
    pass

def new_qpol_module_t(*args, **kwargs): # real signature unknown
    pass

def new_qpol_netifcon_t(*args, **kwargs): # real signature unknown
    pass

def new_qpol_nodecon_t(*args, **kwargs): # real signature unknown
    pass

def new_qpol_policy_t(*args, **kwargs): # real signature unknown
    pass

def new_qpol_portcon_t(*args, **kwargs): # real signature unknown
    pass

def new_qpol_range_trans_t(*args, **kwargs): # real signature unknown
    pass

def new_qpol_role_allow_t(*args, **kwargs): # real signature unknown
    pass

def new_qpol_role_t(*args, **kwargs): # real signature unknown
    pass

def new_qpol_role_trans_t(*args, **kwargs): # real signature unknown
    pass

def new_qpol_syn_avrule_t(*args, **kwargs): # real signature unknown
    pass

def new_qpol_syn_terule_t(*args, **kwargs): # real signature unknown
    pass

def new_qpol_terule_t(*args, **kwargs): # real signature unknown
    pass

def new_qpol_type_set_t(*args, **kwargs): # real signature unknown
    pass

def new_qpol_type_t(*args, **kwargs): # real signature unknown
    pass

def new_qpol_user_t(*args, **kwargs): # real signature unknown
    pass

def new_qpol_validatetrans_t(*args, **kwargs): # real signature unknown
    pass

def qpol_avrule_from_void(*args, **kwargs): # real signature unknown
    pass

def qpol_avrule_t_get_cond(*args, **kwargs): # real signature unknown
    pass

def qpol_avrule_t_get_is_enabled(*args, **kwargs): # real signature unknown
    pass

def qpol_avrule_t_get_object_class(*args, **kwargs): # real signature unknown
    pass

def qpol_avrule_t_get_perm_iter(*args, **kwargs): # real signature unknown
    pass

def qpol_avrule_t_get_rule_type(*args, **kwargs): # real signature unknown
    pass

def qpol_avrule_t_get_source_type(*args, **kwargs): # real signature unknown
    pass

def qpol_avrule_t_get_syn_avrule_iter(*args, **kwargs): # real signature unknown
    pass

def qpol_avrule_t_get_target_type(*args, **kwargs): # real signature unknown
    pass

def qpol_avrule_t_get_which_list(*args, **kwargs): # real signature unknown
    pass

def qpol_avrule_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def qpol_bool_from_void(*args, **kwargs): # real signature unknown
    pass

def qpol_bool_t_get_name(*args, **kwargs): # real signature unknown
    pass

def qpol_bool_t_get_state(*args, **kwargs): # real signature unknown
    pass

def qpol_bool_t_get_value(*args, **kwargs): # real signature unknown
    pass

def qpol_bool_t_set_state(*args, **kwargs): # real signature unknown
    pass

def qpol_bool_t_set_state_no_eval(*args, **kwargs): # real signature unknown
    pass

def qpol_bool_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def qpol_cat_from_void(*args, **kwargs): # real signature unknown
    pass

def qpol_cat_t_get_alias_iter(*args, **kwargs): # real signature unknown
    pass

def qpol_cat_t_get_isalias(*args, **kwargs): # real signature unknown
    pass

def qpol_cat_t_get_name(*args, **kwargs): # real signature unknown
    pass

def qpol_cat_t_get_value(*args, **kwargs): # real signature unknown
    pass

def qpol_cat_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def qpol_class_from_void(*args, **kwargs): # real signature unknown
    pass

def qpol_class_t_get_common(*args, **kwargs): # real signature unknown
    pass

def qpol_class_t_get_constraint_iter(*args, **kwargs): # real signature unknown
    pass

def qpol_class_t_get_name(*args, **kwargs): # real signature unknown
    pass

def qpol_class_t_get_perm_iter(*args, **kwargs): # real signature unknown
    pass

def qpol_class_t_get_validatetrans_iter(*args, **kwargs): # real signature unknown
    pass

def qpol_class_t_get_value(*args, **kwargs): # real signature unknown
    pass

def qpol_class_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def qpol_common_from_void(*args, **kwargs): # real signature unknown
    pass

def qpol_common_t_get_name(*args, **kwargs): # real signature unknown
    pass

def qpol_common_t_get_perm_iter(*args, **kwargs): # real signature unknown
    pass

def qpol_common_t_get_value(*args, **kwargs): # real signature unknown
    pass

def qpol_common_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def qpol_cond_expr_node_from_void(*args, **kwargs): # real signature unknown
    pass

def qpol_cond_expr_node_t_get_bool(*args, **kwargs): # real signature unknown
    pass

def qpol_cond_expr_node_t_get_expr_type(*args, **kwargs): # real signature unknown
    pass

def qpol_cond_expr_node_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def qpol_cond_from_void(*args, **kwargs): # real signature unknown
    pass

def qpol_cond_t_eval(*args, **kwargs): # real signature unknown
    pass

def qpol_cond_t_get_av_false_iter(*args, **kwargs): # real signature unknown
    pass

def qpol_cond_t_get_av_true_iter(*args, **kwargs): # real signature unknown
    pass

def qpol_cond_t_get_expr_node_iter(*args, **kwargs): # real signature unknown
    pass

def qpol_cond_t_get_te_false_iter(*args, **kwargs): # real signature unknown
    pass

def qpol_cond_t_get_te_true_iter(*args, **kwargs): # real signature unknown
    pass

def qpol_cond_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def qpol_constraint_expr_node_from_void(*args, **kwargs): # real signature unknown
    pass

def qpol_constraint_expr_node_t_get_expr_type(*args, **kwargs): # real signature unknown
    pass

def qpol_constraint_expr_node_t_get_names_iter(*args, **kwargs): # real signature unknown
    pass

def qpol_constraint_expr_node_t_get_op(*args, **kwargs): # real signature unknown
    pass

def qpol_constraint_expr_node_t_get_sym_type(*args, **kwargs): # real signature unknown
    pass

def qpol_constraint_expr_node_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def qpol_constraint_from_void(*args, **kwargs): # real signature unknown
    pass

def qpol_constraint_t_get_class(*args, **kwargs): # real signature unknown
    pass

def qpol_constraint_t_get_expr_iter(*args, **kwargs): # real signature unknown
    pass

def qpol_constraint_t_get_perm_iter(*args, **kwargs): # real signature unknown
    pass

def qpol_constraint_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def qpol_context_from_void(*args, **kwargs): # real signature unknown
    pass

def qpol_context_t_get_range(*args, **kwargs): # real signature unknown
    pass

def qpol_context_t_get_role(*args, **kwargs): # real signature unknown
    pass

def qpol_context_t_get_type(*args, **kwargs): # real signature unknown
    pass

def qpol_context_t_get_user(*args, **kwargs): # real signature unknown
    pass

def qpol_context_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def qpol_default_policy_find(*args, **kwargs): # real signature unknown
    pass

def qpol_fs_use_from_void(*args, **kwargs): # real signature unknown
    pass

def qpol_fs_use_t_get_behavior(*args, **kwargs): # real signature unknown
    pass

def qpol_fs_use_t_get_context(*args, **kwargs): # real signature unknown
    pass

def qpol_fs_use_t_get_name(*args, **kwargs): # real signature unknown
    pass

def qpol_fs_use_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def qpol_genfscon_from_void(*args, **kwargs): # real signature unknown
    pass

def qpol_genfscon_t_get_class(*args, **kwargs): # real signature unknown
    pass

def qpol_genfscon_t_get_context(*args, **kwargs): # real signature unknown
    pass

def qpol_genfscon_t_get_name(*args, **kwargs): # real signature unknown
    pass

def qpol_genfscon_t_get_path(*args, **kwargs): # real signature unknown
    pass

def qpol_genfscon_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def qpol_isid_from_void(*args, **kwargs): # real signature unknown
    pass

def qpol_isid_t_get_context(*args, **kwargs): # real signature unknown
    pass

def qpol_isid_t_get_name(*args, **kwargs): # real signature unknown
    pass

def qpol_isid_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def qpol_iterator_t_end(*args, **kwargs): # real signature unknown
    pass

def qpol_iterator_t_get_item(*args, **kwargs): # real signature unknown
    pass

def qpol_iterator_t_get_size(*args, **kwargs): # real signature unknown
    pass

def qpol_iterator_t_next(*args, **kwargs): # real signature unknown
    pass

def qpol_iterator_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def qpol_level_from_void(*args, **kwargs): # real signature unknown
    pass

def qpol_level_t_get_alias_iter(*args, **kwargs): # real signature unknown
    pass

def qpol_level_t_get_cat_iter(*args, **kwargs): # real signature unknown
    pass

def qpol_level_t_get_isalias(*args, **kwargs): # real signature unknown
    pass

def qpol_level_t_get_name(*args, **kwargs): # real signature unknown
    pass

def qpol_level_t_get_value(*args, **kwargs): # real signature unknown
    pass

def qpol_level_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def qpol_mls_level_from_void(*args, **kwargs): # real signature unknown
    pass

def qpol_mls_level_t_get_cat_iter(*args, **kwargs): # real signature unknown
    pass

def qpol_mls_level_t_get_sens_name(*args, **kwargs): # real signature unknown
    pass

def qpol_mls_level_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def qpol_mls_range_from_void(*args, **kwargs): # real signature unknown
    pass

def qpol_mls_range_t_get_high_level(*args, **kwargs): # real signature unknown
    pass

def qpol_mls_range_t_get_low_level(*args, **kwargs): # real signature unknown
    pass

def qpol_mls_range_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def qpol_module_t_get_enabled(*args, **kwargs): # real signature unknown
    pass

def qpol_module_t_get_name(*args, **kwargs): # real signature unknown
    pass

def qpol_module_t_get_path(*args, **kwargs): # real signature unknown
    pass

def qpol_module_t_get_type(*args, **kwargs): # real signature unknown
    pass

def qpol_module_t_get_version(*args, **kwargs): # real signature unknown
    pass

def qpol_module_t_set_enabled(*args, **kwargs): # real signature unknown
    pass

def qpol_module_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def qpol_netifcon_from_void(*args, **kwargs): # real signature unknown
    pass

def qpol_netifcon_t_get_if_con(*args, **kwargs): # real signature unknown
    pass

def qpol_netifcon_t_get_msg_con(*args, **kwargs): # real signature unknown
    pass

def qpol_netifcon_t_get_name(*args, **kwargs): # real signature unknown
    pass

def qpol_netifcon_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def qpol_nodecon_from_void(*args, **kwargs): # real signature unknown
    pass

def qpol_nodecon_t_get_addr(*args, **kwargs): # real signature unknown
    pass

def qpol_nodecon_t_get_context(*args, **kwargs): # real signature unknown
    pass

def qpol_nodecon_t_get_mask(*args, **kwargs): # real signature unknown
    pass

def qpol_nodecon_t_get_protocol(*args, **kwargs): # real signature unknown
    pass

def qpol_nodecon_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def qpol_policy_t_append_module(*args, **kwargs): # real signature unknown
    pass

def qpol_policy_t_build_syn_rule_table(*args, **kwargs): # real signature unknown
    pass

def qpol_policy_t_get_avrule_iter(*args, **kwargs): # real signature unknown
    pass

def qpol_policy_t_get_bool_iter(*args, **kwargs): # real signature unknown
    pass

def qpol_policy_t_get_cat_iter(*args, **kwargs): # real signature unknown
    pass

def qpol_policy_t_get_class_iter(*args, **kwargs): # real signature unknown
    pass

def qpol_policy_t_get_common_iter(*args, **kwargs): # real signature unknown
    pass

def qpol_policy_t_get_cond_iter(*args, **kwargs): # real signature unknown
    pass

def qpol_policy_t_get_constraint_iter(*args, **kwargs): # real signature unknown
    pass

def qpol_policy_t_get_fs_use_iter(*args, **kwargs): # real signature unknown
    pass

def qpol_policy_t_get_genfscon_iter(*args, **kwargs): # real signature unknown
    pass

def qpol_policy_t_get_isid_iter(*args, **kwargs): # real signature unknown
    pass

def qpol_policy_t_get_level_iter(*args, **kwargs): # real signature unknown
    pass

def qpol_policy_t_get_module_iter(*args, **kwargs): # real signature unknown
    pass

def qpol_policy_t_get_netifcon_iter(*args, **kwargs): # real signature unknown
    pass

def qpol_policy_t_get_nodecon_iter(*args, **kwargs): # real signature unknown
    pass

def qpol_policy_t_get_portcon_iter(*args, **kwargs): # real signature unknown
    pass

def qpol_policy_t_get_range_trans_iter(*args, **kwargs): # real signature unknown
    pass

def qpol_policy_t_get_role_allow_iter(*args, **kwargs): # real signature unknown
    pass

def qpol_policy_t_get_role_iter(*args, **kwargs): # real signature unknown
    pass

def qpol_policy_t_get_role_trans_iter(*args, **kwargs): # real signature unknown
    pass

def qpol_policy_t_get_terule_iter(*args, **kwargs): # real signature unknown
    pass

def qpol_policy_t_get_type(*args, **kwargs): # real signature unknown
    pass

def qpol_policy_t_get_type_iter(*args, **kwargs): # real signature unknown
    pass

def qpol_policy_t_get_user_iter(*args, **kwargs): # real signature unknown
    pass

def qpol_policy_t_get_validatetrans_iter(*args, **kwargs): # real signature unknown
    pass

def qpol_policy_t_get_version(*args, **kwargs): # real signature unknown
    pass

def qpol_policy_t_has_capability(*args, **kwargs): # real signature unknown
    pass

def qpol_policy_t_rebuild(*args, **kwargs): # real signature unknown
    pass

def qpol_policy_t_reevaluate_conds(*args, **kwargs): # real signature unknown
    pass

def qpol_policy_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def qpol_portcon_from_void(*args, **kwargs): # real signature unknown
    pass

def qpol_portcon_t_get_context(*args, **kwargs): # real signature unknown
    pass

def qpol_portcon_t_get_high_port(*args, **kwargs): # real signature unknown
    pass

def qpol_portcon_t_get_low_port(*args, **kwargs): # real signature unknown
    pass

def qpol_portcon_t_get_protocol(*args, **kwargs): # real signature unknown
    pass

def qpol_portcon_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def qpol_range_trans_from_void(*args, **kwargs): # real signature unknown
    pass

def qpol_range_trans_t_get_range(*args, **kwargs): # real signature unknown
    pass

def qpol_range_trans_t_get_source_type(*args, **kwargs): # real signature unknown
    pass

def qpol_range_trans_t_get_target_class(*args, **kwargs): # real signature unknown
    pass

def qpol_range_trans_t_get_target_type(*args, **kwargs): # real signature unknown
    pass

def qpol_range_trans_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def qpol_role_allow_from_void(*args, **kwargs): # real signature unknown
    pass

def qpol_role_allow_t_get_source_role(*args, **kwargs): # real signature unknown
    pass

def qpol_role_allow_t_get_target_role(*args, **kwargs): # real signature unknown
    pass

def qpol_role_allow_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def qpol_role_from_void(*args, **kwargs): # real signature unknown
    pass

def qpol_role_trans_from_void(*args, **kwargs): # real signature unknown
    pass

def qpol_role_trans_t_get_default_role(*args, **kwargs): # real signature unknown
    pass

def qpol_role_trans_t_get_source_role(*args, **kwargs): # real signature unknown
    pass

def qpol_role_trans_t_get_target_type(*args, **kwargs): # real signature unknown
    pass

def qpol_role_trans_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def qpol_role_t_get_dominate_iter(*args, **kwargs): # real signature unknown
    pass

def qpol_role_t_get_name(*args, **kwargs): # real signature unknown
    pass

def qpol_role_t_get_type_iter(*args, **kwargs): # real signature unknown
    pass

def qpol_role_t_get_value(*args, **kwargs): # real signature unknown
    pass

def qpol_role_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def qpol_syn_avrule_from_void(*args, **kwargs): # real signature unknown
    pass

def qpol_syn_avrule_t_get_class_iter(*args, **kwargs): # real signature unknown
    pass

def qpol_syn_avrule_t_get_cond(*args, **kwargs): # real signature unknown
    pass

def qpol_syn_avrule_t_get_is_enabled(*args, **kwargs): # real signature unknown
    pass

def qpol_syn_avrule_t_get_is_target_self(*args, **kwargs): # real signature unknown
    pass

def qpol_syn_avrule_t_get_lineno(*args, **kwargs): # real signature unknown
    pass

def qpol_syn_avrule_t_get_perm_iter(*args, **kwargs): # real signature unknown
    pass

def qpol_syn_avrule_t_get_rule_type(*args, **kwargs): # real signature unknown
    pass

def qpol_syn_avrule_t_get_source_type_set(*args, **kwargs): # real signature unknown
    pass

def qpol_syn_avrule_t_get_target_type_set(*args, **kwargs): # real signature unknown
    pass

def qpol_syn_avrule_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def qpol_syn_terule_from_void(*args, **kwargs): # real signature unknown
    pass

def qpol_syn_terule_t_get_class_iter(*args, **kwargs): # real signature unknown
    pass

def qpol_syn_terule_t_get_cond(*args, **kwargs): # real signature unknown
    pass

def qpol_syn_terule_t_get_default_type(*args, **kwargs): # real signature unknown
    pass

def qpol_syn_terule_t_get_is_enabled(*args, **kwargs): # real signature unknown
    pass

def qpol_syn_terule_t_get_lineno(*args, **kwargs): # real signature unknown
    pass

def qpol_syn_terule_t_get_rule_type(*args, **kwargs): # real signature unknown
    pass

def qpol_syn_terule_t_get_source_type_set(*args, **kwargs): # real signature unknown
    pass

def qpol_syn_terule_t_get_target_type_set(*args, **kwargs): # real signature unknown
    pass

def qpol_syn_terule_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def qpol_terule_from_void(*args, **kwargs): # real signature unknown
    pass

def qpol_terule_t_get_cond(*args, **kwargs): # real signature unknown
    pass

def qpol_terule_t_get_default_type(*args, **kwargs): # real signature unknown
    pass

def qpol_terule_t_get_is_enabled(*args, **kwargs): # real signature unknown
    pass

def qpol_terule_t_get_object_class(*args, **kwargs): # real signature unknown
    pass

def qpol_terule_t_get_rule_type(*args, **kwargs): # real signature unknown
    pass

def qpol_terule_t_get_source_type(*args, **kwargs): # real signature unknown
    pass

def qpol_terule_t_get_syn_terule_iter(*args, **kwargs): # real signature unknown
    pass

def qpol_terule_t_get_target_type(*args, **kwargs): # real signature unknown
    pass

def qpol_terule_t_get_which_list(*args, **kwargs): # real signature unknown
    pass

def qpol_terule_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def qpol_type_from_void(*args, **kwargs): # real signature unknown
    pass

def qpol_type_set_from_void(*args, **kwargs): # real signature unknown
    pass

def qpol_type_set_t_get_included_types_iter(*args, **kwargs): # real signature unknown
    pass

def qpol_type_set_t_get_is_comp(*args, **kwargs): # real signature unknown
    pass

def qpol_type_set_t_get_is_star(*args, **kwargs): # real signature unknown
    pass

def qpol_type_set_t_get_subtracted_types_iter(*args, **kwargs): # real signature unknown
    pass

def qpol_type_set_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def qpol_type_t_get_alias_iter(*args, **kwargs): # real signature unknown
    pass

def qpol_type_t_get_attr_iter(*args, **kwargs): # real signature unknown
    pass

def qpol_type_t_get_isalias(*args, **kwargs): # real signature unknown
    pass

def qpol_type_t_get_isattr(*args, **kwargs): # real signature unknown
    pass

def qpol_type_t_get_ispermissive(*args, **kwargs): # real signature unknown
    pass

def qpol_type_t_get_name(*args, **kwargs): # real signature unknown
    pass

def qpol_type_t_get_type_iter(*args, **kwargs): # real signature unknown
    pass

def qpol_type_t_get_value(*args, **kwargs): # real signature unknown
    pass

def qpol_type_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def qpol_user_from_void(*args, **kwargs): # real signature unknown
    pass

def qpol_user_t_get_dfltlevel(*args, **kwargs): # real signature unknown
    pass

def qpol_user_t_get_name(*args, **kwargs): # real signature unknown
    pass

def qpol_user_t_get_range(*args, **kwargs): # real signature unknown
    pass

def qpol_user_t_get_role_iter(*args, **kwargs): # real signature unknown
    pass

def qpol_user_t_get_value(*args, **kwargs): # real signature unknown
    pass

def qpol_user_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def qpol_validatetrans_from_void(*args, **kwargs): # real signature unknown
    pass

def qpol_validatetrans_t_get_class(*args, **kwargs): # real signature unknown
    pass

def qpol_validatetrans_t_get_expr_iter(*args, **kwargs): # real signature unknown
    pass

def qpol_validatetrans_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def SWIG_PyInstanceMethod_New(*args, **kwargs): # real signature unknown
    pass

def to_str(*args, **kwargs): # real signature unknown
    pass

# no classes
