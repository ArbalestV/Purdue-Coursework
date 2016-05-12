# encoding: utf-8
# module opencv._ml calls itself _ml
# from /usr/lib64/python2.6/site-packages/opencv/_ml.so
# by generator 1.136
# no doc

# imports
from _ml import (CvANN_MLP_TrainParams_bp_dw_scale_get, 
    CvANN_MLP_TrainParams_bp_dw_scale_set, 
    CvANN_MLP_TrainParams_bp_moment_scale_get, 
    CvANN_MLP_TrainParams_bp_moment_scale_set, 
    CvANN_MLP_TrainParams_rp_dw0_get, CvANN_MLP_TrainParams_rp_dw0_set, 
    CvANN_MLP_TrainParams_rp_dw_max_get, CvANN_MLP_TrainParams_rp_dw_max_set, 
    CvANN_MLP_TrainParams_rp_dw_min_get, CvANN_MLP_TrainParams_rp_dw_min_set, 
    CvANN_MLP_TrainParams_rp_dw_minus_get, 
    CvANN_MLP_TrainParams_rp_dw_minus_set, 
    CvANN_MLP_TrainParams_rp_dw_plus_get, 
    CvANN_MLP_TrainParams_rp_dw_plus_set, CvANN_MLP_TrainParams_swigregister, 
    CvANN_MLP_TrainParams_term_crit_get, CvANN_MLP_TrainParams_term_crit_set, 
    CvANN_MLP_TrainParams_train_method_get, 
    CvANN_MLP_TrainParams_train_method_set, CvANN_MLP_clear, CvANN_MLP_create, 
    CvANN_MLP_get_layer_count, CvANN_MLP_get_layer_sizes, 
    CvANN_MLP_get_weights, CvANN_MLP_predict, CvANN_MLP_read, 
    CvANN_MLP_swigregister, CvANN_MLP_train, CvANN_MLP_write, 
    CvBoostParams_boost_type_get, CvBoostParams_boost_type_set, 
    CvBoostParams_split_criteria_get, CvBoostParams_split_criteria_set, 
    CvBoostParams_swigregister, CvBoostParams_weak_count_get, 
    CvBoostParams_weak_count_set, CvBoostParams_weight_trim_rate_get, 
    CvBoostParams_weight_trim_rate_set, CvBoostTree_clear, CvBoostTree_read, 
    CvBoostTree_scale, CvBoostTree_swigregister, CvBoostTree_train, 
    CvBoost_calc_error, CvBoost_clear, CvBoost_get_active_vars, 
    CvBoost_get_data, CvBoost_get_params, CvBoost_get_subtree_weights, 
    CvBoost_get_weak_predictors, CvBoost_get_weak_response, 
    CvBoost_get_weights, CvBoost_predict, CvBoost_prune, CvBoost_read, 
    CvBoost_swigregister, CvBoost_train, CvBoost_write, CvDTreeNode_Tn_get, 
    CvDTreeNode_Tn_set, CvDTreeNode_alpha_get, CvDTreeNode_alpha_set, 
    CvDTreeNode_buf_idx_get, CvDTreeNode_buf_idx_set, 
    CvDTreeNode_class_idx_get, CvDTreeNode_class_idx_set, 
    CvDTreeNode_complexity_get, CvDTreeNode_complexity_set, 
    CvDTreeNode_cv_Tn_get, CvDTreeNode_cv_Tn_set, 
    CvDTreeNode_cv_node_error_get, CvDTreeNode_cv_node_error_set, 
    CvDTreeNode_cv_node_risk_get, CvDTreeNode_cv_node_risk_set, 
    CvDTreeNode_depth_get, CvDTreeNode_depth_set, CvDTreeNode_get_num_valid, 
    CvDTreeNode_left_get, CvDTreeNode_left_set, CvDTreeNode_maxlr_get, 
    CvDTreeNode_maxlr_set, CvDTreeNode_node_risk_get, 
    CvDTreeNode_node_risk_set, CvDTreeNode_num_valid_get, 
    CvDTreeNode_num_valid_set, CvDTreeNode_offset_get, CvDTreeNode_offset_set, 
    CvDTreeNode_parent_get, CvDTreeNode_parent_set, CvDTreeNode_right_get, 
    CvDTreeNode_right_set, CvDTreeNode_sample_count_get, 
    CvDTreeNode_sample_count_set, CvDTreeNode_set_num_valid, 
    CvDTreeNode_split_get, CvDTreeNode_split_set, CvDTreeNode_swigregister, 
    CvDTreeNode_tree_error_get, CvDTreeNode_tree_error_set, 
    CvDTreeNode_tree_risk_get, CvDTreeNode_tree_risk_set, 
    CvDTreeNode_value_get, CvDTreeNode_value_set, CvDTreeParams_cv_folds_get, 
    CvDTreeParams_cv_folds_set, CvDTreeParams_max_categories_get, 
    CvDTreeParams_max_categories_set, CvDTreeParams_max_depth_get, 
    CvDTreeParams_max_depth_set, CvDTreeParams_min_sample_count_get, 
    CvDTreeParams_min_sample_count_set, CvDTreeParams_priors_get, 
    CvDTreeParams_priors_set, CvDTreeParams_regression_accuracy_get, 
    CvDTreeParams_regression_accuracy_set, CvDTreeParams_swigregister, 
    CvDTreeParams_truncate_pruned_tree_get, 
    CvDTreeParams_truncate_pruned_tree_set, CvDTreeParams_use_1se_rule_get, 
    CvDTreeParams_use_1se_rule_set, CvDTreeParams_use_surrogates_get, 
    CvDTreeParams_use_surrogates_set, CvDTreeSplit_condensed_idx_get, 
    CvDTreeSplit_condensed_idx_set, CvDTreeSplit_inversed_get, 
    CvDTreeSplit_inversed_set, CvDTreeSplit_next_get, CvDTreeSplit_next_set, 
    CvDTreeSplit_quality_get, CvDTreeSplit_quality_set, 
    CvDTreeSplit_swigregister, CvDTreeSplit_var_idx_get, 
    CvDTreeSplit_var_idx_set, CvDTreeTrainData_buf_count_get, 
    CvDTreeTrainData_buf_count_set, CvDTreeTrainData_buf_get, 
    CvDTreeTrainData_buf_set, CvDTreeTrainData_buf_size_get, 
    CvDTreeTrainData_buf_size_set, CvDTreeTrainData_cat_count_get, 
    CvDTreeTrainData_cat_count_set, CvDTreeTrainData_cat_map_get, 
    CvDTreeTrainData_cat_map_set, CvDTreeTrainData_cat_ofs_get, 
    CvDTreeTrainData_cat_ofs_set, CvDTreeTrainData_cat_var_count_get, 
    CvDTreeTrainData_cat_var_count_set, CvDTreeTrainData_clear, 
    CvDTreeTrainData_counts_get, CvDTreeTrainData_counts_set, 
    CvDTreeTrainData_cv_heap_get, CvDTreeTrainData_cv_heap_set, 
    CvDTreeTrainData_cv_lables_buf_get, CvDTreeTrainData_cv_lables_buf_set, 
    CvDTreeTrainData_data_root_get, CvDTreeTrainData_data_root_set, 
    CvDTreeTrainData_direction_get, CvDTreeTrainData_direction_set, 
    CvDTreeTrainData_do_responses_copy, CvDTreeTrainData_free_node, 
    CvDTreeTrainData_free_node_data, CvDTreeTrainData_free_train_data, 
    CvDTreeTrainData_get_cat_var_data, CvDTreeTrainData_get_child_buf_idx, 
    CvDTreeTrainData_get_class_labels, CvDTreeTrainData_get_cv_labels, 
    CvDTreeTrainData_get_cv_lables_buf, CvDTreeTrainData_get_num_classes, 
    CvDTreeTrainData_get_ord_responses, CvDTreeTrainData_get_ord_var_data, 
    CvDTreeTrainData_get_pred_float_buf, CvDTreeTrainData_get_pred_int_buf, 
    CvDTreeTrainData_get_resp_float_buf, CvDTreeTrainData_get_resp_int_buf, 
    CvDTreeTrainData_get_sample_idx_buf, CvDTreeTrainData_get_sample_indices, 
    CvDTreeTrainData_get_var_type, CvDTreeTrainData_get_vectors, 
    CvDTreeTrainData_get_work_var_count, CvDTreeTrainData_have_labels_get, 
    CvDTreeTrainData_have_labels_set, CvDTreeTrainData_have_priors_get, 
    CvDTreeTrainData_have_priors_set, CvDTreeTrainData_is_buf_16u_get, 
    CvDTreeTrainData_is_buf_16u_set, CvDTreeTrainData_is_classifier_get, 
    CvDTreeTrainData_is_classifier_set, CvDTreeTrainData_max_c_count_get, 
    CvDTreeTrainData_max_c_count_set, CvDTreeTrainData_new_node, 
    CvDTreeTrainData_new_split_cat, CvDTreeTrainData_new_split_ord, 
    CvDTreeTrainData_node_heap_get, CvDTreeTrainData_node_heap_set, 
    CvDTreeTrainData_nv_heap_get, CvDTreeTrainData_nv_heap_set, 
    CvDTreeTrainData_ord_var_count_get, CvDTreeTrainData_ord_var_count_set, 
    CvDTreeTrainData_params_get, CvDTreeTrainData_params_set, 
    CvDTreeTrainData_pred_float_buf_get, CvDTreeTrainData_pred_float_buf_set, 
    CvDTreeTrainData_pred_int_buf_get, CvDTreeTrainData_pred_int_buf_set, 
    CvDTreeTrainData_priors_get, CvDTreeTrainData_priors_mult_get, 
    CvDTreeTrainData_priors_mult_set, CvDTreeTrainData_priors_set, 
    CvDTreeTrainData_read_params, CvDTreeTrainData_resp_float_buf_get, 
    CvDTreeTrainData_resp_float_buf_set, CvDTreeTrainData_resp_int_buf_get, 
    CvDTreeTrainData_resp_int_buf_set, CvDTreeTrainData_responses_copy_get, 
    CvDTreeTrainData_responses_copy_set, CvDTreeTrainData_responses_get, 
    CvDTreeTrainData_responses_set, CvDTreeTrainData_rng_get, 
    CvDTreeTrainData_rng_set, CvDTreeTrainData_sample_count_get, 
    CvDTreeTrainData_sample_count_set, CvDTreeTrainData_sample_idx_buf_get, 
    CvDTreeTrainData_sample_idx_buf_set, CvDTreeTrainData_set_data, 
    CvDTreeTrainData_set_params, CvDTreeTrainData_shared_get, 
    CvDTreeTrainData_shared_set, CvDTreeTrainData_split_buf_get, 
    CvDTreeTrainData_split_buf_set, CvDTreeTrainData_split_heap_get, 
    CvDTreeTrainData_split_heap_set, CvDTreeTrainData_subsample_data, 
    CvDTreeTrainData_swigregister, CvDTreeTrainData_temp_storage_get, 
    CvDTreeTrainData_temp_storage_set, CvDTreeTrainData_tflag_get, 
    CvDTreeTrainData_tflag_set, CvDTreeTrainData_train_data_get, 
    CvDTreeTrainData_train_data_set, CvDTreeTrainData_tree_storage_get, 
    CvDTreeTrainData_tree_storage_set, CvDTreeTrainData_var_all_get, 
    CvDTreeTrainData_var_all_set, CvDTreeTrainData_var_count_get, 
    CvDTreeTrainData_var_count_set, CvDTreeTrainData_var_idx_get, 
    CvDTreeTrainData_var_idx_set, CvDTreeTrainData_var_type_get, 
    CvDTreeTrainData_var_type_set, CvDTreeTrainData_work_var_count_get, 
    CvDTreeTrainData_work_var_count_set, CvDTreeTrainData_write_params, 
    CvDTree_calc_error, CvDTree_clear, CvDTree_get_data, 
    CvDTree_get_pruned_tree_idx, CvDTree_get_root, CvDTree_get_var_importance, 
    CvDTree_predict, CvDTree_pruned_tree_idx_get, CvDTree_pruned_tree_idx_set, 
    CvDTree_read, CvDTree_swigregister, CvDTree_train, CvDTree_write, 
    CvEMParams_cov_mat_type_get, CvEMParams_cov_mat_type_set, 
    CvEMParams_covs_get, CvEMParams_covs_set, CvEMParams_means_get, 
    CvEMParams_means_set, CvEMParams_nclusters_get, CvEMParams_nclusters_set, 
    CvEMParams_probs_get, CvEMParams_probs_set, CvEMParams_start_step_get, 
    CvEMParams_start_step_set, CvEMParams_swigregister, 
    CvEMParams_term_crit_get, CvEMParams_term_crit_set, 
    CvEMParams_weights_get, CvEMParams_weights_set, CvEM_clear, CvEM_get_covs, 
    CvEM_get_log_likelihood, CvEM_get_means, CvEM_get_nclusters, 
    CvEM_get_probs, CvEM_get_weights, CvEM_predict, CvEM_swigregister, 
    CvEM_train, CvERTreeTrainData_get_cat_var_data, 
    CvERTreeTrainData_get_cv_labels, CvERTreeTrainData_get_ord_var_data, 
    CvERTreeTrainData_get_sample_indices, CvERTreeTrainData_get_vectors, 
    CvERTreeTrainData_missing_mask_get, CvERTreeTrainData_missing_mask_set, 
    CvERTreeTrainData_set_data, CvERTreeTrainData_subsample_data, 
    CvERTreeTrainData_swigregister, CvERTrees_swigregister, CvERTrees_train, 
    CvForestERTree_swigregister, CvForestTree_get_var_count, 
    CvForestTree_read, CvForestTree_swigregister, CvForestTree_train, 
    CvKNearest_clear, CvKNearest_find_nearest, CvKNearest_get_max_k, 
    CvKNearest_get_sample_count, CvKNearest_get_var_count, 
    CvKNearest_is_regression, CvKNearest_swigregister, CvKNearest_train, 
    CvMLData_chahge_var_idx, CvMLData_change_var_type, CvMLData_get_delimiter, 
    CvMLData_get_miss_ch, CvMLData_get_missing, CvMLData_get_response_idx, 
    CvMLData_get_responses, CvMLData_get_test_sample_idx, 
    CvMLData_get_train_sample_idx, CvMLData_get_values, CvMLData_get_var_idx, 
    CvMLData_get_var_type, CvMLData_get_var_types, 
    CvMLData_mix_train_and_test_idx, CvMLData_read_csv, 
    CvMLData_set_delimiter, CvMLData_set_miss_ch, CvMLData_set_response_idx, 
    CvMLData_set_train_test_split, CvMLData_set_var_types, 
    CvMLData_swigregister, CvNormalBayesClassifier_clear, 
    CvNormalBayesClassifier_predict, CvNormalBayesClassifier_read, 
    CvNormalBayesClassifier_swigregister, CvNormalBayesClassifier_train, 
    CvNormalBayesClassifier_write, CvPair16u32s_i_get, CvPair16u32s_i_set, 
    CvPair16u32s_swigregister, CvPair16u32s_u_get, CvPair16u32s_u_set, 
    CvParamGrid_check, CvParamGrid_max_val_get, CvParamGrid_max_val_set, 
    CvParamGrid_min_val_get, CvParamGrid_min_val_set, CvParamGrid_step_get, 
    CvParamGrid_step_set, CvParamGrid_swigregister, CvRNG_Wrapper___eq__, 
    CvRNG_Wrapper___ne__, CvRNG_Wrapper_ptr, CvRNG_Wrapper_ref, 
    CvRNG_Wrapper_swigregister, CvRTParams_calc_var_importance_get, 
    CvRTParams_calc_var_importance_set, CvRTParams_nactive_vars_get, 
    CvRTParams_nactive_vars_set, CvRTParams_swigregister, 
    CvRTParams_term_crit_get, CvRTParams_term_crit_set, CvRTrees_calc_error, 
    CvRTrees_clear, CvRTrees_get_active_var_mask, CvRTrees_get_proximity, 
    CvRTrees_get_rng, CvRTrees_get_train_error, CvRTrees_get_tree, 
    CvRTrees_get_tree_count, CvRTrees_get_var_importance, CvRTrees_predict, 
    CvRTrees_predict_prob, CvRTrees_read, CvRTrees_swigregister, 
    CvRTrees_train, CvRTrees_write, CvSVMDecisionFunc_alpha_get, 
    CvSVMDecisionFunc_alpha_set, CvSVMDecisionFunc_rho_get, 
    CvSVMDecisionFunc_rho_set, CvSVMDecisionFunc_sv_count_get, 
    CvSVMDecisionFunc_sv_count_set, CvSVMDecisionFunc_sv_index_get, 
    CvSVMDecisionFunc_sv_index_set, CvSVMDecisionFunc_swigregister, 
    CvSVMKernelRow_data_get, CvSVMKernelRow_data_set, CvSVMKernelRow_next_get, 
    CvSVMKernelRow_next_set, CvSVMKernelRow_prev_get, CvSVMKernelRow_prev_set, 
    CvSVMKernelRow_swigregister, CvSVMKernel_calc, CvSVMKernel_calc_func_get, 
    CvSVMKernel_calc_func_set, CvSVMKernel_calc_linear, 
    CvSVMKernel_calc_non_rbf_base, CvSVMKernel_calc_poly, 
    CvSVMKernel_calc_rbf, CvSVMKernel_calc_sigmoid, CvSVMKernel_clear, 
    CvSVMKernel_create, CvSVMKernel_params_get, CvSVMKernel_params_set, 
    CvSVMKernel_swigregister, CvSVMParams_C_get, CvSVMParams_C_set, 
    CvSVMParams_class_weights_get, CvSVMParams_class_weights_set, 
    CvSVMParams_coef0_get, CvSVMParams_coef0_set, CvSVMParams_degree_get, 
    CvSVMParams_degree_set, CvSVMParams_gamma_get, CvSVMParams_gamma_set, 
    CvSVMParams_kernel_type_get, CvSVMParams_kernel_type_set, 
    CvSVMParams_nu_get, CvSVMParams_nu_set, CvSVMParams_p_get, 
    CvSVMParams_p_set, CvSVMParams_svm_type_get, CvSVMParams_svm_type_set, 
    CvSVMParams_swigregister, CvSVMParams_term_crit_get, 
    CvSVMParams_term_crit_set, CvSVMSolutionInfo_obj_get, 
    CvSVMSolutionInfo_obj_set, CvSVMSolutionInfo_r_get, 
    CvSVMSolutionInfo_r_set, CvSVMSolutionInfo_rho_get, 
    CvSVMSolutionInfo_rho_set, CvSVMSolutionInfo_swigregister, 
    CvSVMSolutionInfo_upper_bound_n_get, CvSVMSolutionInfo_upper_bound_n_set, 
    CvSVMSolutionInfo_upper_bound_p_get, CvSVMSolutionInfo_upper_bound_p_set, 
    CvSVMSolver_C_get, CvSVMSolver_C_set, CvSVMSolver_G_get, 
    CvSVMSolver_G_set, CvSVMSolver_alpha_count_get, 
    CvSVMSolver_alpha_count_set, CvSVMSolver_alpha_get, CvSVMSolver_alpha_set, 
    CvSVMSolver_alpha_status_get, CvSVMSolver_alpha_status_set, 
    CvSVMSolver_b_get, CvSVMSolver_b_set, CvSVMSolver_buf_get, 
    CvSVMSolver_buf_set, CvSVMSolver_cache_line_size_get, 
    CvSVMSolver_cache_line_size_set, CvSVMSolver_cache_size_get, 
    CvSVMSolver_cache_size_set, CvSVMSolver_calc_rho, 
    CvSVMSolver_calc_rho_func_get, CvSVMSolver_calc_rho_func_set, 
    CvSVMSolver_calc_rho_nu_svm, CvSVMSolver_clear, CvSVMSolver_create, 
    CvSVMSolver_eps_get, CvSVMSolver_eps_set, CvSVMSolver_get_row, 
    CvSVMSolver_get_row_base, CvSVMSolver_get_row_func_get, 
    CvSVMSolver_get_row_func_set, CvSVMSolver_get_row_one_class, 
    CvSVMSolver_get_row_svc, CvSVMSolver_get_row_svr, CvSVMSolver_kernel_get, 
    CvSVMSolver_kernel_set, CvSVMSolver_lru_list_get, 
    CvSVMSolver_lru_list_set, CvSVMSolver_max_iter_get, 
    CvSVMSolver_max_iter_set, CvSVMSolver_params_get, CvSVMSolver_params_set, 
    CvSVMSolver_rows_get, CvSVMSolver_rows_set, CvSVMSolver_sample_count_get, 
    CvSVMSolver_sample_count_set, CvSVMSolver_samples_get, 
    CvSVMSolver_samples_set, CvSVMSolver_select_working_set, 
    CvSVMSolver_select_working_set_func_get, 
    CvSVMSolver_select_working_set_func_set, 
    CvSVMSolver_select_working_set_nu_svm, CvSVMSolver_solve_c_svc, 
    CvSVMSolver_solve_eps_svr, CvSVMSolver_solve_generic, 
    CvSVMSolver_solve_nu_svc, CvSVMSolver_solve_nu_svr, 
    CvSVMSolver_solve_one_class, CvSVMSolver_storage_get, 
    CvSVMSolver_storage_set, CvSVMSolver_swigregister, 
    CvSVMSolver_var_count_get, CvSVMSolver_var_count_set, CvSVMSolver_y_get, 
    CvSVMSolver_y_set, CvSVM_clear, CvSVM_get_default_grid, CvSVM_get_params, 
    CvSVM_get_support_vector, CvSVM_get_support_vector_count, 
    CvSVM_get_var_count, CvSVM_predict, CvSVM_read, CvSVM_swigregister, 
    CvSVM_train, CvSVM_train_auto, CvSVM_write, CvStatModel_clear, 
    CvStatModel_load, CvStatModel_read, CvStatModel_save, 
    CvStatModel_swigregister, CvStatModel_write, 
    CvSubdiv2DEdge_Wrapper___eq__, CvSubdiv2DEdge_Wrapper___ne__, 
    CvSubdiv2DEdge_Wrapper_ptr, CvSubdiv2DEdge_Wrapper_ref, 
    CvSubdiv2DEdge_Wrapper_swigregister, 
    CvTrainTestSplit_class_part_count_get, 
    CvTrainTestSplit_class_part_count_set, CvTrainTestSplit_class_part_get, 
    CvTrainTestSplit_class_part_mode_get, 
    CvTrainTestSplit_class_part_mode_set, 
    CvTrainTestSplit_class_part_portion_get, 
    CvTrainTestSplit_class_part_portion_set, 
    CvTrainTestSplit_class_part_swigregister, CvTrainTestSplit_mix_get, 
    CvTrainTestSplit_mix_set, CvTrainTestSplit_swigregister, 
    CvTrainTestSplit_train_sample_part_count_get, 
    CvTrainTestSplit_train_sample_part_count_set, 
    CvTrainTestSplit_train_sample_part_get, 
    CvTrainTestSplit_train_sample_part_mode_get, 
    CvTrainTestSplit_train_sample_part_mode_set, 
    CvTrainTestSplit_train_sample_part_portion_get, 
    CvTrainTestSplit_train_sample_part_portion_set, 
    CvTrainTestSplit_train_sample_part_swigregister, CvVectors_count_get, 
    CvVectors_count_set, CvVectors_data_db_get, CvVectors_data_db_set, 
    CvVectors_data_fl_get, CvVectors_data_fl_set, CvVectors_data_get, 
    CvVectors_data_ptr_get, CvVectors_data_ptr_set, 
    CvVectors_data_swigregister, CvVectors_dims_get, CvVectors_dims_set, 
    CvVectors_next_get, CvVectors_next_set, CvVectors_swigregister, 
    CvVectors_type_get, CvVectors_type_set, SWIG_PyInstanceMethod_New, 
    cvCreateTestSet, cvRandGaussMixture, cvRandMVNormal, delete_CvANN_MLP, 
    delete_CvANN_MLP_TrainParams, delete_CvBoost, delete_CvBoostParams, 
    delete_CvBoostTree, delete_CvDTree, delete_CvDTreeNode, 
    delete_CvDTreeParams, delete_CvDTreeSplit, delete_CvDTreeTrainData, 
    delete_CvEM, delete_CvEMParams, delete_CvERTreeTrainData, 
    delete_CvERTrees, delete_CvForestERTree, delete_CvForestTree, 
    delete_CvKNearest, delete_CvMLData, delete_CvNormalBayesClassifier, 
    delete_CvPair16u32s, delete_CvParamGrid, delete_CvRNG_Wrapper, 
    delete_CvRTParams, delete_CvRTrees, delete_CvSVM, 
    delete_CvSVMDecisionFunc, delete_CvSVMKernel, delete_CvSVMKernelRow, 
    delete_CvSVMParams, delete_CvSVMSolutionInfo, delete_CvSVMSolver, 
    delete_CvStatModel, delete_CvSubdiv2DEdge_Wrapper, 
    delete_CvTrainTestSplit, delete_CvTrainTestSplit_class_part, 
    delete_CvTrainTestSplit_train_sample_part, delete_CvVectors, 
    delete_CvVectors_data, new_CvANN_MLP, new_CvANN_MLP_TrainParams, 
    new_CvBoost, new_CvBoostParams, new_CvBoostTree, new_CvDTree, 
    new_CvDTreeNode, new_CvDTreeParams, new_CvDTreeSplit, 
    new_CvDTreeTrainData, new_CvEM, new_CvEMParams, new_CvERTreeTrainData, 
    new_CvERTrees, new_CvForestERTree, new_CvForestTree, new_CvKNearest, 
    new_CvMLData, new_CvNormalBayesClassifier, new_CvPair16u32s, 
    new_CvParamGrid, new_CvRNG_Wrapper, new_CvRTParams, new_CvRTrees, 
    new_CvSVM, new_CvSVMDecisionFunc, new_CvSVMKernel, new_CvSVMKernelRow, 
    new_CvSVMParams, new_CvSVMSolutionInfo, new_CvSVMSolver, new_CvStatModel, 
    new_CvSubdiv2DEdge_Wrapper, new_CvTrainTestSplit, 
    new_CvTrainTestSplit_class_part, new_CvTrainTestSplit_train_sample_part, 
    new_CvVectors, new_CvVectors_data)


# Variables with simple values

CvANN_MLP_GAUSSIAN = 2
CvANN_MLP_IDENTITY = 0

CvANN_MLP_NO_INPUT_SCALE = 2

CvANN_MLP_NO_OUTPUT_SCALE = 4

CvANN_MLP_SIGMOID_SYM = 1

CvANN_MLP_TrainParams_BACKPROP = 0
CvANN_MLP_TrainParams_RPROP = 1

CvANN_MLP_UPDATE_WEIGHTS = 1

CvBoost_DEFAULT = 0
CvBoost_DISCRETE = 0
CvBoost_GENTLE = 3
CvBoost_GINI = 1
CvBoost_LOGIT = 2
CvBoost_MISCLASS = 3
CvBoost_REAL = 1
CvBoost_SQERR = 4

CvEM_COV_MAT_DIAGONAL = 1
CvEM_COV_MAT_GENERIC = 2
CvEM_COV_MAT_SPHERICAL = 0

CvEM_START_AUTO_STEP = 0

CvEM_START_E_STEP = 1

CvEM_START_M_STEP = 2

CvParamGrid_SVM_C = 0
CvParamGrid_SVM_COEF = 4
CvParamGrid_SVM_DEGREE = 5
CvParamGrid_SVM_GAMMA = 1
CvParamGrid_SVM_NU = 3
CvParamGrid_SVM_P = 2

CvSVM_C = 0
CvSVM_COEF = 4

CvSVM_C_SVC = 100

CvSVM_DEGREE = 5

CvSVM_EPS_SVR = 103

CvSVM_GAMMA = 1
CvSVM_LINEAR = 0
CvSVM_NU = 3

CvSVM_NU_SVC = 101
CvSVM_NU_SVR = 104

CvSVM_ONE_CLASS = 102

CvSVM_P = 2
CvSVM_POLY = 1
CvSVM_RBF = 2
CvSVM_SIGMOID = 3

CV_COL_SAMPLE = 0

CV_COUNT = 0
CV_LOG2PI = 1.8378770664093456
CV_PORTION = 1

CV_ROW_SAMPLE = 1

CV_TEST_ERROR = 1

CV_TRAIN_ERROR = 0

CV_TS_CONCENTRIC_SPHERES = 0

CV_TYPE_NAME_ML_ANN_MLP = 'opencv-ml-ann-mlp'

CV_TYPE_NAME_ML_BOOSTING = 'opencv-ml-boost-tree'
CV_TYPE_NAME_ML_CNN = 'opencv-ml-cnn'
CV_TYPE_NAME_ML_EM = 'opencv-ml-em'
CV_TYPE_NAME_ML_KNN = 'opencv-ml-knn'
CV_TYPE_NAME_ML_NBAYES = 'opencv-ml-bayesian'
CV_TYPE_NAME_ML_RTREES = 'opencv-ml-random-trees'
CV_TYPE_NAME_ML_SVM = 'opencv-ml-svm'
CV_TYPE_NAME_ML_TREE = 'opencv-ml-tree'

CV_VAR_CATEGORICAL = 1
CV_VAR_NUMERICAL = 0
CV_VAR_ORDERED = 0

# no functions
# no classes
