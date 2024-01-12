import sys


def align(axis='ALIGN_AUTO'):
    pass


def align_rotation(method='AUTO', axis='X', correct_aspect=False):
    pass


def average_islands_scale(scale_uv=False, shear=False):
    pass


def copy():
    pass


def cube_project(cube_size=1.0, correct_aspect=True, clip_to_bounds=False, scale_to_bounds=False):
    pass


def cursor_set(location=(0.0, 0.0)):
    pass


def cylinder_project(direction='VIEW_ON_EQUATOR', align='POLAR_ZX', pole='PINCH', seam=False, radius=1.0, correct_aspect=True, clip_to_bounds=False, scale_to_bounds=False):
    pass


def export_layout(filepath="", export_all=False, modified=False, mode='PNG', size=(1024, 1024), opacity=0.25, check_existing=True):
    pass


def follow_active_quads(mode='LENGTH_AVERAGE'):
    pass


def hide(unselected=False):
    pass


def lightmap_pack(PREF_CONTEXT='SEL_FACES', PREF_PACK_IN_ONE=True, PREF_NEW_UVLAYER=False, PREF_BOX_DIV=12, PREF_MARGIN_DIV=0.1):
    pass


def mark_seam(clear=False):
    pass


def minimize_stretch(fill_holes=True, blend=0.0, iterations=0):
    pass


def pack_islands(udim_source='CLOSEST_UDIM', rotate=True, rotate_method='ANY', scale=True, merge_overlap=False, margin_method='SCALED', margin=0.001, pin=False, pin_method='LOCKED', shape_method='CONCAVE'):
    pass


def paste():
    pass


def pin(clear=False, invert=False):
    pass


def project_from_view(orthographic=False, camera_bounds=True, correct_aspect=True, clip_to_bounds=False, scale_to_bounds=False):
    pass


def randomize_uv_transform(random_seed=0, use_loc=True, loc=(0.0, 0.0), use_rot=True, rot=0.0, use_scale=True, scale_even=False, scale=(1.0, 1.0)):
    pass


def remove_doubles(threshold=0.02, use_unselected=False):
    pass


def reset():
    pass


def reveal(select=True):
    pass


def rip(mirror=False, release_confirm=False, use_accurate=False, location=(0.0, 0.0)):
    pass


def rip_move(UV_OT_rip=None, TRANSFORM_OT_translate=None):
    pass


def seams_from_islands(mark_seams=True, mark_sharp=False):
    pass


def select(extend=False, deselect=False, toggle=False, deselect_all=False, select_passthrough=False, location=(0.0, 0.0)):
    pass


def select_all(action='TOGGLE'):
    pass


def select_box(pinned=False, xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True, mode='SET'):
    pass


def select_circle(x=0, y=0, radius=25, wait_for_input=True, mode='SET'):
    pass


def select_edge_ring(extend=False, location=(0.0, 0.0)):
    pass


def select_lasso(path=None, mode='SET'):
    pass


def select_less():
    pass


def select_linked():
    pass


def select_linked_pick(extend=False, deselect=False, location=(0.0, 0.0)):
    pass


def select_loop(extend=False, location=(0.0, 0.0)):
    pass


def select_mode(type='VERTEX'):
    pass


def select_more():
    pass


def select_overlap(extend=False):
    pass


def select_pinned():
    pass


def select_similar(type='PIN', compare='EQUAL', threshold=0.0):
    pass


def select_split():
    pass


def shortest_path_pick(use_face_step=False, use_topology_distance=False, use_fill=False, skip=0, nth=1, offset=0, object_index=-1, index=-1):
    pass


def shortest_path_select(use_face_step=False, use_topology_distance=False, use_fill=False, skip=0, nth=1, offset=0):
    pass


def smart_project(angle_limit=1.15192, margin_method='SCALED', island_margin=0.0, area_weight=0.0, correct_aspect=True, scale_to_bounds=False):
    pass


def snap_cursor(target='PIXELS'):
    pass


def snap_selected(target='PIXELS'):
    pass


def sphere_project(direction='VIEW_ON_EQUATOR', align='POLAR_ZX', pole='PINCH', seam=False, correct_aspect=True, clip_to_bounds=False, scale_to_bounds=False):
    pass


def stitch(use_limit=False, snap_islands=True, limit=0.01, static_island=0, active_object_index=0, midpoint_snap=False, clear_seams=True, mode='VERTEX', stored_mode='VERTEX', selection=None, objects_selection_count=(0, 0, 0, 0, 0, 0)):
    pass


def unwrap(method='ANGLE_BASED', fill_holes=True, correct_aspect=True, use_subsurf_data=False, margin_method='SCALED', margin=0.001):
    pass


def weld():
    pass


