# encoding: utf-8
# module libsvn._diff
# from /usr/lib64/python2.6/site-packages/libsvn/_diff.so
# by generator 1.136
# no doc
# no imports

# Variables with simple values

svn_diff_conflict_display_latest = 4
svn_diff_conflict_display_modified = 3

svn_diff_conflict_display_modified_latest = 0

svn_diff_conflict_display_modified_original_latest = 2

svn_diff_conflict_display_only_conflicts = 5

svn_diff_conflict_display_resolved_modified_latest = 1

svn_diff_datasource_ancestor = 3
svn_diff_datasource_latest = 2
svn_diff_datasource_modified = 1
svn_diff_datasource_original = 0

svn_diff_file_ignore_space_all = 2
svn_diff_file_ignore_space_change = 1
svn_diff_file_ignore_space_none = 0

# functions

def delete_svn_diff_file_options_t(svn_diff_file_options_t_self): # real signature unknown; restored from __doc__
    """ delete_svn_diff_file_options_t(svn_diff_file_options_t self) """
    pass

def delete_svn_diff_fns_t(svn_diff_fns_t_self): # real signature unknown; restored from __doc__
    """ delete_svn_diff_fns_t(svn_diff_fns_t self) """
    pass

def delete_svn_diff_output_fns_t(svn_diff_output_fns_t_self): # real signature unknown; restored from __doc__
    """ delete_svn_diff_output_fns_t(svn_diff_output_fns_t self) """
    pass

def new_svn_diff_file_options_t(): # real signature unknown; restored from __doc__
    """ new_svn_diff_file_options_t() -> svn_diff_file_options_t """
    pass

def new_svn_diff_fns_t(): # real signature unknown; restored from __doc__
    """ new_svn_diff_fns_t() -> svn_diff_fns_t """
    pass

def new_svn_diff_output_fns_t(): # real signature unknown; restored from __doc__
    """ new_svn_diff_output_fns_t() -> svn_diff_output_fns_t """
    pass

def svn_diff_contains_conflicts(svn_diff_t_diff): # real signature unknown; restored from __doc__
    """ svn_diff_contains_conflicts(svn_diff_t diff) -> svn_boolean_t """
    pass

def svn_diff_contains_diffs(svn_diff_t_diff): # real signature unknown; restored from __doc__
    """ svn_diff_contains_diffs(svn_diff_t diff) -> svn_boolean_t """
    pass

def svn_diff_diff(svn_diff_t_diff, void_diff_baton, svn_diff_fns_t_diff_fns, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_diff_diff(svn_diff_t diff, void diff_baton, svn_diff_fns_t diff_fns, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_diff_diff3(svn_diff_t_diff, void_diff_baton, svn_diff_fns_t_diff_fns, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_diff_diff3(svn_diff_t diff, void diff_baton, svn_diff_fns_t diff_fns, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_diff_diff4(svn_diff_t_diff, void_diff_baton, svn_diff_fns_t_diff_fns, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_diff_diff4(svn_diff_t diff, void diff_baton, svn_diff_fns_t diff_fns, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_diff_file_diff(svn_diff_t_diff, char_original, char_modified, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_diff_file_diff(svn_diff_t diff, char original, char modified, apr_pool_t pool) -> svn_error_t """
    pass

def svn_diff_file_diff3(svn_diff_t_diff, char_original, char_modified, char_latest, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_diff_file_diff3(svn_diff_t diff, char original, char modified, char latest, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_diff_file_diff3_2(svn_diff_t_diff, char_original, char_modified, char_latest, svn_diff_file_options_t_options, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_diff_file_diff3_2(svn_diff_t diff, char original, char modified, char latest, 
        svn_diff_file_options_t options, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_diff_file_diff4(svn_diff_t_diff, char_original, char_modified, char_latest, char_ancestor, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_diff_file_diff4(svn_diff_t diff, char original, char modified, char latest, 
        char ancestor, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_diff_file_diff4_2(svn_diff_t_diff, char_original, char_modified, char_latest, char_ancestor, svn_diff_file_options_t_options, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_diff_file_diff4_2(svn_diff_t diff, char original, char modified, char latest, 
        char ancestor, svn_diff_file_options_t options, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_diff_file_diff_2(svn_diff_t_diff, char_original, char_modified, svn_diff_file_options_t_options, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_diff_file_diff_2(svn_diff_t diff, char original, char modified, svn_diff_file_options_t options, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_diff_file_options_create(apr_pool_t_pool): # real signature unknown; restored from __doc__
    """ svn_diff_file_options_create(apr_pool_t pool) -> svn_diff_file_options_t """
    pass

def svn_diff_file_options_parse(svn_diff_file_options_t_options, apr_array_header_t_args, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_diff_file_options_parse(svn_diff_file_options_t options, apr_array_header_t args, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_diff_file_options_t_ignore_eol_style_get(svn_diff_file_options_t_self): # real signature unknown; restored from __doc__
    """ svn_diff_file_options_t_ignore_eol_style_get(svn_diff_file_options_t self) -> svn_boolean_t """
    pass

def svn_diff_file_options_t_ignore_eol_style_set(svn_diff_file_options_t_self, svn_boolean_t_ignore_eol_style): # real signature unknown; restored from __doc__
    """ svn_diff_file_options_t_ignore_eol_style_set(svn_diff_file_options_t self, svn_boolean_t ignore_eol_style) """
    pass

def svn_diff_file_options_t_ignore_space_get(svn_diff_file_options_t_self): # real signature unknown; restored from __doc__
    """ svn_diff_file_options_t_ignore_space_get(svn_diff_file_options_t self) -> svn_diff_file_ignore_space_t """
    pass

def svn_diff_file_options_t_ignore_space_set(svn_diff_file_options_t_self, svn_diff_file_ignore_space_t_ignore_space): # real signature unknown; restored from __doc__
    """ svn_diff_file_options_t_ignore_space_set(svn_diff_file_options_t self, svn_diff_file_ignore_space_t ignore_space) """
    pass

def svn_diff_file_options_t_show_c_function_get(svn_diff_file_options_t_self): # real signature unknown; restored from __doc__
    """ svn_diff_file_options_t_show_c_function_get(svn_diff_file_options_t self) -> svn_boolean_t """
    pass

def svn_diff_file_options_t_show_c_function_set(svn_diff_file_options_t_self, svn_boolean_t_show_c_function): # real signature unknown; restored from __doc__
    """ svn_diff_file_options_t_show_c_function_set(svn_diff_file_options_t self, svn_boolean_t show_c_function) """
    pass

def svn_diff_file_options_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def svn_diff_file_output_merge(svn_stream_t_output_stream, svn_diff_t_diff, char_original_path, char_modified_path, char_latest_path, char_conflict_original, char_conflict_modified, char_conflict_latest, char_conflict_separator, svn_boolean_t_display_original_in_conflict, svn_boolean_t_display_resolved_conflicts, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_diff_file_output_merge(svn_stream_t output_stream, svn_diff_t diff, char original_path, 
        char modified_path, char latest_path, 
        char conflict_original, char conflict_modified, 
        char conflict_latest, char conflict_separator, 
        svn_boolean_t display_original_in_conflict, 
        svn_boolean_t display_resolved_conflicts, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_diff_file_output_merge2(svn_stream_t_output_stream, svn_diff_t_diff, char_original_path, char_modified_path, char_latest_path, char_conflict_original, char_conflict_modified, char_conflict_latest, char_conflict_separator, svn_diff_conflict_display_style_t_conflict_style, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_diff_file_output_merge2(svn_stream_t output_stream, svn_diff_t diff, char original_path, 
        char modified_path, char latest_path, 
        char conflict_original, char conflict_modified, 
        char conflict_latest, char conflict_separator, 
        svn_diff_conflict_display_style_t conflict_style, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_diff_file_output_unified(svn_stream_t_output_stream, svn_diff_t_diff, char_original_path, char_modified_path, char_original_header, char_modified_header, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_diff_file_output_unified(svn_stream_t output_stream, svn_diff_t diff, char original_path, 
        char modified_path, char original_header, 
        char modified_header, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_diff_file_output_unified2(svn_stream_t_output_stream, svn_diff_t_diff, char_original_path, char_modified_path, char_original_header, char_modified_header, char_header_encoding, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_diff_file_output_unified2(svn_stream_t output_stream, svn_diff_t diff, char original_path, 
        char modified_path, char original_header, 
        char modified_header, char header_encoding, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_diff_file_output_unified3(svn_stream_t_output_stream, svn_diff_t_diff, char_original_path, char_modified_path, char_original_header, char_modified_header, char_header_encoding, char_relative_to_dir, svn_boolean_t_show_c_function, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_diff_file_output_unified3(svn_stream_t output_stream, svn_diff_t diff, char original_path, 
        char modified_path, char original_header, 
        char modified_header, char header_encoding, 
        char relative_to_dir, svn_boolean_t show_c_function, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_diff_fns_invoke_datasource_close(svn_diff_fns_t__obj, void_diff_baton, svn_diff_datasource_e_datasource): # real signature unknown; restored from __doc__
    """ svn_diff_fns_invoke_datasource_close(svn_diff_fns_t _obj, void diff_baton, svn_diff_datasource_e datasource) -> svn_error_t """
    pass

def svn_diff_fns_invoke_datasource_get_next_token(svn_diff_fns_t__obj, apr_uint32_t_hash, void_token, void_diff_baton, svn_diff_datasource_e_datasource): # real signature unknown; restored from __doc__
    """
    svn_diff_fns_invoke_datasource_get_next_token(svn_diff_fns_t _obj, apr_uint32_t hash, void token, 
        void diff_baton, svn_diff_datasource_e datasource) -> svn_error_t
    """
    pass

def svn_diff_fns_invoke_datasource_open(svn_diff_fns_t__obj, void_diff_baton, svn_diff_datasource_e_datasource): # real signature unknown; restored from __doc__
    """ svn_diff_fns_invoke_datasource_open(svn_diff_fns_t _obj, void diff_baton, svn_diff_datasource_e datasource) -> svn_error_t """
    pass

def svn_diff_fns_invoke_token_compare(svn_diff_fns_t__obj, void_diff_baton, void_ltoken, void_rtoken, int_compare): # real signature unknown; restored from __doc__
    """
    svn_diff_fns_invoke_token_compare(svn_diff_fns_t _obj, void diff_baton, void ltoken, 
        void rtoken, int compare) -> svn_error_t
    """
    pass

def svn_diff_fns_invoke_token_discard(svn_diff_fns_t__obj, void_diff_baton, void_token): # real signature unknown; restored from __doc__
    """ svn_diff_fns_invoke_token_discard(svn_diff_fns_t _obj, void diff_baton, void token) """
    pass

def svn_diff_fns_invoke_token_discard_all(svn_diff_fns_t__obj, void_diff_baton): # real signature unknown; restored from __doc__
    """ svn_diff_fns_invoke_token_discard_all(svn_diff_fns_t _obj, void diff_baton) """
    pass

def svn_diff_fns_t_datasource_close_get(svn_diff_fns_t_self): # real signature unknown; restored from __doc__
    """ svn_diff_fns_t_datasource_close_get(svn_diff_fns_t self) -> svn_error_t """
    pass

def svn_diff_fns_t_datasource_close_set(svn_diff_fns_t_self, svn_error_t_datasource_close): # real signature unknown; restored from __doc__
    """ svn_diff_fns_t_datasource_close_set(svn_diff_fns_t self, svn_error_t datasource_close) """
    pass

def svn_diff_fns_t_datasource_get_next_token_get(svn_diff_fns_t_self): # real signature unknown; restored from __doc__
    """ svn_diff_fns_t_datasource_get_next_token_get(svn_diff_fns_t self) -> svn_error_t """
    pass

def svn_diff_fns_t_datasource_get_next_token_set(svn_diff_fns_t_self, svn_error_t_datasource_get_next_token): # real signature unknown; restored from __doc__
    """ svn_diff_fns_t_datasource_get_next_token_set(svn_diff_fns_t self, svn_error_t datasource_get_next_token) """
    pass

def svn_diff_fns_t_datasource_open_get(svn_diff_fns_t_self): # real signature unknown; restored from __doc__
    """ svn_diff_fns_t_datasource_open_get(svn_diff_fns_t self) -> svn_error_t """
    pass

def svn_diff_fns_t_datasource_open_set(svn_diff_fns_t_self, svn_error_t_datasource_open): # real signature unknown; restored from __doc__
    """ svn_diff_fns_t_datasource_open_set(svn_diff_fns_t self, svn_error_t datasource_open) """
    pass

def svn_diff_fns_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def svn_diff_fns_t_token_compare_get(svn_diff_fns_t_self): # real signature unknown; restored from __doc__
    """ svn_diff_fns_t_token_compare_get(svn_diff_fns_t self) -> svn_error_t """
    pass

def svn_diff_fns_t_token_compare_set(svn_diff_fns_t_self, svn_error_t_token_compare): # real signature unknown; restored from __doc__
    """ svn_diff_fns_t_token_compare_set(svn_diff_fns_t self, svn_error_t token_compare) """
    pass

def svn_diff_fns_t_token_discard_all_get(svn_diff_fns_t_self): # real signature unknown; restored from __doc__
    """ svn_diff_fns_t_token_discard_all_get(svn_diff_fns_t self) -> void """
    pass

def svn_diff_fns_t_token_discard_all_set(svn_diff_fns_t_self, void_token_discard_all): # real signature unknown; restored from __doc__
    """ svn_diff_fns_t_token_discard_all_set(svn_diff_fns_t self, void token_discard_all) """
    pass

def svn_diff_fns_t_token_discard_get(svn_diff_fns_t_self): # real signature unknown; restored from __doc__
    """ svn_diff_fns_t_token_discard_get(svn_diff_fns_t self) -> void """
    pass

def svn_diff_fns_t_token_discard_set(svn_diff_fns_t_self, void_token_discard): # real signature unknown; restored from __doc__
    """ svn_diff_fns_t_token_discard_set(svn_diff_fns_t self, void token_discard) """
    pass

def svn_diff_mem_string_diff(svn_diff_t_diff, svn_string_t_original, svn_string_t_modified, svn_diff_file_options_t_options, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_diff_mem_string_diff(svn_diff_t diff, svn_string_t original, svn_string_t modified, 
        svn_diff_file_options_t options, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_diff_mem_string_diff3(svn_diff_t_diff, svn_string_t_original, svn_string_t_modified, svn_string_t_latest, svn_diff_file_options_t_options, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_diff_mem_string_diff3(svn_diff_t diff, svn_string_t original, svn_string_t modified, 
        svn_string_t latest, svn_diff_file_options_t options, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_diff_mem_string_diff4(svn_diff_t_diff, svn_string_t_original, svn_string_t_modified, svn_string_t_latest, svn_string_t_ancestor, svn_diff_file_options_t_options, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_diff_mem_string_diff4(svn_diff_t diff, svn_string_t original, svn_string_t modified, 
        svn_string_t latest, svn_string_t ancestor, 
        svn_diff_file_options_t options, apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_diff_mem_string_output_merge(svn_stream_t_output_stream, svn_diff_t_diff, svn_string_t_original, svn_string_t_modified, svn_string_t_latest, char_conflict_original, char_conflict_modified, char_conflict_latest, char_conflict_separator, svn_boolean_t_display_original_in_conflict, svn_boolean_t_display_resolved_conflicts, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_diff_mem_string_output_merge(svn_stream_t output_stream, svn_diff_t diff, svn_string_t original, 
        svn_string_t modified, svn_string_t latest, 
        char conflict_original, char conflict_modified, 
        char conflict_latest, char conflict_separator, 
        svn_boolean_t display_original_in_conflict, 
        svn_boolean_t display_resolved_conflicts, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_diff_mem_string_output_merge2(svn_stream_t_output_stream, svn_diff_t_diff, svn_string_t_original, svn_string_t_modified, svn_string_t_latest, char_conflict_original, char_conflict_modified, char_conflict_latest, char_conflict_separator, svn_diff_conflict_display_style_t_style, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_diff_mem_string_output_merge2(svn_stream_t output_stream, svn_diff_t diff, svn_string_t original, 
        svn_string_t modified, svn_string_t latest, 
        char conflict_original, char conflict_modified, 
        char conflict_latest, char conflict_separator, 
        svn_diff_conflict_display_style_t style, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_diff_mem_string_output_unified(svn_stream_t_output_stream, svn_diff_t_diff, char_original_header, char_modified_header, char_header_encoding, svn_string_t_original, svn_string_t_modified, apr_pool_t_pool): # real signature unknown; restored from __doc__
    """
    svn_diff_mem_string_output_unified(svn_stream_t output_stream, svn_diff_t diff, char original_header, 
        char modified_header, char header_encoding, 
        svn_string_t original, svn_string_t modified, 
        apr_pool_t pool) -> svn_error_t
    """
    pass

def svn_diff_output(svn_diff_t_diff, void_output_baton, svn_diff_output_fns_t_output_fns): # real signature unknown; restored from __doc__
    """ svn_diff_output(svn_diff_t diff, void output_baton, svn_diff_output_fns_t output_fns) -> svn_error_t """
    pass

def svn_diff_output_fns_invoke_output_common(svn_diff_output_fns_t__obj, void_output_baton, apr_off_t_original_start, apr_off_t_original_length, apr_off_t_modified_start, apr_off_t_modified_length, apr_off_t_latest_start, apr_off_t_latest_length): # real signature unknown; restored from __doc__
    """
    svn_diff_output_fns_invoke_output_common(svn_diff_output_fns_t _obj, void output_baton, apr_off_t original_start, 
        apr_off_t original_length, 
        apr_off_t modified_start, apr_off_t modified_length, 
        apr_off_t latest_start, apr_off_t latest_length) -> svn_error_t
    """
    pass

def svn_diff_output_fns_invoke_output_conflict(svn_diff_output_fns_t__obj, void_output_baton, apr_off_t_original_start, apr_off_t_original_length, apr_off_t_modified_start, apr_off_t_modified_length, apr_off_t_latest_start, apr_off_t_latest_length, svn_diff_t_resolved_diff): # real signature unknown; restored from __doc__
    """
    svn_diff_output_fns_invoke_output_conflict(svn_diff_output_fns_t _obj, void output_baton, apr_off_t original_start, 
        apr_off_t original_length, 
        apr_off_t modified_start, apr_off_t modified_length, 
        apr_off_t latest_start, apr_off_t latest_length, 
        svn_diff_t resolved_diff) -> svn_error_t
    """
    pass

def svn_diff_output_fns_invoke_output_diff_common(svn_diff_output_fns_t__obj, void_output_baton, apr_off_t_original_start, apr_off_t_original_length, apr_off_t_modified_start, apr_off_t_modified_length, apr_off_t_latest_start, apr_off_t_latest_length): # real signature unknown; restored from __doc__
    """
    svn_diff_output_fns_invoke_output_diff_common(svn_diff_output_fns_t _obj, void output_baton, apr_off_t original_start, 
        apr_off_t original_length, 
        apr_off_t modified_start, apr_off_t modified_length, 
        apr_off_t latest_start, apr_off_t latest_length) -> svn_error_t
    """
    pass

def svn_diff_output_fns_invoke_output_diff_latest(svn_diff_output_fns_t__obj, void_output_baton, apr_off_t_original_start, apr_off_t_original_length, apr_off_t_modified_start, apr_off_t_modified_length, apr_off_t_latest_start, apr_off_t_latest_length): # real signature unknown; restored from __doc__
    """
    svn_diff_output_fns_invoke_output_diff_latest(svn_diff_output_fns_t _obj, void output_baton, apr_off_t original_start, 
        apr_off_t original_length, 
        apr_off_t modified_start, apr_off_t modified_length, 
        apr_off_t latest_start, apr_off_t latest_length) -> svn_error_t
    """
    pass

def svn_diff_output_fns_invoke_output_diff_modified(svn_diff_output_fns_t__obj, void_output_baton, apr_off_t_original_start, apr_off_t_original_length, apr_off_t_modified_start, apr_off_t_modified_length, apr_off_t_latest_start, apr_off_t_latest_length): # real signature unknown; restored from __doc__
    """
    svn_diff_output_fns_invoke_output_diff_modified(svn_diff_output_fns_t _obj, void output_baton, apr_off_t original_start, 
        apr_off_t original_length, 
        apr_off_t modified_start, apr_off_t modified_length, 
        apr_off_t latest_start, apr_off_t latest_length) -> svn_error_t
    """
    pass

def svn_diff_output_fns_t_output_common_get(svn_diff_output_fns_t_self): # real signature unknown; restored from __doc__
    """ svn_diff_output_fns_t_output_common_get(svn_diff_output_fns_t self) -> svn_error_t """
    pass

def svn_diff_output_fns_t_output_common_set(svn_diff_output_fns_t_self, svn_error_t_output_common): # real signature unknown; restored from __doc__
    """ svn_diff_output_fns_t_output_common_set(svn_diff_output_fns_t self, svn_error_t output_common) """
    pass

def svn_diff_output_fns_t_output_conflict_get(svn_diff_output_fns_t_self): # real signature unknown; restored from __doc__
    """ svn_diff_output_fns_t_output_conflict_get(svn_diff_output_fns_t self) -> svn_error_t """
    pass

def svn_diff_output_fns_t_output_conflict_set(svn_diff_output_fns_t_self, svn_error_t_output_conflict): # real signature unknown; restored from __doc__
    """ svn_diff_output_fns_t_output_conflict_set(svn_diff_output_fns_t self, svn_error_t output_conflict) """
    pass

def svn_diff_output_fns_t_output_diff_common_get(svn_diff_output_fns_t_self): # real signature unknown; restored from __doc__
    """ svn_diff_output_fns_t_output_diff_common_get(svn_diff_output_fns_t self) -> svn_error_t """
    pass

def svn_diff_output_fns_t_output_diff_common_set(svn_diff_output_fns_t_self, svn_error_t_output_diff_common): # real signature unknown; restored from __doc__
    """ svn_diff_output_fns_t_output_diff_common_set(svn_diff_output_fns_t self, svn_error_t output_diff_common) """
    pass

def svn_diff_output_fns_t_output_diff_latest_get(svn_diff_output_fns_t_self): # real signature unknown; restored from __doc__
    """ svn_diff_output_fns_t_output_diff_latest_get(svn_diff_output_fns_t self) -> svn_error_t """
    pass

def svn_diff_output_fns_t_output_diff_latest_set(svn_diff_output_fns_t_self, svn_error_t_output_diff_latest): # real signature unknown; restored from __doc__
    """ svn_diff_output_fns_t_output_diff_latest_set(svn_diff_output_fns_t self, svn_error_t output_diff_latest) """
    pass

def svn_diff_output_fns_t_output_diff_modified_get(svn_diff_output_fns_t_self): # real signature unknown; restored from __doc__
    """ svn_diff_output_fns_t_output_diff_modified_get(svn_diff_output_fns_t self) -> svn_error_t """
    pass

def svn_diff_output_fns_t_output_diff_modified_set(svn_diff_output_fns_t_self, svn_error_t_output_diff_modified): # real signature unknown; restored from __doc__
    """ svn_diff_output_fns_t_output_diff_modified_set(svn_diff_output_fns_t self, svn_error_t output_diff_modified) """
    pass

def svn_diff_output_fns_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def svn_diff_t_swigregister(*args, **kwargs): # real signature unknown
    pass

def svn_diff_version(): # real signature unknown; restored from __doc__
    """ svn_diff_version() -> svn_version_t """
    pass

# no classes
