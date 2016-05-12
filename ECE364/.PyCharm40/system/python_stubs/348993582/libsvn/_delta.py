# encoding: utf-8
# module libsvn._delta
# from /usr/lib64/python2.6/site-packages/libsvn/_delta.so
# by generator 1.136
# no doc
# no imports

# Variables with simple values

svn_txdelta_new = 2
svn_txdelta_source = 0
svn_txdelta_target = 1

# functions

def delete_svn_delta_editor_t(svn_delta_editor_t_self): # real signature unknown; restored from __doc__
    """ delete_svn_delta_editor_t(svn_delta_editor_t self) """
    pass

def delete_svn_txdelta_op_t(svn_txdelta_op_t_self): # real signature unknown; restored from __doc__
    """ delete_svn_txdelta_op_t(svn_txdelta_op_t self) """
    pass

def delete_svn_txdelta_window_t(svn_txdelta_window_t_self): # real signature unknown; restored from __doc__
    """ delete_svn_txdelta_window_t(svn_txdelta_window_t self) """
    pass

def new_svn_delta_editor_t(): # real signature unknown; restored from __doc__
    """ new_svn_delta_editor_t() -> svn_delta_editor_t """
    pass

def new_svn_txdelta_op_t(): # real signature unknown; restored from __doc__
    """ new_svn_txdelta_op_t() -> svn_txdelta_op_t """
    pass

def new_svn_txdelta_window_t(): # real signature unknown; restored from __doc__
    """ new_svn_txdelta_window_t() -> svn_txdelta_window_t """
    pass

def svn_compat_wrap_file_rev_handler(svn_file_rev_handler_t_handler2, void_handler2_baton, svn_file_rev_handler_old_t_handler, void_handler_baton, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_compat_wrap_file_rev_handler(svn_file_rev_handler_t handler2, void handler2_baton, 
        svn_file_rev_handler_old_t handler, void handler_baton, 
        apr_pool_t pool)
    """
    pass

def svn_delta_default_editor(apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_delta_default_editor(apr_pool_t pool) -> svn_delta_editor_t """
    pass

def svn_delta_depth_filter_editor(svn_delta_editor_t_editor, void_edit_baton, svn_delta_editor_t_wrapped_editor, void_wrapped_edit_baton, svn_depth_t_requested_depth, svn_boolean_t_has_target, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_delta_depth_filter_editor(svn_delta_editor_t editor, void edit_baton, svn_delta_editor_t wrapped_editor, 
        void wrapped_edit_baton, 
        svn_depth_t requested_depth, svn_boolean_t has_target, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_delta_editor_invoke_abort_edit(svn_delta_editor_t__obj, void_edit_baton, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_delta_editor_invoke_abort_edit(svn_delta_editor_t _obj, void edit_baton, apr_pool_t pool) -> svn_error_t """
    pass

def svn_delta_editor_invoke_absent_directory(svn_delta_editor_t__obj, char_path, void_parent_baton, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_delta_editor_invoke_absent_directory(svn_delta_editor_t _obj, char path, void parent_baton, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_delta_editor_invoke_absent_file(svn_delta_editor_t__obj, char_path, void_parent_baton, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_delta_editor_invoke_absent_file(svn_delta_editor_t _obj, char path, void parent_baton, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_delta_editor_invoke_add_directory(svn_delta_editor_t__obj, char_path, void_parent_baton, char_copyfrom_path, svn_revnum_t_copyfrom_revision, apr_pool_t_dir_pool, void_child_baton): # real signature unknown; restored from __doc__
    """
    svn_delta_editor_invoke_add_directory(svn_delta_editor_t _obj, char path, void parent_baton, 
        char copyfrom_path, svn_revnum_t copyfrom_revision, 
        apr_pool_t dir_pool, void child_baton) -> svn_error_t
    """
    pass

def svn_delta_editor_invoke_add_file(svn_delta_editor_t__obj, char_path, void_parent_baton, char_copyfrom_path, svn_revnum_t_copyfrom_revision, apr_pool_t_file_pool, void_file_baton): # real signature unknown; restored from __doc__
    """
    svn_delta_editor_invoke_add_file(svn_delta_editor_t _obj, char path, void parent_baton, 
        char copyfrom_path, svn_revnum_t copyfrom_revision, 
        apr_pool_t file_pool, void file_baton) -> svn_error_t
    """
    pass

def svn_delta_editor_invoke_apply_textdelta(svn_delta_editor_t__obj, void_file_baton, char_base_checksum, apr_pool_t_pool, svn_txdelta_window_handler_t_handler, void_handler_baton): # real signature unknown; restored from __doc__
    """
    svn_delta_editor_invoke_apply_textdelta(svn_delta_editor_t _obj, void file_baton, char base_checksum, 
        apr_pool_t pool, svn_txdelta_window_handler_t handler, 
        void handler_baton) -> svn_error_t
    """
    pass

def svn_delta_editor_invoke_change_dir_prop(svn_delta_editor_t__obj, void_dir_baton, char_name, svn_string_t_value, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_delta_editor_invoke_change_dir_prop(svn_delta_editor_t _obj, void dir_baton, char name, 
        svn_string_t value, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_delta_editor_invoke_change_file_prop(svn_delta_editor_t__obj, void_file_baton, char_name, svn_string_t_value, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_delta_editor_invoke_change_file_prop(svn_delta_editor_t _obj, void file_baton, char name, 
        svn_string_t value, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_delta_editor_invoke_close_directory(svn_delta_editor_t__obj, void_dir_baton, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_delta_editor_invoke_close_directory(svn_delta_editor_t _obj, void dir_baton, apr_pool_t pool) -> svn_error_t """
    pass

def svn_delta_editor_invoke_close_edit(svn_delta_editor_t__obj, void_edit_baton, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_delta_editor_invoke_close_edit(svn_delta_editor_t _obj, void edit_baton, apr_pool_t pool) -> svn_error_t """
    pass

def svn_delta_editor_invoke_close_file(svn_delta_editor_t__obj, void_file_baton, char_text_checksum, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_delta_editor_invoke_close_file(svn_delta_editor_t _obj, void file_baton, char text_checksum, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_delta_editor_invoke_delete_entry(svn_delta_editor_t__obj, char_path, svn_revnum_t_revision, void_parent_baton, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_delta_editor_invoke_delete_entry(svn_delta_editor_t _obj, char path, svn_revnum_t revision, 
        void parent_baton, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_delta_editor_invoke_open_directory(svn_delta_editor_t__obj, char_path, void_parent_baton, svn_revnum_t_base_revision, apr_pool_t_dir_pool, void_child_baton): # real signature unknown; restored from __doc__
    """
    svn_delta_editor_invoke_open_directory(svn_delta_editor_t _obj, char path, void parent_baton, 
        svn_revnum_t base_revision, apr_pool_t dir_pool, 
        void child_baton) -> svn_error_t
    """
    pass

def svn_delta_editor_invoke_open_file(svn_delta_editor_t__obj, char_path, void_parent_baton, svn_revnum_t_base_revision, apr_pool_t_file_pool, void_file_baton): # real signature unknown; restored from __doc__
    """
    svn_delta_editor_invoke_open_file(svn_delta_editor_t _obj, char path, void parent_baton, 
        svn_revnum_t base_revision, apr_pool_t file_pool, 
        void file_baton) -> svn_error_t
    """
    pass

def svn_delta_editor_invoke_open_root(svn_delta_editor_t__obj, void_edit_baton, svn_revnum_t_base_revision, apr_pool_t_dir_pool, void_root_baton): # real signature unknown; restored from __doc__
    """
    svn_delta_editor_invoke_open_root(svn_delta_editor_t _obj, void edit_baton, svn_revnum_t base_revision, 
        apr_pool_t dir_pool, void root_baton) -> svn_error_t
    """
    pass

def svn_delta_editor_invoke_set_target_revision(svn_delta_editor_t__obj, void_edit_baton, svn_revnum_t_target_revision, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_delta_editor_invoke_set_target_revision(svn_delta_editor_t _obj, void edit_baton, svn_revnum_t target_revision, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_delta_editor_t_abort_edit_get(svn_delta_editor_t_self): # real signature unknown; restored from __doc__
    """ svn_delta_editor_t_abort_edit_get(svn_delta_editor_t self) -> svn_error_t """
    pass

def svn_delta_editor_t_abort_edit_set(svn_delta_editor_t_self, svn_error_t_abort_edit): # real signature unknown; restored from __doc__
    """ svn_delta_editor_t_abort_edit_set(svn_delta_editor_t self, svn_error_t abort_edit) """
    pass

def svn_delta_editor_t_absent_directory_get(svn_delta_editor_t_self): # real signature unknown; restored from __doc__
    """ svn_delta_editor_t_absent_directory_get(svn_delta_editor_t self) -> svn_error_t """
    pass

def svn_delta_editor_t_absent_directory_set(svn_delta_editor_t_self, svn_error_t_absent_directory): # real signature unknown; restored from __doc__
    """ svn_delta_editor_t_absent_directory_set(svn_delta_editor_t self, svn_error_t absent_directory) """
    pass

def svn_delta_editor_t_absent_file_get(svn_delta_editor_t_self): # real signature unknown; restored from __doc__
    """ svn_delta_editor_t_absent_file_get(svn_delta_editor_t self) -> svn_error_t """
    pass

def svn_delta_editor_t_absent_file_set(svn_delta_editor_t_self, svn_error_t_absent_file): # real signature unknown; restored from __doc__
    """ svn_delta_editor_t_absent_file_set(svn_delta_editor_t self, svn_error_t absent_file) """
    pass

def svn_delta_editor_t_add_directory_get(svn_delta_editor_t_self): # real signature unknown; restored from __doc__
    """ svn_delta_editor_t_add_directory_get(svn_delta_editor_t self) -> svn_error_t """
    pass

def svn_delta_editor_t_add_directory_set(svn_delta_editor_t_self, svn_error_t_add_directory): # real signature unknown; restored from __doc__
    """ svn_delta_editor_t_add_directory_set(svn_delta_editor_t self, svn_error_t add_directory) """
    pass

def svn_delta_editor_t_add_file_get(svn_delta_editor_t_self): # real signature unknown; restored from __doc__
    """ svn_delta_editor_t_add_file_get(svn_delta_editor_t self) -> svn_error_t """
    pass

def svn_delta_editor_t_add_file_set(svn_delta_editor_t_self, svn_error_t_add_file): # real signature unknown; restored from __doc__
    """ svn_delta_editor_t_add_file_set(svn_delta_editor_t self, svn_error_t add_file) """
    pass

def svn_delta_editor_t_apply_textdelta_get(svn_delta_editor_t_self): # real signature unknown; restored from __doc__
    """ svn_delta_editor_t_apply_textdelta_get(svn_delta_editor_t self) -> svn_error_t """
    pass

def svn_delta_editor_t_apply_textdelta_set(svn_delta_editor_t_self, svn_error_t_apply_textdelta): # real signature unknown; restored from __doc__
    """ svn_delta_editor_t_apply_textdelta_set(svn_delta_editor_t self, svn_error_t apply_textdelta) """
    pass

def svn_delta_editor_t_change_dir_prop_get(svn_delta_editor_t_self): # real signature unknown; restored from __doc__
    """ svn_delta_editor_t_change_dir_prop_get(svn_delta_editor_t self) -> svn_error_t """
    pass

def svn_delta_editor_t_change_dir_prop_set(svn_delta_editor_t_self, svn_error_t_change_dir_prop): # real signature unknown; restored from __doc__
    """ svn_delta_editor_t_change_dir_prop_set(svn_delta_editor_t self, svn_error_t change_dir_prop) """
    pass

def svn_delta_editor_t_change_file_prop_get(svn_delta_editor_t_self): # real signature unknown; restored from __doc__
    """ svn_delta_editor_t_change_file_prop_get(svn_delta_editor_t self) -> svn_error_t """
    pass

def svn_delta_editor_t_change_file_prop_set(svn_delta_editor_t_self, svn_error_t_change_file_prop): # real signature unknown; restored from __doc__
    """ svn_delta_editor_t_change_file_prop_set(svn_delta_editor_t self, svn_error_t change_file_prop) """
    pass

def svn_delta_editor_t_close_directory_get(svn_delta_editor_t_self): # real signature unknown; restored from __doc__
    """ svn_delta_editor_t_close_directory_get(svn_delta_editor_t self) -> svn_error_t """
    pass

def svn_delta_editor_t_close_directory_set(svn_delta_editor_t_self, svn_error_t_close_directory): # real signature unknown; restored from __doc__
    """ svn_delta_editor_t_close_directory_set(svn_delta_editor_t self, svn_error_t close_directory) """
    pass

def svn_delta_editor_t_close_edit_get(svn_delta_editor_t_self): # real signature unknown; restored from __doc__
    """ svn_delta_editor_t_close_edit_get(svn_delta_editor_t self) -> svn_error_t """
    pass

def svn_delta_editor_t_close_edit_set(svn_delta_editor_t_self, svn_error_t_close_edit): # real signature unknown; restored from __doc__
    """ svn_delta_editor_t_close_edit_set(svn_delta_editor_t self, svn_error_t close_edit) """
    pass

def svn_delta_editor_t_close_file_get(svn_delta_editor_t_self): # real signature unknown; restored from __doc__
    """ svn_delta_editor_t_close_file_get(svn_delta_editor_t self) -> svn_error_t """
    pass

def svn_delta_editor_t_close_file_set(svn_delta_editor_t_self, svn_error_t_close_file): # real signature unknown; restored from __doc__
    """ svn_delta_editor_t_close_file_set(svn_delta_editor_t self, svn_error_t close_file) """
    pass

def svn_delta_editor_t_delete_entry_get(svn_delta_editor_t_self): # real signature unknown; restored from __doc__
    """ svn_delta_editor_t_delete_entry_get(svn_delta_editor_t self) -> svn_error_t """
    pass

def svn_delta_editor_t_delete_entry_set(svn_delta_editor_t_self, svn_error_t_delete_entry): # real signature unknown; restored from __doc__
    """ svn_delta_editor_t_delete_entry_set(svn_delta_editor_t self, svn_error_t delete_entry) """
    pass

def svn_delta_editor_t_open_directory_get(svn_delta_editor_t_self): # real signature unknown; restored from __doc__
    """ svn_delta_editor_t_open_directory_get(svn_delta_editor_t self) -> svn_error_t """
    pass

def svn_delta_editor_t_open_directory_set(svn_delta_editor_t_self, svn_error_t_open_directory): # real signature unknown; restored from __doc__
    """ svn_delta_editor_t_open_directory_set(svn_delta_editor_t self, svn_error_t open_directory) """
    pass

def svn_delta_editor_t_open_file_get(svn_delta_editor_t_self): # real signature unknown; restored from __doc__
    """ svn_delta_editor_t_open_file_get(svn_delta_editor_t self) -> svn_error_t """
    pass

def svn_delta_editor_t_open_file_set(svn_delta_editor_t_self, svn_error_t_open_file): # real signature unknown; restored from __doc__
    """ svn_delta_editor_t_open_file_set(svn_delta_editor_t self, svn_error_t open_file) """
    pass

def svn_delta_editor_t_open_root_get(svn_delta_editor_t_self): # real signature unknown; restored from __doc__
    """ svn_delta_editor_t_open_root_get(svn_delta_editor_t self) -> svn_error_t """
    pass

def svn_delta_editor_t_open_root_set(svn_delta_editor_t_self, svn_error_t_open_root): # real signature unknown; restored from __doc__
    """ svn_delta_editor_t_open_root_set(svn_delta_editor_t self, svn_error_t open_root) """
    pass

def svn_delta_editor_t_set_target_revision_get(svn_delta_editor_t_self): # real signature unknown; restored from __doc__
    """ svn_delta_editor_t_set_target_revision_get(svn_delta_editor_t self) -> svn_error_t """
    pass

def svn_delta_editor_t_set_target_revision_set(svn_delta_editor_t_self, svn_error_t_set_target_revision): # real signature unknown; restored from __doc__
    """ svn_delta_editor_t_set_target_revision_set(svn_delta_editor_t self, svn_error_t set_target_revision) """
    pass

def svn_delta_editor_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def svn_delta_get_cancellation_editor(svn_cancel_func_t_cancel_func, svn_delta_editor_t_wrapped_editor, void_wrapped_baton, svn_delta_editor_t_editor, void_edit_baton, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_delta_get_cancellation_editor(svn_cancel_func_t cancel_func, svn_delta_editor_t wrapped_editor, 
        void wrapped_baton, svn_delta_editor_t editor, 
        void edit_baton, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_delta_invoke_path_driver_cb_func(svn_delta_path_driver_cb_func_t__obj, void_dir_baton, void_parent_baton, void_callback_baton, char_path, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_delta_invoke_path_driver_cb_func(svn_delta_path_driver_cb_func_t _obj, void dir_baton, 
        void parent_baton, void callback_baton, char path, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_delta_noop_window_handler(svn_txdelta_window_t_window, void_baton): # real signature unknown; restored from __doc__
    """ svn_delta_noop_window_handler(svn_txdelta_window_t window, void baton) -> svn_error_t """
    pass

def svn_delta_path_driver(svn_delta_editor_t_editor, void_edit_baton, svn_revnum_t_revision, apr_array_header_t_paths, svn_delta_path_driver_cb_func_t_callback_func, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_delta_path_driver(svn_delta_editor_t editor, void edit_baton, svn_revnum_t revision, 
        apr_array_header_t paths, svn_delta_path_driver_cb_func_t callback_func, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_delta_path_driver_cb_func_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def svn_delta_version(): # real signature unknown; restored from __doc__
    """ svn_delta_version() -> svn_version_t """
    pass

def svn_file_invoke_rev_handler(svn_file_rev_handler_t__obj, void_baton, char_path, svn_revnum_t_rev, apr_hash_t_rev_props, svn_boolean_t_result_of_merge, svn_txdelta_window_handler_t_delta_handler, void_delta_baton, apr_array_header_t_prop_diffs, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_file_invoke_rev_handler(svn_file_rev_handler_t _obj, void baton, char path, 
        svn_revnum_t rev, apr_hash_t rev_props, svn_boolean_t result_of_merge, 
        svn_txdelta_window_handler_t delta_handler, 
        void delta_baton, apr_array_header_t prop_diffs, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_file_invoke_rev_handler_old(svn_file_rev_handler_old_t__obj, void_baton, char_path, svn_revnum_t_rev, apr_hash_t_rev_props, svn_txdelta_window_handler_t_delta_handler, void_delta_baton, apr_array_header_t_prop_diffs, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_file_invoke_rev_handler_old(svn_file_rev_handler_old_t _obj, void baton, char path, 
        svn_revnum_t rev, apr_hash_t rev_props, 
        svn_txdelta_window_handler_t delta_handler, void delta_baton, 
        apr_array_header_t prop_diffs, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_file_rev_handler_old_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def svn_file_rev_handler_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def svn_swig_py_make_editor(svn_delta_editor_t_editor, void_edit_baton, PyObject_py_editor, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_swig_py_make_editor(svn_delta_editor_t editor, void edit_baton, PyObject py_editor, 
        apr_pool_t pool)
    """
    pass

def svn_txdelta(svn_txdelta_stream_t_stream, svn_stream_t_source, svn_stream_t_target, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_txdelta(svn_txdelta_stream_t stream, svn_stream_t source, svn_stream_t target, 
        apr_pool_t pool)
    """
    pass

def svn_txdelta_apply(svn_stream_t_source, svn_stream_t_target, unsigned_char_result_digest, char_error_info, apr_pool_t_pool, svn_txdelta_window_handler_t_handler, void_handler_baton): # real signature unknown; restored from __doc__
    """
    svn_txdelta_apply(svn_stream_t source, svn_stream_t target, unsigned char result_digest, 
        char error_info, apr_pool_t pool, 
        svn_txdelta_window_handler_t handler, 
        void handler_baton)
    """
    pass

def svn_txdelta_apply_instructions(svn_txdelta_window_t_window, char_sbuf, char_tbuf, apr_size_t_tlen): # real signature unknown; restored from __doc__
    """
    svn_txdelta_apply_instructions(svn_txdelta_window_t window, char sbuf, char tbuf, 
        apr_size_t tlen)
    """
    pass

def svn_txdelta_compose_windows(svn_txdelta_window_t_window_A, svn_txdelta_window_t_window_B, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_txdelta_compose_windows(svn_txdelta_window_t window_A, svn_txdelta_window_t window_B, 
        apr_pool_t pool) -> svn_txdelta_window_t
    """
    pass

def svn_txdelta_invoke_md5_digest_fn(svn_txdelta_md5_digest_fn_t__obj, void_baton): # real signature unknown; restored from __doc__
    """ svn_txdelta_invoke_md5_digest_fn(svn_txdelta_md5_digest_fn_t _obj, void baton) -> unsigned char """
    pass

def svn_txdelta_invoke_next_window_fn(svn_txdelta_next_window_fn_t__obj, svn_txdelta_window_t_window, void_baton, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_txdelta_invoke_next_window_fn(svn_txdelta_next_window_fn_t _obj, svn_txdelta_window_t window, 
        void baton, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_txdelta_invoke_window_handler(svn_txdelta_window_handler_t__obj, svn_txdelta_window_t_window, void_baton): # real signature unknown; restored from __doc__
    """
    svn_txdelta_invoke_window_handler(svn_txdelta_window_handler_t _obj, svn_txdelta_window_t window, 
        void baton) -> svn_error_t
    """
    pass

def svn_txdelta_md5_digest(svn_txdelta_stream_t_stream): # real signature unknown; restored from __doc__
    """ svn_txdelta_md5_digest(svn_txdelta_stream_t stream) -> unsigned char """
    pass

def svn_txdelta_md5_digest_fn_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def svn_txdelta_next_window(svn_txdelta_window_t_window, svn_txdelta_stream_t_stream, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_txdelta_next_window(svn_txdelta_window_t window, svn_txdelta_stream_t stream, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_txdelta_next_window_fn_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def svn_txdelta_op_t_action_code_get(svn_txdelta_op_t_self): # real signature unknown; restored from __doc__
    """ svn_txdelta_op_t_action_code_get(svn_txdelta_op_t self) -> enum svn_delta_action """
    pass

def svn_txdelta_op_t_action_code_set(svn_txdelta_op_t_self, enum_svn_delta_action_action_code): # real signature unknown; restored from __doc__
    """ svn_txdelta_op_t_action_code_set(svn_txdelta_op_t self, enum svn_delta_action action_code) """
    pass

def svn_txdelta_op_t_length_get(svn_txdelta_op_t_self): # real signature unknown; restored from __doc__
    """ svn_txdelta_op_t_length_get(svn_txdelta_op_t self) -> apr_size_t """
    pass

def svn_txdelta_op_t_length_set(svn_txdelta_op_t_self, apr_size_t_length): # real signature unknown; restored from __doc__
    """ svn_txdelta_op_t_length_set(svn_txdelta_op_t self, apr_size_t length) """
    pass

def svn_txdelta_op_t_offset_get(svn_txdelta_op_t_self): # real signature unknown; restored from __doc__
    """ svn_txdelta_op_t_offset_get(svn_txdelta_op_t self) -> apr_size_t """
    pass

def svn_txdelta_op_t_offset_set(svn_txdelta_op_t_self, apr_size_t_offset): # real signature unknown; restored from __doc__
    """ svn_txdelta_op_t_offset_set(svn_txdelta_op_t self, apr_size_t offset) """
    pass

def svn_txdelta_op_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def svn_txdelta_parse_svndiff(svn_txdelta_window_handler_t_handler, void_handler_baton, svn_boolean_t_error_on_early_close, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_txdelta_parse_svndiff(svn_txdelta_window_handler_t handler, void handler_baton, 
        svn_boolean_t error_on_early_close, apr_pool_t pool) -> svn_stream_t
    """
    pass

def svn_txdelta_read_svndiff_window(svn_txdelta_window_t_window, svn_stream_t_stream, int_svndiff_version, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_txdelta_read_svndiff_window(svn_txdelta_window_t window, svn_stream_t stream, int svndiff_version, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_txdelta_run(svn_stream_t_source, svn_stream_t_target, svn_txdelta_window_handler_t_handler, void_handler_baton, svn_checksum_kind_t_checksum_kind, svn_checksum_t_checksum, svn_cancel_func_t_cancel_func, apr_pool_t_result_pool, apr_pool_t_scratch_pool): # real signature unknown; restored from __doc__
    """
    svn_txdelta_run(svn_stream_t source, svn_stream_t target, svn_txdelta_window_handler_t handler, 
        void handler_baton, 
        svn_checksum_kind_t checksum_kind, svn_checksum_t checksum, 
        svn_cancel_func_t cancel_func, 
        apr_pool_t result_pool, apr_pool_t scratch_pool) -> svn_error_t
    """
    pass

def svn_txdelta_send_stream(svn_stream_t_stream, svn_txdelta_window_handler_t_handler, void_handler_baton, unsigned_char_digest, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_txdelta_send_stream(svn_stream_t stream, svn_txdelta_window_handler_t handler, 
        void handler_baton, unsigned char digest, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_txdelta_send_string(svn_string_t_string, svn_txdelta_window_handler_t_handler, void_handler_baton, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_txdelta_send_string(svn_string_t string, svn_txdelta_window_handler_t handler, 
        void handler_baton, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_txdelta_send_txstream(svn_txdelta_stream_t_txstream, svn_txdelta_window_handler_t_handler, void_handler_baton, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_txdelta_send_txstream(svn_txdelta_stream_t txstream, svn_txdelta_window_handler_t handler, 
        void handler_baton, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_txdelta_skip_svndiff_window(apr_file_t_file, int_svndiff_version, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_txdelta_skip_svndiff_window(apr_file_t file, int svndiff_version, apr_pool_t pool) -> svn_error_t """
    pass

def svn_txdelta_stream_create(void_baton, svn_txdelta_next_window_fn_t_next_window, svn_txdelta_md5_digest_fn_t_md5_digest, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_txdelta_stream_create(void baton, svn_txdelta_next_window_fn_t next_window, 
        svn_txdelta_md5_digest_fn_t md5_digest, apr_pool_t pool) -> svn_txdelta_stream_t
    """
    pass

def svn_txdelta_stream_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def svn_txdelta_target_push(svn_txdelta_window_handler_t_handler, void_handler_baton, svn_stream_t_source, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_txdelta_target_push(svn_txdelta_window_handler_t handler, void handler_baton, 
        svn_stream_t source, apr_pool_t pool) -> svn_stream_t
    """
    pass

def svn_txdelta_to_svndiff(svn_stream_t_output, apr_pool_t_pool, svn_txdelta_window_handler_t_handler, void_handler_baton): # real signature unknown; restored from __doc__
    """
    svn_txdelta_to_svndiff(svn_stream_t output, apr_pool_t pool, svn_txdelta_window_handler_t handler, 
        void handler_baton)
    """
    pass

def svn_txdelta_to_svndiff2(svn_txdelta_window_handler_t_handler, void_handler_baton, svn_stream_t_output, int_svndiff_version, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_txdelta_to_svndiff2(svn_txdelta_window_handler_t handler, void handler_baton, 
        svn_stream_t output, int svndiff_version, 
        apr_pool_t pool)
    """
    pass

def svn_txdelta_window_dup(svn_txdelta_window_t_window, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_txdelta_window_dup(svn_txdelta_window_t window, apr_pool_t pool) -> svn_txdelta_window_t """
    pass

def svn_txdelta_window_handler_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def svn_txdelta_window_t_new_data_get(svn_txdelta_window_t_self): # real signature unknown; restored from __doc__
    """ svn_txdelta_window_t_new_data_get(svn_txdelta_window_t self) -> svn_string_t """
    pass

def svn_txdelta_window_t_num_ops_get(svn_txdelta_window_t_self): # real signature unknown; restored from __doc__
    """ svn_txdelta_window_t_num_ops_get(svn_txdelta_window_t self) -> int """
    return 0

def svn_txdelta_window_t_num_ops_set(svn_txdelta_window_t_self, int_num_ops): # real signature unknown; restored from __doc__
    """ svn_txdelta_window_t_num_ops_set(svn_txdelta_window_t self, int num_ops) """
    pass

def svn_txdelta_window_t_ops_get(svn_txdelta_window_t_self): # real signature unknown; restored from __doc__
    """ svn_txdelta_window_t_ops_get(svn_txdelta_window_t self) -> svn_txdelta_op_t """
    pass

def svn_txdelta_window_t_ops_set(svn_txdelta_window_t_self, svn_txdelta_op_t_ops): # real signature unknown; restored from __doc__
    """ svn_txdelta_window_t_ops_set(svn_txdelta_window_t self, svn_txdelta_op_t ops) """
    pass

def svn_txdelta_window_t_src_ops_get(svn_txdelta_window_t_self): # real signature unknown; restored from __doc__
    """ svn_txdelta_window_t_src_ops_get(svn_txdelta_window_t self) -> int """
    return 0

def svn_txdelta_window_t_src_ops_set(svn_txdelta_window_t_self, int_src_ops): # real signature unknown; restored from __doc__
    """ svn_txdelta_window_t_src_ops_set(svn_txdelta_window_t self, int src_ops) """
    pass

def svn_txdelta_window_t_sview_len_get(svn_txdelta_window_t_self): # real signature unknown; restored from __doc__
    """ svn_txdelta_window_t_sview_len_get(svn_txdelta_window_t self) -> apr_size_t """
    pass

def svn_txdelta_window_t_sview_len_set(svn_txdelta_window_t_self, apr_size_t_sview_len): # real signature unknown; restored from __doc__
    """ svn_txdelta_window_t_sview_len_set(svn_txdelta_window_t self, apr_size_t sview_len) """
    pass

def svn_txdelta_window_t_sview_offset_get(svn_txdelta_window_t_self): # real signature unknown; restored from __doc__
    """ svn_txdelta_window_t_sview_offset_get(svn_txdelta_window_t self) -> svn_filesize_t """
    pass

def svn_txdelta_window_t_sview_offset_set(svn_txdelta_window_t_self, svn_filesize_t_sview_offset): # real signature unknown; restored from __doc__
    """ svn_txdelta_window_t_sview_offset_set(svn_txdelta_window_t self, svn_filesize_t sview_offset) """
    pass

def svn_txdelta_window_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def svn_txdelta_window_t_tview_len_get(svn_txdelta_window_t_self): # real signature unknown; restored from __doc__
    """ svn_txdelta_window_t_tview_len_get(svn_txdelta_window_t self) -> apr_size_t """
    pass

def svn_txdelta_window_t_tview_len_set(svn_txdelta_window_t_self, apr_size_t_tview_len): # real signature unknown; restored from __doc__
    """ svn_txdelta_window_t_tview_len_set(svn_txdelta_window_t self, apr_size_t tview_len) """
    pass

# no classes
