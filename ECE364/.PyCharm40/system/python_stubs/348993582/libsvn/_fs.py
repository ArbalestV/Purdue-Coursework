# encoding: utf-8
# module libsvn._fs
# from /usr/lib64/python2.6/site-packages/libsvn/_fs.so
# by generator 1.136
# no doc
# no imports

# Variables with simple values

SVN_FS_CONFIG_BDB_LOG_AUTOREMOVE = 'bdb-log-autoremove'

SVN_FS_CONFIG_BDB_TXN_NOSYNC = 'bdb-txn-nosync'

SVN_FS_CONFIG_FS_TYPE = 'fs-type'

SVN_FS_CONFIG_PRE_1_4_COMPATIBLE = 'pre-1.4-compatible'

SVN_FS_CONFIG_PRE_1_5_COMPATIBLE = 'pre-1.5-compatible'

SVN_FS_CONFIG_PRE_1_6_COMPATIBLE = 'pre-1.6-compatible'

svn_fs_pack_notify_end = 1
svn_fs_pack_notify_start = 0

svn_fs_path_change_add = 1
svn_fs_path_change_delete = 2
svn_fs_path_change_modify = 0
svn_fs_path_change_replace = 3
svn_fs_path_change_reset = 4

SVN_FS_TXN_CHECK_LOCKS = 2
SVN_FS_TXN_CHECK_OOD = 1

SVN_FS_TYPE_BDB = 'bdb'
SVN_FS_TYPE_FSFS = 'fsfs'

# functions

def svn_fs_abort_txn(svn_fs_txn_t_txn, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_fs_abort_txn(svn_fs_txn_t txn, apr_pool_t pool) -> svn_error_t """
    pass

def svn_fs_access_add_lock_token(svn_fs_access_t_access_ctx, char_token): # real signature unknown; restored from __doc__
    """ svn_fs_access_add_lock_token(svn_fs_access_t access_ctx, char token) -> svn_error_t """
    pass

def svn_fs_access_add_lock_token2(svn_fs_access_t_access_ctx, char_path, char_token): # real signature unknown; restored from __doc__
    """ svn_fs_access_add_lock_token2(svn_fs_access_t access_ctx, char path, char token) -> svn_error_t """
    pass

def svn_fs_access_get_username(char_username, svn_fs_access_t_access_ctx): # real signature unknown; restored from __doc__
    """ svn_fs_access_get_username(char username, svn_fs_access_t access_ctx) -> svn_error_t """
    pass

def svn_fs_access_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def svn_fs_apply_text(svn_stream_t_contents_p, svn_fs_root_t_root, char_path, char_result_checksum, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_fs_apply_text(svn_stream_t contents_p, svn_fs_root_t root, char path, 
        char result_checksum, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_fs_apply_textdelta(svn_txdelta_window_handler_t_contents_p, void_contents_baton_p, svn_fs_root_t_root, char_path, char_base_checksum, char_result_checksum, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_fs_apply_textdelta(svn_txdelta_window_handler_t contents_p, void contents_baton_p, 
        svn_fs_root_t root, char path, char base_checksum, 
        char result_checksum, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_fs_begin_txn(svn_fs_txn_t_txn_p, svn_fs_t_fs, svn_revnum_t_rev, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_fs_begin_txn(svn_fs_txn_t txn_p, svn_fs_t fs, svn_revnum_t rev, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_fs_begin_txn2(svn_fs_txn_t_txn_p, svn_fs_t_fs, svn_revnum_t_rev, apr_uint32_t_flags, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_fs_begin_txn2(svn_fs_txn_t txn_p, svn_fs_t fs, svn_revnum_t rev, 
        apr_uint32_t flags, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_fs_berkeley_logfiles(apr_array_header_t_logfiles, char_path, svn_boolean_t_only_unused, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_fs_berkeley_logfiles(apr_array_header_t logfiles, char path, svn_boolean_t only_unused, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_fs_berkeley_path(svn_fs_t_fs, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_fs_berkeley_path(svn_fs_t fs, apr_pool_t pool) -> char """
    return ""

def svn_fs_berkeley_recover(char_path, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_fs_berkeley_recover(char path, apr_pool_t pool) -> svn_error_t """
    pass

def svn_fs_change_node_prop(svn_fs_root_t_root, char_path, char_name, svn_string_t_value, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_fs_change_node_prop(svn_fs_root_t root, char path, char name, svn_string_t value, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_fs_change_rev_prop(svn_fs_t_fs, svn_revnum_t_rev, char_name, svn_string_t_value, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_fs_change_rev_prop(svn_fs_t fs, svn_revnum_t rev, char name, svn_string_t value, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_fs_change_txn_prop(svn_fs_txn_t_txn, char_name, svn_string_t_value, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_fs_change_txn_prop(svn_fs_txn_t txn, char name, svn_string_t value, apr_pool_t pool) -> svn_error_t """
    pass

def svn_fs_change_txn_props(svn_fs_txn_t_txn, apr_array_header_t_props, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_fs_change_txn_props(svn_fs_txn_t txn, apr_array_header_t props, apr_pool_t pool) -> svn_error_t """
    pass

def svn_fs_check_path(svn_node_kind_t_kind_p, svn_fs_root_t_root, char_path, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_fs_check_path(svn_node_kind_t kind_p, svn_fs_root_t root, char path, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_fs_check_related(svn_fs_id_t_id1, svn_fs_id_t_id2): # real signature unknown; restored from __doc__
    """ svn_fs_check_related(svn_fs_id_t id1, svn_fs_id_t id2) -> svn_boolean_t """
    pass

def svn_fs_closest_copy(svn_fs_root_t_root_p, char_path_p, svn_fs_root_t_root, char_path, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_fs_closest_copy(svn_fs_root_t root_p, char path_p, svn_fs_root_t root, 
        char path, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_fs_close_root(svn_fs_root_t_root): # real signature unknown; restored from __doc__
    """ svn_fs_close_root(svn_fs_root_t root) """
    pass

def svn_fs_commit_txn(char_conflict_p, svn_revnum_t_new_rev, svn_fs_txn_t_txn, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_fs_commit_txn(char conflict_p, svn_revnum_t new_rev, svn_fs_txn_t txn, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_fs_compare_ids(svn_fs_id_t_a, svn_fs_id_t_b): # real signature unknown; restored from __doc__
    """ svn_fs_compare_ids(svn_fs_id_t a, svn_fs_id_t b) -> int """
    return 0

def svn_fs_contents_changed(svn_boolean_t_changed_p, svn_fs_root_t_root1, char_path1, svn_fs_root_t_root2, char_path2, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_fs_contents_changed(svn_boolean_t changed_p, svn_fs_root_t root1, char path1, 
        svn_fs_root_t root2, char path2, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_fs_copied_from(svn_revnum_t_rev_p, char_path_p, svn_fs_root_t_root, char_path, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_fs_copied_from(svn_revnum_t rev_p, char path_p, svn_fs_root_t root, 
        char path, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_fs_copy(svn_fs_root_t_from_root, char_from_path, svn_fs_root_t_to_root, char_to_path, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_fs_copy(svn_fs_root_t from_root, char from_path, svn_fs_root_t to_root, 
        char to_path, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_fs_create(svn_fs_t_fs_p, char_path, apr_hash_t_fs_config, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_fs_create(svn_fs_t fs_p, char path, apr_hash_t fs_config, apr_pool_t pool) -> svn_error_t """
    pass

def svn_fs_create_access(svn_fs_access_t_access_ctx, char_username, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_fs_create_access(svn_fs_access_t access_ctx, char username, apr_pool_t pool) -> svn_error_t """
    pass

def svn_fs_create_berkeley(svn_fs_t_fs, char_path): # real signature unknown; restored from __doc__
    """ svn_fs_create_berkeley(svn_fs_t fs, char path) -> svn_error_t """
    pass

def svn_fs_delete(svn_fs_root_t_root, char_path, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_fs_delete(svn_fs_root_t root, char path, apr_pool_t pool) -> svn_error_t """
    pass

def svn_fs_delete_berkeley(char_path, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_fs_delete_berkeley(char path, apr_pool_t pool) -> svn_error_t """
    pass

def svn_fs_delete_fs(char_path, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_fs_delete_fs(char path, apr_pool_t pool) -> svn_error_t """
    pass

def svn_fs_deltify_revision(svn_fs_t_fs, svn_revnum_t_revision, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_fs_deltify_revision(svn_fs_t fs, svn_revnum_t revision, apr_pool_t pool) -> svn_error_t """
    pass

def svn_fs_dirent_t_id_get(svn_fs_dirent_t_self): # real signature unknown; restored from __doc__
    """ svn_fs_dirent_t_id_get(svn_fs_dirent_t self) -> svn_fs_id_t """
    pass

def svn_fs_dirent_t_id_set(svn_fs_dirent_t_self, svn_fs_id_t_id): # real signature unknown; restored from __doc__
    """ svn_fs_dirent_t_id_set(svn_fs_dirent_t self, svn_fs_id_t id) """
    pass

def svn_fs_dirent_t_kind_get(svn_fs_dirent_t_self): # real signature unknown; restored from __doc__
    """ svn_fs_dirent_t_kind_get(svn_fs_dirent_t self) -> svn_node_kind_t """
    pass

def svn_fs_dirent_t_kind_set(svn_fs_dirent_t_self, svn_node_kind_t_kind): # real signature unknown; restored from __doc__
    """ svn_fs_dirent_t_kind_set(svn_fs_dirent_t self, svn_node_kind_t kind) """
    pass

def svn_fs_dirent_t_name_get(svn_fs_dirent_t_self): # real signature unknown; restored from __doc__
    """ svn_fs_dirent_t_name_get(svn_fs_dirent_t self) -> char """
    return ""

def svn_fs_dirent_t_name_set(svn_fs_dirent_t_self, char_name): # real signature unknown; restored from __doc__
    """ svn_fs_dirent_t_name_set(svn_fs_dirent_t self, char name) """
    pass

def svn_fs_dirent_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def svn_fs_dir_entries(apr_hash_t_entries_p, svn_fs_root_t_root, char_path, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_fs_dir_entries(apr_hash_t entries_p, svn_fs_root_t root, char path, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_fs_file_checksum(svn_checksum_t_checksum, svn_checksum_kind_t_kind, svn_fs_root_t_root, char_path, svn_boolean_t_force, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_fs_file_checksum(svn_checksum_t checksum, svn_checksum_kind_t kind, 
        svn_fs_root_t root, char path, svn_boolean_t force, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_fs_file_contents(svn_stream_t_contents, svn_fs_root_t_root, char_path, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_fs_file_contents(svn_stream_t contents, svn_fs_root_t root, char path, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_fs_file_length(svn_filesize_t_length_p, svn_fs_root_t_root, char_path, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_fs_file_length(svn_filesize_t length_p, svn_fs_root_t root, char path, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_fs_file_md5_checksum(unsigned_char_digest, svn_fs_root_t_root, char_path, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_fs_file_md5_checksum(unsigned char digest, svn_fs_root_t root, char path, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_fs_generate_lock_token(char_token, svn_fs_t_fs, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_fs_generate_lock_token(char token, svn_fs_t fs, apr_pool_t pool) -> svn_error_t """
    pass

def svn_fs_get_access(svn_fs_access_t_access_ctx, svn_fs_t_fs): # real signature unknown; restored from __doc__
    """ svn_fs_get_access(svn_fs_access_t access_ctx, svn_fs_t fs) -> svn_error_t """
    pass

def svn_fs_get_file_delta_stream(svn_txdelta_stream_t_stream_p, svn_fs_root_t_source_root, char_source_path, svn_fs_root_t_target_root, char_target_path, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_fs_get_file_delta_stream(svn_txdelta_stream_t stream_p, svn_fs_root_t source_root, 
        char source_path, svn_fs_root_t target_root, 
        char target_path, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_fs_get_lock(svn_lock_t_lock, svn_fs_t_fs, char_path, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_fs_get_lock(svn_lock_t lock, svn_fs_t fs, char path, apr_pool_t pool) -> svn_error_t """
    pass

def svn_fs_get_locks(svn_fs_t_fs, char_path, svn_fs_get_locks_callback_t_get_locks_func, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_fs_get_locks(svn_fs_t fs, char path, svn_fs_get_locks_callback_t get_locks_func, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_fs_get_locks_callback_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def svn_fs_get_mergeinfo(svn_mergeinfo_catalog_t_catalog, svn_fs_root_t_root, apr_array_header_t_paths, svn_mergeinfo_inheritance_t_inherit, svn_boolean_t_include_descendants, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_fs_get_mergeinfo(svn_mergeinfo_catalog_t catalog, svn_fs_root_t root, 
        apr_array_header_t paths, svn_mergeinfo_inheritance_t inherit, 
        svn_boolean_t include_descendants, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_fs_get_uuid(svn_fs_t_fs, char_uuid, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_fs_get_uuid(svn_fs_t fs, char uuid, apr_pool_t pool) -> svn_error_t """
    pass

def svn_fs_history_location(char_path, svn_revnum_t_revision, svn_fs_history_t_history, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_fs_history_location(char path, svn_revnum_t revision, svn_fs_history_t history, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_fs_history_prev(svn_fs_history_t_prev_history_p, svn_fs_history_t_history, svn_boolean_t_cross_copies, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_fs_history_prev(svn_fs_history_t prev_history_p, svn_fs_history_t history, 
        svn_boolean_t cross_copies, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_fs_history_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def svn_fs_hotcopy(char_src_path, char_dest_path, svn_boolean_t_clean, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_fs_hotcopy(char src_path, char dest_path, svn_boolean_t clean, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_fs_hotcopy_berkeley(char_src_path, char_dest_path, svn_boolean_t_clean_logs, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_fs_hotcopy_berkeley(char src_path, char dest_path, svn_boolean_t clean_logs, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_fs_id_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def svn_fs_initialize(apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_fs_initialize(apr_pool_t pool) -> svn_error_t """
    pass

def svn_fs_invoke_get_locks_callback(svn_fs_get_locks_callback_t__obj, void_baton, svn_lock_t_lock, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_fs_invoke_get_locks_callback(svn_fs_get_locks_callback_t _obj, void baton, svn_lock_t lock, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_fs_invoke_pack_notify(svn_fs_pack_notify_t__obj, void_baton, apr_int64_t_shard, svn_fs_pack_notify_action_t_action, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_fs_invoke_pack_notify(svn_fs_pack_notify_t _obj, void baton, apr_int64_t shard, 
        svn_fs_pack_notify_action_t action, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_fs_invoke_warning_callback(svn_fs_warning_callback_t__obj, void_baton, svn_error_t_err): # real signature unknown; restored from __doc__
    """ svn_fs_invoke_warning_callback(svn_fs_warning_callback_t _obj, void baton, svn_error_t err) """
    pass

def svn_fs_is_dir(svn_boolean_t_is_dir, svn_fs_root_t_root, char_path, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_fs_is_dir(svn_boolean_t is_dir, svn_fs_root_t root, char path, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_fs_is_file(svn_boolean_t_is_file, svn_fs_root_t_root, char_path, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_fs_is_file(svn_boolean_t is_file, svn_fs_root_t root, char path, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_fs_is_revision_root(svn_fs_root_t_root): # real signature unknown; restored from __doc__
    """ svn_fs_is_revision_root(svn_fs_root_t root) -> svn_boolean_t """
    pass

def svn_fs_is_txn_root(svn_fs_root_t_root): # real signature unknown; restored from __doc__
    """ svn_fs_is_txn_root(svn_fs_root_t root) -> svn_boolean_t """
    pass

def svn_fs_list_transactions(apr_array_header_t_names_p, svn_fs_t_fs, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_fs_list_transactions(apr_array_header_t names_p, svn_fs_t fs, apr_pool_t pool) -> svn_error_t """
    pass

def svn_fs_lock(svn_lock_t_lock, svn_fs_t_fs, char_path, char_token, char_comment, svn_boolean_t_is_dav_comment, apr_time_t_expiration_date, svn_revnum_t_current_rev, svn_boolean_t_steal_lock, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_fs_lock(svn_lock_t lock, svn_fs_t fs, char path, char token, 
        char comment, svn_boolean_t is_dav_comment, 
        apr_time_t expiration_date, svn_revnum_t current_rev, 
        svn_boolean_t steal_lock, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_fs_make_dir(svn_fs_root_t_root, char_path, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_fs_make_dir(svn_fs_root_t root, char path, apr_pool_t pool) -> svn_error_t """
    pass

def svn_fs_make_file(svn_fs_root_t_root, char_path, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_fs_make_file(svn_fs_root_t root, char path, apr_pool_t pool) -> svn_error_t """
    pass

def svn_fs_merge(char_conflict_p, svn_fs_root_t_source_root, char_source_path, svn_fs_root_t_target_root, char_target_path, svn_fs_root_t_ancestor_root, char_ancestor_path, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_fs_merge(char conflict_p, svn_fs_root_t source_root, char source_path, 
        svn_fs_root_t target_root, char target_path, 
        svn_fs_root_t ancestor_root, char ancestor_path, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_fs_new(apr_hash_t_fs_config, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_fs_new(apr_hash_t fs_config, apr_pool_t pool) -> svn_fs_t """
    pass

def svn_fs_node_created_path(char_created_path, svn_fs_root_t_root, char_path, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_fs_node_created_path(char created_path, svn_fs_root_t root, char path, apr_pool_t pool) -> svn_error_t """
    pass

def svn_fs_node_created_rev(svn_revnum_t_revision, svn_fs_root_t_root, char_path, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_fs_node_created_rev(svn_revnum_t revision, svn_fs_root_t root, char path, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_fs_node_history(svn_fs_history_t_history_p, svn_fs_root_t_root, char_path, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_fs_node_history(svn_fs_history_t history_p, svn_fs_root_t root, char path, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_fs_node_id(svn_fs_id_t_id_p, svn_fs_root_t_root, char_path, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_fs_node_id(svn_fs_id_t id_p, svn_fs_root_t root, char path, apr_pool_t pool) -> svn_error_t """
    pass

def svn_fs_node_origin_rev(svn_revnum_t_revision, svn_fs_root_t_root, char_path, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_fs_node_origin_rev(svn_revnum_t revision, svn_fs_root_t root, char path, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_fs_node_prop(svn_string_t_value_p, svn_fs_root_t_root, char_path, char_propname, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_fs_node_prop(svn_string_t value_p, svn_fs_root_t root, char path, 
        char propname, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_fs_node_proplist(apr_hash_t_table_p, svn_fs_root_t_root, char_path, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_fs_node_proplist(apr_hash_t table_p, svn_fs_root_t root, char path, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_fs_open(svn_fs_t_fs_p, char_path, apr_hash_t_fs_config, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_fs_open(svn_fs_t fs_p, char path, apr_hash_t fs_config, apr_pool_t pool) -> svn_error_t """
    pass

def svn_fs_open_berkeley(svn_fs_t_fs, char_path): # real signature unknown; restored from __doc__
    """ svn_fs_open_berkeley(svn_fs_t fs, char path) -> svn_error_t """
    pass

def svn_fs_open_txn(svn_fs_txn_t_txn, svn_fs_t_fs, char_name, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_fs_open_txn(svn_fs_txn_t txn, svn_fs_t fs, char name, apr_pool_t pool) -> svn_error_t """
    pass

def svn_fs_pack(char_db_path, svn_fs_pack_notify_t_notify_func, void_notify_baton, svn_cancel_func_t_cancel_func, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_fs_pack(char db_path, svn_fs_pack_notify_t notify_func, void notify_baton, 
        svn_cancel_func_t cancel_func, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_fs_pack_notify_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def svn_fs_parse_id(char_data, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_fs_parse_id(char data, apr_pool_t pool) -> svn_fs_id_t """
    pass

def svn_fs_path(svn_fs_t_fs, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_fs_path(svn_fs_t fs, apr_pool_t pool) -> char """
    return ""

def svn_fs_paths_changed(apr_hash_t_changed_paths_p, svn_fs_root_t_root, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_fs_paths_changed(apr_hash_t changed_paths_p, svn_fs_root_t root, apr_pool_t pool) -> svn_error_t """
    pass

def svn_fs_paths_changed2(apr_hash_t_changed_paths_p, svn_fs_root_t_root, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_fs_paths_changed2(apr_hash_t changed_paths_p, svn_fs_root_t root, apr_pool_t pool) -> svn_error_t """
    pass

def svn_fs_path_change2_create(svn_fs_id_t_node_rev_id, svn_fs_path_change_kind_t_change_kind, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_fs_path_change2_create(svn_fs_id_t node_rev_id, svn_fs_path_change_kind_t change_kind, 
        apr_pool_t pool) -> svn_fs_path_change2_t
    """
    pass

def svn_fs_path_change2_t_change_kind_get(svn_fs_path_change2_t_self): # real signature unknown; restored from __doc__
    """ svn_fs_path_change2_t_change_kind_get(svn_fs_path_change2_t self) -> svn_fs_path_change_kind_t """
    pass

def svn_fs_path_change2_t_change_kind_set(svn_fs_path_change2_t_self, svn_fs_path_change_kind_t_change_kind): # real signature unknown; restored from __doc__
    """ svn_fs_path_change2_t_change_kind_set(svn_fs_path_change2_t self, svn_fs_path_change_kind_t change_kind) """
    pass

def svn_fs_path_change2_t_copyfrom_known_get(svn_fs_path_change2_t_self): # real signature unknown; restored from __doc__
    """ svn_fs_path_change2_t_copyfrom_known_get(svn_fs_path_change2_t self) -> svn_boolean_t """
    pass

def svn_fs_path_change2_t_copyfrom_known_set(svn_fs_path_change2_t_self, svn_boolean_t_copyfrom_known): # real signature unknown; restored from __doc__
    """ svn_fs_path_change2_t_copyfrom_known_set(svn_fs_path_change2_t self, svn_boolean_t copyfrom_known) """
    pass

def svn_fs_path_change2_t_copyfrom_path_get(svn_fs_path_change2_t_self): # real signature unknown; restored from __doc__
    """ svn_fs_path_change2_t_copyfrom_path_get(svn_fs_path_change2_t self) -> char """
    return ""

def svn_fs_path_change2_t_copyfrom_path_set(svn_fs_path_change2_t_self, char_copyfrom_path): # real signature unknown; restored from __doc__
    """ svn_fs_path_change2_t_copyfrom_path_set(svn_fs_path_change2_t self, char copyfrom_path) """
    pass

def svn_fs_path_change2_t_copyfrom_rev_get(svn_fs_path_change2_t_self): # real signature unknown; restored from __doc__
    """ svn_fs_path_change2_t_copyfrom_rev_get(svn_fs_path_change2_t self) -> svn_revnum_t """
    pass

def svn_fs_path_change2_t_copyfrom_rev_set(svn_fs_path_change2_t_self, svn_revnum_t_copyfrom_rev): # real signature unknown; restored from __doc__
    """ svn_fs_path_change2_t_copyfrom_rev_set(svn_fs_path_change2_t self, svn_revnum_t copyfrom_rev) """
    pass

def svn_fs_path_change2_t_node_kind_get(svn_fs_path_change2_t_self): # real signature unknown; restored from __doc__
    """ svn_fs_path_change2_t_node_kind_get(svn_fs_path_change2_t self) -> svn_node_kind_t """
    pass

def svn_fs_path_change2_t_node_kind_set(svn_fs_path_change2_t_self, svn_node_kind_t_node_kind): # real signature unknown; restored from __doc__
    """ svn_fs_path_change2_t_node_kind_set(svn_fs_path_change2_t self, svn_node_kind_t node_kind) """
    pass

def svn_fs_path_change2_t_node_rev_id_get(svn_fs_path_change2_t_self): # real signature unknown; restored from __doc__
    """ svn_fs_path_change2_t_node_rev_id_get(svn_fs_path_change2_t self) -> svn_fs_id_t """
    pass

def svn_fs_path_change2_t_node_rev_id_set(svn_fs_path_change2_t_self, svn_fs_id_t_node_rev_id): # real signature unknown; restored from __doc__
    """ svn_fs_path_change2_t_node_rev_id_set(svn_fs_path_change2_t self, svn_fs_id_t node_rev_id) """
    pass

def svn_fs_path_change2_t_prop_mod_get(svn_fs_path_change2_t_self): # real signature unknown; restored from __doc__
    """ svn_fs_path_change2_t_prop_mod_get(svn_fs_path_change2_t self) -> svn_boolean_t """
    pass

def svn_fs_path_change2_t_prop_mod_set(svn_fs_path_change2_t_self, svn_boolean_t_prop_mod): # real signature unknown; restored from __doc__
    """ svn_fs_path_change2_t_prop_mod_set(svn_fs_path_change2_t self, svn_boolean_t prop_mod) """
    pass

def svn_fs_path_change2_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def svn_fs_path_change2_t_text_mod_get(svn_fs_path_change2_t_self): # real signature unknown; restored from __doc__
    """ svn_fs_path_change2_t_text_mod_get(svn_fs_path_change2_t self) -> svn_boolean_t """
    pass

def svn_fs_path_change2_t_text_mod_set(svn_fs_path_change2_t_self, svn_boolean_t_text_mod): # real signature unknown; restored from __doc__
    """ svn_fs_path_change2_t_text_mod_set(svn_fs_path_change2_t self, svn_boolean_t text_mod) """
    pass

def svn_fs_path_change_t_change_kind_get(svn_fs_path_change_t_self): # real signature unknown; restored from __doc__
    """ svn_fs_path_change_t_change_kind_get(svn_fs_path_change_t self) -> svn_fs_path_change_kind_t """
    pass

def svn_fs_path_change_t_change_kind_set(svn_fs_path_change_t_self, svn_fs_path_change_kind_t_change_kind): # real signature unknown; restored from __doc__
    """ svn_fs_path_change_t_change_kind_set(svn_fs_path_change_t self, svn_fs_path_change_kind_t change_kind) """
    pass

def svn_fs_path_change_t_node_rev_id_get(svn_fs_path_change_t_self): # real signature unknown; restored from __doc__
    """ svn_fs_path_change_t_node_rev_id_get(svn_fs_path_change_t self) -> svn_fs_id_t """
    pass

def svn_fs_path_change_t_node_rev_id_set(svn_fs_path_change_t_self, svn_fs_id_t_node_rev_id): # real signature unknown; restored from __doc__
    """ svn_fs_path_change_t_node_rev_id_set(svn_fs_path_change_t self, svn_fs_id_t node_rev_id) """
    pass

def svn_fs_path_change_t_prop_mod_get(svn_fs_path_change_t_self): # real signature unknown; restored from __doc__
    """ svn_fs_path_change_t_prop_mod_get(svn_fs_path_change_t self) -> svn_boolean_t """
    pass

def svn_fs_path_change_t_prop_mod_set(svn_fs_path_change_t_self, svn_boolean_t_prop_mod): # real signature unknown; restored from __doc__
    """ svn_fs_path_change_t_prop_mod_set(svn_fs_path_change_t self, svn_boolean_t prop_mod) """
    pass

def svn_fs_path_change_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def svn_fs_path_change_t_text_mod_get(svn_fs_path_change_t_self): # real signature unknown; restored from __doc__
    """ svn_fs_path_change_t_text_mod_get(svn_fs_path_change_t self) -> svn_boolean_t """
    pass

def svn_fs_path_change_t_text_mod_set(svn_fs_path_change_t_self, svn_boolean_t_text_mod): # real signature unknown; restored from __doc__
    """ svn_fs_path_change_t_text_mod_set(svn_fs_path_change_t self, svn_boolean_t text_mod) """
    pass

def svn_fs_print_modules(svn_stringbuf_t_output, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_fs_print_modules(svn_stringbuf_t output, apr_pool_t pool) -> svn_error_t """
    pass

def svn_fs_props_changed(svn_boolean_t_changed_p, svn_fs_root_t_root1, char_path1, svn_fs_root_t_root2, char_path2, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_fs_props_changed(svn_boolean_t changed_p, svn_fs_root_t root1, char path1, 
        svn_fs_root_t root2, char path2, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_fs_purge_txn(svn_fs_t_fs, char_txn_id, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_fs_purge_txn(svn_fs_t fs, char txn_id, apr_pool_t pool) -> svn_error_t """
    pass

def svn_fs_recover(char_path, svn_cancel_func_t_cancel_func, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_fs_recover(char path, svn_cancel_func_t cancel_func, apr_pool_t pool) -> svn_error_t """
    pass

def svn_fs_revision_link(svn_fs_root_t_from_root, svn_fs_root_t_to_root, char_path, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_fs_revision_link(svn_fs_root_t from_root, svn_fs_root_t to_root, char path, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_fs_revision_prop(svn_string_t_value_p, svn_fs_t_fs, svn_revnum_t_rev, char_propname, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_fs_revision_prop(svn_string_t value_p, svn_fs_t fs, svn_revnum_t rev, 
        char propname, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_fs_revision_proplist(apr_hash_t_table_p, svn_fs_t_fs, svn_revnum_t_rev, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_fs_revision_proplist(apr_hash_t table_p, svn_fs_t fs, svn_revnum_t rev, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_fs_revision_root(svn_fs_root_t_root_p, svn_fs_t_fs, svn_revnum_t_rev, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_fs_revision_root(svn_fs_root_t root_p, svn_fs_t fs, svn_revnum_t rev, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_fs_revision_root_revision(svn_fs_root_t_root): # real signature unknown; restored from __doc__
    """ svn_fs_revision_root_revision(svn_fs_root_t root) -> svn_revnum_t """
    pass

def svn_fs_root_fs(svn_fs_root_t_root): # real signature unknown; restored from __doc__
    """ svn_fs_root_fs(svn_fs_root_t root) -> svn_fs_t """
    pass

def svn_fs_root_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def svn_fs_set_access(svn_fs_t_fs, svn_fs_access_t_access_ctx): # real signature unknown; restored from __doc__
    """ svn_fs_set_access(svn_fs_t fs, svn_fs_access_t access_ctx) -> svn_error_t """
    pass

def svn_fs_set_uuid(svn_fs_t_fs, char_uuid, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_fs_set_uuid(svn_fs_t fs, char uuid, apr_pool_t pool) -> svn_error_t """
    pass

def svn_fs_set_warning_func(svn_fs_t_fs, svn_fs_warning_callback_t_warning, void_warning_baton): # real signature unknown; restored from __doc__
    """ svn_fs_set_warning_func(svn_fs_t fs, svn_fs_warning_callback_t warning, void warning_baton) """
    pass

def svn_fs_txn_base_revision(svn_fs_txn_t_txn): # real signature unknown; restored from __doc__
    """ svn_fs_txn_base_revision(svn_fs_txn_t txn) -> svn_revnum_t """
    pass

def svn_fs_txn_name(char_name_p, svn_fs_txn_t_txn, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_fs_txn_name(char name_p, svn_fs_txn_t txn, apr_pool_t pool) -> svn_error_t """
    pass

def svn_fs_txn_prop(svn_string_t_value_p, svn_fs_txn_t_txn, char_propname, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_fs_txn_prop(svn_string_t value_p, svn_fs_txn_t txn, char propname, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_fs_txn_proplist(apr_hash_t_table_p, svn_fs_txn_t_txn, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_fs_txn_proplist(apr_hash_t table_p, svn_fs_txn_t txn, apr_pool_t pool) -> svn_error_t """
    pass

def svn_fs_txn_root(svn_fs_root_t_root_p, svn_fs_txn_t_txn, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_fs_txn_root(svn_fs_root_t root_p, svn_fs_txn_t txn, apr_pool_t pool) -> svn_error_t """
    pass

def svn_fs_txn_root_base_revision(svn_fs_root_t_root): # real signature unknown; restored from __doc__
    """ svn_fs_txn_root_base_revision(svn_fs_root_t root) -> svn_revnum_t """
    pass

def svn_fs_txn_root_name(svn_fs_root_t_root, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_fs_txn_root_name(svn_fs_root_t root, apr_pool_t pool) -> char """
    return ""

def svn_fs_txn_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def svn_fs_type(char_fs_type, char_path, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_fs_type(char fs_type, char path, apr_pool_t pool) -> svn_error_t """
    pass

def svn_fs_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def svn_fs_unlock(svn_fs_t_fs, char_path, char_token, svn_boolean_t_break_lock, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_fs_unlock(svn_fs_t fs, char path, char token, svn_boolean_t break_lock, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_fs_unparse_id(svn_fs_id_t_id, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_fs_unparse_id(svn_fs_id_t id, apr_pool_t pool) -> svn_string_t """
    pass

def svn_fs_upgrade(char_path, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_fs_upgrade(char path, apr_pool_t pool) -> svn_error_t """
    pass

def svn_fs_version(): # real signature unknown; restored from __doc__
    """ svn_fs_version() -> svn_version_t """
    pass

def svn_fs_warning_callback_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def svn_fs_youngest_rev(svn_revnum_t_youngest_p, svn_fs_t_fs, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_fs_youngest_rev(svn_revnum_t youngest_p, svn_fs_t fs, apr_pool_t pool) -> svn_error_t """
    pass

# no classes
