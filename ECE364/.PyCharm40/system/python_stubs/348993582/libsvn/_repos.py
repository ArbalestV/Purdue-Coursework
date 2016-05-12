# encoding: utf-8
# module libsvn._repos
# from /usr/lib64/python2.6/site-packages/libsvn/_repos.so
# by generator 1.136
# no doc
# no imports

# Variables with simple values

svn_authz_none = 0
svn_authz_read = 1
svn_authz_recursive = 4
svn_authz_write = 2

svn_node_action_add = 1
svn_node_action_change = 0
svn_node_action_delete = 2
svn_node_action_replace = 3

SVN_REPOS_CAPABILITY_MERGEINFO = 'mergeinfo'

SVN_REPOS_DUMPFILE_CONTENT_LENGTH = 'Content-length'

SVN_REPOS_DUMPFILE_FORMAT_VERSION = 3

SVN_REPOS_DUMPFILE_MAGIC_HEADER = 'SVN-fs-dump-format-version'

SVN_REPOS_DUMPFILE_NODE_ACTION = 'Node-action'

SVN_REPOS_DUMPFILE_NODE_COPYFROM_PATH = 'Node-copyfrom-path'
SVN_REPOS_DUMPFILE_NODE_COPYFROM_REV = 'Node-copyfrom-rev'

SVN_REPOS_DUMPFILE_NODE_KIND = 'Node-kind'
SVN_REPOS_DUMPFILE_NODE_PATH = 'Node-path'

SVN_REPOS_DUMPFILE_PROP_CONTENT_LENGTH = 'Prop-content-length'

SVN_REPOS_DUMPFILE_PROP_DELTA = 'Prop-delta'

SVN_REPOS_DUMPFILE_REVISION_NUMBER = 'Revision-number'

SVN_REPOS_DUMPFILE_TEXT_CONTENT_CHECKSUM = 'Text-content-md5'
SVN_REPOS_DUMPFILE_TEXT_CONTENT_LENGTH = 'Text-content-length'
SVN_REPOS_DUMPFILE_TEXT_CONTENT_MD5 = 'Text-content-md5'
SVN_REPOS_DUMPFILE_TEXT_CONTENT_SHA1 = 'Text-content-sha1'

SVN_REPOS_DUMPFILE_TEXT_COPY_SOURCE_CHECKSUM = 'Text-copy-source-md5'
SVN_REPOS_DUMPFILE_TEXT_COPY_SOURCE_MD5 = 'Text-copy-source-md5'
SVN_REPOS_DUMPFILE_TEXT_COPY_SOURCE_SHA1 = 'Text-copy-source-sha1'

SVN_REPOS_DUMPFILE_TEXT_DELTA = 'Text-delta'

SVN_REPOS_DUMPFILE_TEXT_DELTA_BASE_CHECKSUM = 'Text-delta-base-md5'
SVN_REPOS_DUMPFILE_TEXT_DELTA_BASE_MD5 = 'Text-delta-base-md5'
SVN_REPOS_DUMPFILE_TEXT_DELTA_BASE_SHA1 = 'Text-delta-base-sha1'

SVN_REPOS_DUMPFILE_UUID = 'UUID'

svn_repos_load_uuid_default = 0
svn_repos_load_uuid_force = 2
svn_repos_load_uuid_ignore = 1

svn_repos_revision_access_full = 2
svn_repos_revision_access_none = 0
svn_repos_revision_access_partial = 1

# functions

def svn_authz_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def svn_repos_abort_report(void_report_baton, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_repos_abort_report(void report_baton, apr_pool_t pool) -> svn_error_t """
    pass

def svn_repos_authz_callback_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def svn_repos_authz_check_access(svn_authz_t_authz, char_repos_name, char_path, char_user, svn_repos_authz_access_t_required_access, svn_boolean_t_access_granted, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_repos_authz_check_access(svn_authz_t authz, char repos_name, char path, char user, 
        svn_repos_authz_access_t required_access, 
        svn_boolean_t access_granted, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_repos_authz_func_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def svn_repos_authz_read(svn_authz_t_authz_p, char_file, svn_boolean_t_must_exist, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_repos_authz_read(svn_authz_t authz_p, char file, svn_boolean_t must_exist, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_repos_begin_report(void_report_baton, svn_revnum_t_revnum, char_username, svn_repos_t_repos, char_fs_base, char_target, char_tgt_path, svn_boolean_t_text_deltas, svn_boolean_t_recurse, svn_boolean_t_ignore_ancestry, svn_delta_editor_t_editor, void_edit_baton, svn_repos_authz_func_t_authz_read_func, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_repos_begin_report(void report_baton, svn_revnum_t revnum, char username, 
        svn_repos_t repos, char fs_base, char target, 
        char tgt_path, svn_boolean_t text_deltas, 
        svn_boolean_t recurse, svn_boolean_t ignore_ancestry, 
        svn_delta_editor_t editor, void edit_baton, 
        svn_repos_authz_func_t authz_read_func, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_repos_begin_report2(void_report_baton, svn_revnum_t_revnum, svn_repos_t_repos, char_fs_base, char_target, char_tgt_path, svn_boolean_t_text_deltas, svn_depth_t_depth, svn_boolean_t_ignore_ancestry, svn_boolean_t_send_copyfrom_args, svn_delta_editor_t_editor, void_edit_baton, svn_repos_authz_func_t_authz_read_func, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_repos_begin_report2(void report_baton, svn_revnum_t revnum, svn_repos_t repos, 
        char fs_base, char target, char tgt_path, 
        svn_boolean_t text_deltas, svn_depth_t depth, 
        svn_boolean_t ignore_ancestry, svn_boolean_t send_copyfrom_args, 
        svn_delta_editor_t editor, 
        void edit_baton, svn_repos_authz_func_t authz_read_func, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_repos_check_revision_access(svn_repos_revision_access_level_t_access_level, svn_repos_t_repos, svn_revnum_t_revision, svn_repos_authz_func_t_authz_read_func, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_repos_check_revision_access(svn_repos_revision_access_level_t access_level, svn_repos_t repos, 
        svn_revnum_t revision, svn_repos_authz_func_t authz_read_func, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_repos_conf_dir(svn_repos_t_repos, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_repos_conf_dir(svn_repos_t repos, apr_pool_t pool) -> char """
    return ""

def svn_repos_create(svn_repos_t_repos_p, char_path, char_unused_1, char_unused_2, apr_hash_t_config, apr_hash_t_fs_config, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_repos_create(svn_repos_t repos_p, char path, char unused_1, char unused_2, 
        apr_hash_t config, apr_hash_t fs_config, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_repos_dated_revision(svn_revnum_t_revision, svn_repos_t_repos, apr_time_t_tm, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_repos_dated_revision(svn_revnum_t revision, svn_repos_t repos, apr_time_t tm, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_repos_db_env(svn_repos_t_repos, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_repos_db_env(svn_repos_t repos, apr_pool_t pool) -> char """
    return ""

def svn_repos_db_lockfile(svn_repos_t_repos, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_repos_db_lockfile(svn_repos_t repos, apr_pool_t pool) -> char """
    return ""

def svn_repos_db_logfiles(apr_array_header_t_logfiles, char_path, svn_boolean_t_only_unused, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_repos_db_logfiles(apr_array_header_t logfiles, char path, svn_boolean_t only_unused, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_repos_db_logs_lockfile(svn_repos_t_repos, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_repos_db_logs_lockfile(svn_repos_t repos, apr_pool_t pool) -> char """
    return ""

def svn_repos_delete(char_path, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_repos_delete(char path, apr_pool_t pool) -> svn_error_t """
    pass

def svn_repos_deleted_rev(svn_fs_t_fs, char_path, svn_revnum_t_start, svn_revnum_t_end, svn_revnum_t_deleted, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_repos_deleted_rev(svn_fs_t fs, char path, svn_revnum_t start, svn_revnum_t end, 
        svn_revnum_t deleted, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_repos_delete_path(void_report_baton, char_path, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_repos_delete_path(void report_baton, char path, apr_pool_t pool) -> svn_error_t """
    pass

def svn_repos_dir_delta(svn_fs_root_t_src_root, char_src_parent_dir, char_src_entry, svn_fs_root_t_tgt_root, char_tgt_path, svn_delta_editor_t_editor, void_edit_baton, svn_repos_authz_func_t_authz_read_func, svn_boolean_t_text_deltas, svn_boolean_t_recurse, svn_boolean_t_entry_props, svn_boolean_t_ignore_ancestry, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_repos_dir_delta(svn_fs_root_t src_root, char src_parent_dir, char src_entry, 
        svn_fs_root_t tgt_root, char tgt_path, 
        svn_delta_editor_t editor, void edit_baton, 
        svn_repos_authz_func_t authz_read_func, svn_boolean_t text_deltas, 
        svn_boolean_t recurse, 
        svn_boolean_t entry_props, svn_boolean_t ignore_ancestry, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_repos_dir_delta2(svn_fs_root_t_src_root, char_src_parent_dir, char_src_entry, svn_fs_root_t_tgt_root, char_tgt_path, svn_delta_editor_t_editor, void_edit_baton, svn_repos_authz_func_t_authz_read_func, svn_boolean_t_text_deltas, svn_depth_t_depth, svn_boolean_t_entry_props, svn_boolean_t_ignore_ancestry, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_repos_dir_delta2(svn_fs_root_t src_root, char src_parent_dir, char src_entry, 
        svn_fs_root_t tgt_root, char tgt_path, 
        svn_delta_editor_t editor, void edit_baton, 
        svn_repos_authz_func_t authz_read_func, svn_boolean_t text_deltas, 
        svn_depth_t depth, svn_boolean_t entry_props, 
        svn_boolean_t ignore_ancestry, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_repos_dump_fs(svn_repos_t_repos, svn_stream_t_dumpstream, svn_stream_t_feedback_stream, svn_revnum_t_start_rev, svn_revnum_t_end_rev, svn_boolean_t_incremental, svn_cancel_func_t_cancel_func, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_repos_dump_fs(svn_repos_t repos, svn_stream_t dumpstream, svn_stream_t feedback_stream, 
        svn_revnum_t start_rev, 
        svn_revnum_t end_rev, svn_boolean_t incremental, 
        svn_cancel_func_t cancel_func, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_repos_dump_fs2(svn_repos_t_repos, svn_stream_t_dumpstream, svn_stream_t_feedback_stream, svn_revnum_t_start_rev, svn_revnum_t_end_rev, svn_boolean_t_incremental, svn_boolean_t_use_deltas, svn_cancel_func_t_cancel_func, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_repos_dump_fs2(svn_repos_t repos, svn_stream_t dumpstream, svn_stream_t feedback_stream, 
        svn_revnum_t start_rev, 
        svn_revnum_t end_rev, svn_boolean_t incremental, 
        svn_boolean_t use_deltas, svn_cancel_func_t cancel_func, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_repos_file_rev_handler_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def svn_repos_find_root_path(char_path, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_repos_find_root_path(char path, apr_pool_t pool) -> char """
    return ""

def svn_repos_finish_report(void_report_baton, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_repos_finish_report(void report_baton, apr_pool_t pool) -> svn_error_t """
    pass

def svn_repos_fs(svn_repos_t_repos): # real signature unknown; restored from __doc__
    """ svn_repos_fs(svn_repos_t repos) -> svn_fs_t """
    pass

def svn_repos_fs_begin_txn_for_commit(svn_fs_txn_t_txn_p, svn_repos_t_repos, svn_revnum_t_rev, char_author, char_log_msg, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_repos_fs_begin_txn_for_commit(svn_fs_txn_t txn_p, svn_repos_t repos, svn_revnum_t rev, 
        char author, char log_msg, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_repos_fs_begin_txn_for_commit2(svn_fs_txn_t_txn_p, svn_repos_t_repos, svn_revnum_t_rev, apr_hash_t_revprop_table, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_repos_fs_begin_txn_for_commit2(svn_fs_txn_t txn_p, svn_repos_t repos, svn_revnum_t rev, 
        apr_hash_t revprop_table, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_repos_fs_begin_txn_for_update(svn_fs_txn_t_txn_p, svn_repos_t_repos, svn_revnum_t_rev, char_author, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_repos_fs_begin_txn_for_update(svn_fs_txn_t txn_p, svn_repos_t repos, svn_revnum_t rev, 
        char author, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_repos_fs_change_node_prop(svn_fs_root_t_root, char_path, char_name, svn_string_t_value, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_repos_fs_change_node_prop(svn_fs_root_t root, char path, char name, svn_string_t value, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_repos_fs_change_rev_prop(svn_repos_t_repos, svn_revnum_t_rev, char_author, char_name, svn_string_t_new_value, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_repos_fs_change_rev_prop(svn_repos_t repos, svn_revnum_t rev, char author, char name, 
        svn_string_t new_value, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_repos_fs_change_rev_prop2(svn_repos_t_repos, svn_revnum_t_rev, char_author, char_name, svn_string_t_new_value, svn_repos_authz_func_t_authz_read_func, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_repos_fs_change_rev_prop2(svn_repos_t repos, svn_revnum_t rev, char author, char name, 
        svn_string_t new_value, svn_repos_authz_func_t authz_read_func, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_repos_fs_change_rev_prop3(svn_repos_t_repos, svn_revnum_t_rev, char_author, char_name, svn_string_t_new_value, svn_boolean_t_use_pre_revprop_change_hook, svn_boolean_t_use_post_revprop_change_hook, svn_repos_authz_func_t_authz_read_func, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_repos_fs_change_rev_prop3(svn_repos_t repos, svn_revnum_t rev, char author, char name, 
        svn_string_t new_value, svn_boolean_t use_pre_revprop_change_hook, 
        svn_boolean_t use_post_revprop_change_hook, 
        svn_repos_authz_func_t authz_read_func, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_repos_fs_change_txn_prop(svn_fs_txn_t_txn, char_name, svn_string_t_value, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_repos_fs_change_txn_prop(svn_fs_txn_t txn, char name, svn_string_t value, apr_pool_t pool) -> svn_error_t """
    pass

def svn_repos_fs_change_txn_props(svn_fs_txn_t_txn, apr_array_header_t_props, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_repos_fs_change_txn_props(svn_fs_txn_t txn, apr_array_header_t props, apr_pool_t pool) -> svn_error_t """
    pass

def svn_repos_fs_commit_txn(char_conflict_p, svn_repos_t_repos, svn_revnum_t_new_rev, svn_fs_txn_t_txn, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_repos_fs_commit_txn(char conflict_p, svn_repos_t repos, svn_revnum_t new_rev, 
        svn_fs_txn_t txn, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_repos_fs_get_locks(apr_hash_t_locks, svn_repos_t_repos, char_path, svn_repos_authz_func_t_authz_read_func, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_repos_fs_get_locks(apr_hash_t locks, svn_repos_t repos, char path, svn_repos_authz_func_t authz_read_func, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_repos_fs_get_mergeinfo(svn_mergeinfo_catalog_t_catalog, svn_repos_t_repos, apr_array_header_t_paths, svn_revnum_t_revision, svn_mergeinfo_inheritance_t_inherit, svn_boolean_t_include_descendants, svn_repos_authz_func_t_authz_read_func, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_repos_fs_get_mergeinfo(svn_mergeinfo_catalog_t catalog, svn_repos_t repos, 
        apr_array_header_t paths, svn_revnum_t revision, 
        svn_mergeinfo_inheritance_t inherit, svn_boolean_t include_descendants, 
        svn_repos_authz_func_t authz_read_func, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_repos_fs_lock(svn_lock_t_lock, svn_repos_t_repos, char_path, char_token, char_comment, svn_boolean_t_is_dav_comment, apr_time_t_expiration_date, svn_revnum_t_current_rev, svn_boolean_t_steal_lock, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_repos_fs_lock(svn_lock_t lock, svn_repos_t repos, char path, char token, 
        char comment, svn_boolean_t is_dav_comment, 
        apr_time_t expiration_date, svn_revnum_t current_rev, 
        svn_boolean_t steal_lock, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_repos_fs_pack(svn_repos_t_repos, svn_fs_pack_notify_t_notify_func, void_notify_baton, svn_cancel_func_t_cancel_func, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_repos_fs_pack(svn_repos_t repos, svn_fs_pack_notify_t notify_func, 
        void notify_baton, svn_cancel_func_t cancel_func, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_repos_fs_revision_prop(svn_string_t_value_p, svn_repos_t_repos, svn_revnum_t_rev, char_propname, svn_repos_authz_func_t_authz_read_func, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_repos_fs_revision_prop(svn_string_t value_p, svn_repos_t repos, svn_revnum_t rev, 
        char propname, svn_repos_authz_func_t authz_read_func, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_repos_fs_revision_proplist(apr_hash_t_table_p, svn_repos_t_repos, svn_revnum_t_rev, svn_repos_authz_func_t_authz_read_func, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_repos_fs_revision_proplist(apr_hash_t table_p, svn_repos_t repos, svn_revnum_t rev, 
        svn_repos_authz_func_t authz_read_func, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_repos_fs_unlock(svn_repos_t_repos, char_path, char_token, svn_boolean_t_break_lock, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_repos_fs_unlock(svn_repos_t repos, char path, char token, svn_boolean_t break_lock, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_repos_get_committed_info(svn_revnum_t_committed_rev, char_committed_date, char_last_author, svn_fs_root_t_root, char_path, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_repos_get_committed_info(svn_revnum_t committed_rev, char committed_date, char last_author, 
        svn_fs_root_t root, char path, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_repos_get_commit_editor(svn_delta_editor_t_editor, void_edit_baton, svn_repos_t_repos, char_repos_url, char_base_path, char_user, char_log_msg, svn_commit_callback_t_callback, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_repos_get_commit_editor(svn_delta_editor_t editor, void edit_baton, svn_repos_t repos, 
        char repos_url, char base_path, char user, 
        char log_msg, svn_commit_callback_t callback, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_repos_get_commit_editor2(svn_delta_editor_t_editor, void_edit_baton, svn_repos_t_repos, svn_fs_txn_t_txn, char_repos_url, char_base_path, char_user, char_log_msg, svn_commit_callback_t_callback, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_repos_get_commit_editor2(svn_delta_editor_t editor, void edit_baton, svn_repos_t repos, 
        svn_fs_txn_t txn, char repos_url, 
        char base_path, char user, char log_msg, svn_commit_callback_t callback, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_repos_get_commit_editor3(svn_delta_editor_t_editor, void_edit_baton, svn_repos_t_repos, svn_fs_txn_t_txn, char_repos_url, char_base_path, char_user, char_log_msg, svn_commit_callback_t_callback, svn_repos_authz_callback_t_authz_callback, void_authz_baton, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_repos_get_commit_editor3(svn_delta_editor_t editor, void edit_baton, svn_repos_t repos, 
        svn_fs_txn_t txn, char repos_url, 
        char base_path, char user, char log_msg, svn_commit_callback_t callback, 
        svn_repos_authz_callback_t authz_callback, 
        void authz_baton, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_repos_get_commit_editor4(svn_delta_editor_t_editor, void_edit_baton, svn_repos_t_repos, svn_fs_txn_t_txn, char_repos_url, char_base_path, char_user, char_log_msg, svn_commit_callback2_t_callback, svn_repos_authz_callback_t_authz_callback, void_authz_baton, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_repos_get_commit_editor4(svn_delta_editor_t editor, void edit_baton, svn_repos_t repos, 
        svn_fs_txn_t txn, char repos_url, 
        char base_path, char user, char log_msg, svn_commit_callback2_t callback, 
        svn_repos_authz_callback_t authz_callback, 
        void authz_baton, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_repos_get_commit_editor5(svn_delta_editor_t_editor, void_edit_baton, svn_repos_t_repos, svn_fs_txn_t_txn, char_repos_url, char_base_path, apr_hash_t_revprop_table, svn_commit_callback2_t_callback, svn_repos_authz_callback_t_authz_callback, void_authz_baton, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_repos_get_commit_editor5(svn_delta_editor_t editor, void edit_baton, svn_repos_t repos, 
        svn_fs_txn_t txn, char repos_url, 
        char base_path, apr_hash_t revprop_table, svn_commit_callback2_t callback, 
        svn_repos_authz_callback_t authz_callback, 
        void authz_baton, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_repos_get_file_revs(svn_repos_t_repos, char_path, svn_revnum_t_start, svn_revnum_t_end, svn_repos_authz_func_t_authz_read_func, svn_repos_file_rev_handler_t_handler, void_handler_baton, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_repos_get_file_revs(svn_repos_t repos, char path, svn_revnum_t start, svn_revnum_t end, 
        svn_repos_authz_func_t authz_read_func, 
        svn_repos_file_rev_handler_t handler, 
        void handler_baton, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_repos_get_file_revs2(svn_repos_t_repos, char_path, svn_revnum_t_start, svn_revnum_t_end, svn_boolean_t_include_merged_revisions, svn_repos_authz_func_t_authz_read_func, svn_file_rev_handler_t_handler, void_handler_baton, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_repos_get_file_revs2(svn_repos_t repos, char path, svn_revnum_t start, svn_revnum_t end, 
        svn_boolean_t include_merged_revisions, 
        svn_repos_authz_func_t authz_read_func, 
        svn_file_rev_handler_t handler, void handler_baton, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_repos_get_fs_build_parser(parser, void_parse_baton, svn_repos_t_repos, svn_boolean_t_use_history, enum_svn_repos_load_uuid_uuid_action, svn_stream_t_outstream, char_parent_dir, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_repos_get_fs_build_parser( parser, void parse_baton, svn_repos_t repos, svn_boolean_t use_history, 
        enum svn_repos_load_uuid uuid_action, 
        svn_stream_t outstream, char parent_dir, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_repos_get_fs_build_parser2(svn_repos_parse_fns2_t_parser, void_parse_baton, svn_repos_t_repos, svn_boolean_t_use_history, enum_svn_repos_load_uuid_uuid_action, svn_stream_t_outstream, char_parent_dir, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_repos_get_fs_build_parser2(svn_repos_parse_fns2_t parser, void parse_baton, svn_repos_t repos, 
        svn_boolean_t use_history, enum svn_repos_load_uuid uuid_action, 
        svn_stream_t outstream, 
        char parent_dir, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_repos_get_logs(svn_repos_t_repos, apr_array_header_t_paths, svn_revnum_t_start, svn_revnum_t_end, svn_boolean_t_discover_changed_paths, svn_boolean_t_strict_node_history, svn_log_message_receiver_t_receiver, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_repos_get_logs(svn_repos_t repos, apr_array_header_t paths, svn_revnum_t start, 
        svn_revnum_t end, svn_boolean_t discover_changed_paths, 
        svn_boolean_t strict_node_history, 
        svn_log_message_receiver_t receiver, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_repos_get_logs2(svn_repos_t_repos, apr_array_header_t_paths, svn_revnum_t_start, svn_revnum_t_end, svn_boolean_t_discover_changed_paths, svn_boolean_t_strict_node_history, svn_repos_authz_func_t_authz_read_func, svn_log_message_receiver_t_receiver, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_repos_get_logs2(svn_repos_t repos, apr_array_header_t paths, svn_revnum_t start, 
        svn_revnum_t end, svn_boolean_t discover_changed_paths, 
        svn_boolean_t strict_node_history, 
        svn_repos_authz_func_t authz_read_func, 
        svn_log_message_receiver_t receiver, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_repos_get_logs3(svn_repos_t_repos, apr_array_header_t_paths, svn_revnum_t_start, svn_revnum_t_end, int_limit, svn_boolean_t_discover_changed_paths, svn_boolean_t_strict_node_history, svn_repos_authz_func_t_authz_read_func, svn_log_message_receiver_t_receiver, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_repos_get_logs3(svn_repos_t repos, apr_array_header_t paths, svn_revnum_t start, 
        svn_revnum_t end, int limit, svn_boolean_t discover_changed_paths, 
        svn_boolean_t strict_node_history, 
        svn_repos_authz_func_t authz_read_func, 
        svn_log_message_receiver_t receiver, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_repos_get_logs4(svn_repos_t_repos, apr_array_header_t_paths, svn_revnum_t_start, svn_revnum_t_end, int_limit, svn_boolean_t_discover_changed_paths, svn_boolean_t_strict_node_history, svn_boolean_t_include_merged_revisions, apr_array_header_t_revprops, svn_repos_authz_func_t_authz_read_func, svn_log_entry_receiver_t_receiver, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_repos_get_logs4(svn_repos_t repos, apr_array_header_t paths, svn_revnum_t start, 
        svn_revnum_t end, int limit, svn_boolean_t discover_changed_paths, 
        svn_boolean_t strict_node_history, 
        svn_boolean_t include_merged_revisions, 
        apr_array_header_t revprops, 
        svn_repos_authz_func_t authz_read_func, 
        svn_log_entry_receiver_t receiver, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_repos_has_capability(svn_repos_t_repos, svn_boolean_t_has, char_capability, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_repos_has_capability(svn_repos_t repos, svn_boolean_t has, char capability, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_repos_history(svn_fs_t_fs, char_path, svn_repos_history_func_t_history_func, svn_revnum_t_start, svn_revnum_t_end, svn_boolean_t_cross_copies, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_repos_history(svn_fs_t fs, char path, svn_repos_history_func_t history_func, 
        svn_revnum_t start, svn_revnum_t end, 
        svn_boolean_t cross_copies, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_repos_history2(svn_fs_t_fs, char_path, svn_repos_history_func_t_history_func, svn_repos_authz_func_t_authz_read_func, svn_revnum_t_start, svn_revnum_t_end, svn_boolean_t_cross_copies, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_repos_history2(svn_fs_t fs, char path, svn_repos_history_func_t history_func, 
        svn_repos_authz_func_t authz_read_func, 
        svn_revnum_t start, svn_revnum_t end, 
        svn_boolean_t cross_copies, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_repos_history_func_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def svn_repos_hook_dir(svn_repos_t_repos, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_repos_hook_dir(svn_repos_t repos, apr_pool_t pool) -> char """
    return ""

def svn_repos_hotcopy(char_src_path, char_dst_path, svn_boolean_t_clean_logs, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_repos_hotcopy(char src_path, char dst_path, svn_boolean_t clean_logs, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_repos_invoke_authz_callback(svn_repos_authz_callback_t__obj, svn_repos_authz_access_t_required, svn_boolean_t_allowed, svn_fs_root_t_root, char_path, void_baton, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_repos_invoke_authz_callback(svn_repos_authz_callback_t _obj, svn_repos_authz_access_t required, 
        svn_boolean_t allowed, svn_fs_root_t root, 
        char path, void baton, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_repos_invoke_authz_func(svn_repos_authz_func_t__obj, svn_boolean_t_allowed, svn_fs_root_t_root, char_path, void_baton, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_repos_invoke_authz_func(svn_repos_authz_func_t _obj, svn_boolean_t allowed, 
        svn_fs_root_t root, char path, void baton, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_repos_invoke_file_rev_handler(svn_repos_file_rev_handler_t__obj, void_baton, char_path, svn_revnum_t_rev, apr_hash_t_rev_props, svn_txdelta_window_handler_t_delta_handler, void_delta_baton, apr_array_header_t_prop_diffs, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_repos_invoke_file_rev_handler(svn_repos_file_rev_handler_t _obj, void baton, char path, 
        svn_revnum_t rev, apr_hash_t rev_props, 
        svn_txdelta_window_handler_t delta_handler, 
        void delta_baton, apr_array_header_t prop_diffs, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_repos_invoke_history_func(svn_repos_history_func_t__obj, void_baton, char_path, svn_revnum_t_revision, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_repos_invoke_history_func(svn_repos_history_func_t _obj, void baton, char path, 
        svn_revnum_t revision, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_repos_link_path(void_report_baton, char_path, char_link_path, svn_revnum_t_revision, svn_boolean_t_start_empty, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_repos_link_path(void report_baton, char path, char link_path, svn_revnum_t revision, 
        svn_boolean_t start_empty, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_repos_link_path2(void_report_baton, char_path, char_link_path, svn_revnum_t_revision, svn_boolean_t_start_empty, char_lock_token, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_repos_link_path2(void report_baton, char path, char link_path, svn_revnum_t revision, 
        svn_boolean_t start_empty, 
        char lock_token, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_repos_link_path3(void_report_baton, char_path, char_link_path, svn_revnum_t_revision, svn_depth_t_depth, svn_boolean_t_start_empty, char_lock_token, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_repos_link_path3(void report_baton, char path, char link_path, svn_revnum_t revision, 
        svn_depth_t depth, svn_boolean_t start_empty, 
        char lock_token, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_repos_load_fs(svn_repos_t_repos, svn_stream_t_dumpstream, svn_stream_t_feedback_stream, enum_svn_repos_load_uuid_uuid_action, char_parent_dir, svn_cancel_func_t_cancel_func, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_repos_load_fs(svn_repos_t repos, svn_stream_t dumpstream, svn_stream_t feedback_stream, 
        enum svn_repos_load_uuid uuid_action, 
        char parent_dir, svn_cancel_func_t cancel_func, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_repos_load_fs2(svn_repos_t_repos, svn_stream_t_dumpstream, svn_stream_t_feedback_stream, enum_svn_repos_load_uuid_uuid_action, char_parent_dir, svn_boolean_t_use_pre_commit_hook, svn_boolean_t_use_post_commit_hook, svn_cancel_func_t_cancel_func, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_repos_load_fs2(svn_repos_t repos, svn_stream_t dumpstream, svn_stream_t feedback_stream, 
        enum svn_repos_load_uuid uuid_action, 
        char parent_dir, svn_boolean_t use_pre_commit_hook, 
        svn_boolean_t use_post_commit_hook, 
        svn_cancel_func_t cancel_func, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_repos_lock_dir(svn_repos_t_repos, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_repos_lock_dir(svn_repos_t repos, apr_pool_t pool) -> char """
    return ""

def svn_repos_node_editor(svn_delta_editor_t_editor, void_edit_baton, svn_repos_t_repos, svn_fs_root_t_base_root, svn_fs_root_t_root, apr_pool_t_node_pool, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_repos_node_editor(svn_delta_editor_t editor, void edit_baton, svn_repos_t repos, 
        svn_fs_root_t base_root, svn_fs_root_t root, 
        apr_pool_t node_pool, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_repos_node_from_baton(void_edit_baton): # real signature unknown; restored from __doc__
    """ svn_repos_node_from_baton(void edit_baton) -> svn_repos_node_t """
    pass

def svn_repos_node_location_segments(svn_repos_t_repos, char_path, svn_revnum_t_peg_revision, svn_revnum_t_start_rev, svn_revnum_t_end_rev, svn_location_segment_receiver_t_receiver, svn_repos_authz_func_t_authz_read_func, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_repos_node_location_segments(svn_repos_t repos, char path, svn_revnum_t peg_revision, 
        svn_revnum_t start_rev, svn_revnum_t end_rev, 
        svn_location_segment_receiver_t receiver, 
        svn_repos_authz_func_t authz_read_func, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_repos_node_t_action_get(svn_repos_node_t_self): # real signature unknown; restored from __doc__
    """ svn_repos_node_t_action_get(svn_repos_node_t self) -> char """
    return ""

def svn_repos_node_t_action_set(svn_repos_node_t_self, char_action): # real signature unknown; restored from __doc__
    """ svn_repos_node_t_action_set(svn_repos_node_t self, char action) """
    pass

def svn_repos_node_t_child_get(svn_repos_node_t_self): # real signature unknown; restored from __doc__
    """ svn_repos_node_t_child_get(svn_repos_node_t self) -> struct svn_repos_node_t """
    pass

def svn_repos_node_t_child_set(svn_repos_node_t_self, struct_svn_repos_node_t_child): # real signature unknown; restored from __doc__
    """ svn_repos_node_t_child_set(svn_repos_node_t self, struct svn_repos_node_t child) """
    pass

def svn_repos_node_t_copyfrom_path_get(svn_repos_node_t_self): # real signature unknown; restored from __doc__
    """ svn_repos_node_t_copyfrom_path_get(svn_repos_node_t self) -> char """
    return ""

def svn_repos_node_t_copyfrom_path_set(svn_repos_node_t_self, char_copyfrom_path): # real signature unknown; restored from __doc__
    """ svn_repos_node_t_copyfrom_path_set(svn_repos_node_t self, char copyfrom_path) """
    pass

def svn_repos_node_t_copyfrom_rev_get(svn_repos_node_t_self): # real signature unknown; restored from __doc__
    """ svn_repos_node_t_copyfrom_rev_get(svn_repos_node_t self) -> svn_revnum_t """
    pass

def svn_repos_node_t_copyfrom_rev_set(svn_repos_node_t_self, svn_revnum_t_copyfrom_rev): # real signature unknown; restored from __doc__
    """ svn_repos_node_t_copyfrom_rev_set(svn_repos_node_t self, svn_revnum_t copyfrom_rev) """
    pass

def svn_repos_node_t_kind_get(svn_repos_node_t_self): # real signature unknown; restored from __doc__
    """ svn_repos_node_t_kind_get(svn_repos_node_t self) -> svn_node_kind_t """
    pass

def svn_repos_node_t_kind_set(svn_repos_node_t_self, svn_node_kind_t_kind): # real signature unknown; restored from __doc__
    """ svn_repos_node_t_kind_set(svn_repos_node_t self, svn_node_kind_t kind) """
    pass

def svn_repos_node_t_name_get(svn_repos_node_t_self): # real signature unknown; restored from __doc__
    """ svn_repos_node_t_name_get(svn_repos_node_t self) -> char """
    return ""

def svn_repos_node_t_name_set(svn_repos_node_t_self, char_name): # real signature unknown; restored from __doc__
    """ svn_repos_node_t_name_set(svn_repos_node_t self, char name) """
    pass

def svn_repos_node_t_parent_get(svn_repos_node_t_self): # real signature unknown; restored from __doc__
    """ svn_repos_node_t_parent_get(svn_repos_node_t self) -> struct svn_repos_node_t """
    pass

def svn_repos_node_t_parent_set(svn_repos_node_t_self, struct_svn_repos_node_t_parent): # real signature unknown; restored from __doc__
    """ svn_repos_node_t_parent_set(svn_repos_node_t self, struct svn_repos_node_t parent) """
    pass

def svn_repos_node_t_prop_mod_get(svn_repos_node_t_self): # real signature unknown; restored from __doc__
    """ svn_repos_node_t_prop_mod_get(svn_repos_node_t self) -> svn_boolean_t """
    pass

def svn_repos_node_t_prop_mod_set(svn_repos_node_t_self, svn_boolean_t_prop_mod): # real signature unknown; restored from __doc__
    """ svn_repos_node_t_prop_mod_set(svn_repos_node_t self, svn_boolean_t prop_mod) """
    pass

def svn_repos_node_t_sibling_get(svn_repos_node_t_self): # real signature unknown; restored from __doc__
    """ svn_repos_node_t_sibling_get(svn_repos_node_t self) -> struct svn_repos_node_t """
    pass

def svn_repos_node_t_sibling_set(svn_repos_node_t_self, struct_svn_repos_node_t_sibling): # real signature unknown; restored from __doc__
    """ svn_repos_node_t_sibling_set(svn_repos_node_t self, struct svn_repos_node_t sibling) """
    pass

def svn_repos_node_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def svn_repos_node_t_text_mod_get(svn_repos_node_t_self): # real signature unknown; restored from __doc__
    """ svn_repos_node_t_text_mod_get(svn_repos_node_t self) -> svn_boolean_t """
    pass

def svn_repos_node_t_text_mod_set(svn_repos_node_t_self, svn_boolean_t_text_mod): # real signature unknown; restored from __doc__
    """ svn_repos_node_t_text_mod_set(svn_repos_node_t self, svn_boolean_t text_mod) """
    pass

def svn_repos_open(svn_repos_t_repos_p, char_path, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_repos_open(svn_repos_t repos_p, char path, apr_pool_t pool) -> svn_error_t """
    pass

def svn_repos_parser_fns_t_close_node_get(self): # real signature unknown; restored from __doc__
    """ svn_repos_parser_fns_t_close_node_get( self) -> svn_error_t """
    pass

def svn_repos_parser_fns_t_close_node_set(self, svn_error_t_close_node): # real signature unknown; restored from __doc__
    """ svn_repos_parser_fns_t_close_node_set( self, svn_error_t close_node) """
    pass

def svn_repos_parser_fns_t_close_revision_get(self): # real signature unknown; restored from __doc__
    """ svn_repos_parser_fns_t_close_revision_get( self) -> svn_error_t """
    pass

def svn_repos_parser_fns_t_close_revision_set(self, svn_error_t_close_revision): # real signature unknown; restored from __doc__
    """ svn_repos_parser_fns_t_close_revision_set( self, svn_error_t close_revision) """
    pass

def svn_repos_parser_fns_t_new_node_record_get(self): # real signature unknown; restored from __doc__
    """ svn_repos_parser_fns_t_new_node_record_get( self) -> svn_error_t """
    pass

def svn_repos_parser_fns_t_new_node_record_set(self, svn_error_t_new_node_record): # real signature unknown; restored from __doc__
    """ svn_repos_parser_fns_t_new_node_record_set( self, svn_error_t new_node_record) """
    pass

def svn_repos_parser_fns_t_new_revision_record_get(self): # real signature unknown; restored from __doc__
    """ svn_repos_parser_fns_t_new_revision_record_get( self) -> svn_error_t """
    pass

def svn_repos_parser_fns_t_new_revision_record_set(self, svn_error_t_new_revision_record): # real signature unknown; restored from __doc__
    """ svn_repos_parser_fns_t_new_revision_record_set( self, svn_error_t new_revision_record) """
    pass

def svn_repos_parser_fns_t_remove_node_props_get(self): # real signature unknown; restored from __doc__
    """ svn_repos_parser_fns_t_remove_node_props_get( self) -> svn_error_t """
    pass

def svn_repos_parser_fns_t_remove_node_props_set(self, svn_error_t_remove_node_props): # real signature unknown; restored from __doc__
    """ svn_repos_parser_fns_t_remove_node_props_set( self, svn_error_t remove_node_props) """
    pass

def svn_repos_parser_fns_t_set_fulltext_get(self): # real signature unknown; restored from __doc__
    """ svn_repos_parser_fns_t_set_fulltext_get( self) -> svn_error_t """
    pass

def svn_repos_parser_fns_t_set_fulltext_set(self, svn_error_t_set_fulltext): # real signature unknown; restored from __doc__
    """ svn_repos_parser_fns_t_set_fulltext_set( self, svn_error_t set_fulltext) """
    pass

def svn_repos_parser_fns_t_set_node_property_get(self): # real signature unknown; restored from __doc__
    """ svn_repos_parser_fns_t_set_node_property_get( self) -> svn_error_t """
    pass

def svn_repos_parser_fns_t_set_node_property_set(self, svn_error_t_set_node_property): # real signature unknown; restored from __doc__
    """ svn_repos_parser_fns_t_set_node_property_set( self, svn_error_t set_node_property) """
    pass

def svn_repos_parser_fns_t_set_revision_property_get(self): # real signature unknown; restored from __doc__
    """ svn_repos_parser_fns_t_set_revision_property_get( self) -> svn_error_t """
    pass

def svn_repos_parser_fns_t_set_revision_property_set(self, svn_error_t_set_revision_property): # real signature unknown; restored from __doc__
    """ svn_repos_parser_fns_t_set_revision_property_set( self, svn_error_t set_revision_property) """
    pass

def svn_repos_parser_fns_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def svn_repos_parser_fns_t_uuid_record_get(self): # real signature unknown; restored from __doc__
    """ svn_repos_parser_fns_t_uuid_record_get( self) -> svn_error_t """
    pass

def svn_repos_parser_fns_t_uuid_record_set(self, svn_error_t_uuid_record): # real signature unknown; restored from __doc__
    """ svn_repos_parser_fns_t_uuid_record_set( self, svn_error_t uuid_record) """
    pass

def svn_repos_parse_dumpstream(svn_stream_t_stream, parse_fns, void_parse_baton, svn_cancel_func_t_cancel_func, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_repos_parse_dumpstream(svn_stream_t stream,  parse_fns, void parse_baton, 
        svn_cancel_func_t cancel_func, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_repos_parse_dumpstream2(svn_stream_t_stream, svn_repos_parse_fns2_t_parse_fns, void_parse_baton, svn_cancel_func_t_cancel_func, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_repos_parse_dumpstream2(svn_stream_t stream, svn_repos_parse_fns2_t parse_fns, 
        void parse_baton, svn_cancel_func_t cancel_func, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_repos_parse_fns2_invoke_apply_textdelta(svn_repos_parse_fns2_t__obj, svn_txdelta_window_handler_t_handler, void_handler_baton, void_node_baton): # real signature unknown; restored from __doc__
    """
    svn_repos_parse_fns2_invoke_apply_textdelta(svn_repos_parse_fns2_t _obj, svn_txdelta_window_handler_t handler, 
        void handler_baton, void node_baton) -> svn_error_t
    """
    pass

def svn_repos_parse_fns2_invoke_close_node(svn_repos_parse_fns2_t__obj, void_node_baton): # real signature unknown; restored from __doc__
    """ svn_repos_parse_fns2_invoke_close_node(svn_repos_parse_fns2_t _obj, void node_baton) -> svn_error_t """
    pass

def svn_repos_parse_fns2_invoke_close_revision(svn_repos_parse_fns2_t__obj, void_revision_baton): # real signature unknown; restored from __doc__
    """ svn_repos_parse_fns2_invoke_close_revision(svn_repos_parse_fns2_t _obj, void revision_baton) -> svn_error_t """
    pass

def svn_repos_parse_fns2_invoke_delete_node_property(svn_repos_parse_fns2_t__obj, void_node_baton, char_name): # real signature unknown; restored from __doc__
    """ svn_repos_parse_fns2_invoke_delete_node_property(svn_repos_parse_fns2_t _obj, void node_baton, char name) -> svn_error_t """
    pass

def svn_repos_parse_fns2_invoke_new_node_record(svn_repos_parse_fns2_t__obj, void_node_baton, apr_hash_t_headers, void_revision_baton, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_repos_parse_fns2_invoke_new_node_record(svn_repos_parse_fns2_t _obj, void node_baton, apr_hash_t headers, 
        void revision_baton, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_repos_parse_fns2_invoke_new_revision_record(svn_repos_parse_fns2_t__obj, void_revision_baton, apr_hash_t_headers, void_parse_baton, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_repos_parse_fns2_invoke_new_revision_record(svn_repos_parse_fns2_t _obj, void revision_baton, apr_hash_t headers, 
        void parse_baton, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_repos_parse_fns2_invoke_remove_node_props(svn_repos_parse_fns2_t__obj, void_node_baton): # real signature unknown; restored from __doc__
    """ svn_repos_parse_fns2_invoke_remove_node_props(svn_repos_parse_fns2_t _obj, void node_baton) -> svn_error_t """
    pass

def svn_repos_parse_fns2_invoke_set_fulltext(svn_repos_parse_fns2_t__obj, svn_stream_t_stream, void_node_baton): # real signature unknown; restored from __doc__
    """ svn_repos_parse_fns2_invoke_set_fulltext(svn_repos_parse_fns2_t _obj, svn_stream_t stream, void node_baton) -> svn_error_t """
    pass

def svn_repos_parse_fns2_invoke_set_node_property(svn_repos_parse_fns2_t__obj, void_node_baton, char_name, svn_string_t_value): # real signature unknown; restored from __doc__
    """
    svn_repos_parse_fns2_invoke_set_node_property(svn_repos_parse_fns2_t _obj, void node_baton, char name, 
        svn_string_t value) -> svn_error_t
    """
    pass

def svn_repos_parse_fns2_invoke_set_revision_property(svn_repos_parse_fns2_t__obj, void_revision_baton, char_name, svn_string_t_value): # real signature unknown; restored from __doc__
    """
    svn_repos_parse_fns2_invoke_set_revision_property(svn_repos_parse_fns2_t _obj, void revision_baton, char name, 
        svn_string_t value) -> svn_error_t
    """
    pass

def svn_repos_parse_fns2_invoke_uuid_record(svn_repos_parse_fns2_t__obj, char_uuid, void_parse_baton, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_repos_parse_fns2_invoke_uuid_record(svn_repos_parse_fns2_t _obj, char uuid, void parse_baton, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_repos_parse_fns2_t_apply_textdelta_get(svn_repos_parse_fns2_t_self): # real signature unknown; restored from __doc__
    """ svn_repos_parse_fns2_t_apply_textdelta_get(svn_repos_parse_fns2_t self) -> svn_error_t """
    pass

def svn_repos_parse_fns2_t_apply_textdelta_set(svn_repos_parse_fns2_t_self, svn_error_t_apply_textdelta): # real signature unknown; restored from __doc__
    """ svn_repos_parse_fns2_t_apply_textdelta_set(svn_repos_parse_fns2_t self, svn_error_t apply_textdelta) """
    pass

def svn_repos_parse_fns2_t_close_node_get(svn_repos_parse_fns2_t_self): # real signature unknown; restored from __doc__
    """ svn_repos_parse_fns2_t_close_node_get(svn_repos_parse_fns2_t self) -> svn_error_t """
    pass

def svn_repos_parse_fns2_t_close_node_set(svn_repos_parse_fns2_t_self, svn_error_t_close_node): # real signature unknown; restored from __doc__
    """ svn_repos_parse_fns2_t_close_node_set(svn_repos_parse_fns2_t self, svn_error_t close_node) """
    pass

def svn_repos_parse_fns2_t_close_revision_get(svn_repos_parse_fns2_t_self): # real signature unknown; restored from __doc__
    """ svn_repos_parse_fns2_t_close_revision_get(svn_repos_parse_fns2_t self) -> svn_error_t """
    pass

def svn_repos_parse_fns2_t_close_revision_set(svn_repos_parse_fns2_t_self, svn_error_t_close_revision): # real signature unknown; restored from __doc__
    """ svn_repos_parse_fns2_t_close_revision_set(svn_repos_parse_fns2_t self, svn_error_t close_revision) """
    pass

def svn_repos_parse_fns2_t_delete_node_property_get(svn_repos_parse_fns2_t_self): # real signature unknown; restored from __doc__
    """ svn_repos_parse_fns2_t_delete_node_property_get(svn_repos_parse_fns2_t self) -> svn_error_t """
    pass

def svn_repos_parse_fns2_t_delete_node_property_set(svn_repos_parse_fns2_t_self, svn_error_t_delete_node_property): # real signature unknown; restored from __doc__
    """ svn_repos_parse_fns2_t_delete_node_property_set(svn_repos_parse_fns2_t self, svn_error_t delete_node_property) """
    pass

def svn_repos_parse_fns2_t_new_node_record_get(svn_repos_parse_fns2_t_self): # real signature unknown; restored from __doc__
    """ svn_repos_parse_fns2_t_new_node_record_get(svn_repos_parse_fns2_t self) -> svn_error_t """
    pass

def svn_repos_parse_fns2_t_new_node_record_set(svn_repos_parse_fns2_t_self, svn_error_t_new_node_record): # real signature unknown; restored from __doc__
    """ svn_repos_parse_fns2_t_new_node_record_set(svn_repos_parse_fns2_t self, svn_error_t new_node_record) """
    pass

def svn_repos_parse_fns2_t_new_revision_record_get(svn_repos_parse_fns2_t_self): # real signature unknown; restored from __doc__
    """ svn_repos_parse_fns2_t_new_revision_record_get(svn_repos_parse_fns2_t self) -> svn_error_t """
    pass

def svn_repos_parse_fns2_t_new_revision_record_set(svn_repos_parse_fns2_t_self, svn_error_t_new_revision_record): # real signature unknown; restored from __doc__
    """ svn_repos_parse_fns2_t_new_revision_record_set(svn_repos_parse_fns2_t self, svn_error_t new_revision_record) """
    pass

def svn_repos_parse_fns2_t_remove_node_props_get(svn_repos_parse_fns2_t_self): # real signature unknown; restored from __doc__
    """ svn_repos_parse_fns2_t_remove_node_props_get(svn_repos_parse_fns2_t self) -> svn_error_t """
    pass

def svn_repos_parse_fns2_t_remove_node_props_set(svn_repos_parse_fns2_t_self, svn_error_t_remove_node_props): # real signature unknown; restored from __doc__
    """ svn_repos_parse_fns2_t_remove_node_props_set(svn_repos_parse_fns2_t self, svn_error_t remove_node_props) """
    pass

def svn_repos_parse_fns2_t_set_fulltext_get(svn_repos_parse_fns2_t_self): # real signature unknown; restored from __doc__
    """ svn_repos_parse_fns2_t_set_fulltext_get(svn_repos_parse_fns2_t self) -> svn_error_t """
    pass

def svn_repos_parse_fns2_t_set_fulltext_set(svn_repos_parse_fns2_t_self, svn_error_t_set_fulltext): # real signature unknown; restored from __doc__
    """ svn_repos_parse_fns2_t_set_fulltext_set(svn_repos_parse_fns2_t self, svn_error_t set_fulltext) """
    pass

def svn_repos_parse_fns2_t_set_node_property_get(svn_repos_parse_fns2_t_self): # real signature unknown; restored from __doc__
    """ svn_repos_parse_fns2_t_set_node_property_get(svn_repos_parse_fns2_t self) -> svn_error_t """
    pass

def svn_repos_parse_fns2_t_set_node_property_set(svn_repos_parse_fns2_t_self, svn_error_t_set_node_property): # real signature unknown; restored from __doc__
    """ svn_repos_parse_fns2_t_set_node_property_set(svn_repos_parse_fns2_t self, svn_error_t set_node_property) """
    pass

def svn_repos_parse_fns2_t_set_revision_property_get(svn_repos_parse_fns2_t_self): # real signature unknown; restored from __doc__
    """ svn_repos_parse_fns2_t_set_revision_property_get(svn_repos_parse_fns2_t self) -> svn_error_t """
    pass

def svn_repos_parse_fns2_t_set_revision_property_set(svn_repos_parse_fns2_t_self, svn_error_t_set_revision_property): # real signature unknown; restored from __doc__
    """ svn_repos_parse_fns2_t_set_revision_property_set(svn_repos_parse_fns2_t self, svn_error_t set_revision_property) """
    pass

def svn_repos_parse_fns2_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def svn_repos_parse_fns2_t_uuid_record_get(svn_repos_parse_fns2_t_self): # real signature unknown; restored from __doc__
    """ svn_repos_parse_fns2_t_uuid_record_get(svn_repos_parse_fns2_t self) -> svn_error_t """
    pass

def svn_repos_parse_fns2_t_uuid_record_set(svn_repos_parse_fns2_t_self, svn_error_t_uuid_record): # real signature unknown; restored from __doc__
    """ svn_repos_parse_fns2_t_uuid_record_set(svn_repos_parse_fns2_t self, svn_error_t uuid_record) """
    pass

def svn_repos_path(svn_repos_t_repos, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_repos_path(svn_repos_t repos, apr_pool_t pool) -> char """
    return ""

def svn_repos_post_commit_hook(svn_repos_t_repos, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_repos_post_commit_hook(svn_repos_t repos, apr_pool_t pool) -> char """
    return ""

def svn_repos_post_lock_hook(svn_repos_t_repos, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_repos_post_lock_hook(svn_repos_t repos, apr_pool_t pool) -> char """
    return ""

def svn_repos_post_revprop_change_hook(svn_repos_t_repos, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_repos_post_revprop_change_hook(svn_repos_t repos, apr_pool_t pool) -> char """
    return ""

def svn_repos_post_unlock_hook(svn_repos_t_repos, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_repos_post_unlock_hook(svn_repos_t repos, apr_pool_t pool) -> char """
    return ""

def svn_repos_pre_commit_hook(svn_repos_t_repos, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_repos_pre_commit_hook(svn_repos_t repos, apr_pool_t pool) -> char """
    return ""

def svn_repos_pre_lock_hook(svn_repos_t_repos, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_repos_pre_lock_hook(svn_repos_t repos, apr_pool_t pool) -> char """
    return ""

def svn_repos_pre_revprop_change_hook(svn_repos_t_repos, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_repos_pre_revprop_change_hook(svn_repos_t repos, apr_pool_t pool) -> char """
    return ""

def svn_repos_pre_unlock_hook(svn_repos_t_repos, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_repos_pre_unlock_hook(svn_repos_t repos, apr_pool_t pool) -> char """
    return ""

def svn_repos_recover(char_path, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_repos_recover(char path, apr_pool_t pool) -> svn_error_t """
    pass

def svn_repos_recover2(char_path, svn_boolean_t_nonblocking, svn_error_t_start_callback, void_start_callback_baton, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_repos_recover2(char path, svn_boolean_t nonblocking, svn_error_t start_callback, 
        void start_callback_baton, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_repos_recover3(char_path, svn_boolean_t_nonblocking, svn_error_t_start_callback, void_start_callback_baton, svn_cancel_func_t_cancel_func, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_repos_recover3(char path, svn_boolean_t nonblocking, svn_error_t start_callback, 
        void start_callback_baton, svn_cancel_func_t cancel_func, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_repos_remember_client_capabilities(svn_repos_t_repos, apr_array_header_t_capabilities): # real signature unknown; restored from __doc__
    """ svn_repos_remember_client_capabilities(svn_repos_t repos, apr_array_header_t capabilities) -> svn_error_t """
    pass

def svn_repos_replay(svn_fs_root_t_root, svn_delta_editor_t_editor, void_edit_baton, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_repos_replay(svn_fs_root_t root, svn_delta_editor_t editor, void edit_baton, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_repos_replay2(svn_fs_root_t_root, char_base_dir, svn_revnum_t_low_water_mark, svn_boolean_t_send_deltas, svn_delta_editor_t_editor, void_edit_baton, svn_repos_authz_func_t_authz_read_func, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_repos_replay2(svn_fs_root_t root, char base_dir, svn_revnum_t low_water_mark, 
        svn_boolean_t send_deltas, svn_delta_editor_t editor, 
        void edit_baton, svn_repos_authz_func_t authz_read_func, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_repos_set_path(void_report_baton, char_path, svn_revnum_t_revision, svn_boolean_t_start_empty, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_repos_set_path(void report_baton, char path, svn_revnum_t revision, 
        svn_boolean_t start_empty, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_repos_set_path2(void_report_baton, char_path, svn_revnum_t_revision, svn_boolean_t_start_empty, char_lock_token, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_repos_set_path2(void report_baton, char path, svn_revnum_t revision, 
        svn_boolean_t start_empty, char lock_token, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_repos_set_path3(void_report_baton, char_path, svn_revnum_t_revision, svn_depth_t_depth, svn_boolean_t_start_empty, char_lock_token, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_repos_set_path3(void report_baton, char path, svn_revnum_t revision, 
        svn_depth_t depth, svn_boolean_t start_empty, 
        char lock_token, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_repos_start_commit_hook(svn_repos_t_repos, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_repos_start_commit_hook(svn_repos_t repos, apr_pool_t pool) -> char """
    return ""

def svn_repos_stat(svn_dirent_t_dirent, svn_fs_root_t_root, char_path, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_repos_stat(svn_dirent_t dirent, svn_fs_root_t root, char path, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_repos_svnserve_conf(svn_repos_t_repos, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_repos_svnserve_conf(svn_repos_t repos, apr_pool_t pool) -> char """
    return ""

def svn_repos_trace_node_locations(svn_fs_t_fs, apr_hash_t_locations, char_fs_path, svn_revnum_t_peg_revision, apr_array_header_t_location_revisions, svn_repos_authz_func_t_authz_read_func, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_repos_trace_node_locations(svn_fs_t fs, apr_hash_t locations, char fs_path, svn_revnum_t peg_revision, 
        apr_array_header_t location_revisions, 
        svn_repos_authz_func_t authz_read_func, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_repos_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def svn_repos_upgrade(char_path, svn_boolean_t_nonblocking, svn_error_t_start_callback, void_start_callback_baton, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_repos_upgrade(char path, svn_boolean_t nonblocking, svn_error_t start_callback, 
        void start_callback_baton, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_repos_verify_fs(svn_repos_t_repos, svn_stream_t_feedback_stream, svn_revnum_t_start_rev, svn_revnum_t_end_rev, svn_cancel_func_t_cancel_func, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_repos_verify_fs(svn_repos_t repos, svn_stream_t feedback_stream, svn_revnum_t start_rev, 
        svn_revnum_t end_rev, svn_cancel_func_t cancel_func, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_repos_version(): # real signature unknown; restored from __doc__
    """ svn_repos_version() -> svn_version_t """
    pass

# no classes
