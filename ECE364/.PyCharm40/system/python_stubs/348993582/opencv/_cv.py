# encoding: utf-8
# module opencv._cv calls itself _cv
# from /usr/lib64/python2.6/site-packages/opencv/_cv.so
# by generator 1.136
# no doc

# imports
from _cv import (CV_16SC, CV_16UC, CV_32FC, CV_32SC, CV_64FC, CV_8SC, CV_8UC, 
    CV_ARE_CNS_EQ, CV_ARE_DEPTHS_EQ, CV_ARE_SIZES_EQ, CV_ARE_TYPES_EQ, CV_CMP, 
    CV_CURRENT_POINT, CV_ELEM_SIZE, CV_ELEM_SIZE1, CV_HIST_HAS_RANGES, 
    CV_IABS, CV_IMAX, CV_IMIN, CV_INIT_3X3_DELTAS, CV_IS_GRAPH, 
    CV_IS_GRAPH_EDGE_VISITED, CV_IS_GRAPH_ORIENTED, 
    CV_IS_GRAPH_VERTEX_VISITED, CV_IS_HAAR_CLASSIFIER, CV_IS_HIST, 
    CV_IS_IMAGE, CV_IS_IMAGE_HDR, CV_IS_MASK_ARR, CV_IS_MAT, CV_IS_MATND, 
    CV_IS_MATND_HDR, CV_IS_MAT_CONST, CV_IS_MAT_CONT, CV_IS_MAT_HDR, 
    CV_IS_SEQ, CV_IS_SEQ_CHAIN, CV_IS_SEQ_CHAIN_CONTOUR, CV_IS_SEQ_CLOSED, 
    CV_IS_SEQ_CONTOUR, CV_IS_SEQ_CONVEX, CV_IS_SEQ_CURVE, CV_IS_SEQ_HOLE, 
    CV_IS_SEQ_INDEX, CV_IS_SEQ_POINT_SET, CV_IS_SEQ_POINT_SUBSET, 
    CV_IS_SEQ_POLYGON, CV_IS_SEQ_POLYGON_TREE, CV_IS_SEQ_POLYLINE, 
    CV_IS_SEQ_SIMPLE, CV_IS_SET, CV_IS_SET_ELEM, CV_IS_SPARSE_HIST, 
    CV_IS_SPARSE_MAT, CV_IS_SPARSE_MAT_HDR, CV_IS_STORAGE, CV_IS_SUBDIV2D, 
    CV_IS_TEMP_MAT, CV_IS_UNIFORM_HIST, CV_MAKETYPE, CV_MAT_CN, CV_MAT_DEPTH, 
    CV_MAT_ELEM_PTR, CV_MAT_ELEM_PTR_FAST, CV_MAT_TYPE, CV_NEXT_GRAPH_EDGE, 
    CV_NEXT_LINE_POINT, CV_NEXT_SEQ_ELEM, CV_NODE_HAS_NAME, CV_NODE_IDX, 
    CV_NODE_IS_COLLECTION, CV_NODE_IS_EMPTY, CV_NODE_IS_FLOW, CV_NODE_IS_INT, 
    CV_NODE_IS_MAP, CV_NODE_IS_REAL, CV_NODE_IS_SEQ, CV_NODE_IS_STRING, 
    CV_NODE_IS_USER, CV_NODE_SEQ_IS_SIMPLE, CV_NODE_TYPE, CV_NODE_VAL, 
    CV_PREV_POINT, CV_PREV_SEQ_ELEM, CV_READ_CHAIN_POINT, CV_READ_EDGE, 
    CV_READ_SEQ_ELEM, CV_REV_READ_SEQ_ELEM, CV_RGB, CV_SEQ_ELTYPE, 
    CV_SEQ_KIND, CV_SIGN, CV_SUBDIV2D_NEXT_EDGE, CV_SWAP, CV_WRITE_SEQ_ELEM, 
    CV_WRITE_SEQ_ELEM_VAR, Cv32suf_f_get, Cv32suf_f_set, Cv32suf_i_get, 
    Cv32suf_i_set, Cv32suf_swigregister, Cv32suf_u_get, Cv32suf_u_set, 
    Cv64suf_f_get, Cv64suf_f_set, Cv64suf_i_get, Cv64suf_i_set, 
    Cv64suf_swigregister, Cv64suf_u_get, Cv64suf_u_set, CvAttrList_attr_get, 
    CvAttrList_attr_set, CvAttrList_next_get, CvAttrList_next_set, 
    CvAttrList_swigregister, CvAvgComp_neighbors_get, CvAvgComp_neighbors_set, 
    CvAvgComp_rect_get, CvAvgComp_rect_set, CvAvgComp_swigregister, 
    CvBox2D_angle_get, CvBox2D_angle_set, CvBox2D_center_get, 
    CvBox2D_center_set, CvBox2D_size_get, CvBox2D_size_set, 
    CvBox2D_swigregister, CvChainPtReader_block_get, 
    CvChainPtReader_block_max_get, CvChainPtReader_block_max_set, 
    CvChainPtReader_block_min_get, CvChainPtReader_block_min_set, 
    CvChainPtReader_block_set, CvChainPtReader_code_get, 
    CvChainPtReader_code_set, CvChainPtReader_delta_index_get, 
    CvChainPtReader_delta_index_set, CvChainPtReader_deltas_get, 
    CvChainPtReader_deltas_set, CvChainPtReader_header_size_get, 
    CvChainPtReader_header_size_set, CvChainPtReader_prev_elem_get, 
    CvChainPtReader_prev_elem_set, CvChainPtReader_pt_get, 
    CvChainPtReader_pt_set, CvChainPtReader_ptr_get, CvChainPtReader_ptr_set, 
    CvChainPtReader_seq_get, CvChainPtReader_seq_set, 
    CvChainPtReader_swigregister, CvChain_block_max_get, 
    CvChain_block_max_set, CvChain_delta_elems_get, CvChain_delta_elems_set, 
    CvChain_elem_size_get, CvChain_elem_size_set, CvChain_first_get, 
    CvChain_first_set, CvChain_flags_get, CvChain_flags_set, 
    CvChain_free_blocks_get, CvChain_free_blocks_set, CvChain_h_next_get, 
    CvChain_h_next_set, CvChain_h_prev_get, CvChain_h_prev_set, 
    CvChain_header_size_get, CvChain_header_size_set, CvChain_origin_get, 
    CvChain_origin_set, CvChain_ptr_get, CvChain_ptr_set, CvChain_storage_get, 
    CvChain_storage_set, CvChain_swigregister, CvChain_total_get, 
    CvChain_total_set, CvChain_v_next_get, CvChain_v_next_set, 
    CvChain_v_prev_get, CvChain_v_prev_set, CvConDensation_DP_get, 
    CvConDensation_DP_set, CvConDensation_DynamMatr_get, 
    CvConDensation_DynamMatr_set, CvConDensation_MP_get, 
    CvConDensation_MP_set, CvConDensation_RandS_get, CvConDensation_RandS_set, 
    CvConDensation_RandomSample_get, CvConDensation_RandomSample_set, 
    CvConDensation_SamplesNum_get, CvConDensation_SamplesNum_set, 
    CvConDensation_State_get, CvConDensation_State_set, 
    CvConDensation_Temp_get, CvConDensation_Temp_set, 
    CvConDensation_flConfidence_get, CvConDensation_flConfidence_set, 
    CvConDensation_flCumulative_get, CvConDensation_flCumulative_set, 
    CvConDensation_flNewSamples_get, CvConDensation_flNewSamples_set, 
    CvConDensation_flSamples_get, CvConDensation_flSamples_set, 
    CvConDensation_swigregister, CvConnectedComp_area_get, 
    CvConnectedComp_area_set, CvConnectedComp_contour_get, 
    CvConnectedComp_contour_set, CvConnectedComp_rect_get, 
    CvConnectedComp_rect_set, CvConnectedComp_swigregister, 
    CvConnectedComp_value_get, CvConnectedComp_value_set, 
    CvContourTree_block_max_get, CvContourTree_block_max_set, 
    CvContourTree_delta_elems_get, CvContourTree_delta_elems_set, 
    CvContourTree_elem_size_get, CvContourTree_elem_size_set, 
    CvContourTree_first_get, CvContourTree_first_set, CvContourTree_flags_get, 
    CvContourTree_flags_set, CvContourTree_free_blocks_get, 
    CvContourTree_free_blocks_set, CvContourTree_h_next_get, 
    CvContourTree_h_next_set, CvContourTree_h_prev_get, 
    CvContourTree_h_prev_set, CvContourTree_header_size_get, 
    CvContourTree_header_size_set, CvContourTree_p1_get, CvContourTree_p1_set, 
    CvContourTree_p2_get, CvContourTree_p2_set, CvContourTree_ptr_get, 
    CvContourTree_ptr_set, CvContourTree_storage_get, 
    CvContourTree_storage_set, CvContourTree_swigregister, 
    CvContourTree_total_get, CvContourTree_total_set, 
    CvContourTree_v_next_get, CvContourTree_v_next_set, 
    CvContourTree_v_prev_get, CvContourTree_v_prev_set, 
    CvContour_block_max_get, CvContour_block_max_set, CvContour_color_get, 
    CvContour_color_set, CvContour_delta_elems_get, CvContour_delta_elems_set, 
    CvContour_elem_size_get, CvContour_elem_size_set, CvContour_first_get, 
    CvContour_first_set, CvContour_flags_get, CvContour_flags_set, 
    CvContour_free_blocks_get, CvContour_free_blocks_set, 
    CvContour_h_next_get, CvContour_h_next_set, CvContour_h_prev_get, 
    CvContour_h_prev_set, CvContour_header_size_get, 
    CvContour_header_size_set, CvContour_ptr_get, CvContour_ptr_set, 
    CvContour_rect_get, CvContour_rect_set, CvContour_reserved_get, 
    CvContour_reserved_set, CvContour_storage_get, CvContour_storage_set, 
    CvContour_swigregister, CvContour_total_get, CvContour_total_set, 
    CvContour_v_next_get, CvContour_v_next_set, CvContour_v_prev_get, 
    CvContour_v_prev_set, CvConvexityDefect_depth_get, 
    CvConvexityDefect_depth_point_get, CvConvexityDefect_depth_point_set, 
    CvConvexityDefect_depth_set, CvConvexityDefect_end_get, 
    CvConvexityDefect_end_set, CvConvexityDefect_start_get, 
    CvConvexityDefect_start_set, CvConvexityDefect_swigregister, 
    CvFileNode_data_f_get, CvFileNode_data_f_set, CvFileNode_data_get, 
    CvFileNode_data_i_get, CvFileNode_data_i_set, CvFileNode_data_map_get, 
    CvFileNode_data_map_set, CvFileNode_data_seq_get, CvFileNode_data_seq_set, 
    CvFileNode_data_str_get, CvFileNode_data_str_set, 
    CvFileNode_data_swigregister, CvFileNode_info_get, CvFileNode_info_set, 
    CvFileNode_swigregister, CvFileNode_tag_get, CvFileNode_tag_set, 
    CvFont_ascii_get, CvFont_ascii_set, CvFont_cyrillic_get, 
    CvFont_cyrillic_set, CvFont_dx_get, CvFont_dx_set, CvFont_font_face_get, 
    CvFont_font_face_set, CvFont_greek_get, CvFont_greek_set, 
    CvFont_hscale_get, CvFont_hscale_set, CvFont_line_type_get, 
    CvFont_line_type_set, CvFont_shear_get, CvFont_shear_set, 
    CvFont_swigregister, CvFont_thickness_get, CvFont_thickness_set, 
    CvFont_vscale_get, CvFont_vscale_set, CvGraphEdge_flags_get, 
    CvGraphEdge_flags_set, CvGraphEdge_next_get, CvGraphEdge_next_set, 
    CvGraphEdge_swigregister, CvGraphEdge_vtx_get, CvGraphEdge_vtx_set, 
    CvGraphEdge_weight_get, CvGraphEdge_weight_set, CvGraphScanner_dst_get, 
    CvGraphScanner_dst_set, CvGraphScanner_edge_get, CvGraphScanner_edge_set, 
    CvGraphScanner_graph_get, CvGraphScanner_graph_set, 
    CvGraphScanner_index_get, CvGraphScanner_index_set, 
    CvGraphScanner_mask_get, CvGraphScanner_mask_set, 
    CvGraphScanner_stack_get, CvGraphScanner_stack_set, 
    CvGraphScanner_swigregister, CvGraphScanner_vtx_get, 
    CvGraphScanner_vtx_set, CvGraphVtx2D_first_get, CvGraphVtx2D_first_set, 
    CvGraphVtx2D_flags_get, CvGraphVtx2D_flags_set, CvGraphVtx2D_ptr_get, 
    CvGraphVtx2D_ptr_set, CvGraphVtx2D_swigregister, CvGraphVtx_first_get, 
    CvGraphVtx_first_set, CvGraphVtx_flags_get, CvGraphVtx_flags_set, 
    CvGraphVtx_swigregister, CvGraph_active_count_get, 
    CvGraph_active_count_set, CvGraph_block_max_get, CvGraph_block_max_set, 
    CvGraph_delta_elems_get, CvGraph_delta_elems_set, CvGraph_edges_get, 
    CvGraph_edges_set, CvGraph_elem_size_get, CvGraph_elem_size_set, 
    CvGraph_first_get, CvGraph_first_set, CvGraph_flags_get, 
    CvGraph_flags_set, CvGraph_free_blocks_get, CvGraph_free_blocks_set, 
    CvGraph_free_elems_get, CvGraph_free_elems_set, CvGraph_h_next_get, 
    CvGraph_h_next_set, CvGraph_h_prev_get, CvGraph_h_prev_set, 
    CvGraph_header_size_get, CvGraph_header_size_set, CvGraph_ptr_get, 
    CvGraph_ptr_set, CvGraph_storage_get, CvGraph_storage_set, 
    CvGraph_swigregister, CvGraph_total_get, CvGraph_total_set, 
    CvGraph_v_next_get, CvGraph_v_next_set, CvGraph_v_prev_get, 
    CvGraph_v_prev_set, CvHaarClassifierCascade_count_get, 
    CvHaarClassifierCascade_count_set, CvHaarClassifierCascade_flags_get, 
    CvHaarClassifierCascade_flags_set, 
    CvHaarClassifierCascade_hid_cascade_get, 
    CvHaarClassifierCascade_hid_cascade_set, 
    CvHaarClassifierCascade_orig_window_size_get, 
    CvHaarClassifierCascade_orig_window_size_set, 
    CvHaarClassifierCascade_real_window_size_get, 
    CvHaarClassifierCascade_real_window_size_set, 
    CvHaarClassifierCascade_scale_get, CvHaarClassifierCascade_scale_set, 
    CvHaarClassifierCascade_stage_classifier_get, 
    CvHaarClassifierCascade_stage_classifier_set, 
    CvHaarClassifierCascade_swigregister, CvHaarClassifier_alpha_get, 
    CvHaarClassifier_alpha_set, CvHaarClassifier_count_get, 
    CvHaarClassifier_count_set, CvHaarClassifier_haar_feature_get, 
    CvHaarClassifier_haar_feature_set, CvHaarClassifier_left_get, 
    CvHaarClassifier_left_set, CvHaarClassifier_right_get, 
    CvHaarClassifier_right_set, CvHaarClassifier_swigregister, 
    CvHaarClassifier_threshold_get, CvHaarClassifier_threshold_set, 
    CvHaarFeature_rect_get, CvHaarFeature_rect_r_get, 
    CvHaarFeature_rect_r_set, CvHaarFeature_rect_swigregister, 
    CvHaarFeature_rect_weight_get, CvHaarFeature_rect_weight_set, 
    CvHaarFeature_swigregister, CvHaarFeature_tilted_get, 
    CvHaarFeature_tilted_set, CvHaarStageClassifier_child_get, 
    CvHaarStageClassifier_child_set, CvHaarStageClassifier_classifier_get, 
    CvHaarStageClassifier_classifier_set, CvHaarStageClassifier_count_get, 
    CvHaarStageClassifier_count_set, CvHaarStageClassifier_next_get, 
    CvHaarStageClassifier_next_set, CvHaarStageClassifier_parent_get, 
    CvHaarStageClassifier_parent_set, CvHaarStageClassifier_swigregister, 
    CvHaarStageClassifier_threshold_get, CvHaarStageClassifier_threshold_set, 
    CvHistogram_bins_get, CvHistogram_bins_set, CvHistogram_mat_get, 
    CvHistogram_mat_set, CvHistogram_swigregister, CvHistogram_thresh2_get, 
    CvHistogram_thresh2_set, CvHistogram_thresh_get, CvHistogram_thresh_set, 
    CvHistogram_type_get, CvHistogram_type_set, CvHuMoments_hu1_get, 
    CvHuMoments_hu1_set, CvHuMoments_hu2_get, CvHuMoments_hu2_set, 
    CvHuMoments_hu3_get, CvHuMoments_hu3_set, CvHuMoments_hu4_get, 
    CvHuMoments_hu4_set, CvHuMoments_hu5_get, CvHuMoments_hu5_set, 
    CvHuMoments_hu6_get, CvHuMoments_hu6_set, CvHuMoments_hu7_get, 
    CvHuMoments_hu7_set, CvHuMoments_swigregister, CvImage_asIplImage, 
    CvImage_attach, CvImage_channels, CvImage_clear, CvImage_clone, 
    CvImage_coi, CvImage_create, CvImage_data, CvImage_depth, CvImage_detach, 
    CvImage_height, CvImage_is_valid, CvImage_load, CvImage_origin, 
    CvImage_pix_size, CvImage_read, CvImage_release, CvImage_reset_roi, 
    CvImage_roi, CvImage_roi_row, CvImage_roi_size, CvImage_save, 
    CvImage_set_coi, CvImage_set_roi, CvImage_show, CvImage_size, 
    CvImage_step, CvImage_swigregister, CvImage_width, CvImage_write, 
    CvKalman_CP_get, CvKalman_CP_set, CvKalman_DP_get, CvKalman_DP_set, 
    CvKalman_DynamMatr_get, CvKalman_DynamMatr_set, CvKalman_KalmGainMatr_get, 
    CvKalman_KalmGainMatr_set, CvKalman_MNCovariance_get, 
    CvKalman_MNCovariance_set, CvKalman_MP_get, CvKalman_MP_set, 
    CvKalman_MeasurementMatr_get, CvKalman_MeasurementMatr_set, 
    CvKalman_PNCovariance_get, CvKalman_PNCovariance_set, 
    CvKalman_PosterErrorCovariance_get, CvKalman_PosterErrorCovariance_set, 
    CvKalman_PosterState_get, CvKalman_PosterState_set, 
    CvKalman_PriorErrorCovariance_get, CvKalman_PriorErrorCovariance_set, 
    CvKalman_PriorState_get, CvKalman_PriorState_set, CvKalman_Temp1_get, 
    CvKalman_Temp1_set, CvKalman_Temp2_get, CvKalman_Temp2_set, 
    CvKalman_control_matrix_get, CvKalman_control_matrix_set, 
    CvKalman_error_cov_post_get, CvKalman_error_cov_post_set, 
    CvKalman_error_cov_pre_get, CvKalman_error_cov_pre_set, CvKalman_gain_get, 
    CvKalman_gain_set, CvKalman_measurement_matrix_get, 
    CvKalman_measurement_matrix_set, CvKalman_measurement_noise_cov_get, 
    CvKalman_measurement_noise_cov_set, CvKalman_process_noise_cov_get, 
    CvKalman_process_noise_cov_set, CvKalman_state_post_get, 
    CvKalman_state_post_set, CvKalman_state_pre_get, CvKalman_state_pre_set, 
    CvKalman_swigregister, CvKalman_temp1_get, CvKalman_temp1_set, 
    CvKalman_temp2_get, CvKalman_temp2_set, CvKalman_temp3_get, 
    CvKalman_temp3_set, CvKalman_temp4_get, CvKalman_temp4_set, 
    CvKalman_temp5_get, CvKalman_temp5_set, CvKalman_transition_matrix_get, 
    CvKalman_transition_matrix_set, CvLSH_swigregister, 
    CvLineIterator_err_get, CvLineIterator_err_set, 
    CvLineIterator_minus_delta_get, CvLineIterator_minus_delta_set, 
    CvLineIterator_minus_step_get, CvLineIterator_minus_step_set, 
    CvLineIterator_plus_delta_get, CvLineIterator_plus_delta_set, 
    CvLineIterator_plus_step_get, CvLineIterator_plus_step_set, 
    CvLineIterator_ptr_get, CvLineIterator_ptr_set, 
    CvLineIterator_swigregister, CvMSERParams_areaThreshold_get, 
    CvMSERParams_areaThreshold_set, CvMSERParams_delta_get, 
    CvMSERParams_delta_set, CvMSERParams_edgeBlurSize_get, 
    CvMSERParams_edgeBlurSize_set, CvMSERParams_maxArea_get, 
    CvMSERParams_maxArea_set, CvMSERParams_maxEvolution_get, 
    CvMSERParams_maxEvolution_set, CvMSERParams_maxVariation_get, 
    CvMSERParams_maxVariation_set, CvMSERParams_minArea_get, 
    CvMSERParams_minArea_set, CvMSERParams_minDiversity_get, 
    CvMSERParams_minDiversity_set, CvMSERParams_minMargin_get, 
    CvMSERParams_minMargin_set, CvMSERParams_swigregister, 
    CvMatND_data_db_get, CvMatND_data_db_set, CvMatND_data_fl_get, 
    CvMatND_data_fl_set, CvMatND_data_get, CvMatND_data_i_get, 
    CvMatND_data_i_set, CvMatND_data_ptr_get, CvMatND_data_ptr_set, 
    CvMatND_data_s_get, CvMatND_data_s_set, CvMatND_data_swigregister, 
    CvMatND_dim_get, CvMatND_dim_size_get, CvMatND_dim_size_set, 
    CvMatND_dim_step_get, CvMatND_dim_step_set, CvMatND_dim_swigregister, 
    CvMatND_dims_get, CvMatND_dims_set, CvMatND_hdr_refcount_get, 
    CvMatND_hdr_refcount_set, CvMatND_refcount_get, CvMatND_refcount_set, 
    CvMatND_swigregister, CvMatND_type_get, CvMatND_type_set, CvMat___add__, 
    CvMat___and__, CvMat___div__, CvMat___eq__, CvMat___ge__, 
    CvMat___getitem__, CvMat___gt__, CvMat___iadd__, CvMat___iand__, 
    CvMat___idiv__, CvMat___imul__, CvMat___invert__, CvMat___ior__, 
    CvMat___isub__, CvMat___ixor__, CvMat___le__, CvMat___lt__, CvMat___mul__, 
    CvMat___ne__, CvMat___or__, CvMat___pow__, CvMat___radd__, CvMat___rand__, 
    CvMat___rdiv__, CvMat___req__, CvMat___rge__, CvMat___rgt__, 
    CvMat___rle__, CvMat___rlt__, CvMat___rmul__, CvMat___rne__, 
    CvMat___ror__, CvMat___rsub__, CvMat___rxor__, CvMat___setitem__, 
    CvMat___str__, CvMat___sub__, CvMat___xor__, CvMat_cols_get, 
    CvMat_cols_set, CvMat_dataOrder_get, CvMat_dataOrder_set, 
    CvMat_data_db_get, CvMat_data_db_set, CvMat_data_fl_get, 
    CvMat_data_fl_set, CvMat_data_get, CvMat_data_i_get, CvMat_data_i_set, 
    CvMat_data_ptr_get, CvMat_data_ptr_set, CvMat_data_s_get, 
    CvMat_data_s_set, CvMat_data_swigregister, CvMat_depth_get, 
    CvMat_depth_set, CvMat_hdr_refcount_get, CvMat_hdr_refcount_set, 
    CvMat_height_get, CvMat_height_set, CvMat_imageData_get, 
    CvMat_imageData_set, CvMat_imageSize_get, CvMat_imageSize_set, 
    CvMat_nChannels_get, CvMat_nChannels_set, CvMat_origin_get, 
    CvMat_origin_set, CvMat_refcount_get, CvMat_refcount_set, CvMat_rows_get, 
    CvMat_rows_set, CvMat_step_get, CvMat_step_set, CvMat_swigregister, 
    CvMat_type_get, CvMat_type_set, CvMat_widthStep_get, CvMat_widthStep_set, 
    CvMat_width_get, CvMat_width_set, CvMatrix3_m_get, CvMatrix3_m_set, 
    CvMatrix3_swigregister, CvMatrix_addref, CvMatrix_asCvMat, 
    CvMatrix_channels, CvMatrix_clear, CvMatrix_clone, CvMatrix_cols, 
    CvMatrix_create, CvMatrix_data, CvMatrix_depth, CvMatrix_is_valid, 
    CvMatrix_load, CvMatrix_pix_size, CvMatrix_read, CvMatrix_release, 
    CvMatrix_row, CvMatrix_rows, CvMatrix_save, CvMatrix_set, 
    CvMatrix_set_data, CvMatrix_show, CvMatrix_size, CvMatrix_step, 
    CvMatrix_swigregister, CvMatrix_type, CvMatrix_write, CvMemBlock_next_get, 
    CvMemBlock_next_set, CvMemBlock_prev_get, CvMemBlock_prev_set, 
    CvMemBlock_swigregister, CvMemStoragePos_free_space_get, 
    CvMemStoragePos_free_space_set, CvMemStoragePos_swigregister, 
    CvMemStoragePos_top_get, CvMemStoragePos_top_set, 
    CvMemStorage_block_size_get, CvMemStorage_block_size_set, 
    CvMemStorage_bottom_get, CvMemStorage_bottom_set, 
    CvMemStorage_free_space_get, CvMemStorage_free_space_set, 
    CvMemStorage_parent_get, CvMemStorage_parent_set, 
    CvMemStorage_signature_get, CvMemStorage_signature_set, 
    CvMemStorage_swigregister, CvMemStorage_top_get, CvMemStorage_top_set, 
    CvModuleInfo_func_tab_get, CvModuleInfo_func_tab_set, 
    CvModuleInfo_name_get, CvModuleInfo_name_set, CvModuleInfo_next_get, 
    CvModuleInfo_next_set, CvModuleInfo_swigregister, 
    CvModuleInfo_version_get, CvModuleInfo_version_set, CvModule_first_get, 
    CvModule_first_set, CvModule_info_get, CvModule_info_set, 
    CvModule_last_get, CvModule_last_set, CvModule_swigregister, 
    CvMoments_inv_sqrt_m00_get, CvMoments_inv_sqrt_m00_set, CvMoments_m00_get, 
    CvMoments_m00_set, CvMoments_m01_get, CvMoments_m01_set, 
    CvMoments_m02_get, CvMoments_m02_set, CvMoments_m03_get, 
    CvMoments_m03_set, CvMoments_m10_get, CvMoments_m10_set, 
    CvMoments_m11_get, CvMoments_m11_set, CvMoments_m12_get, 
    CvMoments_m12_set, CvMoments_m20_get, CvMoments_m20_set, 
    CvMoments_m21_get, CvMoments_m21_set, CvMoments_m30_get, 
    CvMoments_m30_set, CvMoments_mu02_get, CvMoments_mu02_set, 
    CvMoments_mu03_get, CvMoments_mu03_set, CvMoments_mu11_get, 
    CvMoments_mu11_set, CvMoments_mu12_get, CvMoments_mu12_set, 
    CvMoments_mu20_get, CvMoments_mu20_set, CvMoments_mu21_get, 
    CvMoments_mu21_set, CvMoments_mu30_get, CvMoments_mu30_set, 
    CvMoments_swigregister, CvNArrayIterator_count_get, 
    CvNArrayIterator_count_set, CvNArrayIterator_dims_get, 
    CvNArrayIterator_dims_set, CvNArrayIterator_hdr_get, 
    CvNArrayIterator_hdr_set, CvNArrayIterator_ptr_get, 
    CvNArrayIterator_ptr_set, CvNArrayIterator_size_get, 
    CvNArrayIterator_size_set, CvNArrayIterator_stack_get, 
    CvNArrayIterator_stack_set, CvNArrayIterator_swigregister, 
    CvPluginFuncInfo_default_func_addr_get, 
    CvPluginFuncInfo_default_func_addr_set, CvPluginFuncInfo_func_addr_get, 
    CvPluginFuncInfo_func_addr_set, CvPluginFuncInfo_func_names_get, 
    CvPluginFuncInfo_func_names_set, CvPluginFuncInfo_loaded_from_get, 
    CvPluginFuncInfo_loaded_from_set, CvPluginFuncInfo_search_modules_get, 
    CvPluginFuncInfo_search_modules_set, CvPluginFuncInfo_swigregister, 
    CvPoint2D32f___repr__, CvPoint2D32f___str__, CvPoint2D32f_swigregister, 
    CvPoint2D32f_x_get, CvPoint2D32f_x_set, CvPoint2D32f_y_get, 
    CvPoint2D32f_y_set, CvPoint2D64f_swigregister, CvPoint2D64f_x_get, 
    CvPoint2D64f_x_set, CvPoint2D64f_y_get, CvPoint2D64f_y_set, 
    CvPoint3D32f_swigregister, CvPoint3D32f_x_get, CvPoint3D32f_x_set, 
    CvPoint3D32f_y_get, CvPoint3D32f_y_set, CvPoint3D32f_z_get, 
    CvPoint3D32f_z_set, CvPoint3D64f_swigregister, CvPoint3D64f_x_get, 
    CvPoint3D64f_x_set, CvPoint3D64f_y_get, CvPoint3D64f_y_set, 
    CvPoint3D64f_z_get, CvPoint3D64f_z_set, CvPointVector___bool__, 
    CvPointVector___delitem__, CvPointVector___delslice__, 
    CvPointVector___getitem__, CvPointVector___getslice__, 
    CvPointVector___len__, CvPointVector___nonzero__, 
    CvPointVector___setitem__, CvPointVector___setslice__, 
    CvPointVector_append, CvPointVector_assign, CvPointVector_back, 
    CvPointVector_begin, CvPointVector_capacity, CvPointVector_clear, 
    CvPointVector_empty, CvPointVector_end, CvPointVector_erase, 
    CvPointVector_front, CvPointVector_get_allocator, CvPointVector_insert, 
    CvPointVector_iterator, CvPointVector_pop, CvPointVector_pop_back, 
    CvPointVector_push_back, CvPointVector_rbegin, CvPointVector_rend, 
    CvPointVector_reserve, CvPointVector_resize, CvPointVector_size, 
    CvPointVector_swap, CvPointVector_swigregister, CvPoint___repr__, 
    CvPoint___str__, CvPoint_swigregister, CvPoint_x_get, CvPoint_x_set, 
    CvPoint_y_get, CvPoint_y_set, CvQuadEdge2D_flags_get, 
    CvQuadEdge2D_flags_set, CvQuadEdge2D_next_get, CvQuadEdge2D_next_set, 
    CvQuadEdge2D_pt_get, CvQuadEdge2D_pt_set, CvQuadEdge2D_swigregister, 
    CvRNG_Wrapper___eq__, CvRNG_Wrapper___ne__, CvRNG_Wrapper_ptr, 
    CvRNG_Wrapper_ref, CvRNG_Wrapper_swigregister, CvRect_height_get, 
    CvRect_height_set, CvRect_swigregister, CvRect_width_get, 
    CvRect_width_set, CvRect_x_get, CvRect_x_set, CvRect_y_get, CvRect_y_set, 
    CvSURFParams_extended_get, CvSURFParams_extended_set, 
    CvSURFParams_hessianThreshold_get, CvSURFParams_hessianThreshold_set, 
    CvSURFParams_nOctaveLayers_get, CvSURFParams_nOctaveLayers_set, 
    CvSURFParams_nOctaves_get, CvSURFParams_nOctaves_set, 
    CvSURFParams_swigregister, CvSURFPoint_dir_get, CvSURFPoint_dir_set, 
    CvSURFPoint_hessian_get, CvSURFPoint_hessian_set, 
    CvSURFPoint_laplacian_get, CvSURFPoint_laplacian_set, CvSURFPoint_pt_get, 
    CvSURFPoint_pt_set, CvSURFPoint_size_get, CvSURFPoint_size_set, 
    CvSURFPoint_swigregister, CvScalar___getitem__, CvScalar___repr__, 
    CvScalar___setitem__, CvScalar___str__, CvScalar_swigregister, 
    CvScalar_val_get, CvScalar_val_set, CvSeqBlock_count_get, 
    CvSeqBlock_count_set, CvSeqBlock_data_get, CvSeqBlock_data_set, 
    CvSeqBlock_next_get, CvSeqBlock_next_set, CvSeqBlock_prev_get, 
    CvSeqBlock_prev_set, CvSeqBlock_start_index_get, 
    CvSeqBlock_start_index_set, CvSeqBlock_swigregister, 
    CvSeqReader_block_get, CvSeqReader_block_max_get, 
    CvSeqReader_block_max_set, CvSeqReader_block_min_get, 
    CvSeqReader_block_min_set, CvSeqReader_block_set, 
    CvSeqReader_delta_index_get, CvSeqReader_delta_index_set, 
    CvSeqReader_header_size_get, CvSeqReader_header_size_set, 
    CvSeqReader_prev_elem_get, CvSeqReader_prev_elem_set, CvSeqReader_ptr_get, 
    CvSeqReader_ptr_set, CvSeqReader_seq_get, CvSeqReader_seq_set, 
    CvSeqReader_swigregister, CvSeqWriter_block_get, 
    CvSeqWriter_block_max_get, CvSeqWriter_block_max_set, 
    CvSeqWriter_block_min_get, CvSeqWriter_block_min_set, 
    CvSeqWriter_block_set, CvSeqWriter_header_size_get, 
    CvSeqWriter_header_size_set, CvSeqWriter_ptr_get, CvSeqWriter_ptr_set, 
    CvSeqWriter_seq_get, CvSeqWriter_seq_set, CvSeqWriter_swigregister, 
    CvSeq_CvConnectedComp___getitem__, CvSeq_CvConnectedComp___setitem__, 
    CvSeq_CvConnectedComp_append, CvSeq_CvConnectedComp_cast, 
    CvSeq_CvConnectedComp_pop, CvSeq_CvConnectedComp_swigregister, 
    CvSeq_CvPoint2D32f___getitem__, CvSeq_CvPoint2D32f___setitem__, 
    CvSeq_CvPoint2D32f_append, CvSeq_CvPoint2D32f_cast, 
    CvSeq_CvPoint2D32f_pop, CvSeq_CvPoint2D32f_swigregister, 
    CvSeq_CvPoint_2___getitem__, CvSeq_CvPoint_2___setitem__, 
    CvSeq_CvPoint_2_append, CvSeq_CvPoint_2_cast, CvSeq_CvPoint_2_pop, 
    CvSeq_CvPoint_2_swigregister, CvSeq_CvPoint___getitem__, 
    CvSeq_CvPoint___setitem__, CvSeq_CvPoint_append, CvSeq_CvPoint_cast, 
    CvSeq_CvPoint_pop, CvSeq_CvPoint_swigregister, 
    CvSeq_CvQuadEdge2D___getitem__, CvSeq_CvQuadEdge2D___setitem__, 
    CvSeq_CvQuadEdge2D_append, CvSeq_CvQuadEdge2D_cast, 
    CvSeq_CvQuadEdge2D_pop, CvSeq_CvQuadEdge2D_swigregister, 
    CvSeq_CvRect___getitem__, CvSeq_CvRect___setitem__, CvSeq_CvRect_append, 
    CvSeq_CvRect_cast, CvSeq_CvRect_pop, CvSeq_CvRect_swigregister, 
    CvSeq_CvSeq___getitem__, CvSeq_CvSeq___setitem__, CvSeq_CvSeq_append, 
    CvSeq_CvSeq_cast, CvSeq_CvSeq_pop, CvSeq_CvSeq_swigregister, 
    CvSeq_block_max_get, CvSeq_block_max_set, CvSeq_delta_elems_get, 
    CvSeq_delta_elems_set, CvSeq_elem_size_get, CvSeq_elem_size_set, 
    CvSeq_first_get, CvSeq_first_set, CvSeq_flags_get, CvSeq_flags_set, 
    CvSeq_float_2___getitem__, CvSeq_float_2___setitem__, 
    CvSeq_float_2_append, CvSeq_float_2_cast, CvSeq_float_2_pop, 
    CvSeq_float_2_swigregister, CvSeq_float_3___getitem__, 
    CvSeq_float_3___setitem__, CvSeq_float_3_append, CvSeq_float_3_cast, 
    CvSeq_float_3_pop, CvSeq_float_3_swigregister, CvSeq_free_blocks_get, 
    CvSeq_free_blocks_set, CvSeq_h_next_get, CvSeq_h_next_set, 
    CvSeq_h_prev_get, CvSeq_h_prev_set, CvSeq_header_size_get, 
    CvSeq_header_size_set, CvSeq_ptr_get, CvSeq_ptr_set, CvSeq_storage_get, 
    CvSeq_storage_set, CvSeq_swigregister, CvSeq_total_get, CvSeq_total_set, 
    CvSeq_v_next_get, CvSeq_v_next_set, CvSeq_v_prev_get, CvSeq_v_prev_set, 
    CvSetElem_flags_get, CvSetElem_flags_set, CvSetElem_next_free_get, 
    CvSetElem_next_free_set, CvSetElem_swigregister, CvSet_active_count_get, 
    CvSet_active_count_set, CvSet_block_max_get, CvSet_block_max_set, 
    CvSet_delta_elems_get, CvSet_delta_elems_set, CvSet_elem_size_get, 
    CvSet_elem_size_set, CvSet_first_get, CvSet_first_set, CvSet_flags_get, 
    CvSet_flags_set, CvSet_free_blocks_get, CvSet_free_blocks_set, 
    CvSet_free_elems_get, CvSet_free_elems_set, CvSet_h_next_get, 
    CvSet_h_next_set, CvSet_h_prev_get, CvSet_h_prev_set, 
    CvSet_header_size_get, CvSet_header_size_set, CvSet_ptr_get, 
    CvSet_ptr_set, CvSet_storage_get, CvSet_storage_set, CvSet_swigregister, 
    CvSet_total_get, CvSet_total_set, CvSet_v_next_get, CvSet_v_next_set, 
    CvSet_v_prev_get, CvSet_v_prev_set, CvSize2D32f_height_get, 
    CvSize2D32f_height_set, CvSize2D32f_swigregister, CvSize2D32f_width_get, 
    CvSize2D32f_width_set, CvSize_height_get, CvSize_height_set, 
    CvSize_swigregister, CvSize_width_get, CvSize_width_set, 
    CvSlice_end_index_get, CvSlice_end_index_set, CvSlice_start_index_get, 
    CvSlice_start_index_set, CvSlice_swigregister, 
    CvSparseMatIterator_curidx_get, CvSparseMatIterator_curidx_set, 
    CvSparseMatIterator_mat_get, CvSparseMatIterator_mat_set, 
    CvSparseMatIterator_node_get, CvSparseMatIterator_node_set, 
    CvSparseMatIterator_swigregister, CvSparseMat_dims_get, 
    CvSparseMat_dims_set, CvSparseMat_hashsize_get, CvSparseMat_hashsize_set, 
    CvSparseMat_hashtable_get, CvSparseMat_hashtable_set, 
    CvSparseMat_hdr_refcount_get, CvSparseMat_hdr_refcount_set, 
    CvSparseMat_heap_get, CvSparseMat_heap_set, CvSparseMat_idxoffset_get, 
    CvSparseMat_idxoffset_set, CvSparseMat_refcount_get, 
    CvSparseMat_refcount_set, CvSparseMat_size_get, CvSparseMat_size_set, 
    CvSparseMat_swigregister, CvSparseMat_type_get, CvSparseMat_type_set, 
    CvSparseMat_valoffset_get, CvSparseMat_valoffset_set, 
    CvSparseNode_hashval_get, CvSparseNode_hashval_set, CvSparseNode_next_get, 
    CvSparseNode_next_set, CvSparseNode_swigregister, 
    CvStarDetectorParams_lineThresholdBinarized_get, 
    CvStarDetectorParams_lineThresholdBinarized_set, 
    CvStarDetectorParams_lineThresholdProjected_get, 
    CvStarDetectorParams_lineThresholdProjected_set, 
    CvStarDetectorParams_maxSize_get, CvStarDetectorParams_maxSize_set, 
    CvStarDetectorParams_responseThreshold_get, 
    CvStarDetectorParams_responseThreshold_set, 
    CvStarDetectorParams_suppressNonmaxSize_get, 
    CvStarDetectorParams_suppressNonmaxSize_set, 
    CvStarDetectorParams_swigregister, CvStarKeypoint_pt_get, 
    CvStarKeypoint_pt_set, CvStarKeypoint_response_get, 
    CvStarKeypoint_response_set, CvStarKeypoint_size_get, 
    CvStarKeypoint_size_set, CvStarKeypoint_swigregister, 
    CvStereoBMState_SADWindowSize_get, CvStereoBMState_SADWindowSize_set, 
    CvStereoBMState_dbmax_get, CvStereoBMState_dbmax_set, 
    CvStereoBMState_dbmin_get, CvStereoBMState_dbmin_set, 
    CvStereoBMState_minDisparity_get, CvStereoBMState_minDisparity_set, 
    CvStereoBMState_numberOfDisparities_get, 
    CvStereoBMState_numberOfDisparities_set, CvStereoBMState_preFilterCap_get, 
    CvStereoBMState_preFilterCap_set, CvStereoBMState_preFilterSize_get, 
    CvStereoBMState_preFilterSize_set, CvStereoBMState_preFilterType_get, 
    CvStereoBMState_preFilterType_set, CvStereoBMState_preFilteredImg0_get, 
    CvStereoBMState_preFilteredImg0_set, CvStereoBMState_preFilteredImg1_get, 
    CvStereoBMState_preFilteredImg1_set, CvStereoBMState_slidingSumBuf_get, 
    CvStereoBMState_slidingSumBuf_set, CvStereoBMState_speckleRange_get, 
    CvStereoBMState_speckleRange_set, CvStereoBMState_speckleWindowSize_get, 
    CvStereoBMState_speckleWindowSize_set, CvStereoBMState_swigregister, 
    CvStereoBMState_textureThreshold_get, 
    CvStereoBMState_textureThreshold_set, 
    CvStereoBMState_trySmallerWindows_get, 
    CvStereoBMState_trySmallerWindows_set, 
    CvStereoBMState_uniquenessRatio_get, CvStereoBMState_uniquenessRatio_set, 
    CvStereoGCState_Ithreshold_get, CvStereoGCState_Ithreshold_set, 
    CvStereoGCState_K_get, CvStereoGCState_K_set, CvStereoGCState__lambda_get, 
    CvStereoGCState__lambda_set, CvStereoGCState_dispLeft_get, 
    CvStereoGCState_dispLeft_set, CvStereoGCState_dispRight_get, 
    CvStereoGCState_dispRight_set, CvStereoGCState_edgeBuf_get, 
    CvStereoGCState_edgeBuf_set, CvStereoGCState_interactionRadius_get, 
    CvStereoGCState_interactionRadius_set, CvStereoGCState_lambda1_get, 
    CvStereoGCState_lambda1_set, CvStereoGCState_lambda2_get, 
    CvStereoGCState_lambda2_set, CvStereoGCState_left_get, 
    CvStereoGCState_left_set, CvStereoGCState_maxIters_get, 
    CvStereoGCState_maxIters_set, CvStereoGCState_minDisparity_get, 
    CvStereoGCState_minDisparity_set, CvStereoGCState_numberOfDisparities_get, 
    CvStereoGCState_numberOfDisparities_set, 
    CvStereoGCState_occlusionCost_get, CvStereoGCState_occlusionCost_set, 
    CvStereoGCState_ptrLeft_get, CvStereoGCState_ptrLeft_set, 
    CvStereoGCState_ptrRight_get, CvStereoGCState_ptrRight_set, 
    CvStereoGCState_right_get, CvStereoGCState_right_set, 
    CvStereoGCState_swigregister, CvStereoGCState_vtxBuf_get, 
    CvStereoGCState_vtxBuf_set, CvStringHashNode_hashval_get, 
    CvStringHashNode_hashval_set, CvStringHashNode_next_get, 
    CvStringHashNode_next_set, CvStringHashNode_str_get, 
    CvStringHashNode_str_set, CvStringHashNode_swigregister, CvString_len_get, 
    CvString_len_set, CvString_ptr_get, CvString_ptr_set, 
    CvString_swigregister, CvSubdiv2DEdge_Wrapper___eq__, 
    CvSubdiv2DEdge_Wrapper___ne__, CvSubdiv2DEdge_Wrapper_ptr, 
    CvSubdiv2DEdge_Wrapper_ref, CvSubdiv2DEdge_Wrapper_swigregister, 
    CvSubdiv2DPoint_first_get, CvSubdiv2DPoint_first_set, 
    CvSubdiv2DPoint_flags_get, CvSubdiv2DPoint_flags_set, 
    CvSubdiv2DPoint_pt_get, CvSubdiv2DPoint_pt_set, 
    CvSubdiv2DPoint_swigregister, CvSubdiv2D_active_count_get, 
    CvSubdiv2D_active_count_set, CvSubdiv2D_block_max_get, 
    CvSubdiv2D_block_max_set, CvSubdiv2D_bottomright_get, 
    CvSubdiv2D_bottomright_set, CvSubdiv2D_delta_elems_get, 
    CvSubdiv2D_delta_elems_set, CvSubdiv2D_edges_get, CvSubdiv2D_edges_set, 
    CvSubdiv2D_elem_size_get, CvSubdiv2D_elem_size_set, CvSubdiv2D_first_get, 
    CvSubdiv2D_first_set, CvSubdiv2D_flags_get, CvSubdiv2D_flags_set, 
    CvSubdiv2D_free_blocks_get, CvSubdiv2D_free_blocks_set, 
    CvSubdiv2D_free_elems_get, CvSubdiv2D_free_elems_set, 
    CvSubdiv2D_h_next_get, CvSubdiv2D_h_next_set, CvSubdiv2D_h_prev_get, 
    CvSubdiv2D_h_prev_set, CvSubdiv2D_header_size_get, 
    CvSubdiv2D_header_size_set, CvSubdiv2D_is_geometry_valid_get, 
    CvSubdiv2D_is_geometry_valid_set, CvSubdiv2D_ptr_get, CvSubdiv2D_ptr_set, 
    CvSubdiv2D_quad_edges_get, CvSubdiv2D_quad_edges_set, 
    CvSubdiv2D_recent_edge_get, CvSubdiv2D_recent_edge_set, 
    CvSubdiv2D_storage_get, CvSubdiv2D_storage_set, CvSubdiv2D_swigregister, 
    CvSubdiv2D_topleft_get, CvSubdiv2D_topleft_set, CvSubdiv2D_total_get, 
    CvSubdiv2D_total_set, CvSubdiv2D_typed_edges_get, 
    CvSubdiv2D_typed_edges_set, CvSubdiv2D_v_next_get, CvSubdiv2D_v_next_set, 
    CvSubdiv2D_v_prev_get, CvSubdiv2D_v_prev_set, CvTermCriteria_epsilon_get, 
    CvTermCriteria_epsilon_set, CvTermCriteria_max_iter_get, 
    CvTermCriteria_max_iter_set, CvTermCriteria_swigregister, 
    CvTermCriteria_type_get, CvTermCriteria_type_set, 
    CvTreeNodeIterator_level_get, CvTreeNodeIterator_level_set, 
    CvTreeNodeIterator_max_level_get, CvTreeNodeIterator_max_level_set, 
    CvTreeNodeIterator_node_get, CvTreeNodeIterator_node_set, 
    CvTreeNodeIterator_swigregister, CvTuple_CvPoint_2___getitem__, 
    CvTuple_CvPoint_2___setitem__, CvTuple_CvPoint_2_swigregister, 
    CvTuple_CvPoint_2_val_get, CvTuple_CvPoint_2_val_set, 
    CvTuple_float_2___getitem__, CvTuple_float_2___setitem__, 
    CvTuple_float_2_swigregister, CvTuple_float_2_val_get, 
    CvTuple_float_2_val_set, CvTuple_float_3___getitem__, 
    CvTuple_float_3___setitem__, CvTuple_float_3_swigregister, 
    CvTuple_float_3_val_get, CvTuple_float_3_val_set, CvTypeInfo_clone_get, 
    CvTypeInfo_clone_set, CvTypeInfo_flags_get, CvTypeInfo_flags_set, 
    CvTypeInfo_header_size_get, CvTypeInfo_header_size_set, 
    CvTypeInfo_is_instance_get, CvTypeInfo_is_instance_set, 
    CvTypeInfo_next_get, CvTypeInfo_next_set, CvTypeInfo_prev_get, 
    CvTypeInfo_prev_set, CvTypeInfo_read_get, CvTypeInfo_read_set, 
    CvTypeInfo_release_get, CvTypeInfo_release_set, CvTypeInfo_swigregister, 
    CvTypeInfo_type_name_get, CvTypeInfo_type_name_set, CvTypeInfo_write_get, 
    CvTypeInfo_write_set, CvType_first_get, CvType_first_set, CvType_info_get, 
    CvType_info_set, CvType_last_get, CvType_last_set, CvType_swigregister, 
    FloatVector___bool__, FloatVector___delitem__, FloatVector___delslice__, 
    FloatVector___getitem__, FloatVector___getslice__, FloatVector___len__, 
    FloatVector___nonzero__, FloatVector___setitem__, 
    FloatVector___setslice__, FloatVector_append, FloatVector_assign, 
    FloatVector_back, FloatVector_begin, FloatVector_capacity, 
    FloatVector_clear, FloatVector_empty, FloatVector_end, FloatVector_erase, 
    FloatVector_front, FloatVector_get_allocator, FloatVector_insert, 
    FloatVector_iterator, FloatVector_pop, FloatVector_pop_back, 
    FloatVector_push_back, FloatVector_rbegin, FloatVector_rend, 
    FloatVector_reserve, FloatVector_resize, FloatVector_size, 
    FloatVector_swap, FloatVector_swigregister, IplConvKernelFP_anchorX_get, 
    IplConvKernelFP_anchorX_set, IplConvKernelFP_anchorY_get, 
    IplConvKernelFP_anchorY_set, IplConvKernelFP_nCols_get, 
    IplConvKernelFP_nCols_set, IplConvKernelFP_nRows_get, 
    IplConvKernelFP_nRows_set, IplConvKernelFP_swigregister, 
    IplConvKernelFP_values_get, IplConvKernelFP_values_set, 
    IplConvKernel_anchorX_get, IplConvKernel_anchorX_set, 
    IplConvKernel_anchorY_get, IplConvKernel_anchorY_set, 
    IplConvKernel_nCols_get, IplConvKernel_nCols_set, IplConvKernel_nRows_get, 
    IplConvKernel_nRows_set, IplConvKernel_nShiftR_get, 
    IplConvKernel_nShiftR_set, IplConvKernel_swigregister, 
    IplConvKernel_values_get, IplConvKernel_values_set, IplImage_ID_get, 
    IplImage_ID_set, IplImage___add__, IplImage___and__, IplImage___div__, 
    IplImage___eq__, IplImage___ge__, IplImage___getitem__, IplImage___gt__, 
    IplImage___iadd__, IplImage___iand__, IplImage___idiv__, 
    IplImage___imul__, IplImage___ior__, IplImage___isub__, IplImage___ixor__, 
    IplImage___le__, IplImage___lt__, IplImage___mul__, IplImage___ne__, 
    IplImage___or__, IplImage___pow__, IplImage___radd__, IplImage___rand__, 
    IplImage___rdiv__, IplImage___req__, IplImage___rge__, IplImage___rgt__, 
    IplImage___rle__, IplImage___rlt__, IplImage___rmul__, IplImage___rne__, 
    IplImage___ror__, IplImage___rsub__, IplImage___rxor__, 
    IplImage___setitem__, IplImage___str__, IplImage___sub__, 
    IplImage___xor__, IplImage_align_get, IplImage_align_set, 
    IplImage_dataOrder_get, IplImage_dataOrder_set, IplImage_depth_get, 
    IplImage_depth_set, IplImage_height_get, IplImage_height_set, 
    IplImage_imageSize_get, IplImage_imageSize_set, IplImage_nChannels_get, 
    IplImage_nChannels_set, IplImage_origin_get, IplImage_origin_set, 
    IplImage_roi_get, IplImage_roi_set, IplImage_swigregister, 
    IplImage_widthStep_get, IplImage_widthStep_set, IplImage_width_get, 
    IplImage_width_set, IplROI_coi_get, IplROI_coi_set, IplROI_height_get, 
    IplROI_height_set, IplROI_swigregister, IplROI_width_get, 
    IplROI_width_set, IplROI_xOffset_get, IplROI_xOffset_set, 
    IplROI_yOffset_get, IplROI_yOffset_set, LSHSize, 
    SWIG_PyInstanceMethod_New, SendErrorToPython, SwigPyIterator___add__, 
    SwigPyIterator___eq__, SwigPyIterator___iadd__, SwigPyIterator___isub__, 
    SwigPyIterator___ne__, SwigPyIterator___next__, SwigPyIterator___sub__, 
    SwigPyIterator_advance, SwigPyIterator_copy, SwigPyIterator_decr, 
    SwigPyIterator_distance, SwigPyIterator_equal, SwigPyIterator_incr, 
    SwigPyIterator_next, SwigPyIterator_previous, SwigPyIterator_swigregister, 
    SwigPyIterator_value, cv2DRotationMatrix, cvAXPY, cvAbs, cvAbsDiff, 
    cvAbsDiffS, cvAcc, cvAdaptiveThreshold, cvAdd, cvAddS, cvAddWeighted, 
    cvAlloc, cvAnd, cvAndS, cvApproxChainsUntyped, cvApproxPoly, cvArcLength, 
    cvAttrList, cvAttrValue, cvAvg, cvAvgSdv, cvBackProjectPCA, 
    cvBoundingRect, cvBoxPoints, cvCalcAffineFlowPyrLK, cvCalcArrBackProject, 
    cvCalcArrBackProjectPatch, cvCalcArrHist, cvCalcBackProject, 
    cvCalcBackProjectPatch, cvCalcBayesianProb, cvCalcCovarMatrix, cvCalcEMD2, 
    cvCalcGlobalOrientation, cvCalcHist, cvCalcImageHomography, 
    cvCalcMatMulDeriv, cvCalcMotionGradient, cvCalcOpticalFlowBM, 
    cvCalcOpticalFlowHS, cvCalcOpticalFlowLK, cvCalcOpticalFlowPyrLK, 
    cvCalcPCA, cvCalcPGH, cvCalcProbDensity, cvCalcSubdivVoronoi2D, 
    cvCalibrateCamera2, cvCalibrationMatrixValues, cvCamShift, cvCanny, 
    cvCartToPolar, cvCbrt, cvCeil, cvChangeSeqBlock, cvCheckArr, 
    cvCheckContourConvexity, cvCheckTermCriteria, cvCircle, cvClearGraph, 
    cvClearHist, cvClearMemStorage, cvClearND, cvClearSeq, cvClearSet, 
    cvClearSubdivVoronoi2D, cvClipLine, cvClone, cvCloneGraph, cvCloneImage, 
    cvCloneMat, cvCloneMatND, cvCloneSeq, cvCloneSparseMat, cvCmp, cvCmpS, 
    cvColorToScalar, cvCompareHist, cvCompleteSymm, cvComposeRT, 
    cvComputeCorrespondEpilines, cvConDensInitSampleSet, 
    cvConDensUpdateByTime, cvContourArea, cvContourFromContourTreeUntyped, 
    cvContourPerimeter, cvConvert, cvConvertMaps, cvConvertPointsHomogeneous, 
    cvConvertScale, cvConvertScaleAbs, cvConvexHull2, 
    cvConvexityDefectsUntyped, cvCopy, cvCopyHist, cvCopyMakeBorder, 
    cvCornerEigenValsAndVecs, cvCornerHarris, cvCornerMinEigenVal, 
    cvCorrectMatches, cvCountNonZero, cvCreateChildMemStorage, 
    cvCreateConDensation, cvCreateContourTree, cvCreateData, cvCreateGraph, 
    cvCreateGraphScanner, cvCreateHist, cvCreateImage, cvCreateKDTree, 
    cvCreateKalman, cvCreateLSH, cvCreateMat, cvCreateMatHeader, 
    cvCreateMatND, cvCreateMatNDHeader, cvCreateMemStorage, cvCreateMemoryLSH, 
    cvCreatePOSITObject, cvCreatePyramid, cvCreateSeq, cvCreateSeqBlock, 
    cvCreateSet, cvCreateSparseMat, cvCreateSpillTree, cvCreateStereoBMState, 
    cvCreateStereoGCState, cvCreateStructuringElementEx, cvCreateSubdiv2D, 
    cvCreateSubdivDelaunay2D, cvCrossProduct, cvCvtColor, cvCvtSeqToArray, 
    cvDCT, cvDFT, cvDecRefData, cvDecomposeProjectionMatrix, cvDet, cvDilate, 
    cvDistTransform, cvDiv, cvDotProduct, cvDrawChessboardCorners, 
    cvDrawContours, cvEigenVV, cvEllipse, cvEllipse2Poly, cvEllipseBox, 
    cvEndFindContours, cvEndWriteSeq, cvEndWriteStruct, cvEqualizeHist, 
    cvErode, cvError, cvErrorFromIppStatus, cvErrorStr, 
    cvEstimateRigidTransform, cvExp, cvExtractMSER, cvExtractSURF, 
    cvFastArctan, cvFillConvexPoly, cvFillPoly, cvFilter2D, 
    cvFindChessboardCorners, cvFindContoursUntyped, cvFindCornerSubPix, 
    cvFindDominantPoints, cvFindExtrinsicCameraParams2, cvFindFeatures, 
    cvFindFeaturesBoxed, cvFindFundamentalMat, cvFindGraphEdge, 
    cvFindGraphEdgeByPtr, cvFindHomography, cvFindNearestPoint2D, 
    cvFindNextContour, cvFindStereoCorrespondenceBM, 
    cvFindStereoCorrespondenceGC, cvFindType, cvFirstType, cvFitEllipse2, 
    cvFitLine, cvFlip, cvFloodFill, cvFloor, cvFlushSeqWriter, cvFont, cvFree, 
    cvFree_, cvGEMM, cvGet1D, cvGet2D, cvGet3D, cvGetAffineTransform, 
    cvGetCentralMoment, cvGetCol, cvGetCols, cvGetDiag, cvGetDimSize, 
    cvGetDims, cvGetElemType, cvGetErrInfo, cvGetErrMode, cvGetErrStatus, 
    cvGetFileNode, cvGetFileNodeByName, cvGetFileNodeName, cvGetGraphVtx, 
    cvGetHashedKey, cvGetHuMoments, cvGetMat, cvGetMinMaxHistValue, 
    cvGetModuleInfo, cvGetND, cvGetNextSparseNode, 
    cvGetNormalizedCentralMoment, cvGetNumThreads, cvGetOptimalDFTSize, 
    cvGetPerspectiveTransform, cvGetQuadrangleSubPix, cvGetRawData, 
    cvGetReal1D, cvGetReal2D, cvGetReal3D, cvGetRealND, cvGetRectSubPix, 
    cvGetRootFileNode, cvGetRow, cvGetRows, cvGetSeqElem, cvGetSeqReaderPos, 
    cvGetSetElem, cvGetSize, cvGetSpatialMoment, cvGetStarKeypoints, 
    cvGetSubRect, cvGetTextSize, cvGetThreadNum, cvGetTickCount, 
    cvGetTickFrequency, cvGoodFeaturesToTrack, cvGraphAddEdge, 
    cvGraphAddEdgeByPtr, cvGraphAddVtx, cvGraphEdgeIdx, cvGraphGetEdgeCount, 
    cvGraphGetVtxCount, cvGraphRemoveEdge, cvGraphRemoveEdgeByPtr, 
    cvGraphRemoveVtx, cvGraphRemoveVtxByPtr, cvGraphVtxDegree, 
    cvGraphVtxDegreeByPtr, cvGraphVtxIdx, cvGuiBoxReport, cvHaarDetectObjects, 
    cvHoughCirclesUntyped, cvHoughLinesUntyped, cvInRange, cvInRangeS, 
    cvIncRefData, cvInitFont, cvInitIntrinsicParams2D, cvInitLineIterator, 
    cvInitMatHeader, cvInitMatNDHeader, cvInitNArrayIterator, 
    cvInitSparseMatIterator, cvInitSubdivDelaunay2D, cvInitTreeNodeIterator, 
    cvInitUndistortMap, cvInitUndistortRectifyMap, cvInpaint, 
    cvInsertNodeIntoTree, cvIntegral, cvInvSqrt, cvInvert, cvIplDepth, 
    cvIsInf, cvIsNaN, cvKMeans2, cvKalmanCorrect, cvKalmanPredict, cvLSHAdd, 
    cvLSHQuery, cvLSHRemove, cvLUT, cvLaplace, cvLine, cvLinearPolar, cvLoad, 
    cvLoadHaarClassifierCascade, cvLog, cvLogPolar, cvMSERParams, 
    cvMahalanobis, cvMakeHistHeaderForArray, cvMakeSeqHeaderForArray, cvMat, 
    cvMatMul, cvMatMulAdd, cvMatchContourTrees, cvMatchShapes, 
    cvMatchTemplate, cvMax, cvMaxRect, cvMaxS, cvMeanShift, cvMemStorageAlloc, 
    cvMemStorageAllocString, cvMerge, cvMin, cvMinAreaRect2, 
    cvMinEnclosingCircle, cvMinMaxLoc, cvMinS, cvMixChannels, cvMoments, 
    cvMorphologyEx, cvMul, cvMulSpectrums, cvMulTransposed, cvMultiplyAcc, 
    cvNextGraphItem, cvNextNArraySlice, cvNextTreeNode, cvNorm, cvNormalize, 
    cvNormalizeHist, cvNot, cvNulDevReport, cvOpenFileStorage, cvOr, cvOrS, 
    cvPOSIT, cvPerspectiveTransform, cvPoint, cvPoint2D32f, cvPoint2D64f, 
    cvPoint3D32f, cvPoint3D64f, cvPointFrom32f, cvPointPolygonTest, 
    cvPointSeqFromMat, cvPointTo32f, cvPolarToCart, cvPolyLine, cvPow, 
    cvPreCornerDetect, cvPrevTreeNode, cvProjectPCA, cvProjectPoints2, 
    cvPtr1D, cvPtr2D, cvPtr3D, cvPtrND, cvPutText, cvPyrDown, 
    cvPyrMeanShiftFiltering, cvPyrSegmentationUntyped, cvPyrUp, 
    cvRANSACUpdateNumIters, cvRNG, cvROIToRect, cvRQDecomp3x3, cvRandArr, 
    cvRandInt, cvRandReal, cvRandShuffle, cvRange, cvRawDataToScalar, cvRead, 
    cvReadByName, cvReadChainPoint, cvReadInt, cvReadIntByName, cvReadRawData, 
    cvReadRawDataSlice, cvReadReal, cvReadRealByName, cvReadString, 
    cvReadStringByName, cvRealScalar, cvRect, cvRectToROI, cvRectangle, 
    cvRedirectError, cvReduce, cvRegisterModule, cvRegisterType, 
    cvReleaseData, cvReleaseFeatureTree, cvReleaseFileStorage, cvReleaseLSH, 
    cvReleasePOSITObject, cvReleasePyramid, cvReleaseStereoBMState, 
    cvReleaseStereoGCState, cvRemap, cvRemoveNodeFromTree, cvRepeat, 
    cvReprojectImageTo3D, cvResetImageROI, cvReshape, cvReshapeMatND, 
    cvReshapeND, cvResize, cvRestoreMemStoragePos, cvRodrigues2, cvRound, 
    cvRunHaarClassifierCascade, cvRunningAvg, cvSURFParams, cvSURFPoint, 
    cvSVBkSb, cvSVD, cvSampleLine, cvSave, cvSaveMemStoragePos, cvScalar, 
    cvScalarAll, cvScalarToRawData, cvScaleAdd, cvSegmentMotion, cvSeqElemIdx, 
    cvSeqInsert, cvSeqInsertSlice, cvSeqInvert, cvSeqPartition, cvSeqPop, 
    cvSeqPopFront, cvSeqPopMulti, cvSeqPush, cvSeqPushFront, cvSeqPushMulti, 
    cvSeqRemove, cvSeqRemoveSlice, cvSeqSearch, cvSeqSlice, cvSeqSort, cvSet, 
    cvSet1D, cvSet2D, cvSet3D, cvSetAdd, cvSetData, cvSetErrMode, 
    cvSetErrStatus, cvSetHistBinRanges, cvSetIPLAllocators, cvSetIdentity, 
    cvSetImageIOFunctions, cvSetImagesForHaarClassifierCascade, 
    cvSetMemoryManager, cvSetND, cvSetNew, cvSetNumThreads, cvSetReal1D, 
    cvSetReal2D, cvSetReal3D, cvSetRealND, cvSetRemove, cvSetRemoveByPtr, 
    cvSetSeqBlockSize, cvSetSeqReaderPos, cvSetZero, cvSize, cvSize2D32f, 
    cvSlice, cvSliceLength, cvSmooth, cvSnakeImage, cvSobel, cvSolve, 
    cvSolveCubic, cvSolvePoly, cvSort, cvSplit, cvSqrt, cvSquareAcc, 
    cvStarDetectorParams, cvStarKeypoint, cvStartAppendToSeq, 
    cvStartFindContours, cvStartNextStream, cvStartReadChainPoints, 
    cvStartReadRawData, cvStartReadSeq, cvStartWriteSeq, cvStartWriteStruct, 
    cvStdErrReport, cvStereoCalibrate, cvStereoRectify, 
    cvStereoRectifyUncalibrated, cvSub, cvSubRS, cvSubS, cvSubdiv2DEdgeDst, 
    cvSubdiv2DEdgeOrg, cvSubdiv2DGetEdge, cvSubdiv2DLocate, 
    cvSubdiv2DNextEdge, cvSubdiv2DRotateEdge, cvSubdiv2DSymEdge, 
    cvSubdivDelaunay2DInsert, cvSubstituteContour, cvSum, cvTermCriteria, 
    cvThreshHist, cvThreshold, cvTrace, cvTransform, cvTranspose, 
    cvTreeToNodeSeq, cvTriangleArea, cvTriangulatePoints, cvTypeOf, 
    cvUndistort2, cvUndistortPoints, cvUnregisterType, cvUpdateMotionHistory, 
    cvUseOptimized, cvWarpAffine, cvWarpPerspective, cvWatershed, cvWrite, 
    cvWriteComment, cvWriteFileNode, cvWriteInt, cvWriteRawData, cvWriteReal, 
    cvWriteString, cvXor, cvXorS, cvmGet, cvmSet, delete_Cv32suf, 
    delete_Cv64suf, delete_CvAttrList, delete_CvAvgComp, delete_CvBox2D, 
    delete_CvChain, delete_CvChainPtReader, delete_CvConDensation, 
    delete_CvConnectedComp, delete_CvContour, delete_CvContourTree, 
    delete_CvConvexityDefect, delete_CvFileNode, delete_CvFileNode_data, 
    delete_CvFont, delete_CvGraph, delete_CvGraphEdge, delete_CvGraphScanner, 
    delete_CvGraphVtx, delete_CvGraphVtx2D, delete_CvHaarClassifier, 
    delete_CvHaarClassifierCascade, delete_CvHaarFeature, 
    delete_CvHaarFeature_rect, delete_CvHaarStageClassifier, 
    delete_CvHistogram, delete_CvHuMoments, delete_CvImage, delete_CvKalman, 
    delete_CvLSH, delete_CvLineIterator, delete_CvMSERParams, delete_CvMat, 
    delete_CvMatND, delete_CvMatND_data, delete_CvMatND_dim, 
    delete_CvMat_data, delete_CvMatrix, delete_CvMatrix3, delete_CvMemBlock, 
    delete_CvMemStorage, delete_CvMemStoragePos, delete_CvModule, 
    delete_CvModuleInfo, delete_CvMoments, delete_CvNArrayIterator, 
    delete_CvPluginFuncInfo, delete_CvPoint, delete_CvPoint2D32f, 
    delete_CvPoint2D64f, delete_CvPoint3D32f, delete_CvPoint3D64f, 
    delete_CvPointVector, delete_CvQuadEdge2D, delete_CvRNG_Wrapper, 
    delete_CvRect, delete_CvSURFParams, delete_CvSURFPoint, delete_CvScalar, 
    delete_CvSeq, delete_CvSeqBlock, delete_CvSeqReader, delete_CvSeqWriter, 
    delete_CvSeq_CvConnectedComp, delete_CvSeq_CvPoint, 
    delete_CvSeq_CvPoint2D32f, delete_CvSeq_CvPoint_2, 
    delete_CvSeq_CvQuadEdge2D, delete_CvSeq_CvRect, delete_CvSeq_CvSeq, 
    delete_CvSeq_float_2, delete_CvSeq_float_3, delete_CvSet, 
    delete_CvSetElem, delete_CvSize, delete_CvSize2D32f, delete_CvSlice, 
    delete_CvSparseMat, delete_CvSparseMatIterator, delete_CvSparseNode, 
    delete_CvStarDetectorParams, delete_CvStarKeypoint, 
    delete_CvStereoBMState, delete_CvStereoGCState, delete_CvString, 
    delete_CvStringHashNode, delete_CvSubdiv2D, delete_CvSubdiv2DEdge_Wrapper, 
    delete_CvSubdiv2DPoint, delete_CvTermCriteria, delete_CvTreeNodeIterator, 
    delete_CvTuple_CvPoint_2, delete_CvTuple_float_2, delete_CvTuple_float_3, 
    delete_CvType, delete_CvTypeInfo, delete_FloatVector, 
    delete_IplConvKernel, delete_IplConvKernelFP, delete_IplImage, 
    delete_IplROI, delete_SwigPyIterator, function_ptr_generator, new_Cv32suf, 
    new_Cv64suf, new_CvAttrList, new_CvAvgComp, new_CvBox2D, new_CvChain, 
    new_CvChainPtReader, new_CvConnectedComp, new_CvContour, 
    new_CvContourTree, new_CvConvexityDefect, new_CvFileNode, 
    new_CvFileNode_data, new_CvFont, new_CvGraph, new_CvGraphEdge, 
    new_CvGraphVtx, new_CvGraphVtx2D, new_CvHaarClassifier, new_CvHaarFeature, 
    new_CvHaarFeature_rect, new_CvHaarStageClassifier, new_CvHuMoments, 
    new_CvImage, new_CvLineIterator, new_CvMSERParams, new_CvMatND_data, 
    new_CvMatND_dim, new_CvMat_data, new_CvMatrix, new_CvMatrix3, 
    new_CvMemBlock, new_CvMemStoragePos, new_CvModule, new_CvModuleInfo, 
    new_CvMoments, new_CvNArrayIterator, new_CvPluginFuncInfo, new_CvPoint, 
    new_CvPoint2D32f, new_CvPoint2D64f, new_CvPoint3D32f, new_CvPoint3D64f, 
    new_CvPointVector, new_CvQuadEdge2D, new_CvRNG_Wrapper, new_CvRect, 
    new_CvSURFParams, new_CvSURFPoint, new_CvScalar, new_CvSeq, 
    new_CvSeqBlock, new_CvSeqReader, new_CvSeqWriter, 
    new_CvSeq_CvConnectedComp, new_CvSeq_CvPoint, new_CvSeq_CvPoint2D32f, 
    new_CvSeq_CvPoint_2, new_CvSeq_CvQuadEdge2D, new_CvSeq_CvRect, 
    new_CvSeq_CvSeq, new_CvSeq_float_2, new_CvSeq_float_3, new_CvSet, 
    new_CvSetElem, new_CvSize, new_CvSize2D32f, new_CvSlice, 
    new_CvSparseMatIterator, new_CvSparseNode, new_CvStarDetectorParams, 
    new_CvStarKeypoint, new_CvStereoBMState, new_CvStereoGCState, 
    new_CvString, new_CvStringHashNode, new_CvSubdiv2D, 
    new_CvSubdiv2DEdge_Wrapper, new_CvSubdiv2DPoint, new_CvTermCriteria, 
    new_CvTreeNodeIterator, new_CvTuple_CvPoint_2, new_CvTuple_float_2, 
    new_CvTuple_float_3, new_CvType, new_CvTypeInfo, new_FloatVector, 
    new_IplConvKernelFP, new_IplROI, void_ptr_generator, 
    void_ptrptr_generator)


# Variables with simple values

CV_16S = 3
CV_16SC1 = 3
CV_16SC2 = 11
CV_16SC3 = 19
CV_16SC4 = 27
CV_16U = 2
CV_16UC1 = 2
CV_16UC2 = 10
CV_16UC3 = 18
CV_16UC4 = 26
CV_32F = 5
CV_32FC1 = 5
CV_32FC2 = 13
CV_32FC3 = 21
CV_32FC4 = 29
CV_32S = 4
CV_32SC1 = 4
CV_32SC2 = 12
CV_32SC3 = 20
CV_32SC4 = 28
CV_64F = 6
CV_64FC1 = 6
CV_64FC2 = 14
CV_64FC3 = 22
CV_64FC4 = 30
CV_8S = 1
CV_8SC1 = 1
CV_8SC2 = 9
CV_8SC3 = 17
CV_8SC4 = 25
CV_8U = 0
CV_8UC1 = 0
CV_8UC2 = 8
CV_8UC3 = 16
CV_8UC4 = 24
CV_AA = 16

CV_ADAPTIVE_THRESH_GAUSSIAN_C = 1

CV_ADAPTIVE_THRESH_MEAN_C = 0

CV_ARRAY = 2
CV_AUTOSTEP = 2147483647

CV_AUTO_STEP = 2147483647

CV_BACK = 0
CV_BadAlign = -21
CV_BadAlphaChannel = -18
CV_BadCallBack = -22
CV_BadCOI = -24
CV_BadDataPtr = -12
CV_BadDepth = -17
CV_BadImageSize = -10
CV_BadModelOrChSeq = -14
CV_BadNumChannel1U = -16
CV_BadNumChannels = -15
CV_BadOffset = -11
CV_BadOrder = -19
CV_BadOrigin = -20
CV_BadROISize = -25
CV_BadStep = -13
CV_BadTileSize = -23
CV_BayerBG2BGR = 46
CV_BayerBG2RGB = 48
CV_BayerGB2BGR = 47
CV_BayerGB2RGB = 49
CV_BayerGR2BGR = 49
CV_BayerGR2RGB = 47
CV_BayerRG2BGR = 48
CV_BayerRG2RGB = 46
CV_BGR2BGR555 = 22
CV_BGR2BGR565 = 12
CV_BGR2BGRA = 0
CV_BGR2GRAY = 6
CV_BGR2HLS = 52
CV_BGR2HSV = 40
CV_BGR2Lab = 44
CV_BGR2Luv = 50
CV_BGR2RGB = 4
CV_BGR2RGBA = 2
CV_BGR2XYZ = 32
CV_BGR2YCrCb = 36
CV_BGR5552BGR = 24
CV_BGR5552BGRA = 28
CV_BGR5552GRAY = 31
CV_BGR5552RGB = 25
CV_BGR5552RGBA = 29
CV_BGR5652BGR = 14
CV_BGR5652BGRA = 18
CV_BGR5652GRAY = 21
CV_BGR5652RGB = 15
CV_BGR5652RGBA = 19
CV_BGRA2BGR = 1
CV_BGRA2BGR555 = 26
CV_BGRA2BGR565 = 16
CV_BGRA2GRAY = 10
CV_BGRA2RGB = 3
CV_BGRA2RGBA = 5
CV_BILATERAL = 4
CV_BLUR = 1

CV_BLUR_NO_SCALE = 0

CV_C = 1

CV_CALIB_CB_ADAPTIVE_THRESH = 1

CV_CALIB_CB_FILTER_QUADS = 4

CV_CALIB_CB_NORMALIZE_IMAGE = 2

CV_CALIB_FIX_ASPECT_RATIO = 2

CV_CALIB_FIX_FOCAL_LENGTH = 16

CV_CALIB_FIX_INTRINSIC = 256
CV_CALIB_FIX_K1 = 32
CV_CALIB_FIX_K2 = 64
CV_CALIB_FIX_K3 = 128

CV_CALIB_FIX_PRINCIPAL_POINT = 4

CV_CALIB_SAME_FOCAL_LENGTH = 512

CV_CALIB_USE_INTRINSIC_GUESS = 1

CV_CALIB_ZERO_DISPARITY = 1024

CV_CALIB_ZERO_TANGENT_DIST = 8

CV_CANNY_L2_GRADIENT = -2147483648

CV_CHAIN_APPROX_NONE = 1
CV_CHAIN_APPROX_SIMPLE = 2

CV_CHAIN_APPROX_TC89_KCOS = 4
CV_CHAIN_APPROX_TC89_L1 = 3

CV_CHAIN_CODE = 0

CV_CHECK_QUIET = 2
CV_CHECK_RANGE = 1

CV_CHOLESKY = 3
CV_CLOCKWISE = 1

CV_CMP_EQ = 0
CV_CMP_GE = 2
CV_CMP_GT = 1
CV_CMP_LE = 4
CV_CMP_LT = 3
CV_CMP_NE = 5

CV_CN_MAX = 64
CV_CN_SHIFT = 3

CV_COLORCVT_MAX = 100

CV_COMP_BHATTACHARYYA = 3
CV_COMP_CHISQR = 1
CV_COMP_CORREL = 0
CV_COMP_INTERSECT = 2

CV_CONTOURS_MATCH_I1 = 1
CV_CONTOURS_MATCH_I2 = 2
CV_CONTOURS_MATCH_I3 = 3

CV_CONTOUR_TREES_MATCH_I1 = 1

CV_COUNTER_CLOCKWISE = 2

CV_COVAR_COLS = 16
CV_COVAR_NORMAL = 1
CV_COVAR_ROWS = 8
CV_COVAR_SCALE = 4
CV_COVAR_SCRAMBLED = 0

CV_COVAR_USE_AVG = 2

CV_DEPTH_MAX = 8

CV_DIFF = 16

CV_DIFF_C = 17
CV_DIFF_L1 = 18
CV_DIFF_L2 = 20

CV_DIST_C = 3
CV_DIST_FAIR = 5
CV_DIST_HUBER = 7
CV_DIST_L1 = 1
CV_DIST_L12 = 4
CV_DIST_L2 = 2

CV_DIST_MASK_3 = 3
CV_DIST_MASK_5 = 5
CV_DIST_MASK_PRECISE = 0

CV_DIST_USER = -1
CV_DIST_WELSCH = 6

CV_DOMINANT_IPAN = 1

CV_DXT_FORWARD = 0
CV_DXT_INVERSE = 1

CV_DXT_INVERSE_SCALE = 3

CV_DXT_INV_SCALE = 3

CV_DXT_MUL_CONJ = 8

CV_DXT_ROWS = 4
CV_DXT_SCALE = 2

CV_ErrModeLeaf = 0
CV_ErrModeParent = 1
CV_ErrModeSilent = 2
CV_FILLED = -1

CV_FLOODFILL_FIXED_RANGE = 65536

CV_FLOODFILL_MASK_ONLY = 131072

CV_FM_7POINT = 1
CV_FM_8POINT = 2
CV_FM_LMEDS = 4

CV_FM_LMEDS_ONLY = 4

CV_FM_RANSAC = 8

CV_FM_RANSAC_ONLY = 8

CV_FONT_HERSHEY_COMPLEX = 3

CV_FONT_HERSHEY_COMPLEX_SMALL = 5

CV_FONT_HERSHEY_DUPLEX = 2
CV_FONT_HERSHEY_PLAIN = 1

CV_FONT_HERSHEY_SCRIPT_COMPLEX = 7
CV_FONT_HERSHEY_SCRIPT_SIMPLEX = 6

CV_FONT_HERSHEY_SIMPLEX = 0
CV_FONT_HERSHEY_TRIPLEX = 4

CV_FONT_ITALIC = 16
CV_FONT_VECTOR0 = 0

CV_FRONT = 1
CV_GAUSSIAN = 2

CV_GAUSSIAN_5x5 = 7

CV_GEMM_A_T = 1

CV_GEMM_B_T = 2

CV_GEMM_C_T = 4

CV_GRAPH = 1536

CV_GRAPH_ALL_ITEMS = -1

CV_GRAPH_ANY_EDGE = 30

CV_GRAPH_BACKTRACKING = 64

CV_GRAPH_BACK_EDGE = 4

CV_GRAPH_CROSS_EDGE = 16

CV_GRAPH_FLAG_ORIENTED = 4096

CV_GRAPH_FORWARD_EDGE = 8

CV_GRAPH_FORWARD_EDGE_FLAG = 268435456

CV_GRAPH_ITEM_VISITED_FLAG = 1073741824

CV_GRAPH_NEW_TREE = 32

CV_GRAPH_OVER = -1

CV_GRAPH_SEARCH_TREE_NODE_FLAG = 536870912

CV_GRAPH_TREE_EDGE = 2

CV_GRAPH_VERTEX = 1

CV_GRAY2BGR = 8
CV_GRAY2BGR555 = 30
CV_GRAY2BGR565 = 20
CV_GRAY2BGRA = 9
CV_GRAY2RGB = 8
CV_GRAY2RGBA = 9

CV_HAAR_DO_CANNY_PRUNING = 1

CV_HAAR_DO_ROUGH_SEARCH = 8

CV_HAAR_FEATURE_MAX = 3

CV_HAAR_FIND_BIGGEST_OBJECT = 4

CV_HAAR_MAGIC_VAL = 1112539136

CV_HAAR_SCALE_IMAGE = 2

CV_HeaderIsNull = -9

CV_HIST_ARRAY = 0

CV_HIST_MAGIC_VAL = 1111818240

CV_HIST_RANGES_FLAG = 2048

CV_HIST_SPARSE = 1
CV_HIST_TREE = 1
CV_HIST_UNIFORM = 1

CV_HIST_UNIFORM_FLAG = 1024

CV_HLS2BGR = 60
CV_HLS2RGB = 61

CV_HOUGH_GRADIENT = 3

CV_HOUGH_MULTI_SCALE = 2

CV_HOUGH_PROBABILISTIC = 1
CV_HOUGH_STANDARD = 0

CV_HSV2BGR = 54
CV_HSV2RGB = 55

CV_INPAINT_NS = 0
CV_INPAINT_TELEA = 1

CV_INTER_AREA = 3
CV_INTER_CUBIC = 2
CV_INTER_LINEAR = 1
CV_INTER_NN = 0

CV_KMEANS_USE_INITIAL_LABELS = 1

CV_L1 = 2
CV_L2 = 4
CV_Lab2BGR = 56
CV_Lab2RGB = 57

CV_LINK_RUNS = 5

CV_LKFLOW_GET_MIN_EIGENVALS = 8

CV_LKFLOW_INITIAL_GUESSES = 4

CV_LKFLOW_PYR_A_READY = 1

CV_LKFLOW_PYR_B_READY = 2

CV_LMEDS = 4
CV_LOG2 = 0.69314718055994529
CV_LU = 0
CV_Luv2BGR = 58
CV_Luv2RGB = 59

CV_MAGIC_MASK = -65536

CV_MAJOR_VERSION = 2

CV_MaskIsTiled = -26

CV_MATND_MAGIC_VAL = 1111687168

CV_MAT_CN_MASK = 504

CV_MAT_CONT_FLAG = 16384

CV_MAT_CONT_FLAG_SHIFT = 14

CV_MAT_DEPTH_MASK = 7

CV_MAT_MAGIC_VAL = 1111621632

CV_MAT_TEMP_FLAG = 32768

CV_MAT_TEMP_FLAG_SHIFT = 15

CV_MAT_TYPE_MASK = 511

CV_MAX_ARR = 10
CV_MAX_DIM = 32

CV_MAX_DIM_HEAP = 65536

CV_MAX_SOBEL_KSIZE = 7

CV_MEDIAN = 3
CV_MINMAX = 32

CV_MINOR_VERSION = 0

CV_MOP_BLACKHAT = 6
CV_MOP_CLOSE = 3
CV_MOP_GRADIENT = 4
CV_MOP_OPEN = 2
CV_MOP_TOPHAT = 5

CV_NEXT_AROUND_DST = 34
CV_NEXT_AROUND_LEFT = 19
CV_NEXT_AROUND_ORG = 0
CV_NEXT_AROUND_RIGHT = 49

CV_NODE_EMPTY = 32
CV_NODE_FLOAT = 2
CV_NODE_FLOW = 8
CV_NODE_INT = 1
CV_NODE_INTEGER = 1
CV_NODE_MAP = 6
CV_NODE_NAMED = 64
CV_NODE_NONE = 0
CV_NODE_REAL = 2
CV_NODE_REF = 4
CV_NODE_SEQ = 5

CV_NODE_SEQ_SIMPLE = 256

CV_NODE_STR = 3
CV_NODE_STRING = 3

CV_NODE_TYPE_MASK = 7

CV_NODE_USER = 16

CV_NORMAL = 16

CV_NORM_MASK = 7

CV_NO_CN_CHECK = 2

CV_NO_DEPTH_CHECK = 1

CV_NO_SIZE_CHECK = 4

CV_ORIENTED_GRAPH = 5632

CV_PCA_DATA_AS_COL = 1
CV_PCA_DATA_AS_ROW = 0

CV_PCA_USE_AVG = 2

CV_PI = 3.1415926535897931

CV_POLY_APPROX_DP = 0

CV_PREV_AROUND_DST = 51
CV_PREV_AROUND_LEFT = 32
CV_PREV_AROUND_ORG = 17
CV_PREV_AROUND_RIGHT = 2

CV_PTLOC_ERROR = -2
CV_PTLOC_INSIDE = 0

CV_PTLOC_ON_EDGE = 2

CV_PTLOC_OUTSIDE_RECT = -1

CV_PTLOC_VERTEX = 1

CV_QR = 4

CV_RAND_NORMAL = 1
CV_RAND_UNI = 0

CV_RANSAC = 8

CV_REDUCE_AVG = 1
CV_REDUCE_MAX = 2
CV_REDUCE_MIN = 3
CV_REDUCE_SUM = 0

CV_RELATIVE = 8

CV_RELATIVE_C = 9
CV_RELATIVE_L1 = 10
CV_RELATIVE_L2 = 12

CV_RETR_CCOMP = 2
CV_RETR_EXTERNAL = 0
CV_RETR_LIST = 1
CV_RETR_TREE = 3

CV_RGB2BGR = 4
CV_RGB2BGR555 = 23
CV_RGB2BGR565 = 13
CV_RGB2BGRA = 2
CV_RGB2GRAY = 7
CV_RGB2HLS = 53
CV_RGB2HSV = 41
CV_RGB2Lab = 45
CV_RGB2Luv = 51
CV_RGB2RGBA = 0
CV_RGB2XYZ = 33
CV_RGB2YCrCb = 37
CV_RGBA2BGR = 3
CV_RGBA2BGR555 = 27
CV_RGBA2BGR565 = 17
CV_RGBA2BGRA = 5
CV_RGBA2GRAY = 11
CV_RGBA2RGB = 1
CV_SCHARR = -1

CV_SEQ_CHAIN = 512

CV_SEQ_CHAIN_CONTOUR = 4608

CV_SEQ_CONNECTED_COMP = 0

CV_SEQ_CONTOUR = 4620

CV_SEQ_ELTYPE_BITS = 9
CV_SEQ_ELTYPE_CODE = 0

CV_SEQ_ELTYPE_CONNECTED_COMP = 0

CV_SEQ_ELTYPE_GENERIC = 0

CV_SEQ_ELTYPE_GRAPH_EDGE = 0
CV_SEQ_ELTYPE_GRAPH_VERTEX = 0

CV_SEQ_ELTYPE_INDEX = 4
CV_SEQ_ELTYPE_MASK = 511
CV_SEQ_ELTYPE_POINT = 12
CV_SEQ_ELTYPE_POINT3D = 21
CV_SEQ_ELTYPE_PPOINT = 7
CV_SEQ_ELTYPE_PTR = 7

CV_SEQ_ELTYPE_TRIAN_ATR = 0

CV_SEQ_FLAG_CLOSED = 4096
CV_SEQ_FLAG_CONVEX = 16384
CV_SEQ_FLAG_HOLE = 32768
CV_SEQ_FLAG_SHIFT = 12
CV_SEQ_FLAG_SIMPLE = 8192

CV_SEQ_INDEX = 4

CV_SEQ_KIND_BIN_TREE = 1024

CV_SEQ_KIND_BITS = 3
CV_SEQ_KIND_CURVE = 512
CV_SEQ_KIND_GENERIC = 0
CV_SEQ_KIND_GRAPH = 1536
CV_SEQ_KIND_MASK = 3584
CV_SEQ_KIND_SUBDIV2D = 2048

CV_SEQ_MAGIC_VAL = 1117323264

CV_SEQ_POINT3D_SET = 21

CV_SEQ_POINT_SET = 12

CV_SEQ_POLYGON = 4620

CV_SEQ_POLYGON_TREE = 1024

CV_SEQ_POLYLINE = 524

CV_SEQ_SIMPLE_POLYGON = 12812

CV_SET_ELEM_IDX_MASK = 67108863

CV_SET_MAGIC_VAL = 1117257728

CV_SHAPE_CROSS = 1
CV_SHAPE_CUSTOM = 100
CV_SHAPE_ELLIPSE = 2
CV_SHAPE_RECT = 0

CV_SORT_ASCENDING = 0
CV_SORT_DESCENDING = 16

CV_SORT_EVERY_COLUMN = 1
CV_SORT_EVERY_ROW = 0

CV_SPARSE_MAT_MAGIC_VAL = 1111752704

CV_STEREO_BM_BASIC = 0

CV_STEREO_BM_FISH_EYE = 1

CV_STEREO_BM_NARROW = 2

CV_STEREO_BM_NORMALIZED_RESPONSE = 0

CV_STORAGE_APPEND = 2

CV_STORAGE_MAGIC_VAL = 1116274688

CV_STORAGE_READ = 0
CV_STORAGE_WRITE = 1

CV_STORAGE_WRITE_BINARY = 1
CV_STORAGE_WRITE_TEXT = 1

CV_StsAssert = -215
CV_StsAutoTrace = -8
CV_StsBackTrace = -1
CV_StsBadArg = -5
CV_StsBadFlag = -206
CV_StsBadFunc = -6
CV_StsBadMask = -208
CV_StsBadMemBlock = -214
CV_StsBadPoint = -207
CV_StsBadSize = -201
CV_StsDivByZero = -202
CV_StsError = -2
CV_StsFilterOffsetErr = -31
CV_StsFilterStructContentErr = -29
CV_StsInplaceNotSupported = -203
CV_StsInternal = -3
CV_StsKernelStructContentErr = -30
CV_StsNoConv = -7
CV_StsNoMem = -4
CV_StsNotImplemented = -213
CV_StsNullPtr = -27
CV_StsObjectNotFound = -204
CV_StsOk = 0
CV_StsOutOfRange = -211
CV_StsParseError = -212
CV_StsUnmatchedFormats = -205
CV_StsUnmatchedSizes = -209
CV_StsUnsupportedFormat = -210
CV_StsVecLengthErr = -28

CV_SUBDIV2D_VIRTUAL_POINT_FLAG = 1073741824

CV_SUBMINOR_VERSION = 0

CV_SVD = 1

CV_SVD_MODIFY_A = 1

CV_SVD_SYM = 2

CV_SVD_U_T = 2

CV_SVD_V_T = 4

CV_TERMCRIT_EPS = 2
CV_TERMCRIT_ITER = 1
CV_TERMCRIT_NUMBER = 1

CV_THRESH_BINARY = 0

CV_THRESH_BINARY_INV = 1

CV_THRESH_MASK = 7
CV_THRESH_OTSU = 8
CV_THRESH_TOZERO = 3

CV_THRESH_TOZERO_INV = 4

CV_THRESH_TRUNC = 2

CV_TM_CCOEFF = 4

CV_TM_CCOEFF_NORMED = 5

CV_TM_CCORR = 2

CV_TM_CCORR_NORMED = 3

CV_TM_SQDIFF = 0

CV_TM_SQDIFF_NORMED = 1

CV_TYPE_NAME_GRAPH = 'opencv-graph'
CV_TYPE_NAME_HAAR = 'opencv-haar-classifier'
CV_TYPE_NAME_IMAGE = 'opencv-image'
CV_TYPE_NAME_MAT = 'opencv-matrix'
CV_TYPE_NAME_MATND = 'opencv-nd-matrix'
CV_TYPE_NAME_SEQ = 'opencv-sequence'

CV_TYPE_NAME_SEQ_TREE = 'opencv-sequence-tree'

CV_TYPE_NAME_SPARSE_MAT = 'opencv-sparse-matrix'

CV_USRTYPE1 = 7
CV_VALUE = 1

CV_WARP_FILL_OUTLIERS = 8

CV_WARP_INVERSE_MAP = 16

CV_WHOLE_SEQ_END_INDEX = 1073741823

CV_XYZ2BGR = 34
CV_XYZ2RGB = 35
CV_YCrCb2BGR = 38
CV_YCrCb2RGB = 39

IPL_ALIGN_16BYTES = 16
IPL_ALIGN_32BYTES = 32
IPL_ALIGN_4BYTES = 4
IPL_ALIGN_8BYTES = 8
IPL_ALIGN_DWORD = 4
IPL_ALIGN_QWORD = 8

IPL_BORDER_CONSTANT = 0
IPL_BORDER_REFLECT = 2

IPL_BORDER_REFLECT_101 = 4

IPL_BORDER_REPLICATE = 1
IPL_BORDER_WRAP = 3

IPL_DATA_ORDER_PIXEL = 0
IPL_DATA_ORDER_PLANE = 1

IPL_DEPTH_16S = -2147483632
IPL_DEPTH_16U = 16
IPL_DEPTH_1U = 1
IPL_DEPTH_32F = 32
IPL_DEPTH_32S = -2147483616
IPL_DEPTH_64F = 64
IPL_DEPTH_8S = -2147483640
IPL_DEPTH_8U = 8
IPL_DEPTH_SIGN = -2147483648

IPL_IMAGE_DATA = 2
IPL_IMAGE_HEADER = 1
IPL_IMAGE_ROI = 4

IPL_ORIGIN_BL = 1
IPL_ORIGIN_TL = 0

sizeof_CvContour = 128
sizeof_CvPoint = 8
sizeof_CvSeq = 96

# no functions
# no classes
# variables with complex values

cvar = None # (!) real value is ''

