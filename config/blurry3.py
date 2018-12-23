    augmentation_config.add_table_lines_params = {
        'add_line_prob': 0.5, 'max_line_thickness': 4}
    augmentation_config.rotate_image_params = {'max_angel': 2}
    augmentation_config.affine_transform_shear_params = {'a': 2}
    augmentation_config.affine_transform_change_aspect_ratio_params = {
        'ratio': 0.9}
    augmentation_config.brighten_image_params = {'min_alpha': 0.6}
    augmentation_config.darken_image_params = {'min_alpha': 0.6}
    augmentation_config.add_color_filter_params = {'min_alpha': 0.6}
    augmentation_config.add_random_noise_params = {
        'min_masks': 70, 'max_masks': 80}
    augmentation_config.add_color_font_effect_params = {
        'beta': 0.6, 'max_num_lines': 60}
    augmentation_config.add_erode_edge_effect_params = {
        'kernel_size': (3, 3), 'max_sigmaX': 3}
    augmentation_config.add_resize_blur_effect_params = {
        'resize_ratio_range': (0.8, 1)}
    augmentation_config.add_gaussian_blur_effect_params = {
        'kernel_size': (3, 3), 'max_sigmaX': 3}
    augmentation_config.add_horizontal_motion_blur_effect_params = {
        'min_kernel_size': 3, 'max_kernel_size': 6}
    augmentation_config.add_vertical_motion_blur_effect_params = {
        'min_kernel_size': 3, 'max_kernel_size': 6}
    augmentation_config.add_random_circles_params = {
        'min_alpha': 0.6, 'max_num_circles': 18}
    augmentation_config.add_random_lines_params = {
        'min_alpha': 0.6, 'max_num_lines': 18}
