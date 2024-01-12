import sys


def add_collection(name="", session_uuid=0):
    pass


def add_file(filepath="", hide_props_region=True, check_existing=False, filter_blender=False, filter_backup=False, filter_image=True, filter_movie=True, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, show_multiview=False, use_multiview=False, display_type='DEFAULT', sort_method='', name="", session_uuid=0):
    pass


def add_group(name="", session_uuid=0, show_datablock_in_node=True):
    pass


def add_group_asset(asset_library_type='LOCAL', asset_library_identifier="", relative_asset_identifier=""):
    pass


def add_mask(name="", session_uuid=0):
    pass


def add_material(name="", session_uuid=0):
    pass


def add_node(use_transform=False, settings=None, type=""):
    pass


def add_object(name="", session_uuid=0):
    pass


def add_repeat_zone(use_transform=False, settings=None, offset=(150.0, 0.0)):
    pass


def add_reroute(path=None, cursor=8):
    pass


def add_simulation_zone(use_transform=False, settings=None, offset=(150.0, 0.0)):
    pass


def attach():
    pass


def backimage_fit():
    pass


def backimage_move():
    pass


def backimage_sample():
    pass


def backimage_zoom(factor=1.2):
    pass


def clear_viewer_border():
    pass


def clipboard_copy():
    pass


def clipboard_paste(offset=(0.0, 0.0)):
    pass


def collapse_hide_unused_toggle():
    pass


def cryptomatte_layer_add():
    pass


def cryptomatte_layer_remove():
    pass


def deactivate_viewer():
    pass


def delete():
    pass


def delete_reconnect():
    pass


def detach():
    pass


def detach_translate_attach(NODE_OT_detach=None, TRANSFORM_OT_translate=None, NODE_OT_attach=None):
    pass


def duplicate(keep_inputs=False, linked=True):
    pass


def duplicate_move(NODE_OT_duplicate=None, NODE_OT_translate_attach=None):
    pass


def duplicate_move_keep_inputs(NODE_OT_duplicate=None, NODE_OT_translate_attach=None):
    pass


def duplicate_move_linked(NODE_OT_duplicate=None, NODE_OT_translate_attach=None):
    pass


def find_node():
    pass


def gltf_settings_node_operator():
    pass


def group_edit(exit=False):
    pass


def group_insert():
    pass


def group_make():
    pass


def group_separate(type='COPY'):
    pass


def group_ungroup():
    pass


def hide_socket_toggle():
    pass


def hide_toggle():
    pass


def insert_offset():
    pass


def interface_item_duplicate():
    pass


def interface_item_new(item_type='INPUT'):
    pass


def interface_item_remove():
    pass


def join():
    pass


def link(detach=False, drag_start=(0.0, 0.0), inside_padding=2.0, outside_padding=0.0, speed_ramp=1.0, max_speed=26.0, delay=0.5, zoom_influence=0.5):
    pass


def link_make(replace=False):
    pass


def link_viewer():
    pass


def links_cut(path=None, cursor=12):
    pass


def links_detach():
    pass


def links_mute(path=None, cursor=35):
    pass


def move_detach_links(NODE_OT_links_detach=None, TRANSFORM_OT_translate=None):
    pass


def move_detach_links_release(NODE_OT_links_detach=None, NODE_OT_translate_attach=None):
    pass


def mute_toggle():
    pass


def new_geometry_node_group_assign():
    pass


def new_geometry_node_group_tool():
    pass


def new_geometry_nodes_modifier():
    pass


def new_node_tree(type='', name="NodeTree"):
    pass


def node_color_preset_add(name="", remove_name=False, remove_active=False):
    pass


def node_copy_color():
    pass


def options_toggle():
    pass


def output_file_add_socket(file_path="Image"):
    pass


def output_file_move_active_socket(direction='DOWN'):
    pass


def output_file_remove_active_socket():
    pass


def parent_set():
    pass


def preview_toggle():
    pass


def read_viewlayers():
    pass


def render_changed():
    pass


def repeat_zone_item_add():
    pass


def repeat_zone_item_move(direction='UP'):
    pass


def repeat_zone_item_remove():
    pass


def resize():
    pass


def select(extend=False, deselect=False, toggle=False, deselect_all=False, select_passthrough=False, location=(0, 0), socket_select=False, clear_viewer=False):
    pass


def select_all(action='TOGGLE'):
    pass


def select_box(tweak=False, xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True, mode='SET'):
    pass


def select_circle(x=0, y=0, radius=25, wait_for_input=True, mode='SET'):
    pass


def select_grouped(extend=False, type='TYPE'):
    pass


def select_lasso(tweak=False, path=None, mode='SET'):
    pass


def select_link_viewer(NODE_OT_select=None, NODE_OT_link_viewer=None):
    pass


def select_linked_from():
    pass


def select_linked_to():
    pass


def select_same_type_step(prev=False):
    pass


def shader_script_update():
    pass


def simulation_zone_item_add():
    pass


def simulation_zone_item_move(direction='UP'):
    pass


def simulation_zone_item_remove():
    pass


def switch_view_update():
    pass


def translate_attach(TRANSFORM_OT_translate=None, NODE_OT_attach=None):
    pass


def translate_attach_remove_on_cancel(TRANSFORM_OT_translate=None, NODE_OT_attach=None):
    pass


def tree_path_parent():
    pass


def view_all():
    pass


def view_selected():
    pass


def viewer_border(xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True):
    pass


