import sys


def bake_keys():
    pass


def blend_offset(factor=0.0):
    pass


def blend_to_default(factor=0.0):
    pass


def blend_to_ease(factor=0.0):
    pass


def blend_to_neighbor(factor=0.0):
    pass


def breakdown(factor=0.0):
    pass


def butterworth_smooth(cutoff_frequency=3.0, filter_order=4, samples_per_frame=1, blend=1.0, blend_in_out=1):
    pass


def clean(threshold=0.001, channels=False):
    pass


def click_insert(frame=1.0, value=1.0, extend=False):
    pass


def clickselect(wait_to_deselect_others=False, mouse_x=0, mouse_y=0, extend=False, deselect_all=False, column=False, curves=False):
    pass


def copy():
    pass


def cursor_set(frame=0.0, value=0.0):
    pass


def decimate(mode='RATIO', factor=0.333333, remove_error_margin=0.0):
    pass


def delete(confirm=True):
    pass


def driver_delete_invalid():
    pass


def driver_variables_copy():
    pass


def driver_variables_paste(replace=False):
    pass


def duplicate(mode='TRANSLATION'):
    pass


def duplicate_move(GRAPH_OT_duplicate=None, TRANSFORM_OT_translate=None):
    pass


def ease(factor=0.0):
    pass


def easing_type(type='AUTO'):
    pass


def equalize_handles(side='LEFT', handle_length=5.0, flatten=False):
    pass


def euler_filter():
    pass


def extrapolation_type(type='CONSTANT'):
    pass


def fmodifier_add(type='nullptr', only_active=False):
    pass


def fmodifier_copy():
    pass


def fmodifier_paste(only_active=False, replace=False):
    pass


def frame_jump():
    pass


def gaussian_smooth(factor=1.0, sigma=0.33, filter_width=6):
    pass


def ghost_curves_clear():
    pass


def ghost_curves_create():
    pass


def handle_type(type='FREE'):
    pass


def hide(unselected=False):
    pass


def interpolation_type(type='CONSTANT'):
    pass


def keyframe_insert(type='ALL'):
    pass


def keyframe_jump(next=True):
    pass


def keys_to_samples(confirm=True):
    pass


def match_slope(factor=0.0):
    pass


def mirror(type='CFRA'):
    pass


def paste(offset='START', value_offset='NONE', merge='MIX', flipped=False):
    pass


def previewrange_set():
    pass


def push_pull(factor=1.0):
    pass


def reveal(select=True):
    pass


def samples_to_keys():
    pass


def scale_average(factor=1.0):
    pass


def select_all(action='TOGGLE'):
    pass


def select_box(axis_range=False, include_handles=True, tweak=False, use_curve_selection=True, xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True, mode='SET'):
    pass


def select_circle(x=0, y=0, radius=25, wait_for_input=True, mode='SET', use_curve_selection=True):
    pass


def select_column(mode='KEYS'):
    pass


def select_key_handles(left_handle_action='SELECT', right_handle_action='SELECT', key_action='KEEP'):
    pass


def select_lasso(path=None, mode='SET', use_curve_selection=True):
    pass


def select_leftright(mode='CHECK', extend=False):
    pass


def select_less():
    pass


def select_linked():
    pass


def select_more():
    pass


def shear(factor=0.0, direction='FROM_LEFT'):
    pass


def smooth():
    pass


def snap(type='CFRA'):
    pass


def snap_cursor_value():
    pass


def sound_to_samples(filepath="", check_existing=False, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=True, filter_python=False, filter_font=False, filter_sound=True, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=9, show_multiview=False, use_multiview=False, display_type='DEFAULT', sort_method='', low=0.0, high=100000.0, attack=0.005, release=0.2, threshold=0.0, use_accumulate=False, use_additive=False, use_square=False, sthreshold=0.1):
    pass


def time_offset(frame_offset=0.0):
    pass


def view_all(include_handles=True):
    pass


def view_frame():
    pass


def view_selected(include_handles=True):
    pass


