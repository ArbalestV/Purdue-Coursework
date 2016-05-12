# encoding: utf-8
# module libsvn._client
# from /usr/lib64/python2.6/site-packages/libsvn/_client.so
# by generator 1.136
# no doc
# no imports

# Variables with simple values

SVN_CLIENT_AUTH_PASSWORD = 'password'
SVN_CLIENT_AUTH_USERNAME = 'username'

SVN_CLIENT_COMMIT_ITEM_ADD = 1
SVN_CLIENT_COMMIT_ITEM_DELETE = 2

SVN_CLIENT_COMMIT_ITEM_IS_COPY = 16

SVN_CLIENT_COMMIT_ITEM_LOCK_TOKEN = 32

SVN_CLIENT_COMMIT_ITEM_PROP_MODS = 8

SVN_CLIENT_COMMIT_ITEM_TEXT_MODS = 4

svn_client_diff_summarize_kind_added = 1
svn_client_diff_summarize_kind_deleted = 3
svn_client_diff_summarize_kind_modified = 2
svn_client_diff_summarize_kind_normal = 0

SWIG_SVN_INFO_SIZE_UNKNOWN = 18446744073709551615L

# functions

def delete_svn_client_commit_info_t(svn_client_commit_info_t_self): # real signature unknown; restored from __doc__
    """ delete_svn_client_commit_info_t(svn_client_commit_info_t self) """
    pass

def delete_svn_client_commit_item2_t(svn_client_commit_item2_t_self): # real signature unknown; restored from __doc__
    """ delete_svn_client_commit_item2_t(svn_client_commit_item2_t self) """
    pass

def delete_svn_client_commit_item3_t(svn_client_commit_item3_t_self): # real signature unknown; restored from __doc__
    """ delete_svn_client_commit_item3_t(svn_client_commit_item3_t self) """
    pass

def delete_svn_client_commit_item_t(svn_client_commit_item_t_self): # real signature unknown; restored from __doc__
    """ delete_svn_client_commit_item_t(svn_client_commit_item_t self) """
    pass

def delete_svn_client_copy_source_t(svn_client_copy_source_t_self): # real signature unknown; restored from __doc__
    """ delete_svn_client_copy_source_t(svn_client_copy_source_t self) """
    pass

def delete_svn_client_ctx_t(svn_client_ctx_t_self): # real signature unknown; restored from __doc__
    """ delete_svn_client_ctx_t(svn_client_ctx_t self) """
    pass

def delete_svn_client_diff_summarize_t(svn_client_diff_summarize_t_self): # real signature unknown; restored from __doc__
    """ delete_svn_client_diff_summarize_t(svn_client_diff_summarize_t self) """
    pass

def delete_svn_info_t(svn_info_t_self): # real signature unknown; restored from __doc__
    """ delete_svn_info_t(svn_info_t self) """
    pass

def new_svn_client_commit_info_t(): # real signature unknown; restored from __doc__
    """ new_svn_client_commit_info_t() -> svn_client_commit_info_t """
    pass

def new_svn_client_commit_item2_t(): # real signature unknown; restored from __doc__
    """ new_svn_client_commit_item2_t() -> svn_client_commit_item2_t """
    pass

def new_svn_client_commit_item3_t(): # real signature unknown; restored from __doc__
    """ new_svn_client_commit_item3_t() -> svn_client_commit_item3_t """
    pass

def new_svn_client_commit_item_t(): # real signature unknown; restored from __doc__
    """ new_svn_client_commit_item_t() -> svn_client_commit_item_t """
    pass

def new_svn_client_copy_source_t(): # real signature unknown; restored from __doc__
    """ new_svn_client_copy_source_t() -> svn_client_copy_source_t """
    pass

def new_svn_client_ctx_t(): # real signature unknown; restored from __doc__
    """ new_svn_client_ctx_t() -> svn_client_ctx_t """
    pass

def new_svn_client_diff_summarize_t(): # real signature unknown; restored from __doc__
    """ new_svn_client_diff_summarize_t() -> svn_client_diff_summarize_t """
    pass

def new_svn_info_t(): # real signature unknown; restored from __doc__
    """ new_svn_info_t() -> svn_info_t """
    pass

def svn_changelist_invoke_receiver(svn_changelist_receiver_t__obj, void_baton, char_path, char_changelist, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_changelist_invoke_receiver(svn_changelist_receiver_t _obj, void baton, char path, 
        char changelist, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_changelist_receiver_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def svn_client_add(char_path, svn_boolean_t_recursive, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_add(char path, svn_boolean_t recursive, svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_add2(char_path, svn_boolean_t_recursive, svn_boolean_t_force, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_add2(char path, svn_boolean_t recursive, svn_boolean_t force, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_add3(char_path, svn_boolean_t_recursive, svn_boolean_t_force, svn_boolean_t_no_ignore, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_add3(char path, svn_boolean_t recursive, svn_boolean_t force, 
        svn_boolean_t no_ignore, svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_add4(char_path, svn_depth_t_depth, svn_boolean_t_force, svn_boolean_t_no_ignore, svn_boolean_t_add_parents, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_add4(char path, svn_depth_t depth, svn_boolean_t force, 
        svn_boolean_t no_ignore, svn_boolean_t add_parents, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_add_to_changelist(apr_array_header_t_paths, char_changelist, svn_depth_t_depth, apr_array_header_t_changelists, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_add_to_changelist(apr_array_header_t paths, char changelist, svn_depth_t depth, 
        apr_array_header_t changelists, svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_args_to_target_array(apr_array_header_t_targets_p, apr_getopt_t_os, apr_array_header_t_known_targets, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_args_to_target_array(apr_array_header_t targets_p, apr_getopt_t os, apr_array_header_t known_targets, 
        svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_blame(char_path_or_url, svn_opt_revision_t_start, svn_opt_revision_t_end, svn_client_blame_receiver_t_receiver, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_blame(char path_or_url, svn_opt_revision_t start, svn_opt_revision_t end, 
        svn_client_blame_receiver_t receiver, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_blame2(char_path_or_url, svn_opt_revision_t_peg_revision, svn_opt_revision_t_start, svn_opt_revision_t_end, svn_client_blame_receiver_t_receiver, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_blame2(char path_or_url, svn_opt_revision_t peg_revision, 
        svn_opt_revision_t start, svn_opt_revision_t end, 
        svn_client_blame_receiver_t receiver, svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_blame3(char_path_or_url, svn_opt_revision_t_peg_revision, svn_opt_revision_t_start, svn_opt_revision_t_end, svn_diff_file_options_t_diff_options, svn_boolean_t_ignore_mime_type, svn_client_blame_receiver_t_receiver, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_blame3(char path_or_url, svn_opt_revision_t peg_revision, 
        svn_opt_revision_t start, svn_opt_revision_t end, 
        svn_diff_file_options_t diff_options, svn_boolean_t ignore_mime_type, 
        svn_client_blame_receiver_t receiver, 
        svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_blame4(char_path_or_url, svn_opt_revision_t_peg_revision, svn_opt_revision_t_start, svn_opt_revision_t_end, svn_diff_file_options_t_diff_options, svn_boolean_t_ignore_mime_type, svn_boolean_t_include_merged_revisions, svn_client_blame_receiver2_t_receiver, void_receiver_baton, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_blame4(char path_or_url, svn_opt_revision_t peg_revision, 
        svn_opt_revision_t start, svn_opt_revision_t end, 
        svn_diff_file_options_t diff_options, svn_boolean_t ignore_mime_type, 
        svn_boolean_t include_merged_revisions, 
        svn_client_blame_receiver2_t receiver, 
        void receiver_baton, svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_blame_receiver2_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def svn_client_blame_receiver_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def svn_client_cat(svn_stream_t_out, char_path_or_url, svn_opt_revision_t_revision, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_cat(svn_stream_t out, char path_or_url, svn_opt_revision_t revision, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_cat2(svn_stream_t_out, char_path_or_url, svn_opt_revision_t_peg_revision, svn_opt_revision_t_revision, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_cat2(svn_stream_t out, char path_or_url, svn_opt_revision_t peg_revision, 
        svn_opt_revision_t revision, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_checkout(svn_revnum_t_result_rev, char_URL, char_path, svn_opt_revision_t_revision, svn_boolean_t_recurse, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_checkout(svn_revnum_t result_rev, char URL, char path, svn_opt_revision_t revision, 
        svn_boolean_t recurse, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_checkout2(svn_revnum_t_result_rev, char_URL, char_path, svn_opt_revision_t_peg_revision, svn_opt_revision_t_revision, svn_boolean_t_recurse, svn_boolean_t_ignore_externals, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_checkout2(svn_revnum_t result_rev, char URL, char path, svn_opt_revision_t peg_revision, 
        svn_opt_revision_t revision, 
        svn_boolean_t recurse, svn_boolean_t ignore_externals, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_checkout3(svn_revnum_t_result_rev, char_URL, char_path, svn_opt_revision_t_peg_revision, svn_opt_revision_t_revision, svn_depth_t_depth, svn_boolean_t_ignore_externals, svn_boolean_t_allow_unver_obstructions, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_checkout3(svn_revnum_t result_rev, char URL, char path, svn_opt_revision_t peg_revision, 
        svn_opt_revision_t revision, 
        svn_depth_t depth, svn_boolean_t ignore_externals, 
        svn_boolean_t allow_unver_obstructions, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_cleanup(char_dir, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_client_cleanup(char dir, svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t """
    pass

def svn_client_commit(svn_client_commit_info_t_commit_info_p, apr_array_header_t_targets, svn_boolean_t_nonrecursive, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_commit(svn_client_commit_info_t commit_info_p, apr_array_header_t targets, 
        svn_boolean_t nonrecursive, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_commit2(svn_client_commit_info_t_commit_info_p, apr_array_header_t_targets, svn_boolean_t_recurse, svn_boolean_t_keep_locks, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_commit2(svn_client_commit_info_t commit_info_p, apr_array_header_t targets, 
        svn_boolean_t recurse, svn_boolean_t keep_locks, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_commit3(svn_commit_info_t_commit_info_p, apr_array_header_t_targets, svn_boolean_t_recurse, svn_boolean_t_keep_locks, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_commit3(svn_commit_info_t commit_info_p, apr_array_header_t targets, 
        svn_boolean_t recurse, svn_boolean_t keep_locks, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_commit4(svn_commit_info_t_commit_info_p, apr_array_header_t_targets, svn_depth_t_depth, svn_boolean_t_keep_locks, svn_boolean_t_keep_changelists, apr_array_header_t_changelists, apr_hash_t_revprop_table, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_commit4(svn_commit_info_t commit_info_p, apr_array_header_t targets, 
        svn_depth_t depth, svn_boolean_t keep_locks, 
        svn_boolean_t keep_changelists, apr_array_header_t changelists, 
        apr_hash_t revprop_table, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_commit_info_t_author_get(svn_client_commit_info_t_self): # real signature unknown; restored from __doc__
    """ svn_client_commit_info_t_author_get(svn_client_commit_info_t self) -> char """
    return ""

def svn_client_commit_info_t_author_set(svn_client_commit_info_t_self, char_author): # real signature unknown; restored from __doc__
    """ svn_client_commit_info_t_author_set(svn_client_commit_info_t self, char author) """
    pass

def svn_client_commit_info_t_date_get(svn_client_commit_info_t_self): # real signature unknown; restored from __doc__
    """ svn_client_commit_info_t_date_get(svn_client_commit_info_t self) -> char """
    return ""

def svn_client_commit_info_t_date_set(svn_client_commit_info_t_self, char_date): # real signature unknown; restored from __doc__
    """ svn_client_commit_info_t_date_set(svn_client_commit_info_t self, char date) """
    pass

def svn_client_commit_info_t_revision_get(svn_client_commit_info_t_self): # real signature unknown; restored from __doc__
    """ svn_client_commit_info_t_revision_get(svn_client_commit_info_t self) -> svn_revnum_t """
    pass

def svn_client_commit_info_t_revision_set(svn_client_commit_info_t_self, svn_revnum_t_revision): # real signature unknown; restored from __doc__
    """ svn_client_commit_info_t_revision_set(svn_client_commit_info_t self, svn_revnum_t revision) """
    pass

def svn_client_commit_info_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def svn_client_commit_item2_dup(svn_client_commit_item2_t_item, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_client_commit_item2_dup(svn_client_commit_item2_t item, apr_pool_t pool) -> svn_client_commit_item2_t """
    pass

def svn_client_commit_item2_t_copyfrom_rev_get(svn_client_commit_item2_t_self): # real signature unknown; restored from __doc__
    """ svn_client_commit_item2_t_copyfrom_rev_get(svn_client_commit_item2_t self) -> svn_revnum_t """
    pass

def svn_client_commit_item2_t_copyfrom_rev_set(svn_client_commit_item2_t_self, svn_revnum_t_copyfrom_rev): # real signature unknown; restored from __doc__
    """ svn_client_commit_item2_t_copyfrom_rev_set(svn_client_commit_item2_t self, svn_revnum_t copyfrom_rev) """
    pass

def svn_client_commit_item2_t_copyfrom_url_get(svn_client_commit_item2_t_self): # real signature unknown; restored from __doc__
    """ svn_client_commit_item2_t_copyfrom_url_get(svn_client_commit_item2_t self) -> char """
    return ""

def svn_client_commit_item2_t_copyfrom_url_set(svn_client_commit_item2_t_self, char_copyfrom_url): # real signature unknown; restored from __doc__
    """ svn_client_commit_item2_t_copyfrom_url_set(svn_client_commit_item2_t self, char copyfrom_url) """
    pass

def svn_client_commit_item2_t_kind_get(svn_client_commit_item2_t_self): # real signature unknown; restored from __doc__
    """ svn_client_commit_item2_t_kind_get(svn_client_commit_item2_t self) -> svn_node_kind_t """
    pass

def svn_client_commit_item2_t_kind_set(svn_client_commit_item2_t_self, svn_node_kind_t_kind): # real signature unknown; restored from __doc__
    """ svn_client_commit_item2_t_kind_set(svn_client_commit_item2_t self, svn_node_kind_t kind) """
    pass

def svn_client_commit_item2_t_path_get(svn_client_commit_item2_t_self): # real signature unknown; restored from __doc__
    """ svn_client_commit_item2_t_path_get(svn_client_commit_item2_t self) -> char """
    return ""

def svn_client_commit_item2_t_path_set(svn_client_commit_item2_t_self, char_path): # real signature unknown; restored from __doc__
    """ svn_client_commit_item2_t_path_set(svn_client_commit_item2_t self, char path) """
    pass

def svn_client_commit_item2_t_revision_get(svn_client_commit_item2_t_self): # real signature unknown; restored from __doc__
    """ svn_client_commit_item2_t_revision_get(svn_client_commit_item2_t self) -> svn_revnum_t """
    pass

def svn_client_commit_item2_t_revision_set(svn_client_commit_item2_t_self, svn_revnum_t_revision): # real signature unknown; restored from __doc__
    """ svn_client_commit_item2_t_revision_set(svn_client_commit_item2_t self, svn_revnum_t revision) """
    pass

def svn_client_commit_item2_t_state_flags_get(svn_client_commit_item2_t_self): # real signature unknown; restored from __doc__
    """ svn_client_commit_item2_t_state_flags_get(svn_client_commit_item2_t self) -> apr_byte_t """
    pass

def svn_client_commit_item2_t_state_flags_set(svn_client_commit_item2_t_self, apr_byte_t_state_flags): # real signature unknown; restored from __doc__
    """ svn_client_commit_item2_t_state_flags_set(svn_client_commit_item2_t self, apr_byte_t state_flags) """
    pass

def svn_client_commit_item2_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def svn_client_commit_item2_t_url_get(svn_client_commit_item2_t_self): # real signature unknown; restored from __doc__
    """ svn_client_commit_item2_t_url_get(svn_client_commit_item2_t self) -> char """
    return ""

def svn_client_commit_item2_t_url_set(svn_client_commit_item2_t_self, char_url): # real signature unknown; restored from __doc__
    """ svn_client_commit_item2_t_url_set(svn_client_commit_item2_t self, char url) """
    pass

def svn_client_commit_item2_t_wcprop_changes_get(svn_client_commit_item2_t_self): # real signature unknown; restored from __doc__
    """ svn_client_commit_item2_t_wcprop_changes_get(svn_client_commit_item2_t self) -> apr_array_header_t """
    pass

def svn_client_commit_item2_t_wcprop_changes_set(svn_client_commit_item2_t_self, apr_array_header_t_wcprop_changes): # real signature unknown; restored from __doc__
    """ svn_client_commit_item2_t_wcprop_changes_set(svn_client_commit_item2_t self, apr_array_header_t wcprop_changes) """
    pass

def svn_client_commit_item3_create(apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_client_commit_item3_create(apr_pool_t pool) -> svn_client_commit_item3_t """
    pass

def svn_client_commit_item3_dup(svn_client_commit_item3_t_item, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_client_commit_item3_dup(svn_client_commit_item3_t item, apr_pool_t pool) -> svn_client_commit_item3_t """
    pass

def svn_client_commit_item3_t_copyfrom_rev_get(svn_client_commit_item3_t_self): # real signature unknown; restored from __doc__
    """ svn_client_commit_item3_t_copyfrom_rev_get(svn_client_commit_item3_t self) -> svn_revnum_t """
    pass

def svn_client_commit_item3_t_copyfrom_rev_set(svn_client_commit_item3_t_self, svn_revnum_t_copyfrom_rev): # real signature unknown; restored from __doc__
    """ svn_client_commit_item3_t_copyfrom_rev_set(svn_client_commit_item3_t self, svn_revnum_t copyfrom_rev) """
    pass

def svn_client_commit_item3_t_copyfrom_url_get(svn_client_commit_item3_t_self): # real signature unknown; restored from __doc__
    """ svn_client_commit_item3_t_copyfrom_url_get(svn_client_commit_item3_t self) -> char """
    return ""

def svn_client_commit_item3_t_copyfrom_url_set(svn_client_commit_item3_t_self, char_copyfrom_url): # real signature unknown; restored from __doc__
    """ svn_client_commit_item3_t_copyfrom_url_set(svn_client_commit_item3_t self, char copyfrom_url) """
    pass

def svn_client_commit_item3_t_incoming_prop_changes_get(svn_client_commit_item3_t_self): # real signature unknown; restored from __doc__
    """ svn_client_commit_item3_t_incoming_prop_changes_get(svn_client_commit_item3_t self) -> apr_array_header_t """
    pass

def svn_client_commit_item3_t_incoming_prop_changes_set(svn_client_commit_item3_t_self, apr_array_header_t_incoming_prop_changes): # real signature unknown; restored from __doc__
    """ svn_client_commit_item3_t_incoming_prop_changes_set(svn_client_commit_item3_t self, apr_array_header_t incoming_prop_changes) """
    pass

def svn_client_commit_item3_t_kind_get(svn_client_commit_item3_t_self): # real signature unknown; restored from __doc__
    """ svn_client_commit_item3_t_kind_get(svn_client_commit_item3_t self) -> svn_node_kind_t """
    pass

def svn_client_commit_item3_t_kind_set(svn_client_commit_item3_t_self, svn_node_kind_t_kind): # real signature unknown; restored from __doc__
    """ svn_client_commit_item3_t_kind_set(svn_client_commit_item3_t self, svn_node_kind_t kind) """
    pass

def svn_client_commit_item3_t_outgoing_prop_changes_get(svn_client_commit_item3_t_self): # real signature unknown; restored from __doc__
    """ svn_client_commit_item3_t_outgoing_prop_changes_get(svn_client_commit_item3_t self) -> apr_array_header_t """
    pass

def svn_client_commit_item3_t_outgoing_prop_changes_set(svn_client_commit_item3_t_self, apr_array_header_t_outgoing_prop_changes): # real signature unknown; restored from __doc__
    """ svn_client_commit_item3_t_outgoing_prop_changes_set(svn_client_commit_item3_t self, apr_array_header_t outgoing_prop_changes) """
    pass

def svn_client_commit_item3_t_path_get(svn_client_commit_item3_t_self): # real signature unknown; restored from __doc__
    """ svn_client_commit_item3_t_path_get(svn_client_commit_item3_t self) -> char """
    return ""

def svn_client_commit_item3_t_path_set(svn_client_commit_item3_t_self, char_path): # real signature unknown; restored from __doc__
    """ svn_client_commit_item3_t_path_set(svn_client_commit_item3_t self, char path) """
    pass

def svn_client_commit_item3_t_revision_get(svn_client_commit_item3_t_self): # real signature unknown; restored from __doc__
    """ svn_client_commit_item3_t_revision_get(svn_client_commit_item3_t self) -> svn_revnum_t """
    pass

def svn_client_commit_item3_t_revision_set(svn_client_commit_item3_t_self, svn_revnum_t_revision): # real signature unknown; restored from __doc__
    """ svn_client_commit_item3_t_revision_set(svn_client_commit_item3_t self, svn_revnum_t revision) """
    pass

def svn_client_commit_item3_t_state_flags_get(svn_client_commit_item3_t_self): # real signature unknown; restored from __doc__
    """ svn_client_commit_item3_t_state_flags_get(svn_client_commit_item3_t self) -> apr_byte_t """
    pass

def svn_client_commit_item3_t_state_flags_set(svn_client_commit_item3_t_self, apr_byte_t_state_flags): # real signature unknown; restored from __doc__
    """ svn_client_commit_item3_t_state_flags_set(svn_client_commit_item3_t self, apr_byte_t state_flags) """
    pass

def svn_client_commit_item3_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def svn_client_commit_item3_t_url_get(svn_client_commit_item3_t_self): # real signature unknown; restored from __doc__
    """ svn_client_commit_item3_t_url_get(svn_client_commit_item3_t self) -> char """
    return ""

def svn_client_commit_item3_t_url_set(svn_client_commit_item3_t_self, char_url): # real signature unknown; restored from __doc__
    """ svn_client_commit_item3_t_url_set(svn_client_commit_item3_t self, char url) """
    pass

def svn_client_commit_item_create(svn_client_commit_item3_t_item, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_client_commit_item_create(svn_client_commit_item3_t item, apr_pool_t pool) -> svn_error_t """
    pass

def svn_client_commit_item_t_copyfrom_url_get(svn_client_commit_item_t_self): # real signature unknown; restored from __doc__
    """ svn_client_commit_item_t_copyfrom_url_get(svn_client_commit_item_t self) -> char """
    return ""

def svn_client_commit_item_t_copyfrom_url_set(svn_client_commit_item_t_self, char_copyfrom_url): # real signature unknown; restored from __doc__
    """ svn_client_commit_item_t_copyfrom_url_set(svn_client_commit_item_t self, char copyfrom_url) """
    pass

def svn_client_commit_item_t_kind_get(svn_client_commit_item_t_self): # real signature unknown; restored from __doc__
    """ svn_client_commit_item_t_kind_get(svn_client_commit_item_t self) -> svn_node_kind_t """
    pass

def svn_client_commit_item_t_kind_set(svn_client_commit_item_t_self, svn_node_kind_t_kind): # real signature unknown; restored from __doc__
    """ svn_client_commit_item_t_kind_set(svn_client_commit_item_t self, svn_node_kind_t kind) """
    pass

def svn_client_commit_item_t_path_get(svn_client_commit_item_t_self): # real signature unknown; restored from __doc__
    """ svn_client_commit_item_t_path_get(svn_client_commit_item_t self) -> char """
    return ""

def svn_client_commit_item_t_path_set(svn_client_commit_item_t_self, char_path): # real signature unknown; restored from __doc__
    """ svn_client_commit_item_t_path_set(svn_client_commit_item_t self, char path) """
    pass

def svn_client_commit_item_t_revision_get(svn_client_commit_item_t_self): # real signature unknown; restored from __doc__
    """ svn_client_commit_item_t_revision_get(svn_client_commit_item_t self) -> svn_revnum_t """
    pass

def svn_client_commit_item_t_revision_set(svn_client_commit_item_t_self, svn_revnum_t_revision): # real signature unknown; restored from __doc__
    """ svn_client_commit_item_t_revision_set(svn_client_commit_item_t self, svn_revnum_t revision) """
    pass

def svn_client_commit_item_t_state_flags_get(svn_client_commit_item_t_self): # real signature unknown; restored from __doc__
    """ svn_client_commit_item_t_state_flags_get(svn_client_commit_item_t self) -> apr_byte_t """
    pass

def svn_client_commit_item_t_state_flags_set(svn_client_commit_item_t_self, apr_byte_t_state_flags): # real signature unknown; restored from __doc__
    """ svn_client_commit_item_t_state_flags_set(svn_client_commit_item_t self, apr_byte_t state_flags) """
    pass

def svn_client_commit_item_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def svn_client_commit_item_t_url_get(svn_client_commit_item_t_self): # real signature unknown; restored from __doc__
    """ svn_client_commit_item_t_url_get(svn_client_commit_item_t self) -> char """
    return ""

def svn_client_commit_item_t_url_set(svn_client_commit_item_t_self, char_url): # real signature unknown; restored from __doc__
    """ svn_client_commit_item_t_url_set(svn_client_commit_item_t self, char url) """
    pass

def svn_client_commit_item_t_wcprop_changes_get(svn_client_commit_item_t_self): # real signature unknown; restored from __doc__
    """ svn_client_commit_item_t_wcprop_changes_get(svn_client_commit_item_t self) -> apr_array_header_t """
    pass

def svn_client_commit_item_t_wcprop_changes_set(svn_client_commit_item_t_self, apr_array_header_t_wcprop_changes): # real signature unknown; restored from __doc__
    """ svn_client_commit_item_t_wcprop_changes_set(svn_client_commit_item_t self, apr_array_header_t wcprop_changes) """
    pass

def svn_client_copy(svn_client_commit_info_t_commit_info_p, char_src_path, svn_opt_revision_t_src_revision, char_dst_path, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_copy(svn_client_commit_info_t commit_info_p, char src_path, 
        svn_opt_revision_t src_revision, char dst_path, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_copy2(svn_commit_info_t_commit_info_p, char_src_path, svn_opt_revision_t_src_revision, char_dst_path, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_copy2(svn_commit_info_t commit_info_p, char src_path, svn_opt_revision_t src_revision, 
        char dst_path, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_copy3(svn_commit_info_t_commit_info_p, char_src_path, svn_opt_revision_t_src_revision, char_dst_path, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_copy3(svn_commit_info_t commit_info_p, char src_path, svn_opt_revision_t src_revision, 
        char dst_path, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_copy4(svn_commit_info_t_commit_info_p, apr_array_header_t_sources, char_dst_path, svn_boolean_t_copy_as_child, svn_boolean_t_make_parents, apr_hash_t_revprop_table, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_copy4(svn_commit_info_t commit_info_p, apr_array_header_t sources, 
        char dst_path, svn_boolean_t copy_as_child, 
        svn_boolean_t make_parents, apr_hash_t revprop_table, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_copy5(svn_commit_info_t_commit_info_p, apr_array_header_t_sources, char_dst_path, svn_boolean_t_copy_as_child, svn_boolean_t_make_parents, svn_boolean_t_ignore_externals, apr_hash_t_revprop_table, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_copy5(svn_commit_info_t commit_info_p, apr_array_header_t sources, 
        char dst_path, svn_boolean_t copy_as_child, 
        svn_boolean_t make_parents, svn_boolean_t ignore_externals, 
        apr_hash_t revprop_table, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_copy_source_t_path_get(svn_client_copy_source_t_self): # real signature unknown; restored from __doc__
    """ svn_client_copy_source_t_path_get(svn_client_copy_source_t self) -> char """
    return ""

def svn_client_copy_source_t_path_set(svn_client_copy_source_t_self, char_path): # real signature unknown; restored from __doc__
    """ svn_client_copy_source_t_path_set(svn_client_copy_source_t self, char path) """
    pass

def svn_client_copy_source_t_peg_revision_get(svn_client_copy_source_t_self): # real signature unknown; restored from __doc__
    """ svn_client_copy_source_t_peg_revision_get(svn_client_copy_source_t self) -> svn_opt_revision_t """
    pass

def svn_client_copy_source_t_peg_revision_set(svn_client_copy_source_t_self, svn_opt_revision_t_peg_revision): # real signature unknown; restored from __doc__
    """ svn_client_copy_source_t_peg_revision_set(svn_client_copy_source_t self, svn_opt_revision_t peg_revision) """
    pass

def svn_client_copy_source_t_revision_get(svn_client_copy_source_t_self): # real signature unknown; restored from __doc__
    """ svn_client_copy_source_t_revision_get(svn_client_copy_source_t self) -> svn_opt_revision_t """
    pass

def svn_client_copy_source_t_revision_set(svn_client_copy_source_t_self, svn_opt_revision_t_revision): # real signature unknown; restored from __doc__
    """ svn_client_copy_source_t_revision_set(svn_client_copy_source_t self, svn_opt_revision_t revision) """
    pass

def svn_client_copy_source_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def svn_client_create_context(svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_client_create_context(svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t """
    pass

def svn_client_ctx_t_auth_baton_get(svn_client_ctx_t_self): # real signature unknown; restored from __doc__
    """ svn_client_ctx_t_auth_baton_get(svn_client_ctx_t self) -> svn_auth_baton_t """
    pass

def svn_client_ctx_t_auth_baton_set(svn_client_ctx_t_self, svn_auth_baton_t_auth_baton): # real signature unknown; restored from __doc__
    """ svn_client_ctx_t_auth_baton_set(svn_client_ctx_t self, svn_auth_baton_t auth_baton) """
    pass

def svn_client_ctx_t_cancel_baton_get(svn_client_ctx_t_self): # real signature unknown; restored from __doc__
    """ svn_client_ctx_t_cancel_baton_get(svn_client_ctx_t self) -> void """
    pass

def svn_client_ctx_t_cancel_baton_set(svn_client_ctx_t_self, void_cancel_baton): # real signature unknown; restored from __doc__
    """ svn_client_ctx_t_cancel_baton_set(svn_client_ctx_t self, void cancel_baton) """
    pass

def svn_client_ctx_t_cancel_func_get(svn_client_ctx_t_self): # real signature unknown; restored from __doc__
    """ svn_client_ctx_t_cancel_func_get(svn_client_ctx_t self) -> svn_cancel_func_t """
    pass

def svn_client_ctx_t_cancel_func_set(svn_client_ctx_t_self, svn_cancel_func_t_cancel_func): # real signature unknown; restored from __doc__
    """ svn_client_ctx_t_cancel_func_set(svn_client_ctx_t self, svn_cancel_func_t cancel_func) """
    pass

def svn_client_ctx_t_client_name_get(svn_client_ctx_t_self): # real signature unknown; restored from __doc__
    """ svn_client_ctx_t_client_name_get(svn_client_ctx_t self) -> char """
    return ""

def svn_client_ctx_t_client_name_set(svn_client_ctx_t_self, char_client_name): # real signature unknown; restored from __doc__
    """ svn_client_ctx_t_client_name_set(svn_client_ctx_t self, char client_name) """
    pass

def svn_client_ctx_t_config_get(svn_client_ctx_t_self): # real signature unknown; restored from __doc__
    """ svn_client_ctx_t_config_get(svn_client_ctx_t self) -> apr_hash_t """
    pass

def svn_client_ctx_t_config_set(svn_client_ctx_t_self, apr_hash_t_config): # real signature unknown; restored from __doc__
    """ svn_client_ctx_t_config_set(svn_client_ctx_t self, apr_hash_t config) """
    pass

def svn_client_ctx_t_conflict_baton_get(svn_client_ctx_t_self): # real signature unknown; restored from __doc__
    """ svn_client_ctx_t_conflict_baton_get(svn_client_ctx_t self) -> void """
    pass

def svn_client_ctx_t_conflict_baton_set(svn_client_ctx_t_self, void_conflict_baton): # real signature unknown; restored from __doc__
    """ svn_client_ctx_t_conflict_baton_set(svn_client_ctx_t self, void conflict_baton) """
    pass

def svn_client_ctx_t_conflict_func_get(svn_client_ctx_t_self): # real signature unknown; restored from __doc__
    """ svn_client_ctx_t_conflict_func_get(svn_client_ctx_t self) -> svn_wc_conflict_resolver_func_t """
    pass

def svn_client_ctx_t_conflict_func_set(svn_client_ctx_t_self, svn_wc_conflict_resolver_func_t_conflict_func): # real signature unknown; restored from __doc__
    """ svn_client_ctx_t_conflict_func_set(svn_client_ctx_t self, svn_wc_conflict_resolver_func_t conflict_func) """
    pass

def svn_client_ctx_t_log_msg_baton2_get(svn_client_ctx_t_self): # real signature unknown; restored from __doc__
    """ svn_client_ctx_t_log_msg_baton2_get(svn_client_ctx_t self) -> void """
    pass

def svn_client_ctx_t_log_msg_baton2_set(svn_client_ctx_t_self, void_log_msg_baton2): # real signature unknown; restored from __doc__
    """ svn_client_ctx_t_log_msg_baton2_set(svn_client_ctx_t self, void log_msg_baton2) """
    pass

def svn_client_ctx_t_log_msg_baton3_get(svn_client_ctx_t_self): # real signature unknown; restored from __doc__
    """ svn_client_ctx_t_log_msg_baton3_get(svn_client_ctx_t self) -> void """
    pass

def svn_client_ctx_t_log_msg_baton3_set(svn_client_ctx_t_self, void_log_msg_baton3): # real signature unknown; restored from __doc__
    """ svn_client_ctx_t_log_msg_baton3_set(svn_client_ctx_t self, void log_msg_baton3) """
    pass

def svn_client_ctx_t_log_msg_baton_get(svn_client_ctx_t_self): # real signature unknown; restored from __doc__
    """ svn_client_ctx_t_log_msg_baton_get(svn_client_ctx_t self) -> void """
    pass

def svn_client_ctx_t_log_msg_baton_set(svn_client_ctx_t_self, void_log_msg_baton): # real signature unknown; restored from __doc__
    """ svn_client_ctx_t_log_msg_baton_set(svn_client_ctx_t self, void log_msg_baton) """
    pass

def svn_client_ctx_t_log_msg_func2_get(svn_client_ctx_t_self): # real signature unknown; restored from __doc__
    """ svn_client_ctx_t_log_msg_func2_get(svn_client_ctx_t self) -> svn_client_get_commit_log2_t """
    pass

def svn_client_ctx_t_log_msg_func2_set(svn_client_ctx_t_self, svn_client_get_commit_log2_t_log_msg_func2): # real signature unknown; restored from __doc__
    """ svn_client_ctx_t_log_msg_func2_set(svn_client_ctx_t self, svn_client_get_commit_log2_t log_msg_func2) """
    pass

def svn_client_ctx_t_log_msg_func3_get(svn_client_ctx_t_self): # real signature unknown; restored from __doc__
    """ svn_client_ctx_t_log_msg_func3_get(svn_client_ctx_t self) -> svn_client_get_commit_log3_t """
    pass

def svn_client_ctx_t_log_msg_func3_set(svn_client_ctx_t_self, svn_client_get_commit_log3_t_log_msg_func3): # real signature unknown; restored from __doc__
    """ svn_client_ctx_t_log_msg_func3_set(svn_client_ctx_t self, svn_client_get_commit_log3_t log_msg_func3) """
    pass

def svn_client_ctx_t_log_msg_func_get(svn_client_ctx_t_self): # real signature unknown; restored from __doc__
    """ svn_client_ctx_t_log_msg_func_get(svn_client_ctx_t self) -> svn_client_get_commit_log_t """
    pass

def svn_client_ctx_t_log_msg_func_set(svn_client_ctx_t_self, svn_client_get_commit_log_t_log_msg_func): # real signature unknown; restored from __doc__
    """ svn_client_ctx_t_log_msg_func_set(svn_client_ctx_t self, svn_client_get_commit_log_t log_msg_func) """
    pass

def svn_client_ctx_t_mimetypes_map_get(svn_client_ctx_t_self): # real signature unknown; restored from __doc__
    """ svn_client_ctx_t_mimetypes_map_get(svn_client_ctx_t self) -> apr_hash_t """
    pass

def svn_client_ctx_t_mimetypes_map_set(svn_client_ctx_t_self, apr_hash_t_mimetypes_map): # real signature unknown; restored from __doc__
    """ svn_client_ctx_t_mimetypes_map_set(svn_client_ctx_t self, apr_hash_t mimetypes_map) """
    pass

def svn_client_ctx_t_notify_baton2_get(svn_client_ctx_t_self): # real signature unknown; restored from __doc__
    """ svn_client_ctx_t_notify_baton2_get(svn_client_ctx_t self) -> void """
    pass

def svn_client_ctx_t_notify_baton2_set(svn_client_ctx_t_self, void_notify_baton2): # real signature unknown; restored from __doc__
    """ svn_client_ctx_t_notify_baton2_set(svn_client_ctx_t self, void notify_baton2) """
    pass

def svn_client_ctx_t_notify_baton_get(svn_client_ctx_t_self): # real signature unknown; restored from __doc__
    """ svn_client_ctx_t_notify_baton_get(svn_client_ctx_t self) -> void """
    pass

def svn_client_ctx_t_notify_baton_set(svn_client_ctx_t_self, void_notify_baton): # real signature unknown; restored from __doc__
    """ svn_client_ctx_t_notify_baton_set(svn_client_ctx_t self, void notify_baton) """
    pass

def svn_client_ctx_t_notify_func2_get(svn_client_ctx_t_self): # real signature unknown; restored from __doc__
    """ svn_client_ctx_t_notify_func2_get(svn_client_ctx_t self) -> svn_wc_notify_func2_t """
    pass

def svn_client_ctx_t_notify_func2_set(svn_client_ctx_t_self, svn_wc_notify_func2_t_notify_func2): # real signature unknown; restored from __doc__
    """ svn_client_ctx_t_notify_func2_set(svn_client_ctx_t self, svn_wc_notify_func2_t notify_func2) """
    pass

def svn_client_ctx_t_notify_func_get(svn_client_ctx_t_self): # real signature unknown; restored from __doc__
    """ svn_client_ctx_t_notify_func_get(svn_client_ctx_t self) -> svn_wc_notify_func_t """
    pass

def svn_client_ctx_t_notify_func_set(svn_client_ctx_t_self, svn_wc_notify_func_t_notify_func): # real signature unknown; restored from __doc__
    """ svn_client_ctx_t_notify_func_set(svn_client_ctx_t self, svn_wc_notify_func_t notify_func) """
    pass

def svn_client_ctx_t_progress_baton_get(svn_client_ctx_t_self): # real signature unknown; restored from __doc__
    """ svn_client_ctx_t_progress_baton_get(svn_client_ctx_t self) -> void """
    pass

def svn_client_ctx_t_progress_baton_set(svn_client_ctx_t_self, void_progress_baton): # real signature unknown; restored from __doc__
    """ svn_client_ctx_t_progress_baton_set(svn_client_ctx_t self, void progress_baton) """
    pass

def svn_client_ctx_t_progress_func_get(svn_client_ctx_t_self): # real signature unknown; restored from __doc__
    """ svn_client_ctx_t_progress_func_get(svn_client_ctx_t self) -> svn_ra_progress_notify_func_t """
    pass

def svn_client_ctx_t_progress_func_set(svn_client_ctx_t_self, svn_ra_progress_notify_func_t_progress_func): # real signature unknown; restored from __doc__
    """ svn_client_ctx_t_progress_func_set(svn_client_ctx_t self, svn_ra_progress_notify_func_t progress_func) """
    pass

def svn_client_ctx_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def svn_client_delete(svn_client_commit_info_t_commit_info_p, apr_array_header_t_paths, svn_boolean_t_force, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_delete(svn_client_commit_info_t commit_info_p, apr_array_header_t paths, 
        svn_boolean_t force, svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_delete2(svn_commit_info_t_commit_info_p, apr_array_header_t_paths, svn_boolean_t_force, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_delete2(svn_commit_info_t commit_info_p, apr_array_header_t paths, 
        svn_boolean_t force, svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_delete3(svn_commit_info_t_commit_info_p, apr_array_header_t_paths, svn_boolean_t_force, svn_boolean_t_keep_local, apr_hash_t_revprop_table, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_delete3(svn_commit_info_t commit_info_p, apr_array_header_t paths, 
        svn_boolean_t force, svn_boolean_t keep_local, 
        apr_hash_t revprop_table, svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_diff(apr_array_header_t_diff_options, char_path1, svn_opt_revision_t_revision1, char_path2, svn_opt_revision_t_revision2, svn_boolean_t_recurse, svn_boolean_t_ignore_ancestry, svn_boolean_t_no_diff_deleted, apr_file_t_outfile, apr_file_t_errfile, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_diff(apr_array_header_t diff_options, char path1, svn_opt_revision_t revision1, 
        char path2, svn_opt_revision_t revision2, 
        svn_boolean_t recurse, svn_boolean_t ignore_ancestry, 
        svn_boolean_t no_diff_deleted, 
        apr_file_t outfile, apr_file_t errfile, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_diff2(apr_array_header_t_diff_options, char_path1, svn_opt_revision_t_revision1, char_path2, svn_opt_revision_t_revision2, svn_boolean_t_recurse, svn_boolean_t_ignore_ancestry, svn_boolean_t_no_diff_deleted, svn_boolean_t_ignore_content_type, apr_file_t_outfile, apr_file_t_errfile, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_diff2(apr_array_header_t diff_options, char path1, svn_opt_revision_t revision1, 
        char path2, svn_opt_revision_t revision2, 
        svn_boolean_t recurse, svn_boolean_t ignore_ancestry, 
        svn_boolean_t no_diff_deleted, 
        svn_boolean_t ignore_content_type, 
        apr_file_t outfile, apr_file_t errfile, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_diff3(apr_array_header_t_diff_options, char_path1, svn_opt_revision_t_revision1, char_path2, svn_opt_revision_t_revision2, svn_boolean_t_recurse, svn_boolean_t_ignore_ancestry, svn_boolean_t_no_diff_deleted, svn_boolean_t_ignore_content_type, char_header_encoding, apr_file_t_outfile, apr_file_t_errfile, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_diff3(apr_array_header_t diff_options, char path1, svn_opt_revision_t revision1, 
        char path2, svn_opt_revision_t revision2, 
        svn_boolean_t recurse, svn_boolean_t ignore_ancestry, 
        svn_boolean_t no_diff_deleted, 
        svn_boolean_t ignore_content_type, 
        char header_encoding, apr_file_t outfile, 
        apr_file_t errfile, svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_diff4(apr_array_header_t_diff_options, char_path1, svn_opt_revision_t_revision1, char_path2, svn_opt_revision_t_revision2, char_relative_to_dir, svn_depth_t_depth, svn_boolean_t_ignore_ancestry, svn_boolean_t_no_diff_deleted, svn_boolean_t_ignore_content_type, char_header_encoding, apr_file_t_outfile, apr_file_t_errfile, apr_array_header_t_changelists, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_diff4(apr_array_header_t diff_options, char path1, svn_opt_revision_t revision1, 
        char path2, svn_opt_revision_t revision2, 
        char relative_to_dir, svn_depth_t depth, 
        svn_boolean_t ignore_ancestry, 
        svn_boolean_t no_diff_deleted, svn_boolean_t ignore_content_type, 
        char header_encoding, 
        apr_file_t outfile, apr_file_t errfile, apr_array_header_t changelists, 
        svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_diff_peg(apr_array_header_t_diff_options, char_path, svn_opt_revision_t_peg_revision, svn_opt_revision_t_start_revision, svn_opt_revision_t_end_revision, svn_boolean_t_recurse, svn_boolean_t_ignore_ancestry, svn_boolean_t_no_diff_deleted, apr_file_t_outfile, apr_file_t_errfile, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_diff_peg(apr_array_header_t diff_options, char path, svn_opt_revision_t peg_revision, 
        svn_opt_revision_t start_revision, 
        svn_opt_revision_t end_revision, 
        svn_boolean_t recurse, svn_boolean_t ignore_ancestry, 
        svn_boolean_t no_diff_deleted, apr_file_t outfile, 
        apr_file_t errfile, svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_diff_peg2(apr_array_header_t_diff_options, char_path, svn_opt_revision_t_peg_revision, svn_opt_revision_t_start_revision, svn_opt_revision_t_end_revision, svn_boolean_t_recurse, svn_boolean_t_ignore_ancestry, svn_boolean_t_no_diff_deleted, svn_boolean_t_ignore_content_type, apr_file_t_outfile, apr_file_t_errfile, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_diff_peg2(apr_array_header_t diff_options, char path, svn_opt_revision_t peg_revision, 
        svn_opt_revision_t start_revision, 
        svn_opt_revision_t end_revision, 
        svn_boolean_t recurse, svn_boolean_t ignore_ancestry, 
        svn_boolean_t no_diff_deleted, svn_boolean_t ignore_content_type, 
        apr_file_t outfile, 
        apr_file_t errfile, svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_diff_peg3(apr_array_header_t_diff_options, char_path, svn_opt_revision_t_peg_revision, svn_opt_revision_t_start_revision, svn_opt_revision_t_end_revision, svn_boolean_t_recurse, svn_boolean_t_ignore_ancestry, svn_boolean_t_no_diff_deleted, svn_boolean_t_ignore_content_type, char_header_encoding, apr_file_t_outfile, apr_file_t_errfile, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_diff_peg3(apr_array_header_t diff_options, char path, svn_opt_revision_t peg_revision, 
        svn_opt_revision_t start_revision, 
        svn_opt_revision_t end_revision, 
        svn_boolean_t recurse, svn_boolean_t ignore_ancestry, 
        svn_boolean_t no_diff_deleted, svn_boolean_t ignore_content_type, 
        char header_encoding, 
        apr_file_t outfile, apr_file_t errfile, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_diff_peg4(apr_array_header_t_diff_options, char_path, svn_opt_revision_t_peg_revision, svn_opt_revision_t_start_revision, svn_opt_revision_t_end_revision, char_relative_to_dir, svn_depth_t_depth, svn_boolean_t_ignore_ancestry, svn_boolean_t_no_diff_deleted, svn_boolean_t_ignore_content_type, char_header_encoding, apr_file_t_outfile, apr_file_t_errfile, apr_array_header_t_changelists, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_diff_peg4(apr_array_header_t diff_options, char path, svn_opt_revision_t peg_revision, 
        svn_opt_revision_t start_revision, 
        svn_opt_revision_t end_revision, 
        char relative_to_dir, svn_depth_t depth, 
        svn_boolean_t ignore_ancestry, svn_boolean_t no_diff_deleted, 
        svn_boolean_t ignore_content_type, 
        char header_encoding, apr_file_t outfile, 
        apr_file_t errfile, apr_array_header_t changelists, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_diff_summarize(char_path1, svn_opt_revision_t_revision1, char_path2, svn_opt_revision_t_revision2, svn_boolean_t_recurse, svn_boolean_t_ignore_ancestry, svn_client_diff_summarize_func_t_summarize_func, void_summarize_baton, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_diff_summarize(char path1, svn_opt_revision_t revision1, char path2, 
        svn_opt_revision_t revision2, svn_boolean_t recurse, 
        svn_boolean_t ignore_ancestry, svn_client_diff_summarize_func_t summarize_func, 
        void summarize_baton, 
        svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_diff_summarize2(char_path1, svn_opt_revision_t_revision1, char_path2, svn_opt_revision_t_revision2, svn_depth_t_depth, svn_boolean_t_ignore_ancestry, apr_array_header_t_changelists, svn_client_diff_summarize_func_t_summarize_func, void_summarize_baton, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_diff_summarize2(char path1, svn_opt_revision_t revision1, char path2, 
        svn_opt_revision_t revision2, svn_depth_t depth, 
        svn_boolean_t ignore_ancestry, apr_array_header_t changelists, 
        svn_client_diff_summarize_func_t summarize_func, 
        void summarize_baton, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_diff_summarize_dup(svn_client_diff_summarize_t_diff, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_client_diff_summarize_dup(svn_client_diff_summarize_t diff, apr_pool_t pool) -> svn_client_diff_summarize_t """
    pass

def svn_client_diff_summarize_func_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def svn_client_diff_summarize_peg(char_path, svn_opt_revision_t_peg_revision, svn_opt_revision_t_start_revision, svn_opt_revision_t_end_revision, svn_boolean_t_recurse, svn_boolean_t_ignore_ancestry, svn_client_diff_summarize_func_t_summarize_func, void_summarize_baton, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_diff_summarize_peg(char path, svn_opt_revision_t peg_revision, svn_opt_revision_t start_revision, 
        svn_opt_revision_t end_revision, 
        svn_boolean_t recurse, svn_boolean_t ignore_ancestry, 
        svn_client_diff_summarize_func_t summarize_func, 
        void summarize_baton, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_diff_summarize_peg2(char_path, svn_opt_revision_t_peg_revision, svn_opt_revision_t_start_revision, svn_opt_revision_t_end_revision, svn_depth_t_depth, svn_boolean_t_ignore_ancestry, apr_array_header_t_changelists, svn_client_diff_summarize_func_t_summarize_func, void_summarize_baton, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_diff_summarize_peg2(char path, svn_opt_revision_t peg_revision, svn_opt_revision_t start_revision, 
        svn_opt_revision_t end_revision, 
        svn_depth_t depth, svn_boolean_t ignore_ancestry, 
        apr_array_header_t changelists, 
        svn_client_diff_summarize_func_t summarize_func, 
        void summarize_baton, svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_diff_summarize_t_node_kind_get(svn_client_diff_summarize_t_self): # real signature unknown; restored from __doc__
    """ svn_client_diff_summarize_t_node_kind_get(svn_client_diff_summarize_t self) -> svn_node_kind_t """
    pass

def svn_client_diff_summarize_t_node_kind_set(svn_client_diff_summarize_t_self, svn_node_kind_t_node_kind): # real signature unknown; restored from __doc__
    """ svn_client_diff_summarize_t_node_kind_set(svn_client_diff_summarize_t self, svn_node_kind_t node_kind) """
    pass

def svn_client_diff_summarize_t_path_get(svn_client_diff_summarize_t_self): # real signature unknown; restored from __doc__
    """ svn_client_diff_summarize_t_path_get(svn_client_diff_summarize_t self) -> char """
    return ""

def svn_client_diff_summarize_t_path_set(svn_client_diff_summarize_t_self, char_path): # real signature unknown; restored from __doc__
    """ svn_client_diff_summarize_t_path_set(svn_client_diff_summarize_t self, char path) """
    pass

def svn_client_diff_summarize_t_prop_changed_get(svn_client_diff_summarize_t_self): # real signature unknown; restored from __doc__
    """ svn_client_diff_summarize_t_prop_changed_get(svn_client_diff_summarize_t self) -> svn_boolean_t """
    pass

def svn_client_diff_summarize_t_prop_changed_set(svn_client_diff_summarize_t_self, svn_boolean_t_prop_changed): # real signature unknown; restored from __doc__
    """ svn_client_diff_summarize_t_prop_changed_set(svn_client_diff_summarize_t self, svn_boolean_t prop_changed) """
    pass

def svn_client_diff_summarize_t_summarize_kind_get(svn_client_diff_summarize_t_self): # real signature unknown; restored from __doc__
    """ svn_client_diff_summarize_t_summarize_kind_get(svn_client_diff_summarize_t self) -> svn_client_diff_summarize_kind_t """
    pass

def svn_client_diff_summarize_t_summarize_kind_set(svn_client_diff_summarize_t_self, svn_client_diff_summarize_kind_t_summarize_kind): # real signature unknown; restored from __doc__
    """ svn_client_diff_summarize_t_summarize_kind_set(svn_client_diff_summarize_t self, svn_client_diff_summarize_kind_t summarize_kind) """
    pass

def svn_client_diff_summarize_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def svn_client_export(svn_revnum_t_result_rev, char_from, char_to, svn_opt_revision_t_revision, svn_boolean_t_force, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_export(svn_revnum_t result_rev, char from, char to, svn_opt_revision_t revision, 
        svn_boolean_t force, svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_export2(svn_revnum_t_result_rev, char_from, char_to, svn_opt_revision_t_revision, svn_boolean_t_force, char_native_eol, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_export2(svn_revnum_t result_rev, char from, char to, svn_opt_revision_t revision, 
        svn_boolean_t force, char native_eol, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_export3(svn_revnum_t_result_rev, char_from, char_to, svn_opt_revision_t_peg_revision, svn_opt_revision_t_revision, svn_boolean_t_overwrite, svn_boolean_t_ignore_externals, svn_boolean_t_recurse, char_native_eol, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_export3(svn_revnum_t result_rev, char from, char to, svn_opt_revision_t peg_revision, 
        svn_opt_revision_t revision, 
        svn_boolean_t overwrite, svn_boolean_t ignore_externals, 
        svn_boolean_t recurse, 
        char native_eol, svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_export4(svn_revnum_t_result_rev, char_from, char_to, svn_opt_revision_t_peg_revision, svn_opt_revision_t_revision, svn_boolean_t_overwrite, svn_boolean_t_ignore_externals, svn_depth_t_depth, char_native_eol, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_export4(svn_revnum_t result_rev, char from, char to, svn_opt_revision_t peg_revision, 
        svn_opt_revision_t revision, 
        svn_boolean_t overwrite, svn_boolean_t ignore_externals, 
        svn_depth_t depth, char native_eol, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_get_changelists(char_path, apr_array_header_t_changelists, svn_depth_t_depth, svn_changelist_receiver_t_callback_func, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_get_changelists(char path, apr_array_header_t changelists, svn_depth_t depth, 
        svn_changelist_receiver_t callback_func, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_get_commit_log2_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def svn_client_get_commit_log3_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def svn_client_get_commit_log_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def svn_client_get_simple_prompt_provider(svn_auth_provider_object_t_provider, svn_auth_simple_prompt_func_t_prompt_func, int_retry_limit, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_get_simple_prompt_provider(svn_auth_provider_object_t provider, svn_auth_simple_prompt_func_t prompt_func, 
        int retry_limit, 
        apr_pool_t pool)
    """
    pass

def svn_client_get_simple_provider(svn_auth_provider_object_t_provider, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_client_get_simple_provider(svn_auth_provider_object_t provider, apr_pool_t pool) """
    pass

def svn_client_get_ssl_client_cert_file_provider(svn_auth_provider_object_t_provider, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_client_get_ssl_client_cert_file_provider(svn_auth_provider_object_t provider, apr_pool_t pool) """
    pass

def svn_client_get_ssl_client_cert_prompt_provider(svn_auth_provider_object_t_provider, svn_auth_ssl_client_cert_prompt_func_t_prompt_func, int_retry_limit, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_get_ssl_client_cert_prompt_provider(svn_auth_provider_object_t provider, svn_auth_ssl_client_cert_prompt_func_t prompt_func, 
        int retry_limit, 
        apr_pool_t pool)
    """
    pass

def svn_client_get_ssl_client_cert_pw_file_provider(svn_auth_provider_object_t_provider, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_client_get_ssl_client_cert_pw_file_provider(svn_auth_provider_object_t provider, apr_pool_t pool) """
    pass

def svn_client_get_ssl_client_cert_pw_prompt_provider(svn_auth_provider_object_t_provider, svn_auth_ssl_client_cert_pw_prompt_func_t_prompt_func, int_retry_limit, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_get_ssl_client_cert_pw_prompt_provider(svn_auth_provider_object_t provider, svn_auth_ssl_client_cert_pw_prompt_func_t prompt_func, 
        int retry_limit, 
        apr_pool_t pool)
    """
    pass

def svn_client_get_ssl_server_trust_file_provider(svn_auth_provider_object_t_provider, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_client_get_ssl_server_trust_file_provider(svn_auth_provider_object_t provider, apr_pool_t pool) """
    pass

def svn_client_get_ssl_server_trust_prompt_provider(svn_auth_provider_object_t_provider, svn_auth_ssl_server_trust_prompt_func_t_prompt_func, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_get_ssl_server_trust_prompt_provider(svn_auth_provider_object_t provider, svn_auth_ssl_server_trust_prompt_func_t prompt_func, 
        apr_pool_t pool)
    """
    pass

def svn_client_get_username_prompt_provider(svn_auth_provider_object_t_provider, svn_auth_username_prompt_func_t_prompt_func, int_retry_limit, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_get_username_prompt_provider(svn_auth_provider_object_t provider, svn_auth_username_prompt_func_t prompt_func, 
        int retry_limit, 
        apr_pool_t pool)
    """
    pass

def svn_client_get_username_provider(svn_auth_provider_object_t_provider, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_client_get_username_provider(svn_auth_provider_object_t provider, apr_pool_t pool) """
    pass

def svn_client_import(svn_client_commit_info_t_commit_info_p, char_path, char_url, svn_boolean_t_nonrecursive, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_import(svn_client_commit_info_t commit_info_p, char path, 
        char url, svn_boolean_t nonrecursive, svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_import2(svn_commit_info_t_commit_info_p, char_path, char_url, svn_boolean_t_nonrecursive, svn_boolean_t_no_ignore, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_import2(svn_commit_info_t commit_info_p, char path, char url, 
        svn_boolean_t nonrecursive, svn_boolean_t no_ignore, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_import3(svn_commit_info_t_commit_info_p, char_path, char_url, svn_depth_t_depth, svn_boolean_t_no_ignore, svn_boolean_t_ignore_unknown_node_types, apr_hash_t_revprop_table, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_import3(svn_commit_info_t commit_info_p, char path, char url, 
        svn_depth_t depth, svn_boolean_t no_ignore, 
        svn_boolean_t ignore_unknown_node_types, apr_hash_t revprop_table, 
        svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_info(char_path_or_url, svn_opt_revision_t_peg_revision, svn_opt_revision_t_revision, svn_info_receiver_t_receiver, svn_boolean_t_recurse, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_info(char path_or_url, svn_opt_revision_t peg_revision, 
        svn_opt_revision_t revision, svn_info_receiver_t receiver, 
        svn_boolean_t recurse, svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_info2(char_path_or_url, svn_opt_revision_t_peg_revision, svn_opt_revision_t_revision, svn_info_receiver_t_receiver, svn_depth_t_depth, apr_array_header_t_changelists, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_info2(char path_or_url, svn_opt_revision_t peg_revision, 
        svn_opt_revision_t revision, svn_info_receiver_t receiver, 
        svn_depth_t depth, apr_array_header_t changelists, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_invoke_blame_receiver(svn_client_blame_receiver_t__obj, void_baton, apr_int64_t_line_no, svn_revnum_t_revision, char_author, char_date, char_line, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_invoke_blame_receiver(svn_client_blame_receiver_t _obj, void baton, apr_int64_t line_no, 
        svn_revnum_t revision, char author, 
        char date, char line, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_invoke_blame_receiver2(svn_client_blame_receiver2_t__obj, void_baton, apr_int64_t_line_no, svn_revnum_t_revision, char_author, char_date, svn_revnum_t_merged_revision, char_merged_author, char_merged_date, char_merged_path, char_line, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_invoke_blame_receiver2(svn_client_blame_receiver2_t _obj, void baton, apr_int64_t line_no, 
        svn_revnum_t revision, char author, 
        char date, svn_revnum_t merged_revision, 
        char merged_author, char merged_date, char merged_path, 
        char line, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_invoke_diff_summarize_func(svn_client_diff_summarize_func_t__obj, svn_client_diff_summarize_t_diff, void_baton, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_invoke_diff_summarize_func(svn_client_diff_summarize_func_t _obj, svn_client_diff_summarize_t diff, 
        void baton, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_invoke_get_commit_log(svn_client_get_commit_log_t__obj, char_log_msg, char_tmp_file, apr_array_header_t_commit_items, void_baton, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_invoke_get_commit_log(svn_client_get_commit_log_t _obj, char log_msg, char tmp_file, 
        apr_array_header_t commit_items, 
        void baton, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_invoke_get_commit_log2(svn_client_get_commit_log2_t__obj, char_log_msg, char_tmp_file, apr_array_header_t_commit_items, void_baton, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_invoke_get_commit_log2(svn_client_get_commit_log2_t _obj, char log_msg, char tmp_file, 
        apr_array_header_t commit_items, 
        void baton, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_invoke_get_commit_log3(svn_client_get_commit_log3_t__obj, char_log_msg, char_tmp_file, apr_array_header_t_commit_items, void_baton, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_invoke_get_commit_log3(svn_client_get_commit_log3_t _obj, char log_msg, char tmp_file, 
        apr_array_header_t commit_items, 
        void baton, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_invoke_list_func(svn_client_list_func_t__obj, void_baton, char_path, svn_dirent_t_dirent, svn_lock_t_lock, char_abs_path, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_invoke_list_func(svn_client_list_func_t _obj, void baton, char path, 
        svn_dirent_t dirent, svn_lock_t lock, char abs_path, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_list(char_path_or_url, svn_opt_revision_t_peg_revision, svn_opt_revision_t_revision, svn_boolean_t_recurse, apr_uint32_t_dirent_fields, svn_boolean_t_fetch_locks, svn_client_list_func_t_list_func, void_baton, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_list(char path_or_url, svn_opt_revision_t peg_revision, 
        svn_opt_revision_t revision, svn_boolean_t recurse, 
        apr_uint32_t dirent_fields, svn_boolean_t fetch_locks, 
        svn_client_list_func_t list_func, 
        void baton, svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_list2(char_path_or_url, svn_opt_revision_t_peg_revision, svn_opt_revision_t_revision, svn_depth_t_depth, apr_uint32_t_dirent_fields, svn_boolean_t_fetch_locks, svn_client_list_func_t_list_func, void_baton, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_list2(char path_or_url, svn_opt_revision_t peg_revision, 
        svn_opt_revision_t revision, svn_depth_t depth, 
        apr_uint32_t dirent_fields, svn_boolean_t fetch_locks, 
        svn_client_list_func_t list_func, 
        void baton, svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_list_func_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def svn_client_lock(apr_array_header_t_targets, char_comment, svn_boolean_t_steal_lock, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_lock(apr_array_header_t targets, char comment, svn_boolean_t steal_lock, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_log(apr_array_header_t_targets, svn_opt_revision_t_start, svn_opt_revision_t_end, svn_boolean_t_discover_changed_paths, svn_boolean_t_strict_node_history, svn_log_message_receiver_t_receiver, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_log(apr_array_header_t targets, svn_opt_revision_t start, 
        svn_opt_revision_t end, svn_boolean_t discover_changed_paths, 
        svn_boolean_t strict_node_history, 
        svn_log_message_receiver_t receiver, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_log2(apr_array_header_t_targets, svn_opt_revision_t_start, svn_opt_revision_t_end, int_limit, svn_boolean_t_discover_changed_paths, svn_boolean_t_strict_node_history, svn_log_message_receiver_t_receiver, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_log2(apr_array_header_t targets, svn_opt_revision_t start, 
        svn_opt_revision_t end, int limit, svn_boolean_t discover_changed_paths, 
        svn_boolean_t strict_node_history, 
        svn_log_message_receiver_t receiver, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_log3(apr_array_header_t_targets, svn_opt_revision_t_peg_revision, svn_opt_revision_t_start, svn_opt_revision_t_end, int_limit, svn_boolean_t_discover_changed_paths, svn_boolean_t_strict_node_history, svn_log_message_receiver_t_receiver, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_log3(apr_array_header_t targets, svn_opt_revision_t peg_revision, 
        svn_opt_revision_t start, svn_opt_revision_t end, 
        int limit, svn_boolean_t discover_changed_paths, 
        svn_boolean_t strict_node_history, 
        svn_log_message_receiver_t receiver, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_log4(apr_array_header_t_targets, svn_opt_revision_t_peg_revision, svn_opt_revision_t_start, svn_opt_revision_t_end, int_limit, svn_boolean_t_discover_changed_paths, svn_boolean_t_strict_node_history, svn_boolean_t_include_merged_revisions, apr_array_header_t_revprops, svn_log_entry_receiver_t_receiver, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_log4(apr_array_header_t targets, svn_opt_revision_t peg_revision, 
        svn_opt_revision_t start, svn_opt_revision_t end, 
        int limit, svn_boolean_t discover_changed_paths, 
        svn_boolean_t strict_node_history, 
        svn_boolean_t include_merged_revisions, 
        apr_array_header_t revprops, svn_log_entry_receiver_t receiver, 
        svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_log5(apr_array_header_t_targets, svn_opt_revision_t_peg_revision, apr_array_header_t_revision_ranges, int_limit, svn_boolean_t_discover_changed_paths, svn_boolean_t_strict_node_history, svn_boolean_t_include_merged_revisions, apr_array_header_t_revprops, svn_log_entry_receiver_t_receiver, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_log5(apr_array_header_t targets, svn_opt_revision_t peg_revision, 
        apr_array_header_t revision_ranges, 
        int limit, svn_boolean_t discover_changed_paths, 
        svn_boolean_t strict_node_history, svn_boolean_t include_merged_revisions, 
        apr_array_header_t revprops, 
        svn_log_entry_receiver_t receiver, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_ls(apr_hash_t_dirents, char_path_or_url, svn_opt_revision_t_revision, svn_boolean_t_recurse, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_ls(apr_hash_t dirents, char path_or_url, svn_opt_revision_t revision, 
        svn_boolean_t recurse, svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_ls2(apr_hash_t_dirents, char_path_or_url, svn_opt_revision_t_peg_revision, svn_opt_revision_t_revision, svn_boolean_t_recurse, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_ls2(apr_hash_t dirents, char path_or_url, svn_opt_revision_t peg_revision, 
        svn_opt_revision_t revision, 
        svn_boolean_t recurse, svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_ls3(apr_hash_t_dirents, apr_hash_t_locks, char_path_or_url, svn_opt_revision_t_peg_revision, svn_opt_revision_t_revision, svn_boolean_t_recurse, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_ls3(apr_hash_t dirents, apr_hash_t locks, char path_or_url, 
        svn_opt_revision_t peg_revision, svn_opt_revision_t revision, 
        svn_boolean_t recurse, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_merge(char_source1, svn_opt_revision_t_revision1, char_source2, svn_opt_revision_t_revision2, char_target_wcpath, svn_boolean_t_recurse, svn_boolean_t_ignore_ancestry, svn_boolean_t_force, svn_boolean_t_dry_run, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_merge(char source1, svn_opt_revision_t revision1, char source2, 
        svn_opt_revision_t revision2, char target_wcpath, 
        svn_boolean_t recurse, svn_boolean_t ignore_ancestry, 
        svn_boolean_t force, svn_boolean_t dry_run, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_merge2(char_source1, svn_opt_revision_t_revision1, char_source2, svn_opt_revision_t_revision2, char_target_wcpath, svn_boolean_t_recurse, svn_boolean_t_ignore_ancestry, svn_boolean_t_force, svn_boolean_t_dry_run, apr_array_header_t_merge_options, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_merge2(char source1, svn_opt_revision_t revision1, char source2, 
        svn_opt_revision_t revision2, char target_wcpath, 
        svn_boolean_t recurse, svn_boolean_t ignore_ancestry, 
        svn_boolean_t force, svn_boolean_t dry_run, 
        apr_array_header_t merge_options, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_merge3(char_source1, svn_opt_revision_t_revision1, char_source2, svn_opt_revision_t_revision2, char_target_wcpath, svn_depth_t_depth, svn_boolean_t_ignore_ancestry, svn_boolean_t_force, svn_boolean_t_record_only, svn_boolean_t_dry_run, apr_array_header_t_merge_options, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_merge3(char source1, svn_opt_revision_t revision1, char source2, 
        svn_opt_revision_t revision2, char target_wcpath, 
        svn_depth_t depth, svn_boolean_t ignore_ancestry, 
        svn_boolean_t force, svn_boolean_t record_only, 
        svn_boolean_t dry_run, apr_array_header_t merge_options, 
        svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_mergeinfo_get_merged(apr_hash_t_mergeinfo, char_path_or_url, svn_opt_revision_t_peg_revision, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_mergeinfo_get_merged(apr_hash_t mergeinfo, char path_or_url, svn_opt_revision_t peg_revision, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_mergeinfo_log_eligible(char_path_or_url, svn_opt_revision_t_peg_revision, char_merge_source_path_or_url, svn_opt_revision_t_src_peg_revision, svn_log_entry_receiver_t_receiver, svn_boolean_t_discover_changed_paths, apr_array_header_t_revprops, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_mergeinfo_log_eligible(char path_or_url, svn_opt_revision_t peg_revision, 
        char merge_source_path_or_url, svn_opt_revision_t src_peg_revision, 
        svn_log_entry_receiver_t receiver, 
        svn_boolean_t discover_changed_paths, 
        apr_array_header_t revprops, svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_mergeinfo_log_merged(char_path_or_url, svn_opt_revision_t_peg_revision, char_merge_source_path_or_url, svn_opt_revision_t_src_peg_revision, svn_log_entry_receiver_t_receiver, svn_boolean_t_discover_changed_paths, apr_array_header_t_revprops, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_mergeinfo_log_merged(char path_or_url, svn_opt_revision_t peg_revision, 
        char merge_source_path_or_url, svn_opt_revision_t src_peg_revision, 
        svn_log_entry_receiver_t receiver, 
        svn_boolean_t discover_changed_paths, 
        apr_array_header_t revprops, svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_merge_peg(char_source, svn_opt_revision_t_revision1, svn_opt_revision_t_revision2, svn_opt_revision_t_peg_revision, char_target_wcpath, svn_boolean_t_recurse, svn_boolean_t_ignore_ancestry, svn_boolean_t_force, svn_boolean_t_dry_run, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_merge_peg(char source, svn_opt_revision_t revision1, svn_opt_revision_t revision2, 
        svn_opt_revision_t peg_revision, 
        char target_wcpath, svn_boolean_t recurse, 
        svn_boolean_t ignore_ancestry, svn_boolean_t force, 
        svn_boolean_t dry_run, svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_merge_peg2(char_source, svn_opt_revision_t_revision1, svn_opt_revision_t_revision2, svn_opt_revision_t_peg_revision, char_target_wcpath, svn_boolean_t_recurse, svn_boolean_t_ignore_ancestry, svn_boolean_t_force, svn_boolean_t_dry_run, apr_array_header_t_merge_options, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_merge_peg2(char source, svn_opt_revision_t revision1, svn_opt_revision_t revision2, 
        svn_opt_revision_t peg_revision, 
        char target_wcpath, svn_boolean_t recurse, 
        svn_boolean_t ignore_ancestry, svn_boolean_t force, 
        svn_boolean_t dry_run, apr_array_header_t merge_options, 
        svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_merge_peg3(char_source, apr_array_header_t_ranges_to_merge, svn_opt_revision_t_peg_revision, char_target_wcpath, svn_depth_t_depth, svn_boolean_t_ignore_ancestry, svn_boolean_t_force, svn_boolean_t_record_only, svn_boolean_t_dry_run, apr_array_header_t_merge_options, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_merge_peg3(char source, apr_array_header_t ranges_to_merge, svn_opt_revision_t peg_revision, 
        char target_wcpath, 
        svn_depth_t depth, svn_boolean_t ignore_ancestry, 
        svn_boolean_t force, svn_boolean_t record_only, 
        svn_boolean_t dry_run, apr_array_header_t merge_options, 
        svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_merge_reintegrate(char_source, svn_opt_revision_t_peg_revision, char_target_wcpath, svn_boolean_t_dry_run, apr_array_header_t_merge_options, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_merge_reintegrate(char source, svn_opt_revision_t peg_revision, char target_wcpath, 
        svn_boolean_t dry_run, apr_array_header_t merge_options, 
        svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_mkdir(svn_client_commit_info_t_commit_info_p, apr_array_header_t_paths, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_mkdir(svn_client_commit_info_t commit_info_p, apr_array_header_t paths, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_mkdir2(svn_commit_info_t_commit_info_p, apr_array_header_t_paths, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_mkdir2(svn_commit_info_t commit_info_p, apr_array_header_t paths, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_mkdir3(svn_commit_info_t_commit_info_p, apr_array_header_t_paths, svn_boolean_t_make_parents, apr_hash_t_revprop_table, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_mkdir3(svn_commit_info_t commit_info_p, apr_array_header_t paths, 
        svn_boolean_t make_parents, apr_hash_t revprop_table, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_move(svn_client_commit_info_t_commit_info_p, char_src_path, svn_opt_revision_t_src_revision, char_dst_path, svn_boolean_t_force, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_move(svn_client_commit_info_t commit_info_p, char src_path, 
        svn_opt_revision_t src_revision, char dst_path, 
        svn_boolean_t force, svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_move2(svn_client_commit_info_t_commit_info_p, char_src_path, char_dst_path, svn_boolean_t_force, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_move2(svn_client_commit_info_t commit_info_p, char src_path, 
        char dst_path, svn_boolean_t force, svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_move3(svn_commit_info_t_commit_info_p, char_src_path, char_dst_path, svn_boolean_t_force, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_move3(svn_commit_info_t commit_info_p, char src_path, char dst_path, 
        svn_boolean_t force, svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_move4(svn_commit_info_t_commit_info_p, char_src_path, char_dst_path, svn_boolean_t_force, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_move4(svn_commit_info_t commit_info_p, char src_path, char dst_path, 
        svn_boolean_t force, svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_move5(svn_commit_info_t_commit_info_p, apr_array_header_t_src_paths, char_dst_path, svn_boolean_t_force, svn_boolean_t_move_as_child, svn_boolean_t_make_parents, apr_hash_t_revprop_table, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_move5(svn_commit_info_t commit_info_p, apr_array_header_t src_paths, 
        char dst_path, svn_boolean_t force, 
        svn_boolean_t move_as_child, svn_boolean_t make_parents, 
        apr_hash_t revprop_table, svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_open_ra_session(svn_ra_session_t_session, char_url, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_open_ra_session(svn_ra_session_t session, char url, svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_propget(apr_hash_t_props, char_propname, char_target, svn_opt_revision_t_revision, svn_boolean_t_recurse, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_propget(apr_hash_t props, char propname, char target, svn_opt_revision_t revision, 
        svn_boolean_t recurse, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_propget2(apr_hash_t_props, char_propname, char_target, svn_opt_revision_t_peg_revision, svn_opt_revision_t_revision, svn_boolean_t_recurse, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_propget2(apr_hash_t props, char propname, char target, svn_opt_revision_t peg_revision, 
        svn_opt_revision_t revision, 
        svn_boolean_t recurse, svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_propget3(apr_hash_t_props, char_propname, char_target, svn_opt_revision_t_peg_revision, svn_opt_revision_t_revision, svn_revnum_t_actual_revnum, svn_depth_t_depth, apr_array_header_t_changelists, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_propget3(apr_hash_t props, char propname, char target, svn_opt_revision_t peg_revision, 
        svn_opt_revision_t revision, 
        svn_revnum_t actual_revnum, svn_depth_t depth, 
        apr_array_header_t changelists, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_proplist(apr_array_header_t_props, char_target, svn_opt_revision_t_revision, svn_boolean_t_recurse, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_proplist(apr_array_header_t props, char target, svn_opt_revision_t revision, 
        svn_boolean_t recurse, svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_proplist2(apr_array_header_t_props, char_target, svn_opt_revision_t_peg_revision, svn_opt_revision_t_revision, svn_boolean_t_recurse, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_proplist2(apr_array_header_t props, char target, svn_opt_revision_t peg_revision, 
        svn_opt_revision_t revision, 
        svn_boolean_t recurse, svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_proplist3(char_target, svn_opt_revision_t_peg_revision, svn_opt_revision_t_revision, svn_depth_t_depth, apr_array_header_t_changelists, svn_proplist_receiver_t_receiver, void_receiver_baton, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_proplist3(char target, svn_opt_revision_t peg_revision, svn_opt_revision_t revision, 
        svn_depth_t depth, apr_array_header_t changelists, 
        svn_proplist_receiver_t receiver, 
        void receiver_baton, svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_proplist_item_dup(item, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_client_proplist_item_dup( item, apr_pool_t pool) """
    pass

def svn_client_propset(char_propname, svn_string_t_propval, char_target, svn_boolean_t_recurse, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_propset(char propname, svn_string_t propval, char target, svn_boolean_t recurse, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_propset2(char_propname, svn_string_t_propval, char_target, svn_boolean_t_recurse, svn_boolean_t_skip_checks, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_propset2(char propname, svn_string_t propval, char target, svn_boolean_t recurse, 
        svn_boolean_t skip_checks, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_propset3(svn_commit_info_t_commit_info_p, char_propname, svn_string_t_propval, char_target, svn_depth_t_depth, svn_boolean_t_skip_checks, svn_revnum_t_base_revision_for_url, apr_array_header_t_changelists, apr_hash_t_revprop_table, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_propset3(svn_commit_info_t commit_info_p, char propname, svn_string_t propval, 
        char target, svn_depth_t depth, 
        svn_boolean_t skip_checks, svn_revnum_t base_revision_for_url, 
        apr_array_header_t changelists, 
        apr_hash_t revprop_table, svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_relocate(char_dir, char_from, char_to, svn_boolean_t_recurse, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_relocate(char dir, char from, char to, svn_boolean_t recurse, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_remove_from_changelists(apr_array_header_t_paths, svn_depth_t_depth, apr_array_header_t_changelists, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_remove_from_changelists(apr_array_header_t paths, svn_depth_t depth, apr_array_header_t changelists, 
        svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_resolve(char_path, svn_depth_t_depth, svn_wc_conflict_choice_t_conflict_choice, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_resolve(char path, svn_depth_t depth, svn_wc_conflict_choice_t conflict_choice, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_resolved(char_path, svn_boolean_t_recursive, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_resolved(char path, svn_boolean_t recursive, svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_revert(apr_array_header_t_paths, svn_boolean_t_recursive, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_revert(apr_array_header_t paths, svn_boolean_t recursive, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_revert2(apr_array_header_t_paths, svn_depth_t_depth, apr_array_header_t_changelists, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_revert2(apr_array_header_t paths, svn_depth_t depth, apr_array_header_t changelists, 
        svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_revprop_get(char_propname, svn_string_t_propval, char_URL, svn_opt_revision_t_revision, svn_revnum_t_set_rev, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_revprop_get(char propname, svn_string_t propval, char URL, svn_opt_revision_t revision, 
        svn_revnum_t set_rev, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_revprop_list(apr_hash_t_props, char_URL, svn_opt_revision_t_revision, svn_revnum_t_set_rev, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_revprop_list(apr_hash_t props, char URL, svn_opt_revision_t revision, 
        svn_revnum_t set_rev, svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_revprop_set(char_propname, svn_string_t_propval, char_URL, svn_opt_revision_t_revision, svn_revnum_t_set_rev, svn_boolean_t_force, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_revprop_set(char propname, svn_string_t propval, char URL, svn_opt_revision_t revision, 
        svn_revnum_t set_rev, 
        svn_boolean_t force, svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_revprop_set2(char_propname, svn_string_t_propval, svn_string_t_original_propval, char_URL, svn_opt_revision_t_revision, svn_revnum_t_set_rev, svn_boolean_t_force, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_revprop_set2(char propname, svn_string_t propval, svn_string_t original_propval, 
        char URL, svn_opt_revision_t revision, 
        svn_revnum_t set_rev, svn_boolean_t force, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_root_url_from_path(char_url, char_path_or_url, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_client_root_url_from_path(char url, char path_or_url, svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t """
    pass

def svn_client_status(svn_revnum_t_result_rev, char_path, svn_opt_revision_t_revision, svn_wc_status_func_t_status_func, svn_boolean_t_recurse, svn_boolean_t_get_all, svn_boolean_t_update, svn_boolean_t_no_ignore, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_status(svn_revnum_t result_rev, char path, svn_opt_revision_t revision, 
        svn_wc_status_func_t status_func, 
        svn_boolean_t recurse, svn_boolean_t get_all, 
        svn_boolean_t update, svn_boolean_t no_ignore, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_status2(svn_revnum_t_result_rev, char_path, svn_opt_revision_t_revision, svn_wc_status_func2_t_status_func, svn_boolean_t_recurse, svn_boolean_t_get_all, svn_boolean_t_update, svn_boolean_t_no_ignore, svn_boolean_t_ignore_externals, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_status2(svn_revnum_t result_rev, char path, svn_opt_revision_t revision, 
        svn_wc_status_func2_t status_func, 
        svn_boolean_t recurse, svn_boolean_t get_all, 
        svn_boolean_t update, svn_boolean_t no_ignore, 
        svn_boolean_t ignore_externals, svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_status3(svn_revnum_t_result_rev, char_path, svn_opt_revision_t_revision, svn_wc_status_func2_t_status_func, svn_depth_t_depth, svn_boolean_t_get_all, svn_boolean_t_update, svn_boolean_t_no_ignore, svn_boolean_t_ignore_externals, apr_array_header_t_changelists, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_status3(svn_revnum_t result_rev, char path, svn_opt_revision_t revision, 
        svn_wc_status_func2_t status_func, 
        svn_depth_t depth, svn_boolean_t get_all, 
        svn_boolean_t update, svn_boolean_t no_ignore, 
        svn_boolean_t ignore_externals, apr_array_header_t changelists, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_status4(svn_revnum_t_result_rev, char_path, svn_opt_revision_t_revision, svn_wc_status_func3_t_status_func, void_status_baton, svn_depth_t_depth, svn_boolean_t_get_all, svn_boolean_t_update, svn_boolean_t_no_ignore, svn_boolean_t_ignore_externals, apr_array_header_t_changelists, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_status4(svn_revnum_t result_rev, char path, svn_opt_revision_t revision, 
        svn_wc_status_func3_t status_func, 
        void status_baton, svn_depth_t depth, svn_boolean_t get_all, 
        svn_boolean_t update, svn_boolean_t no_ignore, 
        svn_boolean_t ignore_externals, 
        apr_array_header_t changelists, svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_suggest_merge_sources(apr_array_header_t_suggestions, char_path_or_url, svn_opt_revision_t_peg_revision, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_suggest_merge_sources(apr_array_header_t suggestions, char path_or_url, svn_opt_revision_t peg_revision, 
        svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_switch(svn_revnum_t_result_rev, char_path, char_url, svn_opt_revision_t_revision, svn_boolean_t_recurse, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_switch(svn_revnum_t result_rev, char path, char url, svn_opt_revision_t revision, 
        svn_boolean_t recurse, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_switch2(svn_revnum_t_result_rev, char_path, char_url, svn_opt_revision_t_peg_revision, svn_opt_revision_t_revision, svn_depth_t_depth, svn_boolean_t_depth_is_sticky, svn_boolean_t_ignore_externals, svn_boolean_t_allow_unver_obstructions, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_switch2(svn_revnum_t result_rev, char path, char url, svn_opt_revision_t peg_revision, 
        svn_opt_revision_t revision, 
        svn_depth_t depth, svn_boolean_t depth_is_sticky, 
        svn_boolean_t ignore_externals, 
        svn_boolean_t allow_unver_obstructions, svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_unlock(apr_array_header_t_targets, svn_boolean_t_break_lock, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_unlock(apr_array_header_t targets, svn_boolean_t break_lock, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_update(svn_revnum_t_result_rev, char_path, svn_opt_revision_t_revision, svn_boolean_t_recurse, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_update(svn_revnum_t result_rev, char path, svn_opt_revision_t revision, 
        svn_boolean_t recurse, svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_update2(apr_array_header_t_result_revs, apr_array_header_t_paths, svn_opt_revision_t_revision, svn_boolean_t_recurse, svn_boolean_t_ignore_externals, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_update2(apr_array_header_t result_revs, apr_array_header_t paths, 
        svn_opt_revision_t revision, svn_boolean_t recurse, 
        svn_boolean_t ignore_externals, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_update3(apr_array_header_t_result_revs, apr_array_header_t_paths, svn_opt_revision_t_revision, svn_depth_t_depth, svn_boolean_t_depth_is_sticky, svn_boolean_t_ignore_externals, svn_boolean_t_allow_unver_obstructions, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_update3(apr_array_header_t result_revs, apr_array_header_t paths, 
        svn_opt_revision_t revision, svn_depth_t depth, 
        svn_boolean_t depth_is_sticky, svn_boolean_t ignore_externals, 
        svn_boolean_t allow_unver_obstructions, 
        svn_client_ctx_t ctx, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_url_from_path(char_url, char_path_or_url, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_client_url_from_path(char url, char path_or_url, apr_pool_t pool) -> svn_error_t """
    pass

def svn_client_uuid_from_path(char_uuid, char_path, svn_wc_adm_access_t_adm_access, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_client_uuid_from_path(char uuid, char path, svn_wc_adm_access_t adm_access, 
        svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_client_uuid_from_url(char_uuid, char_url, svn_client_ctx_t_ctx, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_client_uuid_from_url(char uuid, char url, svn_client_ctx_t ctx, apr_pool_t pool) -> svn_error_t """
    pass

def svn_client_version(): # real signature unknown; restored from __doc__
    """ svn_client_version() -> svn_version_t """
    pass

def svn_info_dup(svn_info_t_info, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_info_dup(svn_info_t info, apr_pool_t pool) -> svn_info_t """
    pass

def svn_info_invoke_receiver(svn_info_receiver_t__obj, void_baton, char_path, svn_info_t_info, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_info_invoke_receiver(svn_info_receiver_t _obj, void baton, char path, svn_info_t info, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_info_receiver_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def svn_info_t_changelist_get(svn_info_t_self): # real signature unknown; restored from __doc__
    """ svn_info_t_changelist_get(svn_info_t self) -> char """
    return ""

def svn_info_t_changelist_set(svn_info_t_self, char_changelist): # real signature unknown; restored from __doc__
    """ svn_info_t_changelist_set(svn_info_t self, char changelist) """
    pass

def svn_info_t_checksum_get(svn_info_t_self): # real signature unknown; restored from __doc__
    """ svn_info_t_checksum_get(svn_info_t self) -> char """
    return ""

def svn_info_t_checksum_set(svn_info_t_self, char_checksum): # real signature unknown; restored from __doc__
    """ svn_info_t_checksum_set(svn_info_t self, char checksum) """
    pass

def svn_info_t_conflict_new_get(svn_info_t_self): # real signature unknown; restored from __doc__
    """ svn_info_t_conflict_new_get(svn_info_t self) -> char """
    return ""

def svn_info_t_conflict_new_set(svn_info_t_self, char_conflict_new): # real signature unknown; restored from __doc__
    """ svn_info_t_conflict_new_set(svn_info_t self, char conflict_new) """
    pass

def svn_info_t_conflict_old_get(svn_info_t_self): # real signature unknown; restored from __doc__
    """ svn_info_t_conflict_old_get(svn_info_t self) -> char """
    return ""

def svn_info_t_conflict_old_set(svn_info_t_self, char_conflict_old): # real signature unknown; restored from __doc__
    """ svn_info_t_conflict_old_set(svn_info_t self, char conflict_old) """
    pass

def svn_info_t_conflict_wrk_get(svn_info_t_self): # real signature unknown; restored from __doc__
    """ svn_info_t_conflict_wrk_get(svn_info_t self) -> char """
    return ""

def svn_info_t_conflict_wrk_set(svn_info_t_self, char_conflict_wrk): # real signature unknown; restored from __doc__
    """ svn_info_t_conflict_wrk_set(svn_info_t self, char conflict_wrk) """
    pass

def svn_info_t_copyfrom_rev_get(svn_info_t_self): # real signature unknown; restored from __doc__
    """ svn_info_t_copyfrom_rev_get(svn_info_t self) -> svn_revnum_t """
    pass

def svn_info_t_copyfrom_rev_set(svn_info_t_self, svn_revnum_t_copyfrom_rev): # real signature unknown; restored from __doc__
    """ svn_info_t_copyfrom_rev_set(svn_info_t self, svn_revnum_t copyfrom_rev) """
    pass

def svn_info_t_copyfrom_url_get(svn_info_t_self): # real signature unknown; restored from __doc__
    """ svn_info_t_copyfrom_url_get(svn_info_t self) -> char """
    return ""

def svn_info_t_copyfrom_url_set(svn_info_t_self, char_copyfrom_url): # real signature unknown; restored from __doc__
    """ svn_info_t_copyfrom_url_set(svn_info_t self, char copyfrom_url) """
    pass

def svn_info_t_depth_get(svn_info_t_self): # real signature unknown; restored from __doc__
    """ svn_info_t_depth_get(svn_info_t self) -> svn_depth_t """
    pass

def svn_info_t_depth_set(svn_info_t_self, svn_depth_t_depth): # real signature unknown; restored from __doc__
    """ svn_info_t_depth_set(svn_info_t self, svn_depth_t depth) """
    pass

def svn_info_t_has_wc_info_get(svn_info_t_self): # real signature unknown; restored from __doc__
    """ svn_info_t_has_wc_info_get(svn_info_t self) -> svn_boolean_t """
    pass

def svn_info_t_has_wc_info_set(svn_info_t_self, svn_boolean_t_has_wc_info): # real signature unknown; restored from __doc__
    """ svn_info_t_has_wc_info_set(svn_info_t self, svn_boolean_t has_wc_info) """
    pass

def svn_info_t_kind_get(svn_info_t_self): # real signature unknown; restored from __doc__
    """ svn_info_t_kind_get(svn_info_t self) -> svn_node_kind_t """
    pass

def svn_info_t_kind_set(svn_info_t_self, svn_node_kind_t_kind): # real signature unknown; restored from __doc__
    """ svn_info_t_kind_set(svn_info_t self, svn_node_kind_t kind) """
    pass

def svn_info_t_last_changed_author_get(svn_info_t_self): # real signature unknown; restored from __doc__
    """ svn_info_t_last_changed_author_get(svn_info_t self) -> char """
    return ""

def svn_info_t_last_changed_author_set(svn_info_t_self, char_last_changed_author): # real signature unknown; restored from __doc__
    """ svn_info_t_last_changed_author_set(svn_info_t self, char last_changed_author) """
    pass

def svn_info_t_last_changed_date_get(svn_info_t_self): # real signature unknown; restored from __doc__
    """ svn_info_t_last_changed_date_get(svn_info_t self) -> apr_time_t """
    pass

def svn_info_t_last_changed_date_set(svn_info_t_self, apr_time_t_last_changed_date): # real signature unknown; restored from __doc__
    """ svn_info_t_last_changed_date_set(svn_info_t self, apr_time_t last_changed_date) """
    pass

def svn_info_t_last_changed_rev_get(svn_info_t_self): # real signature unknown; restored from __doc__
    """ svn_info_t_last_changed_rev_get(svn_info_t self) -> svn_revnum_t """
    pass

def svn_info_t_last_changed_rev_set(svn_info_t_self, svn_revnum_t_last_changed_rev): # real signature unknown; restored from __doc__
    """ svn_info_t_last_changed_rev_set(svn_info_t self, svn_revnum_t last_changed_rev) """
    pass

def svn_info_t_lock_get(svn_info_t_self): # real signature unknown; restored from __doc__
    """ svn_info_t_lock_get(svn_info_t self) -> svn_lock_t """
    pass

def svn_info_t_lock_set(svn_info_t_self, svn_lock_t_lock): # real signature unknown; restored from __doc__
    """ svn_info_t_lock_set(svn_info_t self, svn_lock_t lock) """
    pass

def svn_info_t_prejfile_get(svn_info_t_self): # real signature unknown; restored from __doc__
    """ svn_info_t_prejfile_get(svn_info_t self) -> char """
    return ""

def svn_info_t_prejfile_set(svn_info_t_self, char_prejfile): # real signature unknown; restored from __doc__
    """ svn_info_t_prejfile_set(svn_info_t self, char prejfile) """
    pass

def svn_info_t_prop_time_get(svn_info_t_self): # real signature unknown; restored from __doc__
    """ svn_info_t_prop_time_get(svn_info_t self) -> apr_time_t """
    pass

def svn_info_t_prop_time_set(svn_info_t_self, apr_time_t_prop_time): # real signature unknown; restored from __doc__
    """ svn_info_t_prop_time_set(svn_info_t self, apr_time_t prop_time) """
    pass

def svn_info_t_repos_root_URL_get(svn_info_t_self): # real signature unknown; restored from __doc__
    """ svn_info_t_repos_root_URL_get(svn_info_t self) -> char """
    return ""

def svn_info_t_repos_root_URL_set(svn_info_t_self, char_repos_root_URL): # real signature unknown; restored from __doc__
    """ svn_info_t_repos_root_URL_set(svn_info_t self, char repos_root_URL) """
    pass

def svn_info_t_repos_UUID_get(svn_info_t_self): # real signature unknown; restored from __doc__
    """ svn_info_t_repos_UUID_get(svn_info_t self) -> char """
    return ""

def svn_info_t_repos_UUID_set(svn_info_t_self, char_repos_UUID): # real signature unknown; restored from __doc__
    """ svn_info_t_repos_UUID_set(svn_info_t self, char repos_UUID) """
    pass

def svn_info_t_rev_get(svn_info_t_self): # real signature unknown; restored from __doc__
    """ svn_info_t_rev_get(svn_info_t self) -> svn_revnum_t """
    pass

def svn_info_t_rev_set(svn_info_t_self, svn_revnum_t_rev): # real signature unknown; restored from __doc__
    """ svn_info_t_rev_set(svn_info_t self, svn_revnum_t rev) """
    pass

def svn_info_t_schedule_get(svn_info_t_self): # real signature unknown; restored from __doc__
    """ svn_info_t_schedule_get(svn_info_t self) -> svn_wc_schedule_t """
    pass

def svn_info_t_schedule_set(svn_info_t_self, svn_wc_schedule_t_schedule): # real signature unknown; restored from __doc__
    """ svn_info_t_schedule_set(svn_info_t self, svn_wc_schedule_t schedule) """
    pass

def svn_info_t_size64_get(svn_info_t_self): # real signature unknown; restored from __doc__
    """ svn_info_t_size64_get(svn_info_t self) -> svn_filesize_t """
    pass

def svn_info_t_size64_set(svn_info_t_self, svn_filesize_t_size64): # real signature unknown; restored from __doc__
    """ svn_info_t_size64_set(svn_info_t self, svn_filesize_t size64) """
    pass

def svn_info_t_size_get(svn_info_t_self): # real signature unknown; restored from __doc__
    """ svn_info_t_size_get(svn_info_t self) -> apr_size_t """
    pass

def svn_info_t_size_set(svn_info_t_self, apr_size_t_size): # real signature unknown; restored from __doc__
    """ svn_info_t_size_set(svn_info_t self, apr_size_t size) """
    pass

def svn_info_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def svn_info_t_text_time_get(svn_info_t_self): # real signature unknown; restored from __doc__
    """ svn_info_t_text_time_get(svn_info_t self) -> apr_time_t """
    pass

def svn_info_t_text_time_set(svn_info_t_self, apr_time_t_text_time): # real signature unknown; restored from __doc__
    """ svn_info_t_text_time_set(svn_info_t self, apr_time_t text_time) """
    pass

def svn_info_t_tree_conflict_get(svn_info_t_self): # real signature unknown; restored from __doc__
    """ svn_info_t_tree_conflict_get(svn_info_t self) -> svn_wc_conflict_description_t """
    pass

def svn_info_t_tree_conflict_set(svn_info_t_self, svn_wc_conflict_description_t_tree_conflict): # real signature unknown; restored from __doc__
    """ svn_info_t_tree_conflict_set(svn_info_t self, svn_wc_conflict_description_t tree_conflict) """
    pass

def svn_info_t_URL_get(svn_info_t_self): # real signature unknown; restored from __doc__
    """ svn_info_t_URL_get(svn_info_t self) -> char """
    return ""

def svn_info_t_URL_set(svn_info_t_self, char_URL): # real signature unknown; restored from __doc__
    """ svn_info_t_URL_set(svn_info_t self, char URL) """
    pass

def svn_info_t_working_size64_get(svn_info_t_self): # real signature unknown; restored from __doc__
    """ svn_info_t_working_size64_get(svn_info_t self) -> svn_filesize_t """
    pass

def svn_info_t_working_size64_set(svn_info_t_self, svn_filesize_t_working_size64): # real signature unknown; restored from __doc__
    """ svn_info_t_working_size64_set(svn_info_t self, svn_filesize_t working_size64) """
    pass

def svn_info_t_working_size_get(svn_info_t_self): # real signature unknown; restored from __doc__
    """ svn_info_t_working_size_get(svn_info_t self) -> apr_size_t """
    pass

def svn_info_t_working_size_set(svn_info_t_self, apr_size_t_working_size): # real signature unknown; restored from __doc__
    """ svn_info_t_working_size_set(svn_info_t self, apr_size_t working_size) """
    pass

def svn_proplist_invoke_receiver(svn_proplist_receiver_t__obj, void_baton, char_path, apr_hash_t_prop_hash, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_proplist_invoke_receiver(svn_proplist_receiver_t _obj, void baton, char path, 
        apr_hash_t prop_hash, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_proplist_receiver_t_swigregister(*args, **kwargs): # real signature unknown
    pass

# no classes
# variables with complex values

svn_swig_py_cancel_func = None # (!) real value is ''

svn_swig_py_get_commit_log_func = None # (!) real value is ''

svn_swig_py_notify_func = None # (!) real value is ''

