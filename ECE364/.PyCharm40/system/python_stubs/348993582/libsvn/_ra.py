# encoding: utf-8
# module libsvn._ra
# from /usr/lib64/python2.6/site-packages/libsvn/_ra.so
# by generator 1.136
# no doc
# no imports

# Variables with simple values

SVN_RA_ABI_VERSION = 2

SVN_RA_CAPABILITY_COMMIT_REVPROPS = 'commit-revprops'

SVN_RA_CAPABILITY_DEPTH = 'depth'

SVN_RA_CAPABILITY_LOG_REVPROPS = 'log-revprops'

SVN_RA_CAPABILITY_MERGEINFO = 'mergeinfo'

SVN_RA_CAPABILITY_PARTIAL_REPLAY = 'partial-replay'

# functions

def delete_svn_ra_callbacks2_t(svn_ra_callbacks2_t_self): # real signature unknown; restored from __doc__
    """ delete_svn_ra_callbacks2_t(svn_ra_callbacks2_t self) """
    pass

def delete_svn_ra_callbacks_t(svn_ra_callbacks_t_self): # real signature unknown; restored from __doc__
    """ delete_svn_ra_callbacks_t(svn_ra_callbacks_t self) """
    pass

def delete_svn_ra_plugin_t(svn_ra_plugin_t_self): # real signature unknown; restored from __doc__
    """ delete_svn_ra_plugin_t(svn_ra_plugin_t self) """
    pass

def delete_svn_ra_reporter2_t(svn_ra_reporter2_t_self): # real signature unknown; restored from __doc__
    """ delete_svn_ra_reporter2_t(svn_ra_reporter2_t self) """
    pass

def delete_svn_ra_reporter3_t(svn_ra_reporter3_t_self): # real signature unknown; restored from __doc__
    """ delete_svn_ra_reporter3_t(svn_ra_reporter3_t self) """
    pass

def delete_svn_ra_reporter_t(svn_ra_reporter_t_self): # real signature unknown; restored from __doc__
    """ delete_svn_ra_reporter_t(svn_ra_reporter_t self) """
    pass

def new_svn_ra_callbacks2_t(): # real signature unknown; restored from __doc__
    """ new_svn_ra_callbacks2_t() -> svn_ra_callbacks2_t """
    pass

def new_svn_ra_callbacks_t(): # real signature unknown; restored from __doc__
    """ new_svn_ra_callbacks_t() -> svn_ra_callbacks_t """
    pass

def new_svn_ra_plugin_t(): # real signature unknown; restored from __doc__
    """ new_svn_ra_plugin_t() -> svn_ra_plugin_t """
    pass

def new_svn_ra_reporter2_t(): # real signature unknown; restored from __doc__
    """ new_svn_ra_reporter2_t() -> svn_ra_reporter2_t """
    pass

def new_svn_ra_reporter3_t(): # real signature unknown; restored from __doc__
    """ new_svn_ra_reporter3_t() -> svn_ra_reporter3_t """
    pass

def new_svn_ra_reporter_t(): # real signature unknown; restored from __doc__
    """ new_svn_ra_reporter_t() -> svn_ra_reporter_t """
    pass

def svn_ra_callbacks2_invoke_open_tmp_file(svn_ra_callbacks2_t__obj, apr_file_t_fp, void_callback_baton, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_callbacks2_invoke_open_tmp_file(svn_ra_callbacks2_t _obj, apr_file_t fp, void callback_baton, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_callbacks2_t_auth_baton_get(svn_ra_callbacks2_t_self): # real signature unknown; restored from __doc__
    """ svn_ra_callbacks2_t_auth_baton_get(svn_ra_callbacks2_t self) -> svn_auth_baton_t """
    pass

def svn_ra_callbacks2_t_auth_baton_set(svn_ra_callbacks2_t_self, svn_auth_baton_t_auth_baton): # real signature unknown; restored from __doc__
    """ svn_ra_callbacks2_t_auth_baton_set(svn_ra_callbacks2_t self, svn_auth_baton_t auth_baton) """
    pass

def svn_ra_callbacks2_t_cancel_func_get(svn_ra_callbacks2_t_self): # real signature unknown; restored from __doc__
    """ svn_ra_callbacks2_t_cancel_func_get(svn_ra_callbacks2_t self) -> svn_cancel_func_t """
    pass

def svn_ra_callbacks2_t_cancel_func_set(svn_ra_callbacks2_t_self, svn_cancel_func_t_cancel_func): # real signature unknown; restored from __doc__
    """ svn_ra_callbacks2_t_cancel_func_set(svn_ra_callbacks2_t self, svn_cancel_func_t cancel_func) """
    pass

def svn_ra_callbacks2_t_get_client_string_get(svn_ra_callbacks2_t_self): # real signature unknown; restored from __doc__
    """ svn_ra_callbacks2_t_get_client_string_get(svn_ra_callbacks2_t self) -> svn_ra_get_client_string_func_t """
    pass

def svn_ra_callbacks2_t_get_client_string_set(svn_ra_callbacks2_t_self, svn_ra_get_client_string_func_t_get_client_string): # real signature unknown; restored from __doc__
    """ svn_ra_callbacks2_t_get_client_string_set(svn_ra_callbacks2_t self, svn_ra_get_client_string_func_t get_client_string) """
    pass

def svn_ra_callbacks2_t_get_wc_prop_get(svn_ra_callbacks2_t_self): # real signature unknown; restored from __doc__
    """ svn_ra_callbacks2_t_get_wc_prop_get(svn_ra_callbacks2_t self) -> svn_ra_get_wc_prop_func_t """
    pass

def svn_ra_callbacks2_t_get_wc_prop_set(svn_ra_callbacks2_t_self, svn_ra_get_wc_prop_func_t_get_wc_prop): # real signature unknown; restored from __doc__
    """ svn_ra_callbacks2_t_get_wc_prop_set(svn_ra_callbacks2_t self, svn_ra_get_wc_prop_func_t get_wc_prop) """
    pass

def svn_ra_callbacks2_t_invalidate_wc_props_get(svn_ra_callbacks2_t_self): # real signature unknown; restored from __doc__
    """ svn_ra_callbacks2_t_invalidate_wc_props_get(svn_ra_callbacks2_t self) -> svn_ra_invalidate_wc_props_func_t """
    pass

def svn_ra_callbacks2_t_invalidate_wc_props_set(svn_ra_callbacks2_t_self, svn_ra_invalidate_wc_props_func_t_invalidate_wc_props): # real signature unknown; restored from __doc__
    """ svn_ra_callbacks2_t_invalidate_wc_props_set(svn_ra_callbacks2_t self, svn_ra_invalidate_wc_props_func_t invalidate_wc_props) """
    pass

def svn_ra_callbacks2_t_open_tmp_file_get(svn_ra_callbacks2_t_self): # real signature unknown; restored from __doc__
    """ svn_ra_callbacks2_t_open_tmp_file_get(svn_ra_callbacks2_t self) -> svn_error_t """
    pass

def svn_ra_callbacks2_t_open_tmp_file_set(svn_ra_callbacks2_t_self, svn_error_t_open_tmp_file): # real signature unknown; restored from __doc__
    """ svn_ra_callbacks2_t_open_tmp_file_set(svn_ra_callbacks2_t self, svn_error_t open_tmp_file) """
    pass

def svn_ra_callbacks2_t_progress_baton_get(svn_ra_callbacks2_t_self): # real signature unknown; restored from __doc__
    """ svn_ra_callbacks2_t_progress_baton_get(svn_ra_callbacks2_t self) -> void """
    pass

def svn_ra_callbacks2_t_progress_baton_set(svn_ra_callbacks2_t_self, void_progress_baton): # real signature unknown; restored from __doc__
    """ svn_ra_callbacks2_t_progress_baton_set(svn_ra_callbacks2_t self, void progress_baton) """
    pass

def svn_ra_callbacks2_t_progress_func_get(svn_ra_callbacks2_t_self): # real signature unknown; restored from __doc__
    """ svn_ra_callbacks2_t_progress_func_get(svn_ra_callbacks2_t self) -> svn_ra_progress_notify_func_t """
    pass

def svn_ra_callbacks2_t_progress_func_set(svn_ra_callbacks2_t_self, svn_ra_progress_notify_func_t_progress_func): # real signature unknown; restored from __doc__
    """ svn_ra_callbacks2_t_progress_func_set(svn_ra_callbacks2_t self, svn_ra_progress_notify_func_t progress_func) """
    pass

def svn_ra_callbacks2_t_push_wc_prop_get(svn_ra_callbacks2_t_self): # real signature unknown; restored from __doc__
    """ svn_ra_callbacks2_t_push_wc_prop_get(svn_ra_callbacks2_t self) -> svn_ra_push_wc_prop_func_t """
    pass

def svn_ra_callbacks2_t_push_wc_prop_set(svn_ra_callbacks2_t_self, svn_ra_push_wc_prop_func_t_push_wc_prop): # real signature unknown; restored from __doc__
    """ svn_ra_callbacks2_t_push_wc_prop_set(svn_ra_callbacks2_t self, svn_ra_push_wc_prop_func_t push_wc_prop) """
    pass

def svn_ra_callbacks2_t_set_wc_prop_get(svn_ra_callbacks2_t_self): # real signature unknown; restored from __doc__
    """ svn_ra_callbacks2_t_set_wc_prop_get(svn_ra_callbacks2_t self) -> svn_ra_set_wc_prop_func_t """
    pass

def svn_ra_callbacks2_t_set_wc_prop_set(svn_ra_callbacks2_t_self, svn_ra_set_wc_prop_func_t_set_wc_prop): # real signature unknown; restored from __doc__
    """ svn_ra_callbacks2_t_set_wc_prop_set(svn_ra_callbacks2_t self, svn_ra_set_wc_prop_func_t set_wc_prop) """
    pass

def svn_ra_callbacks2_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def svn_ra_callbacks_invoke_open_tmp_file(svn_ra_callbacks_t__obj, apr_file_t_fp, void_callback_baton, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_callbacks_invoke_open_tmp_file(svn_ra_callbacks_t _obj, apr_file_t fp, void callback_baton, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_callbacks_t_auth_baton_get(svn_ra_callbacks_t_self): # real signature unknown; restored from __doc__
    """ svn_ra_callbacks_t_auth_baton_get(svn_ra_callbacks_t self) -> svn_auth_baton_t """
    pass

def svn_ra_callbacks_t_auth_baton_set(svn_ra_callbacks_t_self, svn_auth_baton_t_auth_baton): # real signature unknown; restored from __doc__
    """ svn_ra_callbacks_t_auth_baton_set(svn_ra_callbacks_t self, svn_auth_baton_t auth_baton) """
    pass

def svn_ra_callbacks_t_get_wc_prop_get(svn_ra_callbacks_t_self): # real signature unknown; restored from __doc__
    """ svn_ra_callbacks_t_get_wc_prop_get(svn_ra_callbacks_t self) -> svn_ra_get_wc_prop_func_t """
    pass

def svn_ra_callbacks_t_get_wc_prop_set(svn_ra_callbacks_t_self, svn_ra_get_wc_prop_func_t_get_wc_prop): # real signature unknown; restored from __doc__
    """ svn_ra_callbacks_t_get_wc_prop_set(svn_ra_callbacks_t self, svn_ra_get_wc_prop_func_t get_wc_prop) """
    pass

def svn_ra_callbacks_t_invalidate_wc_props_get(svn_ra_callbacks_t_self): # real signature unknown; restored from __doc__
    """ svn_ra_callbacks_t_invalidate_wc_props_get(svn_ra_callbacks_t self) -> svn_ra_invalidate_wc_props_func_t """
    pass

def svn_ra_callbacks_t_invalidate_wc_props_set(svn_ra_callbacks_t_self, svn_ra_invalidate_wc_props_func_t_invalidate_wc_props): # real signature unknown; restored from __doc__
    """ svn_ra_callbacks_t_invalidate_wc_props_set(svn_ra_callbacks_t self, svn_ra_invalidate_wc_props_func_t invalidate_wc_props) """
    pass

def svn_ra_callbacks_t_open_tmp_file_get(svn_ra_callbacks_t_self): # real signature unknown; restored from __doc__
    """ svn_ra_callbacks_t_open_tmp_file_get(svn_ra_callbacks_t self) -> svn_error_t """
    pass

def svn_ra_callbacks_t_open_tmp_file_set(svn_ra_callbacks_t_self, svn_error_t_open_tmp_file): # real signature unknown; restored from __doc__
    """ svn_ra_callbacks_t_open_tmp_file_set(svn_ra_callbacks_t self, svn_error_t open_tmp_file) """
    pass

def svn_ra_callbacks_t_push_wc_prop_get(svn_ra_callbacks_t_self): # real signature unknown; restored from __doc__
    """ svn_ra_callbacks_t_push_wc_prop_get(svn_ra_callbacks_t self) -> svn_ra_push_wc_prop_func_t """
    pass

def svn_ra_callbacks_t_push_wc_prop_set(svn_ra_callbacks_t_self, svn_ra_push_wc_prop_func_t_push_wc_prop): # real signature unknown; restored from __doc__
    """ svn_ra_callbacks_t_push_wc_prop_set(svn_ra_callbacks_t self, svn_ra_push_wc_prop_func_t push_wc_prop) """
    pass

def svn_ra_callbacks_t_set_wc_prop_get(svn_ra_callbacks_t_self): # real signature unknown; restored from __doc__
    """ svn_ra_callbacks_t_set_wc_prop_get(svn_ra_callbacks_t self) -> svn_ra_set_wc_prop_func_t """
    pass

def svn_ra_callbacks_t_set_wc_prop_set(svn_ra_callbacks_t_self, svn_ra_set_wc_prop_func_t_set_wc_prop): # real signature unknown; restored from __doc__
    """ svn_ra_callbacks_t_set_wc_prop_set(svn_ra_callbacks_t self, svn_ra_set_wc_prop_func_t set_wc_prop) """
    pass

def svn_ra_callbacks_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def svn_ra_change_rev_prop(svn_ra_session_t_session, svn_revnum_t_rev, char_name, svn_string_t_value, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_change_rev_prop(svn_ra_session_t session, svn_revnum_t rev, char name, 
        svn_string_t value, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_check_path(svn_ra_session_t_session, char_path, svn_revnum_t_revision, svn_node_kind_t_kind, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_check_path(svn_ra_session_t session, char path, svn_revnum_t revision, 
        svn_node_kind_t kind, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_create_callbacks(svn_ra_callbacks2_t_callbacks, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_ra_create_callbacks(svn_ra_callbacks2_t callbacks, apr_pool_t pool) -> svn_error_t """
    pass

def svn_ra_do_diff(svn_ra_session_t_session, svn_ra_reporter2_t_reporter, void_report_baton, svn_revnum_t_revision, char_diff_target, svn_boolean_t_recurse, svn_boolean_t_ignore_ancestry, char_versus_url, svn_delta_editor_t_diff_editor, void_diff_baton, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_do_diff(svn_ra_session_t session, svn_ra_reporter2_t reporter, 
        void report_baton, svn_revnum_t revision, 
        char diff_target, svn_boolean_t recurse, svn_boolean_t ignore_ancestry, 
        char versus_url, 
        svn_delta_editor_t diff_editor, void diff_baton, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_do_diff2(svn_ra_session_t_session, svn_ra_reporter2_t_reporter, void_report_baton, svn_revnum_t_revision, char_diff_target, svn_boolean_t_recurse, svn_boolean_t_ignore_ancestry, svn_boolean_t_text_deltas, char_versus_url, svn_delta_editor_t_diff_editor, void_diff_baton, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_do_diff2(svn_ra_session_t session, svn_ra_reporter2_t reporter, 
        void report_baton, svn_revnum_t revision, 
        char diff_target, svn_boolean_t recurse, svn_boolean_t ignore_ancestry, 
        svn_boolean_t text_deltas, 
        char versus_url, svn_delta_editor_t diff_editor, 
        void diff_baton, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_do_diff3(svn_ra_session_t_session, svn_ra_reporter3_t_reporter, void_report_baton, svn_revnum_t_revision, char_diff_target, svn_depth_t_depth, svn_boolean_t_ignore_ancestry, svn_boolean_t_text_deltas, char_versus_url, svn_delta_editor_t_diff_editor, void_diff_baton, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_do_diff3(svn_ra_session_t session, svn_ra_reporter3_t reporter, 
        void report_baton, svn_revnum_t revision, 
        char diff_target, svn_depth_t depth, svn_boolean_t ignore_ancestry, 
        svn_boolean_t text_deltas, 
        char versus_url, svn_delta_editor_t diff_editor, 
        void diff_baton, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_do_status(svn_ra_session_t_session, svn_ra_reporter2_t_reporter, void_report_baton, char_status_target, svn_revnum_t_revision, svn_boolean_t_recurse, svn_delta_editor_t_status_editor, void_status_baton, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_do_status(svn_ra_session_t session, svn_ra_reporter2_t reporter, 
        void report_baton, char status_target, svn_revnum_t revision, 
        svn_boolean_t recurse, svn_delta_editor_t status_editor, 
        void status_baton, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_do_status2(svn_ra_session_t_session, svn_ra_reporter3_t_reporter, void_report_baton, char_status_target, svn_revnum_t_revision, svn_depth_t_depth, svn_delta_editor_t_status_editor, void_status_baton, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_do_status2(svn_ra_session_t session, svn_ra_reporter3_t reporter, 
        void report_baton, char status_target, svn_revnum_t revision, 
        svn_depth_t depth, svn_delta_editor_t status_editor, 
        void status_baton, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_do_switch(svn_ra_session_t_session, svn_ra_reporter2_t_reporter, void_report_baton, svn_revnum_t_revision_to_switch_to, char_switch_target, svn_boolean_t_recurse, char_switch_url, svn_delta_editor_t_switch_editor, void_switch_baton, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_do_switch(svn_ra_session_t session, svn_ra_reporter2_t reporter, 
        void report_baton, svn_revnum_t revision_to_switch_to, 
        char switch_target, svn_boolean_t recurse, 
        char switch_url, svn_delta_editor_t switch_editor, 
        void switch_baton, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_do_switch2(svn_ra_session_t_session, svn_ra_reporter3_t_reporter, void_report_baton, svn_revnum_t_revision_to_switch_to, char_switch_target, svn_depth_t_depth, char_switch_url, svn_delta_editor_t_switch_editor, void_switch_baton, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_do_switch2(svn_ra_session_t session, svn_ra_reporter3_t reporter, 
        void report_baton, svn_revnum_t revision_to_switch_to, 
        char switch_target, svn_depth_t depth, 
        char switch_url, svn_delta_editor_t switch_editor, 
        void switch_baton, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_do_update(svn_ra_session_t_session, svn_ra_reporter2_t_reporter, void_report_baton, svn_revnum_t_revision_to_update_to, char_update_target, svn_boolean_t_recurse, svn_delta_editor_t_update_editor, void_update_baton, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_do_update(svn_ra_session_t session, svn_ra_reporter2_t reporter, 
        void report_baton, svn_revnum_t revision_to_update_to, 
        char update_target, svn_boolean_t recurse, 
        svn_delta_editor_t update_editor, 
        void update_baton, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_do_update2(svn_ra_session_t_session, svn_ra_reporter3_t_reporter, void_report_baton, svn_revnum_t_revision_to_update_to, char_update_target, svn_depth_t_depth, svn_boolean_t_send_copyfrom_args, svn_delta_editor_t_update_editor, void_update_baton, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_do_update2(svn_ra_session_t session, svn_ra_reporter3_t reporter, 
        void report_baton, svn_revnum_t revision_to_update_to, 
        char update_target, svn_depth_t depth, 
        svn_boolean_t send_copyfrom_args, svn_delta_editor_t update_editor, 
        void update_baton, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_file_rev_handler_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def svn_ra_get_client_string_func_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def svn_ra_get_commit_editor(svn_ra_session_t_session, svn_delta_editor_t_editor, void_edit_baton, char_log_msg, svn_commit_callback_t_callback, apr_hash_t_lock_tokens, svn_boolean_t_keep_locks, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_get_commit_editor(svn_ra_session_t session, svn_delta_editor_t editor, 
        void edit_baton, char log_msg, svn_commit_callback_t callback, 
        apr_hash_t lock_tokens, svn_boolean_t keep_locks, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_get_commit_editor2(svn_ra_session_t_session, svn_delta_editor_t_editor, void_edit_baton, char_log_msg, svn_commit_callback2_t_callback, apr_hash_t_lock_tokens, svn_boolean_t_keep_locks, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_get_commit_editor2(svn_ra_session_t session, svn_delta_editor_t editor, 
        void edit_baton, char log_msg, svn_commit_callback2_t callback, 
        apr_hash_t lock_tokens, 
        svn_boolean_t keep_locks, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_get_commit_editor3(svn_ra_session_t_session, svn_delta_editor_t_editor, void_edit_baton, apr_hash_t_revprop_table, svn_commit_callback2_t_callback, apr_hash_t_lock_tokens, svn_boolean_t_keep_locks, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_get_commit_editor3(svn_ra_session_t session, svn_delta_editor_t editor, 
        void edit_baton, apr_hash_t revprop_table, 
        svn_commit_callback2_t callback, apr_hash_t lock_tokens, 
        svn_boolean_t keep_locks, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_get_dated_revision(svn_ra_session_t_session, svn_revnum_t_revision, apr_time_t_tm, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_get_dated_revision(svn_ra_session_t session, svn_revnum_t revision, apr_time_t tm, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_get_deleted_rev(svn_ra_session_t_session, char_path, svn_revnum_t_peg_revision, svn_revnum_t_end_revision, svn_revnum_t_revision_deleted, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_get_deleted_rev(svn_ra_session_t session, char path, svn_revnum_t peg_revision, 
        svn_revnum_t end_revision, svn_revnum_t revision_deleted, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_get_dir(svn_ra_session_t_session, char_path, svn_revnum_t_revision, apr_hash_t_dirents, svn_revnum_t_fetched_rev, apr_hash_t_props, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_get_dir(svn_ra_session_t session, char path, svn_revnum_t revision, 
        apr_hash_t dirents, svn_revnum_t fetched_rev, 
        apr_hash_t props, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_get_dir2(svn_ra_session_t_session, apr_hash_t_dirents, svn_revnum_t_fetched_rev, apr_hash_t_props, char_path, svn_revnum_t_revision, apr_uint32_t_dirent_fields, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_get_dir2(svn_ra_session_t session, apr_hash_t dirents, svn_revnum_t fetched_rev, 
        apr_hash_t props, char path, 
        svn_revnum_t revision, apr_uint32_t dirent_fields, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_get_file(svn_ra_session_t_session, char_path, svn_revnum_t_revision, svn_stream_t_stream, svn_revnum_t_fetched_rev, apr_hash_t_props, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_get_file(svn_ra_session_t session, char path, svn_revnum_t revision, 
        svn_stream_t stream, svn_revnum_t fetched_rev, 
        apr_hash_t props, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_get_file_revs(svn_ra_session_t_session, char_path, svn_revnum_t_start, svn_revnum_t_end, svn_ra_file_rev_handler_t_handler, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_get_file_revs(svn_ra_session_t session, char path, svn_revnum_t start, 
        svn_revnum_t end, svn_ra_file_rev_handler_t handler, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_get_file_revs2(svn_ra_session_t_session, char_path, svn_revnum_t_start, svn_revnum_t_end, svn_boolean_t_include_merged_revisions, svn_file_rev_handler_t_handler, void_handler_baton, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_get_file_revs2(svn_ra_session_t session, char path, svn_revnum_t start, 
        svn_revnum_t end, svn_boolean_t include_merged_revisions, 
        svn_file_rev_handler_t handler, 
        void handler_baton, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_get_latest_revnum(svn_ra_session_t_session, svn_revnum_t_latest_revnum, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_get_latest_revnum(svn_ra_session_t session, svn_revnum_t latest_revnum, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_get_latest_revnum_func_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def svn_ra_get_locations(svn_ra_session_t_session, apr_hash_t_locations, char_path, svn_revnum_t_peg_revision, apr_array_header_t_location_revisions, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_get_locations(svn_ra_session_t session, apr_hash_t locations, char path, 
        svn_revnum_t peg_revision, apr_array_header_t location_revisions, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_get_location_segments(svn_ra_session_t_session, char_path, svn_revnum_t_peg_revision, svn_revnum_t_start_rev, svn_revnum_t_end_rev, svn_location_segment_receiver_t_receiver, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_get_location_segments(svn_ra_session_t session, char path, svn_revnum_t peg_revision, 
        svn_revnum_t start_rev, svn_revnum_t end_rev, 
        svn_location_segment_receiver_t receiver, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_get_lock(svn_ra_session_t_session, svn_lock_t_lock, char_path, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_get_lock(svn_ra_session_t session, svn_lock_t lock, char path, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_get_locks(svn_ra_session_t_session, apr_hash_t_locks, char_path, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_get_locks(svn_ra_session_t session, apr_hash_t locks, char path, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_get_log(svn_ra_session_t_session, apr_array_header_t_paths, svn_revnum_t_start, svn_revnum_t_end, int_limit, svn_boolean_t_discover_changed_paths, svn_boolean_t_strict_node_history, svn_log_message_receiver_t_receiver, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_get_log(svn_ra_session_t session, apr_array_header_t paths, 
        svn_revnum_t start, svn_revnum_t end, int limit, 
        svn_boolean_t discover_changed_paths, svn_boolean_t strict_node_history, 
        svn_log_message_receiver_t receiver, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_get_log2(svn_ra_session_t_session, apr_array_header_t_paths, svn_revnum_t_start, svn_revnum_t_end, int_limit, svn_boolean_t_discover_changed_paths, svn_boolean_t_strict_node_history, svn_boolean_t_include_merged_revisions, apr_array_header_t_revprops, svn_log_entry_receiver_t_receiver, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_get_log2(svn_ra_session_t session, apr_array_header_t paths, 
        svn_revnum_t start, svn_revnum_t end, int limit, 
        svn_boolean_t discover_changed_paths, svn_boolean_t strict_node_history, 
        svn_boolean_t include_merged_revisions, 
        apr_array_header_t revprops, 
        svn_log_entry_receiver_t receiver, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_get_mergeinfo(svn_ra_session_t_session, svn_mergeinfo_catalog_t_catalog, apr_array_header_t_paths, svn_revnum_t_revision, svn_mergeinfo_inheritance_t_inherit, svn_boolean_t_include_descendants, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_get_mergeinfo(svn_ra_session_t session, svn_mergeinfo_catalog_t catalog, 
        apr_array_header_t paths, svn_revnum_t revision, 
        svn_mergeinfo_inheritance_t inherit, 
        svn_boolean_t include_descendants, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_get_ra_library(svn_ra_plugin_t_library, void_ra_baton, char_url, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_ra_get_ra_library(svn_ra_plugin_t library, void ra_baton, char url, apr_pool_t pool) -> svn_error_t """
    pass

def svn_ra_get_repos_root(svn_ra_session_t_session, char_url, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_ra_get_repos_root(svn_ra_session_t session, char url, apr_pool_t pool) -> svn_error_t """
    pass

def svn_ra_get_repos_root2(svn_ra_session_t_session, char_url, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_ra_get_repos_root2(svn_ra_session_t session, char url, apr_pool_t pool) -> svn_error_t """
    pass

def svn_ra_get_session_url(svn_ra_session_t_ra_session, char_url, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_ra_get_session_url(svn_ra_session_t ra_session, char url, apr_pool_t pool) -> svn_error_t """
    pass

def svn_ra_get_uuid(svn_ra_session_t_session, char_uuid, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_ra_get_uuid(svn_ra_session_t session, char uuid, apr_pool_t pool) -> svn_error_t """
    pass

def svn_ra_get_uuid2(svn_ra_session_t_session, char_uuid, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_ra_get_uuid2(svn_ra_session_t session, char uuid, apr_pool_t pool) -> svn_error_t """
    pass

def svn_ra_get_wc_prop_func_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def svn_ra_has_capability(svn_ra_session_t_session, svn_boolean_t_has, char_capability, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_has_capability(svn_ra_session_t session, svn_boolean_t has, char capability, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_initialize(apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_ra_initialize(apr_pool_t pool) -> svn_error_t """
    pass

def svn_ra_init_func_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def svn_ra_init_ra_libs(void_ra_baton, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_ra_init_ra_libs(void ra_baton, apr_pool_t pool) -> svn_error_t """
    pass

def svn_ra_invalidate_wc_props_func_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def svn_ra_invoke_file_rev_handler(svn_ra_file_rev_handler_t__obj, void_baton, char_path, svn_revnum_t_rev, apr_hash_t_rev_props, svn_txdelta_window_handler_t_delta_handler, void_delta_baton, apr_array_header_t_prop_diffs, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_invoke_file_rev_handler(svn_ra_file_rev_handler_t _obj, void baton, char path, 
        svn_revnum_t rev, apr_hash_t rev_props, svn_txdelta_window_handler_t delta_handler, 
        void delta_baton, 
        apr_array_header_t prop_diffs, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_invoke_get_client_string_func(svn_ra_get_client_string_func_t__obj, void_baton, char_name, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_invoke_get_client_string_func(svn_ra_get_client_string_func_t _obj, void baton, char name, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_invoke_get_latest_revnum_func(svn_ra_get_latest_revnum_func_t__obj, void_session_baton, svn_revnum_t_latest_revnum): # real signature unknown; restored from __doc__
    """
    svn_ra_invoke_get_latest_revnum_func(svn_ra_get_latest_revnum_func_t _obj, void session_baton, 
        svn_revnum_t latest_revnum) -> svn_error_t
    """
    pass

def svn_ra_invoke_get_wc_prop_func(svn_ra_get_wc_prop_func_t__obj, void_baton, char_relpath, char_name, svn_string_t_value, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_invoke_get_wc_prop_func(svn_ra_get_wc_prop_func_t _obj, void baton, char relpath, 
        char name, svn_string_t value, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_invoke_init_func(svn_ra_init_func_t__obj, int_abi_version, apr_pool_t_pool, apr_hash_t_hash): # real signature unknown; restored from __doc__
    """
    svn_ra_invoke_init_func(svn_ra_init_func_t _obj, int abi_version, apr_pool_t pool, 
        apr_hash_t hash) -> svn_error_t
    """
    pass

def svn_ra_invoke_invalidate_wc_props_func(svn_ra_invalidate_wc_props_func_t__obj, void_baton, char_path, char_name, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_invoke_invalidate_wc_props_func(svn_ra_invalidate_wc_props_func_t _obj, void baton, 
        char path, char name, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_invoke_lock_callback(svn_ra_lock_callback_t__obj, void_baton, char_path, svn_boolean_t_do_lock, svn_lock_t_lock, svn_error_t_ra_err, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_invoke_lock_callback(svn_ra_lock_callback_t _obj, void baton, char path, 
        svn_boolean_t do_lock, svn_lock_t lock, svn_error_t ra_err, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_invoke_progress_notify_func(svn_ra_progress_notify_func_t__obj, apr_off_t_progress, apr_off_t_total, void_baton, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_invoke_progress_notify_func(svn_ra_progress_notify_func_t _obj, apr_off_t progress, 
        apr_off_t total, void baton, apr_pool_t pool)
    """
    pass

def svn_ra_invoke_push_wc_prop_func(svn_ra_push_wc_prop_func_t__obj, void_baton, char_path, char_name, svn_string_t_value, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_invoke_push_wc_prop_func(svn_ra_push_wc_prop_func_t _obj, void baton, char path, 
        char name, svn_string_t value, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_invoke_replay_revfinish_callback(svn_ra_replay_revfinish_callback_t__obj, svn_revnum_t_revision, void_replay_baton, svn_delta_editor_t_editor, void_edit_baton, apr_hash_t_rev_props, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_invoke_replay_revfinish_callback(svn_ra_replay_revfinish_callback_t _obj, svn_revnum_t revision, 
        void replay_baton, svn_delta_editor_t editor, 
        void edit_baton, apr_hash_t rev_props, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_invoke_replay_revstart_callback(svn_ra_replay_revstart_callback_t__obj, svn_revnum_t_revision, void_replay_baton, svn_delta_editor_t_editor, void_edit_baton, apr_hash_t_rev_props, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_invoke_replay_revstart_callback(svn_ra_replay_revstart_callback_t _obj, svn_revnum_t revision, 
        void replay_baton, svn_delta_editor_t editor, 
        void edit_baton, apr_hash_t rev_props, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_invoke_set_wc_prop_func(svn_ra_set_wc_prop_func_t__obj, void_baton, char_path, char_name, svn_string_t_value, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_invoke_set_wc_prop_func(svn_ra_set_wc_prop_func_t _obj, void baton, char path, 
        char name, svn_string_t value, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_lock(svn_ra_session_t_session, apr_hash_t_path_revs, char_comment, svn_boolean_t_steal_lock, svn_ra_lock_callback_t_lock_func, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_lock(svn_ra_session_t session, apr_hash_t path_revs, char comment, 
        svn_boolean_t steal_lock, svn_ra_lock_callback_t lock_func, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_lock_callback_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def svn_ra_open(svn_ra_session_t_session_p, char_repos_URL, svn_ra_callbacks_t_callbacks, void_callback_baton, apr_hash_t_config, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_open(svn_ra_session_t session_p, char repos_URL, svn_ra_callbacks_t callbacks, 
        void callback_baton, apr_hash_t config, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_open2(svn_ra_session_t_session_p, char_repos_URL, svn_ra_callbacks2_t_callbacks, apr_hash_t_config, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_open2(svn_ra_session_t session_p, char repos_URL, svn_ra_callbacks2_t callbacks, 
        apr_hash_t config, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_open3(svn_ra_session_t_session_p, char_repos_URL, char_uuid, svn_ra_callbacks2_t_callbacks, apr_hash_t_config, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_open3(svn_ra_session_t session_p, char repos_URL, char uuid, 
        svn_ra_callbacks2_t callbacks, apr_hash_t config, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_plugin_invoke_change_rev_prop(svn_ra_plugin_t__obj, void_session_baton, svn_revnum_t_rev, char_name, svn_string_t_value, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_plugin_invoke_change_rev_prop(svn_ra_plugin_t _obj, void session_baton, svn_revnum_t rev, 
        char name, svn_string_t value, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_plugin_invoke_check_path(svn_ra_plugin_t__obj, void_session_baton, char_path, svn_revnum_t_revision, svn_node_kind_t_kind, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_plugin_invoke_check_path(svn_ra_plugin_t _obj, void session_baton, char path, 
        svn_revnum_t revision, svn_node_kind_t kind, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_plugin_invoke_do_diff(svn_ra_plugin_t__obj, void_session_baton, svn_ra_reporter_t_reporter, void_report_baton, svn_revnum_t_revision, char_diff_target, svn_boolean_t_recurse, svn_boolean_t_ignore_ancestry, char_versus_url, svn_delta_editor_t_diff_editor, void_diff_baton, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_plugin_invoke_do_diff(svn_ra_plugin_t _obj, void session_baton, svn_ra_reporter_t reporter, 
        void report_baton, svn_revnum_t revision, 
        char diff_target, svn_boolean_t recurse, 
        svn_boolean_t ignore_ancestry, char versus_url, 
        svn_delta_editor_t diff_editor, 
        void diff_baton, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_plugin_invoke_do_status(svn_ra_plugin_t__obj, void_session_baton, svn_ra_reporter_t_reporter, void_report_baton, char_status_target, svn_revnum_t_revision, svn_boolean_t_recurse, svn_delta_editor_t_status_editor, void_status_baton, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_plugin_invoke_do_status(svn_ra_plugin_t _obj, void session_baton, svn_ra_reporter_t reporter, 
        void report_baton, char status_target, 
        svn_revnum_t revision, svn_boolean_t recurse, 
        svn_delta_editor_t status_editor, 
        void status_baton, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_plugin_invoke_do_switch(svn_ra_plugin_t__obj, void_session_baton, svn_ra_reporter_t_reporter, void_report_baton, svn_revnum_t_revision_to_switch_to, char_switch_target, svn_boolean_t_recurse, char_switch_url, svn_delta_editor_t_switch_editor, void_switch_baton, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_plugin_invoke_do_switch(svn_ra_plugin_t _obj, void session_baton, svn_ra_reporter_t reporter, 
        void report_baton, svn_revnum_t revision_to_switch_to, 
        char switch_target, 
        svn_boolean_t recurse, char switch_url, svn_delta_editor_t switch_editor, 
        void switch_baton, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_plugin_invoke_do_update(svn_ra_plugin_t__obj, void_session_baton, svn_ra_reporter_t_reporter, void_report_baton, svn_revnum_t_revision_to_update_to, char_update_target, svn_boolean_t_recurse, svn_delta_editor_t_update_editor, void_update_baton, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_plugin_invoke_do_update(svn_ra_plugin_t _obj, void session_baton, svn_ra_reporter_t reporter, 
        void report_baton, svn_revnum_t revision_to_update_to, 
        char update_target, 
        svn_boolean_t recurse, svn_delta_editor_t update_editor, 
        void update_baton, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_plugin_invoke_get_commit_editor(svn_ra_plugin_t__obj, void_session_baton, svn_delta_editor_t_editor, void_edit_baton, char_log_msg, svn_commit_callback_t_callback, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_plugin_invoke_get_commit_editor(svn_ra_plugin_t _obj, void session_baton, svn_delta_editor_t editor, 
        void edit_baton, char log_msg, 
        svn_commit_callback_t callback, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_plugin_invoke_get_dated_revision(svn_ra_plugin_t__obj, void_session_baton, svn_revnum_t_revision, apr_time_t_tm, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_plugin_invoke_get_dated_revision(svn_ra_plugin_t _obj, void session_baton, svn_revnum_t revision, 
        apr_time_t tm, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_plugin_invoke_get_dir(svn_ra_plugin_t__obj, void_session_baton, char_path, svn_revnum_t_revision, apr_hash_t_dirents, svn_revnum_t_fetched_rev, apr_hash_t_props, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_plugin_invoke_get_dir(svn_ra_plugin_t _obj, void session_baton, char path, 
        svn_revnum_t revision, apr_hash_t dirents, 
        svn_revnum_t fetched_rev, apr_hash_t props, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_plugin_invoke_get_file(svn_ra_plugin_t__obj, void_session_baton, char_path, svn_revnum_t_revision, svn_stream_t_stream, svn_revnum_t_fetched_rev, apr_hash_t_props, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_plugin_invoke_get_file(svn_ra_plugin_t _obj, void session_baton, char path, 
        svn_revnum_t revision, svn_stream_t stream, 
        svn_revnum_t fetched_rev, apr_hash_t props, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_plugin_invoke_get_file_revs(svn_ra_plugin_t__obj, void_session_baton, char_path, svn_revnum_t_start, svn_revnum_t_end, svn_ra_file_rev_handler_t_handler, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_plugin_invoke_get_file_revs(svn_ra_plugin_t _obj, void session_baton, char path, 
        svn_revnum_t start, svn_revnum_t end, svn_ra_file_rev_handler_t handler, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_plugin_invoke_get_latest_revnum(svn_ra_plugin_t__obj, void_session_baton, svn_revnum_t_latest_revnum, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_plugin_invoke_get_latest_revnum(svn_ra_plugin_t _obj, void session_baton, svn_revnum_t latest_revnum, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_plugin_invoke_get_locations(svn_ra_plugin_t__obj, void_session_baton, apr_hash_t_locations, char_path, svn_revnum_t_peg_revision, apr_array_header_t_location_revisions, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_plugin_invoke_get_locations(svn_ra_plugin_t _obj, void session_baton, apr_hash_t locations, 
        char path, svn_revnum_t peg_revision, 
        apr_array_header_t location_revisions, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_plugin_invoke_get_log(svn_ra_plugin_t__obj, void_session_baton, apr_array_header_t_paths, svn_revnum_t_start, svn_revnum_t_end, svn_boolean_t_discover_changed_paths, svn_boolean_t_strict_node_history, svn_log_message_receiver_t_receiver, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_plugin_invoke_get_log(svn_ra_plugin_t _obj, void session_baton, apr_array_header_t paths, 
        svn_revnum_t start, svn_revnum_t end, 
        svn_boolean_t discover_changed_paths, 
        svn_boolean_t strict_node_history, svn_log_message_receiver_t receiver, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_plugin_invoke_get_repos_root(svn_ra_plugin_t__obj, void_session_baton, char_url, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_plugin_invoke_get_repos_root(svn_ra_plugin_t _obj, void session_baton, char url, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_plugin_invoke_get_uuid(svn_ra_plugin_t__obj, void_session_baton, char_uuid, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_plugin_invoke_get_uuid(svn_ra_plugin_t _obj, void session_baton, char uuid, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_plugin_invoke_get_version(svn_ra_plugin_t__obj): # real signature unknown; restored from __doc__
    """ svn_ra_plugin_invoke_get_version(svn_ra_plugin_t _obj) -> svn_version_t """
    pass

def svn_ra_plugin_invoke_open(svn_ra_plugin_t__obj, void_session_baton, char_repos_URL, svn_ra_callbacks_t_callbacks, void_callback_baton, apr_hash_t_config, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_plugin_invoke_open(svn_ra_plugin_t _obj, void session_baton, char repos_URL, 
        svn_ra_callbacks_t callbacks, void callback_baton, 
        apr_hash_t config, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_plugin_invoke_rev_prop(svn_ra_plugin_t__obj, void_session_baton, svn_revnum_t_rev, char_name, svn_string_t_value, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_plugin_invoke_rev_prop(svn_ra_plugin_t _obj, void session_baton, svn_revnum_t rev, 
        char name, svn_string_t value, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_plugin_invoke_rev_proplist(svn_ra_plugin_t__obj, void_session_baton, svn_revnum_t_rev, apr_hash_t_props, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_plugin_invoke_rev_proplist(svn_ra_plugin_t _obj, void session_baton, svn_revnum_t rev, 
        apr_hash_t props, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_plugin_t_change_rev_prop_get(svn_ra_plugin_t_self): # real signature unknown; restored from __doc__
    """ svn_ra_plugin_t_change_rev_prop_get(svn_ra_plugin_t self) -> svn_error_t """
    pass

def svn_ra_plugin_t_change_rev_prop_set(svn_ra_plugin_t_self, svn_error_t_change_rev_prop): # real signature unknown; restored from __doc__
    """ svn_ra_plugin_t_change_rev_prop_set(svn_ra_plugin_t self, svn_error_t change_rev_prop) """
    pass

def svn_ra_plugin_t_check_path_get(svn_ra_plugin_t_self): # real signature unknown; restored from __doc__
    """ svn_ra_plugin_t_check_path_get(svn_ra_plugin_t self) -> svn_error_t """
    pass

def svn_ra_plugin_t_check_path_set(svn_ra_plugin_t_self, svn_error_t_check_path): # real signature unknown; restored from __doc__
    """ svn_ra_plugin_t_check_path_set(svn_ra_plugin_t self, svn_error_t check_path) """
    pass

def svn_ra_plugin_t_description_get(svn_ra_plugin_t_self): # real signature unknown; restored from __doc__
    """ svn_ra_plugin_t_description_get(svn_ra_plugin_t self) -> char """
    return ""

def svn_ra_plugin_t_description_set(svn_ra_plugin_t_self, char_description): # real signature unknown; restored from __doc__
    """ svn_ra_plugin_t_description_set(svn_ra_plugin_t self, char description) """
    pass

def svn_ra_plugin_t_do_diff_get(svn_ra_plugin_t_self): # real signature unknown; restored from __doc__
    """ svn_ra_plugin_t_do_diff_get(svn_ra_plugin_t self) -> svn_error_t """
    pass

def svn_ra_plugin_t_do_diff_set(svn_ra_plugin_t_self, svn_error_t_do_diff): # real signature unknown; restored from __doc__
    """ svn_ra_plugin_t_do_diff_set(svn_ra_plugin_t self, svn_error_t do_diff) """
    pass

def svn_ra_plugin_t_do_status_get(svn_ra_plugin_t_self): # real signature unknown; restored from __doc__
    """ svn_ra_plugin_t_do_status_get(svn_ra_plugin_t self) -> svn_error_t """
    pass

def svn_ra_plugin_t_do_status_set(svn_ra_plugin_t_self, svn_error_t_do_status): # real signature unknown; restored from __doc__
    """ svn_ra_plugin_t_do_status_set(svn_ra_plugin_t self, svn_error_t do_status) """
    pass

def svn_ra_plugin_t_do_switch_get(svn_ra_plugin_t_self): # real signature unknown; restored from __doc__
    """ svn_ra_plugin_t_do_switch_get(svn_ra_plugin_t self) -> svn_error_t """
    pass

def svn_ra_plugin_t_do_switch_set(svn_ra_plugin_t_self, svn_error_t_do_switch): # real signature unknown; restored from __doc__
    """ svn_ra_plugin_t_do_switch_set(svn_ra_plugin_t self, svn_error_t do_switch) """
    pass

def svn_ra_plugin_t_do_update_get(svn_ra_plugin_t_self): # real signature unknown; restored from __doc__
    """ svn_ra_plugin_t_do_update_get(svn_ra_plugin_t self) -> svn_error_t """
    pass

def svn_ra_plugin_t_do_update_set(svn_ra_plugin_t_self, svn_error_t_do_update): # real signature unknown; restored from __doc__
    """ svn_ra_plugin_t_do_update_set(svn_ra_plugin_t self, svn_error_t do_update) """
    pass

def svn_ra_plugin_t_get_commit_editor_get(svn_ra_plugin_t_self): # real signature unknown; restored from __doc__
    """ svn_ra_plugin_t_get_commit_editor_get(svn_ra_plugin_t self) -> svn_error_t """
    pass

def svn_ra_plugin_t_get_commit_editor_set(svn_ra_plugin_t_self, svn_error_t_get_commit_editor): # real signature unknown; restored from __doc__
    """ svn_ra_plugin_t_get_commit_editor_set(svn_ra_plugin_t self, svn_error_t get_commit_editor) """
    pass

def svn_ra_plugin_t_get_dated_revision_get(svn_ra_plugin_t_self): # real signature unknown; restored from __doc__
    """ svn_ra_plugin_t_get_dated_revision_get(svn_ra_plugin_t self) -> svn_error_t """
    pass

def svn_ra_plugin_t_get_dated_revision_set(svn_ra_plugin_t_self, svn_error_t_get_dated_revision): # real signature unknown; restored from __doc__
    """ svn_ra_plugin_t_get_dated_revision_set(svn_ra_plugin_t self, svn_error_t get_dated_revision) """
    pass

def svn_ra_plugin_t_get_dir_get(svn_ra_plugin_t_self): # real signature unknown; restored from __doc__
    """ svn_ra_plugin_t_get_dir_get(svn_ra_plugin_t self) -> svn_error_t """
    pass

def svn_ra_plugin_t_get_dir_set(svn_ra_plugin_t_self, svn_error_t_get_dir): # real signature unknown; restored from __doc__
    """ svn_ra_plugin_t_get_dir_set(svn_ra_plugin_t self, svn_error_t get_dir) """
    pass

def svn_ra_plugin_t_get_file_get(svn_ra_plugin_t_self): # real signature unknown; restored from __doc__
    """ svn_ra_plugin_t_get_file_get(svn_ra_plugin_t self) -> svn_error_t """
    pass

def svn_ra_plugin_t_get_file_revs_get(svn_ra_plugin_t_self): # real signature unknown; restored from __doc__
    """ svn_ra_plugin_t_get_file_revs_get(svn_ra_plugin_t self) -> svn_error_t """
    pass

def svn_ra_plugin_t_get_file_revs_set(svn_ra_plugin_t_self, svn_error_t_get_file_revs): # real signature unknown; restored from __doc__
    """ svn_ra_plugin_t_get_file_revs_set(svn_ra_plugin_t self, svn_error_t get_file_revs) """
    pass

def svn_ra_plugin_t_get_file_set(svn_ra_plugin_t_self, svn_error_t_get_file): # real signature unknown; restored from __doc__
    """ svn_ra_plugin_t_get_file_set(svn_ra_plugin_t self, svn_error_t get_file) """
    pass

def svn_ra_plugin_t_get_latest_revnum_get(svn_ra_plugin_t_self): # real signature unknown; restored from __doc__
    """ svn_ra_plugin_t_get_latest_revnum_get(svn_ra_plugin_t self) -> svn_error_t """
    pass

def svn_ra_plugin_t_get_latest_revnum_set(svn_ra_plugin_t_self, svn_error_t_get_latest_revnum): # real signature unknown; restored from __doc__
    """ svn_ra_plugin_t_get_latest_revnum_set(svn_ra_plugin_t self, svn_error_t get_latest_revnum) """
    pass

def svn_ra_plugin_t_get_locations_get(svn_ra_plugin_t_self): # real signature unknown; restored from __doc__
    """ svn_ra_plugin_t_get_locations_get(svn_ra_plugin_t self) -> svn_error_t """
    pass

def svn_ra_plugin_t_get_locations_set(svn_ra_plugin_t_self, svn_error_t_get_locations): # real signature unknown; restored from __doc__
    """ svn_ra_plugin_t_get_locations_set(svn_ra_plugin_t self, svn_error_t get_locations) """
    pass

def svn_ra_plugin_t_get_log_get(svn_ra_plugin_t_self): # real signature unknown; restored from __doc__
    """ svn_ra_plugin_t_get_log_get(svn_ra_plugin_t self) -> svn_error_t """
    pass

def svn_ra_plugin_t_get_log_set(svn_ra_plugin_t_self, svn_error_t_get_log): # real signature unknown; restored from __doc__
    """ svn_ra_plugin_t_get_log_set(svn_ra_plugin_t self, svn_error_t get_log) """
    pass

def svn_ra_plugin_t_get_repos_root_get(svn_ra_plugin_t_self): # real signature unknown; restored from __doc__
    """ svn_ra_plugin_t_get_repos_root_get(svn_ra_plugin_t self) -> svn_error_t """
    pass

def svn_ra_plugin_t_get_repos_root_set(svn_ra_plugin_t_self, svn_error_t_get_repos_root): # real signature unknown; restored from __doc__
    """ svn_ra_plugin_t_get_repos_root_set(svn_ra_plugin_t self, svn_error_t get_repos_root) """
    pass

def svn_ra_plugin_t_get_uuid_get(svn_ra_plugin_t_self): # real signature unknown; restored from __doc__
    """ svn_ra_plugin_t_get_uuid_get(svn_ra_plugin_t self) -> svn_error_t """
    pass

def svn_ra_plugin_t_get_uuid_set(svn_ra_plugin_t_self, svn_error_t_get_uuid): # real signature unknown; restored from __doc__
    """ svn_ra_plugin_t_get_uuid_set(svn_ra_plugin_t self, svn_error_t get_uuid) """
    pass

def svn_ra_plugin_t_get_version_get(svn_ra_plugin_t_self): # real signature unknown; restored from __doc__
    """ svn_ra_plugin_t_get_version_get(svn_ra_plugin_t self) -> svn_version_t """
    pass

def svn_ra_plugin_t_get_version_set(svn_ra_plugin_t_self, svn_version_t_get_version): # real signature unknown; restored from __doc__
    """ svn_ra_plugin_t_get_version_set(svn_ra_plugin_t self, svn_version_t get_version) """
    pass

def svn_ra_plugin_t_name_get(svn_ra_plugin_t_self): # real signature unknown; restored from __doc__
    """ svn_ra_plugin_t_name_get(svn_ra_plugin_t self) -> char """
    return ""

def svn_ra_plugin_t_name_set(svn_ra_plugin_t_self, char_name): # real signature unknown; restored from __doc__
    """ svn_ra_plugin_t_name_set(svn_ra_plugin_t self, char name) """
    pass

def svn_ra_plugin_t_open_get(svn_ra_plugin_t_self): # real signature unknown; restored from __doc__
    """ svn_ra_plugin_t_open_get(svn_ra_plugin_t self) -> svn_error_t """
    pass

def svn_ra_plugin_t_open_set(svn_ra_plugin_t_self, svn_error_t_open): # real signature unknown; restored from __doc__
    """ svn_ra_plugin_t_open_set(svn_ra_plugin_t self, svn_error_t open) """
    pass

def svn_ra_plugin_t_rev_proplist_get(svn_ra_plugin_t_self): # real signature unknown; restored from __doc__
    """ svn_ra_plugin_t_rev_proplist_get(svn_ra_plugin_t self) -> svn_error_t """
    pass

def svn_ra_plugin_t_rev_proplist_set(svn_ra_plugin_t_self, svn_error_t_rev_proplist): # real signature unknown; restored from __doc__
    """ svn_ra_plugin_t_rev_proplist_set(svn_ra_plugin_t self, svn_error_t rev_proplist) """
    pass

def svn_ra_plugin_t_rev_prop_get(svn_ra_plugin_t_self): # real signature unknown; restored from __doc__
    """ svn_ra_plugin_t_rev_prop_get(svn_ra_plugin_t self) -> svn_error_t """
    pass

def svn_ra_plugin_t_rev_prop_set(svn_ra_plugin_t_self, svn_error_t_rev_prop): # real signature unknown; restored from __doc__
    """ svn_ra_plugin_t_rev_prop_set(svn_ra_plugin_t self, svn_error_t rev_prop) """
    pass

def svn_ra_plugin_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def svn_ra_print_modules(svn_stringbuf_t_output, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_ra_print_modules(svn_stringbuf_t output, apr_pool_t pool) -> svn_error_t """
    pass

def svn_ra_print_ra_libraries(svn_stringbuf_t_descriptions, void_ra_baton, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_ra_print_ra_libraries(svn_stringbuf_t descriptions, void ra_baton, apr_pool_t pool) -> svn_error_t """
    pass

def svn_ra_progress_notify_func_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def svn_ra_push_wc_prop_func_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def svn_ra_reparent(svn_ra_session_t_ra_session, char_url, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_ra_reparent(svn_ra_session_t ra_session, char url, apr_pool_t pool) -> svn_error_t """
    pass

def svn_ra_replay(svn_ra_session_t_session, svn_revnum_t_revision, svn_revnum_t_low_water_mark, svn_boolean_t_send_deltas, svn_delta_editor_t_editor, void_edit_baton, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_replay(svn_ra_session_t session, svn_revnum_t revision, svn_revnum_t low_water_mark, 
        svn_boolean_t send_deltas, 
        svn_delta_editor_t editor, void edit_baton, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_replay_range(svn_ra_session_t_session, svn_revnum_t_start_revision, svn_revnum_t_end_revision, svn_revnum_t_low_water_mark, svn_boolean_t_send_deltas, svn_ra_replay_revstart_callback_t_revstart_func, svn_ra_replay_revfinish_callback_t_revfinish_func, void_replay_baton, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_replay_range(svn_ra_session_t session, svn_revnum_t start_revision, 
        svn_revnum_t end_revision, svn_revnum_t low_water_mark, 
        svn_boolean_t send_deltas, svn_ra_replay_revstart_callback_t revstart_func, 
        svn_ra_replay_revfinish_callback_t revfinish_func, 
        void replay_baton, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_replay_revfinish_callback_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def svn_ra_replay_revstart_callback_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def svn_ra_reporter2_invoke_abort_report(svn_ra_reporter2_t__obj, void_report_baton, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_ra_reporter2_invoke_abort_report(svn_ra_reporter2_t _obj, void report_baton, apr_pool_t pool) -> svn_error_t """
    pass

def svn_ra_reporter2_invoke_delete_path(svn_ra_reporter2_t__obj, void_report_baton, char_path, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_reporter2_invoke_delete_path(svn_ra_reporter2_t _obj, void report_baton, char path, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_reporter2_invoke_finish_report(svn_ra_reporter2_t__obj, void_report_baton, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_ra_reporter2_invoke_finish_report(svn_ra_reporter2_t _obj, void report_baton, apr_pool_t pool) -> svn_error_t """
    pass

def svn_ra_reporter2_invoke_link_path(svn_ra_reporter2_t__obj, void_report_baton, char_path, char_url, svn_revnum_t_revision, svn_boolean_t_start_empty, char_lock_token, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_reporter2_invoke_link_path(svn_ra_reporter2_t _obj, void report_baton, char path, 
        char url, svn_revnum_t revision, svn_boolean_t start_empty, 
        char lock_token, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_reporter2_invoke_set_path(svn_ra_reporter2_t__obj, void_report_baton, char_path, svn_revnum_t_revision, svn_boolean_t_start_empty, char_lock_token, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_reporter2_invoke_set_path(svn_ra_reporter2_t _obj, void report_baton, char path, 
        svn_revnum_t revision, svn_boolean_t start_empty, 
        char lock_token, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_reporter2_t_abort_report_get(svn_ra_reporter2_t_self): # real signature unknown; restored from __doc__
    """ svn_ra_reporter2_t_abort_report_get(svn_ra_reporter2_t self) -> svn_error_t """
    pass

def svn_ra_reporter2_t_abort_report_set(svn_ra_reporter2_t_self, svn_error_t_abort_report): # real signature unknown; restored from __doc__
    """ svn_ra_reporter2_t_abort_report_set(svn_ra_reporter2_t self, svn_error_t abort_report) """
    pass

def svn_ra_reporter2_t_delete_path_get(svn_ra_reporter2_t_self): # real signature unknown; restored from __doc__
    """ svn_ra_reporter2_t_delete_path_get(svn_ra_reporter2_t self) -> svn_error_t """
    pass

def svn_ra_reporter2_t_delete_path_set(svn_ra_reporter2_t_self, svn_error_t_delete_path): # real signature unknown; restored from __doc__
    """ svn_ra_reporter2_t_delete_path_set(svn_ra_reporter2_t self, svn_error_t delete_path) """
    pass

def svn_ra_reporter2_t_finish_report_get(svn_ra_reporter2_t_self): # real signature unknown; restored from __doc__
    """ svn_ra_reporter2_t_finish_report_get(svn_ra_reporter2_t self) -> svn_error_t """
    pass

def svn_ra_reporter2_t_finish_report_set(svn_ra_reporter2_t_self, svn_error_t_finish_report): # real signature unknown; restored from __doc__
    """ svn_ra_reporter2_t_finish_report_set(svn_ra_reporter2_t self, svn_error_t finish_report) """
    pass

def svn_ra_reporter2_t_link_path_get(svn_ra_reporter2_t_self): # real signature unknown; restored from __doc__
    """ svn_ra_reporter2_t_link_path_get(svn_ra_reporter2_t self) -> svn_error_t """
    pass

def svn_ra_reporter2_t_link_path_set(svn_ra_reporter2_t_self, svn_error_t_link_path): # real signature unknown; restored from __doc__
    """ svn_ra_reporter2_t_link_path_set(svn_ra_reporter2_t self, svn_error_t link_path) """
    pass

def svn_ra_reporter2_t_set_path_get(svn_ra_reporter2_t_self): # real signature unknown; restored from __doc__
    """ svn_ra_reporter2_t_set_path_get(svn_ra_reporter2_t self) -> svn_error_t """
    pass

def svn_ra_reporter2_t_set_path_set(svn_ra_reporter2_t_self, svn_error_t_set_path): # real signature unknown; restored from __doc__
    """ svn_ra_reporter2_t_set_path_set(svn_ra_reporter2_t self, svn_error_t set_path) """
    pass

def svn_ra_reporter2_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def svn_ra_reporter3_invoke_abort_report(svn_ra_reporter3_t__obj, void_report_baton, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_ra_reporter3_invoke_abort_report(svn_ra_reporter3_t _obj, void report_baton, apr_pool_t pool) -> svn_error_t """
    pass

def svn_ra_reporter3_invoke_delete_path(svn_ra_reporter3_t__obj, void_report_baton, char_path, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_reporter3_invoke_delete_path(svn_ra_reporter3_t _obj, void report_baton, char path, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_reporter3_invoke_finish_report(svn_ra_reporter3_t__obj, void_report_baton, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_ra_reporter3_invoke_finish_report(svn_ra_reporter3_t _obj, void report_baton, apr_pool_t pool) -> svn_error_t """
    pass

def svn_ra_reporter3_invoke_link_path(svn_ra_reporter3_t__obj, void_report_baton, char_path, char_url, svn_revnum_t_revision, svn_depth_t_depth, svn_boolean_t_start_empty, char_lock_token, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_reporter3_invoke_link_path(svn_ra_reporter3_t _obj, void report_baton, char path, 
        char url, svn_revnum_t revision, svn_depth_t depth, 
        svn_boolean_t start_empty, char lock_token, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_reporter3_invoke_set_path(svn_ra_reporter3_t__obj, void_report_baton, char_path, svn_revnum_t_revision, svn_depth_t_depth, svn_boolean_t_start_empty, char_lock_token, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_reporter3_invoke_set_path(svn_ra_reporter3_t _obj, void report_baton, char path, 
        svn_revnum_t revision, svn_depth_t depth, 
        svn_boolean_t start_empty, char lock_token, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_reporter3_t_abort_report_get(svn_ra_reporter3_t_self): # real signature unknown; restored from __doc__
    """ svn_ra_reporter3_t_abort_report_get(svn_ra_reporter3_t self) -> svn_error_t """
    pass

def svn_ra_reporter3_t_abort_report_set(svn_ra_reporter3_t_self, svn_error_t_abort_report): # real signature unknown; restored from __doc__
    """ svn_ra_reporter3_t_abort_report_set(svn_ra_reporter3_t self, svn_error_t abort_report) """
    pass

def svn_ra_reporter3_t_delete_path_get(svn_ra_reporter3_t_self): # real signature unknown; restored from __doc__
    """ svn_ra_reporter3_t_delete_path_get(svn_ra_reporter3_t self) -> svn_error_t """
    pass

def svn_ra_reporter3_t_delete_path_set(svn_ra_reporter3_t_self, svn_error_t_delete_path): # real signature unknown; restored from __doc__
    """ svn_ra_reporter3_t_delete_path_set(svn_ra_reporter3_t self, svn_error_t delete_path) """
    pass

def svn_ra_reporter3_t_finish_report_get(svn_ra_reporter3_t_self): # real signature unknown; restored from __doc__
    """ svn_ra_reporter3_t_finish_report_get(svn_ra_reporter3_t self) -> svn_error_t """
    pass

def svn_ra_reporter3_t_finish_report_set(svn_ra_reporter3_t_self, svn_error_t_finish_report): # real signature unknown; restored from __doc__
    """ svn_ra_reporter3_t_finish_report_set(svn_ra_reporter3_t self, svn_error_t finish_report) """
    pass

def svn_ra_reporter3_t_link_path_get(svn_ra_reporter3_t_self): # real signature unknown; restored from __doc__
    """ svn_ra_reporter3_t_link_path_get(svn_ra_reporter3_t self) -> svn_error_t """
    pass

def svn_ra_reporter3_t_link_path_set(svn_ra_reporter3_t_self, svn_error_t_link_path): # real signature unknown; restored from __doc__
    """ svn_ra_reporter3_t_link_path_set(svn_ra_reporter3_t self, svn_error_t link_path) """
    pass

def svn_ra_reporter3_t_set_path_get(svn_ra_reporter3_t_self): # real signature unknown; restored from __doc__
    """ svn_ra_reporter3_t_set_path_get(svn_ra_reporter3_t self) -> svn_error_t """
    pass

def svn_ra_reporter3_t_set_path_set(svn_ra_reporter3_t_self, svn_error_t_set_path): # real signature unknown; restored from __doc__
    """ svn_ra_reporter3_t_set_path_set(svn_ra_reporter3_t self, svn_error_t set_path) """
    pass

def svn_ra_reporter3_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def svn_ra_reporter_invoke_abort_report(svn_ra_reporter_t__obj, void_report_baton, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_ra_reporter_invoke_abort_report(svn_ra_reporter_t _obj, void report_baton, apr_pool_t pool) -> svn_error_t """
    pass

def svn_ra_reporter_invoke_delete_path(svn_ra_reporter_t__obj, void_report_baton, char_path, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_reporter_invoke_delete_path(svn_ra_reporter_t _obj, void report_baton, char path, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_reporter_invoke_finish_report(svn_ra_reporter_t__obj, void_report_baton, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_ra_reporter_invoke_finish_report(svn_ra_reporter_t _obj, void report_baton, apr_pool_t pool) -> svn_error_t """
    pass

def svn_ra_reporter_invoke_link_path(svn_ra_reporter_t__obj, void_report_baton, char_path, char_url, svn_revnum_t_revision, svn_boolean_t_start_empty, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_reporter_invoke_link_path(svn_ra_reporter_t _obj, void report_baton, char path, 
        char url, svn_revnum_t revision, svn_boolean_t start_empty, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_reporter_invoke_set_path(svn_ra_reporter_t__obj, void_report_baton, char_path, svn_revnum_t_revision, svn_boolean_t_start_empty, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_reporter_invoke_set_path(svn_ra_reporter_t _obj, void report_baton, char path, 
        svn_revnum_t revision, svn_boolean_t start_empty, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_reporter_t_abort_report_get(svn_ra_reporter_t_self): # real signature unknown; restored from __doc__
    """ svn_ra_reporter_t_abort_report_get(svn_ra_reporter_t self) -> svn_error_t """
    pass

def svn_ra_reporter_t_abort_report_set(svn_ra_reporter_t_self, svn_error_t_abort_report): # real signature unknown; restored from __doc__
    """ svn_ra_reporter_t_abort_report_set(svn_ra_reporter_t self, svn_error_t abort_report) """
    pass

def svn_ra_reporter_t_delete_path_get(svn_ra_reporter_t_self): # real signature unknown; restored from __doc__
    """ svn_ra_reporter_t_delete_path_get(svn_ra_reporter_t self) -> svn_error_t """
    pass

def svn_ra_reporter_t_delete_path_set(svn_ra_reporter_t_self, svn_error_t_delete_path): # real signature unknown; restored from __doc__
    """ svn_ra_reporter_t_delete_path_set(svn_ra_reporter_t self, svn_error_t delete_path) """
    pass

def svn_ra_reporter_t_finish_report_get(svn_ra_reporter_t_self): # real signature unknown; restored from __doc__
    """ svn_ra_reporter_t_finish_report_get(svn_ra_reporter_t self) -> svn_error_t """
    pass

def svn_ra_reporter_t_finish_report_set(svn_ra_reporter_t_self, svn_error_t_finish_report): # real signature unknown; restored from __doc__
    """ svn_ra_reporter_t_finish_report_set(svn_ra_reporter_t self, svn_error_t finish_report) """
    pass

def svn_ra_reporter_t_link_path_get(svn_ra_reporter_t_self): # real signature unknown; restored from __doc__
    """ svn_ra_reporter_t_link_path_get(svn_ra_reporter_t self) -> svn_error_t """
    pass

def svn_ra_reporter_t_link_path_set(svn_ra_reporter_t_self, svn_error_t_link_path): # real signature unknown; restored from __doc__
    """ svn_ra_reporter_t_link_path_set(svn_ra_reporter_t self, svn_error_t link_path) """
    pass

def svn_ra_reporter_t_set_path_get(svn_ra_reporter_t_self): # real signature unknown; restored from __doc__
    """ svn_ra_reporter_t_set_path_get(svn_ra_reporter_t self) -> svn_error_t """
    pass

def svn_ra_reporter_t_set_path_set(svn_ra_reporter_t_self, svn_error_t_set_path): # real signature unknown; restored from __doc__
    """ svn_ra_reporter_t_set_path_set(svn_ra_reporter_t self, svn_error_t set_path) """
    pass

def svn_ra_reporter_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def svn_ra_rev_prop(svn_ra_session_t_session, svn_revnum_t_rev, char_name, svn_string_t_value, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_rev_prop(svn_ra_session_t session, svn_revnum_t rev, char name, 
        svn_string_t value, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_rev_proplist(svn_ra_session_t_session, svn_revnum_t_rev, apr_hash_t_props, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_rev_proplist(svn_ra_session_t session, svn_revnum_t rev, apr_hash_t props, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_session_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def svn_ra_set_wc_prop_func_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def svn_ra_stat(svn_ra_session_t_session, char_path, svn_revnum_t_revision, svn_dirent_t_dirent, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_stat(svn_ra_session_t session, char path, svn_revnum_t revision, 
        svn_dirent_t dirent, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_unlock(svn_ra_session_t_session, apr_hash_t_path_tokens, svn_boolean_t_break_lock, svn_ra_lock_callback_t_lock_func, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_ra_unlock(svn_ra_session_t session, apr_hash_t path_tokens, svn_boolean_t break_lock, 
        svn_ra_lock_callback_t lock_func, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_ra_version(): # real signature unknown; restored from __doc__
    """ svn_ra_version() -> svn_version_t """
    pass

# no classes
