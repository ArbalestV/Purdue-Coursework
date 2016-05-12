# encoding: utf-8
# module setools._apol
# from /usr/lib64/python2.6/site-packages/setools/_apol.so
# by generator 1.136
# no doc
# no imports

# Variables with simple values

APOL_DOMAIN_TRANS_DIRECTION_FORWARD = 1
APOL_DOMAIN_TRANS_DIRECTION_REVERSE = 2

APOL_DOMAIN_TRANS_RULE_ENTRYPOINT = 8
APOL_DOMAIN_TRANS_RULE_EXEC = 2

APOL_DOMAIN_TRANS_RULE_EXEC_NO_TRANS = 4

APOL_DOMAIN_TRANS_RULE_PROC_TRANS = 1

APOL_DOMAIN_TRANS_RULE_SETEXEC = 32

APOL_DOMAIN_TRANS_RULE_TYPE_TRANS = 16

APOL_DOMAIN_TRANS_SEARCH_BOTH = 3
APOL_DOMAIN_TRANS_SEARCH_INVALID = 2
APOL_DOMAIN_TRANS_SEARCH_VALID = 1

APOL_INFOFLOW_BOTH = 3
APOL_INFOFLOW_EITHER = 4
APOL_INFOFLOW_IN = 1

APOL_INFOFLOW_MODE_DIRECT = 1
APOL_INFOFLOW_MODE_TRANS = 2

APOL_INFOFLOW_OUT = 2

APOL_MLS_DOM = 1
APOL_MLS_DOMBY = 2
APOL_MLS_EQ = 0
APOL_MLS_INCOMP = 3

APOL_PERMMAP_BOTH = 3

APOL_PERMMAP_MAX_WEIGHT = 10

APOL_PERMMAP_MIN_WEIGHT = 1

APOL_PERMMAP_NONE = 16
APOL_PERMMAP_READ = 1
APOL_PERMMAP_UNMAPPED = 0
APOL_PERMMAP_WRITE = 2

APOL_POLICY_PATH_TYPE_MODULAR = 1
APOL_POLICY_PATH_TYPE_MONOLITHIC = 0

APOL_QUERY_EXACT = 6
APOL_QUERY_FLAGS = 14
APOL_QUERY_INTERSECT = 8
APOL_QUERY_SUB = 2
APOL_QUERY_SUPER = 4

APOL_QUERY_SYMBOL_IS_ATTRIBUTE = 2
APOL_QUERY_SYMBOL_IS_TYPE = 1

APOL_RELABEL_DIR_BOTH = 3
APOL_RELABEL_DIR_FROM = 2
APOL_RELABEL_DIR_SUBJECT = 4
APOL_RELABEL_DIR_TO = 1

APOL_TYPES_RELATION_ALLOW_RULES = 256

APOL_TYPES_RELATION_COMMON_ATTRIBS = 1
APOL_TYPES_RELATION_COMMON_ROLES = 2
APOL_TYPES_RELATION_COMMON_USERS = 4

APOL_TYPES_RELATION_DIRECT_FLOW = 4096

APOL_TYPES_RELATION_DISSIMILAR_ACCESS = 32

APOL_TYPES_RELATION_DOMAIN_TRANS_AB = 1024
APOL_TYPES_RELATION_DOMAIN_TRANS_BA = 2048

APOL_TYPES_RELATION_SIMILAR_ACCESS = 16

APOL_TYPES_RELATION_TRANS_FLOW_AB = 16384
APOL_TYPES_RELATION_TRANS_FLOW_BA = 32768

APOL_TYPES_RELATION_TYPE_RULES = 512

# functions

def apol_attr_query_t_run(*args, **kwargs): # real signature unknown
    pass

def apol_attr_query_t_set_attr(*args, **kwargs): # real signature unknown
    pass

def apol_attr_query_t_set_regex(*args, **kwargs): # real signature unknown
    pass

def apol_attr_query_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def apol_avrule_list_to_syn_avrules(*args, **kwargs): # real signature unknown
    pass

def apol_avrule_query_t_append_class(*args, **kwargs): # real signature unknown
    pass

def apol_avrule_query_t_append_perm(*args, **kwargs): # real signature unknown
    pass

def apol_avrule_query_t_run(*args, **kwargs): # real signature unknown
    pass

def apol_avrule_query_t_run_syn(*args, **kwargs): # real signature unknown
    pass

def apol_avrule_query_t_set_all_perms(*args, **kwargs): # real signature unknown
    pass

def apol_avrule_query_t_set_bool(*args, **kwargs): # real signature unknown
    pass

def apol_avrule_query_t_set_enabled(*args, **kwargs): # real signature unknown
    pass

def apol_avrule_query_t_set_regex(*args, **kwargs): # real signature unknown
    pass

def apol_avrule_query_t_set_rules(*args, **kwargs): # real signature unknown
    pass

def apol_avrule_query_t_set_source(*args, **kwargs): # real signature unknown
    pass

def apol_avrule_query_t_set_source_any(*args, **kwargs): # real signature unknown
    pass

def apol_avrule_query_t_set_source_component(*args, **kwargs): # real signature unknown
    pass

def apol_avrule_query_t_set_target(*args, **kwargs): # real signature unknown
    pass

def apol_avrule_query_t_set_target_component(*args, **kwargs): # real signature unknown
    pass

def apol_avrule_query_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def apol_avrule_render(*args, **kwargs): # real signature unknown
    pass

def apol_avrule_to_syn_avrules(*args, **kwargs): # real signature unknown
    pass

def apol_bool_query_t_run(*args, **kwargs): # real signature unknown
    pass

def apol_bool_query_t_set_bool(*args, **kwargs): # real signature unknown
    pass

def apol_bool_query_t_set_regex(*args, **kwargs): # real signature unknown
    pass

def apol_bool_query_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def apol_cat_query_t_run(*args, **kwargs): # real signature unknown
    pass

def apol_cat_query_t_set_cat(*args, **kwargs): # real signature unknown
    pass

def apol_cat_query_t_set_regex(*args, **kwargs): # real signature unknown
    pass

def apol_cat_query_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def apol_class_query_t_run(*args, **kwargs): # real signature unknown
    pass

def apol_class_query_t_set_class(*args, **kwargs): # real signature unknown
    pass

def apol_class_query_t_set_common(*args, **kwargs): # real signature unknown
    pass

def apol_class_query_t_set_regex(*args, **kwargs): # real signature unknown
    pass

def apol_class_query_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def apol_common_query_t_run(*args, **kwargs): # real signature unknown
    pass

def apol_common_query_t_set_common(*args, **kwargs): # real signature unknown
    pass

def apol_common_query_t_set_regex(*args, **kwargs): # real signature unknown
    pass

def apol_common_query_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def apol_cond_expr_render(*args, **kwargs): # real signature unknown
    pass

def apol_cond_expr_type_to_str(*args, **kwargs): # real signature unknown
    pass

def apol_cond_query_t_run(*args, **kwargs): # real signature unknown
    pass

def apol_cond_query_t_set_bool(*args, **kwargs): # real signature unknown
    pass

def apol_cond_query_t_set_regex(*args, **kwargs): # real signature unknown
    pass

def apol_cond_query_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def apol_constraint_query_t_run(*args, **kwargs): # real signature unknown
    pass

def apol_constraint_query_t_set_class(*args, **kwargs): # real signature unknown
    pass

def apol_constraint_query_t_set_perm(*args, **kwargs): # real signature unknown
    pass

def apol_constraint_query_t_set_regex(*args, **kwargs): # real signature unknown
    pass

def apol_constraint_query_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def apol_context_compare(*args, **kwargs): # real signature unknown
    pass

def apol_context_t_convert(*args, **kwargs): # real signature unknown
    pass

def apol_context_t_get_range(*args, **kwargs): # real signature unknown
    pass

def apol_context_t_get_role(*args, **kwargs): # real signature unknown
    pass

def apol_context_t_get_type(*args, **kwargs): # real signature unknown
    pass

def apol_context_t_get_user(*args, **kwargs): # real signature unknown
    pass

def apol_context_t_render(*args, **kwargs): # real signature unknown
    pass

def apol_context_t_set_range(*args, **kwargs): # real signature unknown
    pass

def apol_context_t_set_role(*args, **kwargs): # real signature unknown
    pass

def apol_context_t_set_type(*args, **kwargs): # real signature unknown
    pass

def apol_context_t_set_user(*args, **kwargs): # real signature unknown
    pass

def apol_context_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def apol_context_t_validate(*args, **kwargs): # real signature unknown
    pass

def apol_context_t_validate_partial(*args, **kwargs): # real signature unknown
    pass

def apol_domain_trans_analysis_t_append_access_type(*args, **kwargs): # real signature unknown
    pass

def apol_domain_trans_analysis_t_append_class(*args, **kwargs): # real signature unknown
    pass

def apol_domain_trans_analysis_t_append_perm(*args, **kwargs): # real signature unknown
    pass

def apol_domain_trans_analysis_t_run(*args, **kwargs): # real signature unknown
    pass

def apol_domain_trans_analysis_t_set_direction(*args, **kwargs): # real signature unknown
    pass

def apol_domain_trans_analysis_t_set_result_regex(*args, **kwargs): # real signature unknown
    pass

def apol_domain_trans_analysis_t_set_start_type(*args, **kwargs): # real signature unknown
    pass

def apol_domain_trans_analysis_t_set_valid(*args, **kwargs): # real signature unknown
    pass

def apol_domain_trans_analysis_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def apol_domain_trans_result_from_void(*args, **kwargs): # real signature unknown
    pass

def apol_domain_trans_result_t_get_access_rules(*args, **kwargs): # real signature unknown
    pass

def apol_domain_trans_result_t_get_end_type(*args, **kwargs): # real signature unknown
    pass

def apol_domain_trans_result_t_get_entrypoint_rules(*args, **kwargs): # real signature unknown
    pass

def apol_domain_trans_result_t_get_entrypoint_type(*args, **kwargs): # real signature unknown
    pass

def apol_domain_trans_result_t_get_exec_rules(*args, **kwargs): # real signature unknown
    pass

def apol_domain_trans_result_t_get_is_valid(*args, **kwargs): # real signature unknown
    pass

def apol_domain_trans_result_t_get_proc_trans_rules(*args, **kwargs): # real signature unknown
    pass

def apol_domain_trans_result_t_get_setexec_rules(*args, **kwargs): # real signature unknown
    pass

def apol_domain_trans_result_t_get_start_type(*args, **kwargs): # real signature unknown
    pass

def apol_domain_trans_result_t_get_type_trans_rules(*args, **kwargs): # real signature unknown
    pass

def apol_domain_trans_result_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def apol_domain_trans_table_verify_trans(*args, **kwargs): # real signature unknown
    pass

def apol_file_find_path(*args, **kwargs): # real signature unknown
    pass

def apol_file_is_policy_path_list(*args, **kwargs): # real signature unknown
    pass

def apol_fs_use_behavior_to_str(*args, **kwargs): # real signature unknown
    pass

def apol_fs_use_query_t_run(*args, **kwargs): # real signature unknown
    pass

def apol_fs_use_query_t_set_behavior(*args, **kwargs): # real signature unknown
    pass

def apol_fs_use_query_t_set_context(*args, **kwargs): # real signature unknown
    pass

def apol_fs_use_query_t_set_filesystem(*args, **kwargs): # real signature unknown
    pass

def apol_fs_use_query_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def apol_fs_use_render(*args, **kwargs): # real signature unknown
    pass

def apol_genfscon_query_t_run(*args, **kwargs): # real signature unknown
    pass

def apol_genfscon_query_t_set_context(*args, **kwargs): # real signature unknown
    pass

def apol_genfscon_query_t_set_filesystem(*args, **kwargs): # real signature unknown
    pass

def apol_genfscon_query_t_set_objclass(*args, **kwargs): # real signature unknown
    pass

def apol_genfscon_query_t_set_path(*args, **kwargs): # real signature unknown
    pass

def apol_genfscon_query_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def apol_genfscon_render(*args, **kwargs): # real signature unknown
    pass

def apol_infoflow_analysis_t_append_class_perm(*args, **kwargs): # real signature unknown
    pass

def apol_infoflow_analysis_t_append_intermediate(*args, **kwargs): # real signature unknown
    pass

def apol_infoflow_analysis_t_run(*args, **kwargs): # real signature unknown
    pass

def apol_infoflow_analysis_t_set_dir(*args, **kwargs): # real signature unknown
    pass

def apol_infoflow_analysis_t_set_min_weight(*args, **kwargs): # real signature unknown
    pass

def apol_infoflow_analysis_t_set_mode(*args, **kwargs): # real signature unknown
    pass

def apol_infoflow_analysis_t_set_result_regex(*args, **kwargs): # real signature unknown
    pass

def apol_infoflow_analysis_t_set_type(*args, **kwargs): # real signature unknown
    pass

def apol_infoflow_analysis_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def apol_infoflow_graph_t_do_more(*args, **kwargs): # real signature unknown
    pass

def apol_infoflow_graph_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def apol_infoflow_graph_t_trans_further_next(*args, **kwargs): # real signature unknown
    pass

def apol_infoflow_graph_t_trans_further_prepare(*args, **kwargs): # real signature unknown
    pass

def apol_infoflow_result_from_void(*args, **kwargs): # real signature unknown
    pass

def apol_infoflow_result_t_get_dir(*args, **kwargs): # real signature unknown
    pass

def apol_infoflow_result_t_get_end_type(*args, **kwargs): # real signature unknown
    pass

def apol_infoflow_result_t_get_length(*args, **kwargs): # real signature unknown
    pass

def apol_infoflow_result_t_get_start_type(*args, **kwargs): # real signature unknown
    pass

def apol_infoflow_result_t_get_steps(*args, **kwargs): # real signature unknown
    pass

def apol_infoflow_result_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def apol_infoflow_step_from_void(*args, **kwargs): # real signature unknown
    pass

def apol_infoflow_step_t_get_end_type(*args, **kwargs): # real signature unknown
    pass

def apol_infoflow_step_t_get_rules(*args, **kwargs): # real signature unknown
    pass

def apol_infoflow_step_t_get_start_type(*args, **kwargs): # real signature unknown
    pass

def apol_infoflow_step_t_get_weight(*args, **kwargs): # real signature unknown
    pass

def apol_infoflow_step_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def apol_infoflow_t_extract_graph(*args, **kwargs): # real signature unknown
    pass

def apol_infoflow_t_extract_result_vector(*args, **kwargs): # real signature unknown
    pass

def apol_infoflow_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def apol_ipv4_addr_render(*args, **kwargs): # real signature unknown
    pass

def apol_ipv6_addr_render(*args, **kwargs): # real signature unknown
    pass

def apol_ip_t_get_protocol(*args, **kwargs): # real signature unknown
    pass

def apol_ip_t_ip_get(*args, **kwargs): # real signature unknown
    pass

def apol_ip_t_ip_set(*args, **kwargs): # real signature unknown
    pass

def apol_ip_t_proto_get(*args, **kwargs): # real signature unknown
    pass

def apol_ip_t_proto_set(*args, **kwargs): # real signature unknown
    pass

def apol_ip_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def apol_isid_query_t_run(*args, **kwargs): # real signature unknown
    pass

def apol_isid_query_t_set_context(*args, **kwargs): # real signature unknown
    pass

def apol_isid_query_t_set_name(*args, **kwargs): # real signature unknown
    pass

def apol_isid_query_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def apol_level_query_t_run(*args, **kwargs): # real signature unknown
    pass

def apol_level_query_t_set_cat(*args, **kwargs): # real signature unknown
    pass

def apol_level_query_t_set_regex(*args, **kwargs): # real signature unknown
    pass

def apol_level_query_t_set_sens(*args, **kwargs): # real signature unknown
    pass

def apol_level_query_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def apol_mls_cats_compare(*args, **kwargs): # real signature unknown
    pass

def apol_mls_level_compare(*args, **kwargs): # real signature unknown
    pass

def apol_mls_level_from_void(*args, **kwargs): # real signature unknown
    pass

def apol_mls_level_t_append_cats(*args, **kwargs): # real signature unknown
    pass

def apol_mls_level_t_convert(*args, **kwargs): # real signature unknown
    pass

def apol_mls_level_t_get_cats(*args, **kwargs): # real signature unknown
    pass

def apol_mls_level_t_get_sens(*args, **kwargs): # real signature unknown
    pass

def apol_mls_level_t_is_literal(*args, **kwargs): # real signature unknown
    pass

def apol_mls_level_t_render(*args, **kwargs): # real signature unknown
    pass

def apol_mls_level_t_set_sens(*args, **kwargs): # real signature unknown
    pass

def apol_mls_level_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def apol_mls_level_t_validate(*args, **kwargs): # real signature unknown
    pass

def apol_mls_range_compare(*args, **kwargs): # real signature unknown
    pass

def apol_mls_range_contain_subrange(*args, **kwargs): # real signature unknown
    pass

def apol_mls_range_from_void(*args, **kwargs): # real signature unknown
    pass

def apol_mls_range_t_convert(*args, **kwargs): # real signature unknown
    pass

def apol_mls_range_t_get_high(*args, **kwargs): # real signature unknown
    pass

def apol_mls_range_t_get_levels(*args, **kwargs): # real signature unknown
    pass

def apol_mls_range_t_get_low(*args, **kwargs): # real signature unknown
    pass

def apol_mls_range_t_is_literal(*args, **kwargs): # real signature unknown
    pass

def apol_mls_range_t_render(*args, **kwargs): # real signature unknown
    pass

def apol_mls_range_t_set_high(*args, **kwargs): # real signature unknown
    pass

def apol_mls_range_t_set_low(*args, **kwargs): # real signature unknown
    pass

def apol_mls_range_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def apol_mls_range_t_validate(*args, **kwargs): # real signature unknown
    pass

def apol_mls_sens_compare(*args, **kwargs): # real signature unknown
    pass

def apol_netifcon_query_t_run(*args, **kwargs): # real signature unknown
    pass

def apol_netifcon_query_t_set_device(*args, **kwargs): # real signature unknown
    pass

def apol_netifcon_query_t_set_if_context(*args, **kwargs): # real signature unknown
    pass

def apol_netifcon_query_t_set_msg_context(*args, **kwargs): # real signature unknown
    pass

def apol_netifcon_query_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def apol_netifcon_render(*args, **kwargs): # real signature unknown
    pass

def apol_nodecon_query_t_run(*args, **kwargs): # real signature unknown
    pass

def apol_nodecon_query_t_set_addr(*args, **kwargs): # real signature unknown
    pass

def apol_nodecon_query_t_set_context(*args, **kwargs): # real signature unknown
    pass

def apol_nodecon_query_t_set_mask(*args, **kwargs): # real signature unknown
    pass

def apol_nodecon_query_t_set_protocol(*args, **kwargs): # real signature unknown
    pass

def apol_nodecon_query_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def apol_nodecon_render(*args, **kwargs): # real signature unknown
    pass

def apol_objclass_to_str(*args, **kwargs): # real signature unknown
    pass

def apol_perm_query_t_run(*args, **kwargs): # real signature unknown
    pass

def apol_perm_query_t_set_perm(*args, **kwargs): # real signature unknown
    pass

def apol_perm_query_t_set_regex(*args, **kwargs): # real signature unknown
    pass

def apol_perm_query_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def apol_policy_path_compare(*args, **kwargs): # real signature unknown
    pass

def apol_policy_path_t_get_modules(*args, **kwargs): # real signature unknown
    pass

def apol_policy_path_t_get_primary(*args, **kwargs): # real signature unknown
    pass

def apol_policy_path_t_get_type(*args, **kwargs): # real signature unknown
    pass

def apol_policy_path_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def apol_policy_path_t_to_file(*args, **kwargs): # real signature unknown
    pass

def apol_policy_path_t_to_string(*args, **kwargs): # real signature unknown
    pass

def apol_policy_t_build_domain_trans_table(*args, **kwargs): # real signature unknown
    pass

def apol_policy_t_get_permmap_direction(*args, **kwargs): # real signature unknown
    pass

def apol_policy_t_get_permmap_weight(*args, **kwargs): # real signature unknown
    pass

def apol_policy_t_get_policy_type(*args, **kwargs): # real signature unknown
    pass

def apol_policy_t_get_qpol(*args, **kwargs): # real signature unknown
    pass

def apol_policy_t_get_version_type_mls_str(*args, **kwargs): # real signature unknown
    pass

def apol_policy_t_is_mls(*args, **kwargs): # real signature unknown
    pass

def apol_policy_t_open_permmap(*args, **kwargs): # real signature unknown
    pass

def apol_policy_t_reset_domain_trans_table(*args, **kwargs): # real signature unknown
    pass

def apol_policy_t_save_permmap(*args, **kwargs): # real signature unknown
    pass

def apol_policy_t_set_permmap(*args, **kwargs): # real signature unknown
    pass

def apol_policy_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def apol_portcon_query_t_run(*args, **kwargs): # real signature unknown
    pass

def apol_portcon_query_t_set_context(*args, **kwargs): # real signature unknown
    pass

def apol_portcon_query_t_set_high(*args, **kwargs): # real signature unknown
    pass

def apol_portcon_query_t_set_low(*args, **kwargs): # real signature unknown
    pass

def apol_portcon_query_t_set_protocol(*args, **kwargs): # real signature unknown
    pass

def apol_portcon_query_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def apol_portcon_render(*args, **kwargs): # real signature unknown
    pass

def apol_protocol_to_str(*args, **kwargs): # real signature unknown
    pass

def apol_qpol_context_render(*args, **kwargs): # real signature unknown
    pass

def apol_range_trans_query_t_append_class(*args, **kwargs): # real signature unknown
    pass

def apol_range_trans_query_t_run(*args, **kwargs): # real signature unknown
    pass

def apol_range_trans_query_t_set_range(*args, **kwargs): # real signature unknown
    pass

def apol_range_trans_query_t_set_regex(*args, **kwargs): # real signature unknown
    pass

def apol_range_trans_query_t_set_source(*args, **kwargs): # real signature unknown
    pass

def apol_range_trans_query_t_set_source_any(*args, **kwargs): # real signature unknown
    pass

def apol_range_trans_query_t_set_target(*args, **kwargs): # real signature unknown
    pass

def apol_range_trans_query_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def apol_range_trans_render(*args, **kwargs): # real signature unknown
    pass

def apol_relabel_analysis_t_append_class(*args, **kwargs): # real signature unknown
    pass

def apol_relabel_analysis_t_append_subject(*args, **kwargs): # real signature unknown
    pass

def apol_relabel_analysis_t_run(*args, **kwargs): # real signature unknown
    pass

def apol_relabel_analysis_t_set_dir(*args, **kwargs): # real signature unknown
    pass

def apol_relabel_analysis_t_set_result_regex(*args, **kwargs): # real signature unknown
    pass

def apol_relabel_analysis_t_set_type(*args, **kwargs): # real signature unknown
    pass

def apol_relabel_analysis_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def apol_relabel_result_from_void(*args, **kwargs): # real signature unknown
    pass

def apol_relabel_result_pair_from_void(*args, **kwargs): # real signature unknown
    pass

def apol_relabel_result_pair_t_get_intermediate_type(*args, **kwargs): # real signature unknown
    pass

def apol_relabel_result_pair_t_get_ruleA(*args, **kwargs): # real signature unknown
    pass

def apol_relabel_result_pair_t_get_ruleB(*args, **kwargs): # real signature unknown
    pass

def apol_relabel_result_pair_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def apol_relabel_result_t_get_both(*args, **kwargs): # real signature unknown
    pass

def apol_relabel_result_t_get_from(*args, **kwargs): # real signature unknown
    pass

def apol_relabel_result_t_get_result_type(*args, **kwargs): # real signature unknown
    pass

def apol_relabel_result_t_get_to(*args, **kwargs): # real signature unknown
    pass

def apol_relabel_result_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def apol_role_allow_query_t_run(*args, **kwargs): # real signature unknown
    pass

def apol_role_allow_query_t_set_regex(*args, **kwargs): # real signature unknown
    pass

def apol_role_allow_query_t_set_source(*args, **kwargs): # real signature unknown
    pass

def apol_role_allow_query_t_set_source_any(*args, **kwargs): # real signature unknown
    pass

def apol_role_allow_query_t_set_target(*args, **kwargs): # real signature unknown
    pass

def apol_role_allow_query_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def apol_role_allow_render(*args, **kwargs): # real signature unknown
    pass

def apol_role_has_type(*args, **kwargs): # real signature unknown
    pass

def apol_role_query_t_run(*args, **kwargs): # real signature unknown
    pass

def apol_role_query_t_set_regex(*args, **kwargs): # real signature unknown
    pass

def apol_role_query_t_set_role(*args, **kwargs): # real signature unknown
    pass

def apol_role_query_t_set_type(*args, **kwargs): # real signature unknown
    pass

def apol_role_query_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def apol_role_trans_query_t_run(*args, **kwargs): # real signature unknown
    pass

def apol_role_trans_query_t_set_default(*args, **kwargs): # real signature unknown
    pass

def apol_role_trans_query_t_set_regex(*args, **kwargs): # real signature unknown
    pass

def apol_role_trans_query_t_set_source(*args, **kwargs): # real signature unknown
    pass

def apol_role_trans_query_t_set_source_any(*args, **kwargs): # real signature unknown
    pass

def apol_role_trans_query_t_set_target(*args, **kwargs): # real signature unknown
    pass

def apol_role_trans_query_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def apol_role_trans_render(*args, **kwargs): # real signature unknown
    pass

def apol_rule_type_to_str(*args, **kwargs): # real signature unknown
    pass

def apol_string_vector_t_append(*args, **kwargs): # real signature unknown
    pass

def apol_string_vector_t_append_unique(*args, **kwargs): # real signature unknown
    pass

def apol_string_vector_t_cat(*args, **kwargs): # real signature unknown
    pass

def apol_string_vector_t_get_capacity(*args, **kwargs): # real signature unknown
    pass

def apol_string_vector_t_get_element(*args, **kwargs): # real signature unknown
    pass

def apol_string_vector_t_get_index(*args, **kwargs): # real signature unknown
    pass

def apol_string_vector_t_get_size(*args, **kwargs): # real signature unknown
    pass

def apol_string_vector_t_remove(*args, **kwargs): # real signature unknown
    pass

def apol_string_vector_t_sort(*args, **kwargs): # real signature unknown
    pass

def apol_string_vector_t_sort_uniquify(*args, **kwargs): # real signature unknown
    pass

def apol_string_vector_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def apol_str_to_fs_use_behavior(*args, **kwargs): # real signature unknown
    pass

def apol_str_to_internal_ip(*args, **kwargs): # real signature unknown
    pass

def apol_str_to_objclass(*args, **kwargs): # real signature unknown
    pass

def apol_str_to_protocol(*args, **kwargs): # real signature unknown
    pass

def apol_syn_avrule_render(*args, **kwargs): # real signature unknown
    pass

def apol_syn_terule_render(*args, **kwargs): # real signature unknown
    pass

def apol_terule_list_to_syn_terules(*args, **kwargs): # real signature unknown
    pass

def apol_terule_query_t_append_class(*args, **kwargs): # real signature unknown
    pass

def apol_terule_query_t_run(*args, **kwargs): # real signature unknown
    pass

def apol_terule_query_t_run_syn(*args, **kwargs): # real signature unknown
    pass

def apol_terule_query_t_set_bool(*args, **kwargs): # real signature unknown
    pass

def apol_terule_query_t_set_default(*args, **kwargs): # real signature unknown
    pass

def apol_terule_query_t_set_enabled(*args, **kwargs): # real signature unknown
    pass

def apol_terule_query_t_set_regex(*args, **kwargs): # real signature unknown
    pass

def apol_terule_query_t_set_rules(*args, **kwargs): # real signature unknown
    pass

def apol_terule_query_t_set_source(*args, **kwargs): # real signature unknown
    pass

def apol_terule_query_t_set_source_any(*args, **kwargs): # real signature unknown
    pass

def apol_terule_query_t_set_source_component(*args, **kwargs): # real signature unknown
    pass

def apol_terule_query_t_set_target(*args, **kwargs): # real signature unknown
    pass

def apol_terule_query_t_set_target_component(*args, **kwargs): # real signature unknown
    pass

def apol_terule_query_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def apol_terule_render(*args, **kwargs): # real signature unknown
    pass

def apol_terule_to_syn_terules(*args, **kwargs): # real signature unknown
    pass

def apol_types_relation_access_from_void(*args, **kwargs): # real signature unknown
    pass

def apol_types_relation_access_t_get_rules(*args, **kwargs): # real signature unknown
    pass

def apol_types_relation_access_t_get_type(*args, **kwargs): # real signature unknown
    pass

def apol_types_relation_access_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def apol_types_relation_analysis_t_run(*args, **kwargs): # real signature unknown
    pass

def apol_types_relation_analysis_t_set_analyses(*args, **kwargs): # real signature unknown
    pass

def apol_types_relation_analysis_t_set_first_type(*args, **kwargs): # real signature unknown
    pass

def apol_types_relation_analysis_t_set_other_type(*args, **kwargs): # real signature unknown
    pass

def apol_types_relation_analysis_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def apol_types_relation_result_t_get_allowrules(*args, **kwargs): # real signature unknown
    pass

def apol_types_relation_result_t_get_attributes(*args, **kwargs): # real signature unknown
    pass

def apol_types_relation_result_t_get_directflows(*args, **kwargs): # real signature unknown
    pass

def apol_types_relation_result_t_get_dissimilar_first(*args, **kwargs): # real signature unknown
    pass

def apol_types_relation_result_t_get_dissimilar_other(*args, **kwargs): # real signature unknown
    pass

def apol_types_relation_result_t_get_domainsAB(*args, **kwargs): # real signature unknown
    pass

def apol_types_relation_result_t_get_domainsBA(*args, **kwargs): # real signature unknown
    pass

def apol_types_relation_result_t_get_roles(*args, **kwargs): # real signature unknown
    pass

def apol_types_relation_result_t_get_similar_first(*args, **kwargs): # real signature unknown
    pass

def apol_types_relation_result_t_get_similar_other(*args, **kwargs): # real signature unknown
    pass

def apol_types_relation_result_t_get_transflowsAB(*args, **kwargs): # real signature unknown
    pass

def apol_types_relation_result_t_get_transflowsBA(*args, **kwargs): # real signature unknown
    pass

def apol_types_relation_result_t_get_typerules(*args, **kwargs): # real signature unknown
    pass

def apol_types_relation_result_t_get_users(*args, **kwargs): # real signature unknown
    pass

def apol_types_relation_result_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def apol_type_query_t_run(*args, **kwargs): # real signature unknown
    pass

def apol_type_query_t_set_regex(*args, **kwargs): # real signature unknown
    pass

def apol_type_query_t_set_type(*args, **kwargs): # real signature unknown
    pass

def apol_type_query_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def apol_user_query_t_run(*args, **kwargs): # real signature unknown
    pass

def apol_user_query_t_set_default_level(*args, **kwargs): # real signature unknown
    pass

def apol_user_query_t_set_range(*args, **kwargs): # real signature unknown
    pass

def apol_user_query_t_set_regex(*args, **kwargs): # real signature unknown
    pass

def apol_user_query_t_set_role(*args, **kwargs): # real signature unknown
    pass

def apol_user_query_t_set_user(*args, **kwargs): # real signature unknown
    pass

def apol_user_query_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def apol_validatetrans_query_t_run(*args, **kwargs): # real signature unknown
    pass

def apol_validatetrans_query_t_set_class(*args, **kwargs): # real signature unknown
    pass

def apol_validatetrans_query_t_set_regex(*args, **kwargs): # real signature unknown
    pass

def apol_validatetrans_query_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def apol_vector_compare(*args, **kwargs): # real signature unknown
    pass

def apol_vector_t_append(*args, **kwargs): # real signature unknown
    pass

def apol_vector_t_append_unique(*args, **kwargs): # real signature unknown
    pass

def apol_vector_t_cat(*args, **kwargs): # real signature unknown
    pass

def apol_vector_t_get_capacity(*args, **kwargs): # real signature unknown
    pass

def apol_vector_t_get_element(*args, **kwargs): # real signature unknown
    pass

def apol_vector_t_get_size(*args, **kwargs): # real signature unknown
    pass

def apol_vector_t_remove(*args, **kwargs): # real signature unknown
    pass

def apol_vector_t_sort(*args, **kwargs): # real signature unknown
    pass

def apol_vector_t_sort_uniquify(*args, **kwargs): # real signature unknown
    pass

def apol_vector_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def delete_apol_attr_query_t(*args, **kwargs): # real signature unknown
    pass

def delete_apol_avrule_query_t(*args, **kwargs): # real signature unknown
    pass

def delete_apol_bool_query_t(*args, **kwargs): # real signature unknown
    pass

def delete_apol_cat_query_t(*args, **kwargs): # real signature unknown
    pass

def delete_apol_class_query_t(*args, **kwargs): # real signature unknown
    pass

def delete_apol_common_query_t(*args, **kwargs): # real signature unknown
    pass

def delete_apol_cond_query_t(*args, **kwargs): # real signature unknown
    pass

def delete_apol_constraint_query_t(*args, **kwargs): # real signature unknown
    pass

def delete_apol_context_t(*args, **kwargs): # real signature unknown
    pass

def delete_apol_domain_trans_analysis_t(*args, **kwargs): # real signature unknown
    pass

def delete_apol_domain_trans_result_t(*args, **kwargs): # real signature unknown
    pass

def delete_apol_fs_use_query_t(*args, **kwargs): # real signature unknown
    pass

def delete_apol_genfscon_query_t(*args, **kwargs): # real signature unknown
    pass

def delete_apol_infoflow_analysis_t(*args, **kwargs): # real signature unknown
    pass

def delete_apol_infoflow_graph_t(*args, **kwargs): # real signature unknown
    pass

def delete_apol_infoflow_result_t(*args, **kwargs): # real signature unknown
    pass

def delete_apol_infoflow_step_t(*args, **kwargs): # real signature unknown
    pass

def delete_apol_infoflow_t(*args, **kwargs): # real signature unknown
    pass

def delete_apol_ip_t(*args, **kwargs): # real signature unknown
    pass

def delete_apol_isid_query_t(*args, **kwargs): # real signature unknown
    pass

def delete_apol_level_query_t(*args, **kwargs): # real signature unknown
    pass

def delete_apol_mls_level_t(*args, **kwargs): # real signature unknown
    pass

def delete_apol_mls_range_t(*args, **kwargs): # real signature unknown
    pass

def delete_apol_netifcon_query_t(*args, **kwargs): # real signature unknown
    pass

def delete_apol_nodecon_query_t(*args, **kwargs): # real signature unknown
    pass

def delete_apol_perm_query_t(*args, **kwargs): # real signature unknown
    pass

def delete_apol_policy_path_t(*args, **kwargs): # real signature unknown
    pass

def delete_apol_policy_t(*args, **kwargs): # real signature unknown
    pass

def delete_apol_portcon_query_t(*args, **kwargs): # real signature unknown
    pass

def delete_apol_range_trans_query_t(*args, **kwargs): # real signature unknown
    pass

def delete_apol_relabel_analysis_t(*args, **kwargs): # real signature unknown
    pass

def delete_apol_relabel_result_pair_t(*args, **kwargs): # real signature unknown
    pass

def delete_apol_relabel_result_t(*args, **kwargs): # real signature unknown
    pass

def delete_apol_role_allow_query_t(*args, **kwargs): # real signature unknown
    pass

def delete_apol_role_query_t(*args, **kwargs): # real signature unknown
    pass

def delete_apol_role_trans_query_t(*args, **kwargs): # real signature unknown
    pass

def delete_apol_string_vector_t(*args, **kwargs): # real signature unknown
    pass

def delete_apol_terule_query_t(*args, **kwargs): # real signature unknown
    pass

def delete_apol_types_relation_access_t(*args, **kwargs): # real signature unknown
    pass

def delete_apol_types_relation_analysis_t(*args, **kwargs): # real signature unknown
    pass

def delete_apol_types_relation_result_t(*args, **kwargs): # real signature unknown
    pass

def delete_apol_type_query_t(*args, **kwargs): # real signature unknown
    pass

def delete_apol_user_query_t(*args, **kwargs): # real signature unknown
    pass

def delete_apol_validatetrans_query_t(*args, **kwargs): # real signature unknown
    pass

def delete_apol_vector_t(*args, **kwargs): # real signature unknown
    pass

def libapol_get_version(*args, **kwargs): # real signature unknown
    pass

def new_apol_attr_query_t(*args, **kwargs): # real signature unknown
    pass

def new_apol_avrule_query_t(*args, **kwargs): # real signature unknown
    pass

def new_apol_bool_query_t(*args, **kwargs): # real signature unknown
    pass

def new_apol_cat_query_t(*args, **kwargs): # real signature unknown
    pass

def new_apol_class_query_t(*args, **kwargs): # real signature unknown
    pass

def new_apol_common_query_t(*args, **kwargs): # real signature unknown
    pass

def new_apol_cond_query_t(*args, **kwargs): # real signature unknown
    pass

def new_apol_constraint_query_t(*args, **kwargs): # real signature unknown
    pass

def new_apol_context_t(*args, **kwargs): # real signature unknown
    pass

def new_apol_domain_trans_analysis_t(*args, **kwargs): # real signature unknown
    pass

def new_apol_domain_trans_result_t(*args, **kwargs): # real signature unknown
    pass

def new_apol_fs_use_query_t(*args, **kwargs): # real signature unknown
    pass

def new_apol_genfscon_query_t(*args, **kwargs): # real signature unknown
    pass

def new_apol_infoflow_analysis_t(*args, **kwargs): # real signature unknown
    pass

def new_apol_infoflow_graph_t(*args, **kwargs): # real signature unknown
    pass

def new_apol_infoflow_result_t(*args, **kwargs): # real signature unknown
    pass

def new_apol_infoflow_step_t(*args, **kwargs): # real signature unknown
    pass

def new_apol_infoflow_t(*args, **kwargs): # real signature unknown
    pass

def new_apol_ip_t(*args, **kwargs): # real signature unknown
    pass

def new_apol_isid_query_t(*args, **kwargs): # real signature unknown
    pass

def new_apol_level_query_t(*args, **kwargs): # real signature unknown
    pass

def new_apol_mls_level_t(*args, **kwargs): # real signature unknown
    pass

def new_apol_mls_range_t(*args, **kwargs): # real signature unknown
    pass

def new_apol_netifcon_query_t(*args, **kwargs): # real signature unknown
    pass

def new_apol_nodecon_query_t(*args, **kwargs): # real signature unknown
    pass

def new_apol_perm_query_t(*args, **kwargs): # real signature unknown
    pass

def new_apol_policy_path_t(*args, **kwargs): # real signature unknown
    pass

def new_apol_policy_t(*args, **kwargs): # real signature unknown
    pass

def new_apol_portcon_query_t(*args, **kwargs): # real signature unknown
    pass

def new_apol_range_trans_query_t(*args, **kwargs): # real signature unknown
    pass

def new_apol_relabel_analysis_t(*args, **kwargs): # real signature unknown
    pass

def new_apol_relabel_result_pair_t(*args, **kwargs): # real signature unknown
    pass

def new_apol_relabel_result_t(*args, **kwargs): # real signature unknown
    pass

def new_apol_role_allow_query_t(*args, **kwargs): # real signature unknown
    pass

def new_apol_role_query_t(*args, **kwargs): # real signature unknown
    pass

def new_apol_role_trans_query_t(*args, **kwargs): # real signature unknown
    pass

def new_apol_string_vector_t(*args, **kwargs): # real signature unknown
    pass

def new_apol_terule_query_t(*args, **kwargs): # real signature unknown
    pass

def new_apol_types_relation_access_t(*args, **kwargs): # real signature unknown
    pass

def new_apol_types_relation_analysis_t(*args, **kwargs): # real signature unknown
    pass

def new_apol_types_relation_result_t(*args, **kwargs): # real signature unknown
    pass

def new_apol_type_query_t(*args, **kwargs): # real signature unknown
    pass

def new_apol_user_query_t(*args, **kwargs): # real signature unknown
    pass

def new_apol_validatetrans_query_t(*args, **kwargs): # real signature unknown
    pass

def new_apol_vector_t(*args, **kwargs): # real signature unknown
    pass

def SWIG_PyInstanceMethod_New(*args, **kwargs): # real signature unknown
    pass

# no classes
