import sys


def active_frame_delete():
    pass


def active_frames_delete_all():
    pass


def annotate(mode='DRAW', arrowstyle_start='NONE', arrowstyle_end='NONE', use_stabilizer=False, stabilizer_factor=0.75, stabilizer_radius=35, stroke=None, wait_for_input=True):
    pass


def annotation_active_frame_delete():
    pass


def annotation_add():
    pass


def bake_grease_pencil_animation(frame_start=1, frame_end=250, step=1, only_selected=False, frame_target=1, project_type='KEEP'):
    pass


def bake_mesh_animation(target='NEW', frame_start=1, frame_end=250, step=1, thickness=1, angle=1.22173, offset=0.001, seams=False, faces=True, only_selected=False, frame_target=1, project_type='VIEW'):
    pass


def blank_frame_add(all_layers=False):
    pass


def brush_reset():
    pass


def brush_reset_all():
    pass


def convert(type='PATH', bevel_depth=0.0, bevel_resolution=0, use_normalize_weights=True, radius_multiplier=1.0, use_link_strokes=False, timing_mode='FULL', frame_range=100, start_frame=1, use_realtime=False, end_frame=250, gap_duration=0.0, gap_randomness=0.0, seed=0, use_timing_data=False):
    pass


def convert_old_files(annotation=False):
    pass


def copy():
    pass


def data_unlink():
    pass


def delete(type='POINTS'):
    pass


def dissolve(type='POINTS'):
    pass


def draw(mode='DRAW', stroke=None, wait_for_input=True, disable_straight=False, disable_fill=False, disable_stabilizer=False, guide_last_angle=0.0):
    pass


def duplicate():
    pass


def duplicate_move(GPENCIL_OT_duplicate=None, TRANSFORM_OT_translate=None):
    pass


def editmode_toggle(back=False):
    pass


def extract_palette_vertex(selected=False, threshold=1):
    pass


def extrude():
    pass


def extrude_move(GPENCIL_OT_extrude=None, TRANSFORM_OT_translate=None):
    pass


def fill(on_back=False):
    pass


def frame_clean_duplicate(type='ALL'):
    pass


def frame_clean_fill(mode='ACTIVE'):
    pass


def frame_clean_loose(limit=1):
    pass


def frame_duplicate(mode='ACTIVE'):
    pass


def generate_weights(mode='NAME', armature='DEFAULT', ratio=0.1, decay=0.8):
    pass


def guide_rotate(increment=True, angle=0.0):
    pass


def hide(unselected=False):
    pass


def image_to_grease_pencil(size=0.005, mask=False):
    pass


def interpolate(shift=0.0, layers='ACTIVE', interpolate_selected_only=False, exclude_breakdowns=False, flip='AUTO', smooth_steps=1, smooth_factor=0.0, release_confirm=False):
    pass


def interpolate_reverse():
    pass


def interpolate_sequence(step=1, layers='ACTIVE', interpolate_selected_only=False, exclude_breakdowns=False, flip='AUTO', smooth_steps=1, smooth_factor=0.0, type='LINEAR', easing='AUTO', back=1.702, amplitude=0.15, period=0.15):
    pass


def layer_active(layer=0):
    pass


def layer_add(layer=0, new_layer_name=""):
    pass


def layer_annotation_add():
    pass


def layer_annotation_move(type='UP'):
    pass


def layer_annotation_remove():
    pass


def layer_change(layer='DEFAULT'):
    pass


def layer_duplicate(mode='ALL'):
    pass


def layer_duplicate_object(mode='ALL', only_active=True):
    pass


def layer_isolate(affect_visibility=False):
    pass


def layer_mask_add(name=""):
    pass


def layer_mask_move(type='UP'):
    pass


def layer_mask_remove():
    pass


def layer_merge(mode='ACTIVE'):
    pass


def layer_move(type='UP'):
    pass


def layer_remove():
    pass


def lock_all():
    pass


def lock_layer():
    pass


def material_hide(unselected=False):
    pass


def material_isolate(affect_visibility=False):
    pass


def material_lock_all():
    pass


def material_lock_unused():
    pass


def material_reveal():
    pass


def material_select(deselect=False):
    pass


def material_set(slot='DEFAULT'):
    pass


def material_to_vertex_color(remove=True, palette=True, selected=False, threshold=3):
    pass


def material_unlock_all():
    pass


def materials_copy_to_object(only_active=True):
    pass


def move_to_layer(layer=0, new_layer_name=""):
    pass


def paintmode_toggle(back=False):
    pass


def paste(type='ACTIVE', paste_back=False):
    pass


def primitive_box(subdivision=3, edges=1, type='BOX', wait_for_input=True):
    pass


def primitive_circle(subdivision=94, edges=1, type='CIRCLE', wait_for_input=True):
    pass


def primitive_curve(subdivision=62, edges=1, type='CURVE', wait_for_input=True):
    pass


def primitive_line(subdivision=6, edges=1, type='LINE', wait_for_input=True):
    pass


def primitive_polyline(subdivision=6, edges=1, type='POLYLINE', wait_for_input=True):
    pass


def recalc_geometry():
    pass


def reproject(type='VIEW', keep_original=False, offset=0.0):
    pass


def reset_transform_fill(mode='ALL'):
    pass


def reveal(select=True):
    pass


def sculpt_paint(stroke=None, wait_for_input=True):
    pass


def sculptmode_toggle(back=False):
    pass


def segment_add(modifier=""):
    pass


def segment_move(modifier="", type='UP'):
    pass


def segment_remove(modifier="", index=0):
    pass


def select(extend=False, deselect=False, toggle=False, deselect_all=False, select_passthrough=False, entire_strokes=False, location=(0, 0), use_shift_extend=False):
    pass


def select_all(action='TOGGLE'):
    pass


def select_alternate(unselect_ends=False):
    pass


def select_box(xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True, mode='SET'):
    pass


def select_circle(x=0, y=0, radius=25, wait_for_input=True, mode='SET'):
    pass


def select_first(only_selected_strokes=False, extend=False):
    pass


def select_grouped(type='LAYER'):
    pass


def select_lasso(mode='SET', path=None):
    pass


def select_last(only_selected_strokes=False, extend=False):
    pass


def select_less():
    pass


def select_linked():
    pass


def select_more():
    pass


def select_random(ratio=0.5, seed=0, action='SELECT', unselect_ends=False):
    pass


def select_vertex_color(threshold=0):
    pass


def selection_opacity_toggle():
    pass


def selectmode_toggle(mode=0):
    pass


def set_active_material():
    pass


def snap_cursor_to_selected():
    pass


def snap_to_cursor(use_offset=True):
    pass


def snap_to_grid():
    pass


def stroke_apply_thickness():
    pass


def stroke_arrange(direction='UP'):
    pass


def stroke_caps_set(type='TOGGLE'):
    pass


def stroke_change_color(material=""):
    pass


def stroke_cutter(path=None, flat_caps=False):
    pass


def stroke_cyclical_set(type='TOGGLE', geometry=False):
    pass


def stroke_editcurve_set_handle_type(type='AUTOMATIC'):
    pass


def stroke_enter_editcurve_mode(error_threshold=0.1):
    pass


def stroke_flip():
    pass


def stroke_join(type='JOIN', leave_gaps=False):
    pass


def stroke_merge(mode='STROKE', back=False, additive=False, cyclic=False, clear_point=False, clear_stroke=False):
    pass


def stroke_merge_by_distance(threshold=0.001, use_unselected=False):
    pass


def stroke_merge_material(hue_threshold=0.001, sat_threshold=0.001, val_threshold=0.001):
    pass


def stroke_normalize(mode='THICKNESS', factor=1.0, value=10):
    pass


def stroke_outline(view_mode='VIEW', material_mode='ACTIVE', thickness=1, keep=True, subdivisions=3, length=0.0):
    pass


def stroke_reset_vertex_color(mode='BOTH'):
    pass


def stroke_sample(length=0.1, sharp_threshold=0.1):
    pass


def stroke_separate(mode='POINT'):
    pass


def stroke_simplify(factor=0.0):
    pass


def stroke_simplify_fixed(step=1):
    pass


def stroke_smooth(repeat=2, factor=1.0, only_selected=True, smooth_position=True, smooth_thickness=True, smooth_strength=False, smooth_uv=False):
    pass


def stroke_split():
    pass


def stroke_start_set():
    pass


def stroke_subdivide(number_cuts=1, factor=0.0, repeat=1, only_selected=True, smooth_position=True, smooth_thickness=True, smooth_strength=False, smooth_uv=False):
    pass


def stroke_trim():
    pass


def time_segment_add(modifier=""):
    pass


def time_segment_move(modifier="", type='UP'):
    pass


def time_segment_remove(modifier="", index=0):
    pass


def tint_flip():
    pass


def trace_image(target='NEW', thickness=10, resolution=5, scale=1.0, sample=0.0, threshold=0.5, turnpolicy='MINORITY', mode='SINGLE', use_current_frame=True, frame_number=0):
    pass


def transform_fill(mode='ROTATE', location=(0.0, 0.0), rotation=0.0, scale=0.0, release_confirm=False):
    pass


def unlock_all():
    pass


def vertex_color_brightness_contrast(mode='BOTH', brightness=0.0, contrast=0.0):
    pass


def vertex_color_hsv(mode='BOTH', h=0.5, s=1.0, v=1.0):
    pass


def vertex_color_invert(mode='BOTH'):
    pass


def vertex_color_levels(mode='BOTH', offset=0.0, gain=1.0):
    pass


def vertex_color_set(mode='BOTH', factor=1.0):
    pass


def vertex_group_assign():
    pass


def vertex_group_deselect():
    pass


def vertex_group_invert():
    pass


def vertex_group_normalize():
    pass


def vertex_group_normalize_all(lock_active=True):
    pass


def vertex_group_remove_from():
    pass


def vertex_group_select():
    pass


def vertex_group_smooth(factor=0.5, repeat=1):
    pass


def vertex_paint(stroke=None, wait_for_input=True):
    pass


def vertexmode_toggle(back=False):
    pass


def weight_paint(stroke=None, wait_for_input=True):
    pass


def weight_sample():
    pass


def weight_toggle_direction():
    pass


def weightmode_toggle(back=False):
    pass


