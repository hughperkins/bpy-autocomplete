import sys


def brush_stroke(stroke=None, mode='NORMAL', ignore_background_click=False):
    pass


def cloth_filter(start_mouse=(0, 0), area_normal_radius=0.25, strength=1.0, iteration_count=1, event_history=None, type='GRAVITY', force_axis={'X', 'Y', 'Z'}, orientation='LOCAL', cloth_mass=1.0, cloth_damping=0.0, use_face_sets=False, use_collisions=False):
    pass


def color_filter(start_mouse=(0, 0), area_normal_radius=0.25, strength=1.0, iteration_count=1, event_history=None, type='FILL', fill_color=(1.0, 1.0, 1.0)):
    pass


def detail_flood_fill():
    pass


def dynamic_topology_toggle():
    pass


def dyntopo_detail_size_edit():
    pass


def expand(target='MASK', falloff_type='GEODESIC', invert=False, use_mask_preserve=False, use_falloff_gradient=False, use_modify_active=False, use_reposition_pivot=True, max_geodesic_move_preview=10000, use_auto_mask=False, normal_falloff_smooth=2):
    pass


def face_set_box_gesture(xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True, use_front_faces_only=False, use_limit_to_segment=False):
    pass


def face_set_change_visibility(mode='TOGGLE'):
    pass


def face_set_edit(active_face_set=1, mode='GROW', strength=1.0, modify_hidden=True):
    pass


def face_set_invert_visibility():
    pass


def face_set_lasso_gesture(path=None, use_front_faces_only=False, use_limit_to_segment=False):
    pass


def face_sets_create(mode='MASKED'):
    pass


def face_sets_init(mode='LOOSE_PARTS', threshold=0.5):
    pass


def face_sets_randomize_colors():
    pass


def mask_by_color(contiguous=False, invert=False, preserve_previous_mask=False, threshold=0.35):
    pass


def mask_filter(filter_type='SMOOTH', iterations=1, auto_iteration_count=True):
    pass


def mask_from_cavity(mix_mode='MIX', mix_factor=1.0, settings_source='OPERATOR', factor=0.5, blur_steps=2, use_curve=False, invert=False):
    pass


def mask_init(mode='RANDOM_PER_VERTEX'):
    pass


def mesh_filter(start_mouse=(0, 0), area_normal_radius=0.25, strength=1.0, iteration_count=1, event_history=None, type='INFLATE', deform_axis={'X', 'Y', 'Z'}, orientation='LOCAL', surface_smooth_shape_preservation=0.5, surface_smooth_current_vertex=0.5, sharpen_smooth_ratio=0.35, sharpen_intensify_detail_strength=0.0, sharpen_curvature_smooth_iterations=0):
    pass


def optimize():
    pass


def project_line_gesture(xstart=0, xend=0, ystart=0, yend=0, flip=False, cursor=5, use_front_faces_only=False, use_limit_to_segment=False):
    pass


def reveal_all():
    pass


def sample_color():
    pass


def sample_detail_size(location=(0, 0), mode='DYNTOPO'):
    pass


def sculptmode_toggle():
    pass


def set_detail_size():
    pass


def set_persistent_base():
    pass


def set_pivot_position(mode='UNMASKED', mouse_x=0.0, mouse_y=0.0):
    pass


def symmetrize(merge_tolerance=0.0005):
    pass


def trim_box_gesture(xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True, use_front_faces_only=False, use_limit_to_segment=False, trim_mode='DIFFERENCE', use_cursor_depth=False, trim_orientation='VIEW', trim_extrude_mode='FIXED'):
    pass


def trim_lasso_gesture(path=None, use_front_faces_only=False, use_limit_to_segment=False, trim_mode='DIFFERENCE', use_cursor_depth=False, trim_orientation='VIEW', trim_extrude_mode='FIXED'):
    pass


def uv_sculpt_stroke(mode='NORMAL'):
    pass


