import sys


def add(radius=1.0, type='EMPTY', enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0)):
    pass


def add_modifier_menu():
    pass


def add_named(linked=False, name="", session_uuid=0, matrix=((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0)), drop_x=0, drop_y=0):
    pass


def align(bb_quality=True, align_mode='OPT_2', relative_to='OPT_4', align_axis={}):
    pass


def anim_transforms_to_deltas():
    pass


def armature_add(radius=1.0, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0)):
    pass


def assign_property_defaults(process_data=True, process_bones=True):
    pass


def bake(type='COMBINED', pass_filter={}, filepath="", width=512, height=512, margin=16, margin_type='EXTEND', use_selected_to_active=False, max_ray_distance=0.0, cage_extrusion=0.0, cage_object="", normal_space='TANGENT', normal_r='POS_X', normal_g='POS_Y', normal_b='POS_Z', target='IMAGE_TEXTURES', save_mode='INTERNAL', use_clear=False, use_cage=False, use_split_materials=False, use_automatic_name=False, uv_layer=""):
    pass


def bake_image():
    pass


def camera_add(enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0)):
    pass


def clear_override_library():
    pass


def collection_add():
    pass


def collection_external_asset_drop(session_uuid=0, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0), use_instance=True, drop_x=0, drop_y=0, collection=''):
    pass


def collection_instance_add(name="Collection", collection='', align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0), session_uuid=0, drop_x=0, drop_y=0):
    pass


def collection_link(collection=''):
    pass


def collection_objects_select():
    pass


def collection_remove():
    pass


def collection_unlink():
    pass


def constraint_add(type=''):
    pass


def constraint_add_with_targets(type=''):
    pass


def constraints_clear():
    pass


def constraints_copy():
    pass


def convert(target='MESH', keep_original=False, merge_customdata=True, angle=1.22173, thickness=5, seams=False, faces=True, offset=0.01):
    pass


def correctivesmooth_bind(modifier=""):
    pass


def curves_empty_hair_add(align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0)):
    pass


def curves_random_add(align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0)):
    pass


def data_instance_add(name="", session_uuid=0, type='ACTION', align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0), drop_x=0, drop_y=0):
    pass


def data_transfer(use_reverse_transfer=False, use_freeze=False, data_type='', use_create=True, vert_mapping='NEAREST', edge_mapping='NEAREST', loop_mapping='NEAREST_POLYNOR', poly_mapping='NEAREST', use_auto_transform=False, use_object_transform=True, use_max_distance=False, max_distance=1.0, ray_radius=0.0, islands_precision=0.1, layers_select_src='ACTIVE', layers_select_dst='ACTIVE', mix_mode='REPLACE', mix_factor=1.0):
    pass


def datalayout_transfer(modifier="", data_type='', use_delete=False, layers_select_src='ACTIVE', layers_select_dst='ACTIVE'):
    pass


def delete(use_global=False, confirm=True):
    pass


def drop_geometry_nodes(session_uuid=0, show_datablock_in_modifier=True):
    pass


def drop_named_image(filepath="", relative_path=True, name="", session_uuid=0, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0)):
    pass


def drop_named_material(name="", session_uuid=0):
    pass


def duplicate(linked=False, mode='TRANSLATION'):
    pass


def duplicate_move(OBJECT_OT_duplicate=None, TRANSFORM_OT_translate=None):
    pass


def duplicate_move_linked(OBJECT_OT_duplicate=None, TRANSFORM_OT_translate=None):
    pass


def duplicates_make_real(use_base_parent=False, use_hierarchy=False):
    pass


def editmode_toggle():
    pass


def effector_add(type='FORCE', radius=1.0, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0)):
    pass


def empty_add(type='PLAIN_AXES', radius=1.0, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0)):
    pass


def explode_refresh(modifier=""):
    pass


def forcefield_toggle():
    pass


def geometry_node_tree_copy_assign():
    pass


def geometry_nodes_input_attribute_toggle(input_name="", modifier_name=""):
    pass


def geometry_nodes_move_to_nodes():
    pass


def gpencil_add(radius=1.0, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0), type='EMPTY', use_in_front=True, stroke_depth_offset=0.05, use_lights=False, stroke_depth_order='3D'):
    pass


def gpencil_modifier_add(type='GP_THICK'):
    pass


def gpencil_modifier_apply(apply_as='DATA', modifier="", report=False):
    pass


def gpencil_modifier_copy(modifier=""):
    pass


def gpencil_modifier_copy_to_selected(modifier=""):
    pass


def gpencil_modifier_move_down(modifier=""):
    pass


def gpencil_modifier_move_to_index(modifier="", index=0):
    pass


def gpencil_modifier_move_up(modifier=""):
    pass


def gpencil_modifier_remove(modifier="", report=False):
    pass


def grease_pencil_add(type='EMPTY', radius=1.0, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0)):
    pass


def hide_collection(collection_index=-1, toggle=False, extend=False):
    pass


def hide_render_clear_all():
    pass


def hide_view_clear(select=True):
    pass


def hide_view_set(unselected=False):
    pass


def hook_add_newob():
    pass


def hook_add_selob(use_bone=False):
    pass


def hook_assign(modifier=''):
    pass


def hook_recenter(modifier=''):
    pass


def hook_remove(modifier=''):
    pass


def hook_reset(modifier=''):
    pass


def hook_select(modifier=''):
    pass


def instance_offset_from_cursor():
    pass


def instance_offset_from_object():
    pass


def instance_offset_to_cursor():
    pass


def isolate_type_render():
    pass


def join():
    pass


def join_shapes():
    pass


def join_uvs():
    pass


def laplaciandeform_bind(modifier=""):
    pass


def light_add(type='POINT', radius=1.0, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0)):
    pass


def light_linking_blocker_collection_new():
    pass


def light_linking_blockers_link(link_state='INCLUDE'):
    pass


def light_linking_blockers_select():
    pass


def light_linking_receiver_collection_new():
    pass


def light_linking_receivers_link(link_state='INCLUDE'):
    pass


def light_linking_receivers_select():
    pass


def light_linking_unlink_from_collection():
    pass


def lightprobe_add(type='CUBEMAP', radius=1.0, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0)):
    pass


def lightprobe_cache_bake(delay=0, subset='ALL'):
    pass


def lightprobe_cache_free(subset='SELECTED'):
    pass


def lineart_bake_strokes():
    pass


def lineart_bake_strokes_all():
    pass


def lineart_clear():
    pass


def lineart_clear_all():
    pass


def link_to_collection(collection_index=-1, is_new=False, new_collection_name=""):
    pass


def load_background_image(filepath="", filter_image=True, filter_movie=True, filter_folder=True, view_align=True):
    pass


def load_reference_image(filepath="", filter_image=True, filter_movie=True, filter_folder=True, view_align=True):
    pass


def location_clear(clear_delta=False):
    pass


def make_dupli_face():
    pass


def make_links_data(type='OBDATA'):
    pass


def make_links_scene(scene=''):
    pass


def make_local(type='SELECT_OBJECT'):
    pass


def make_override_library(collection=0):
    pass


def make_single_user(type='SELECTED_OBJECTS', object=False, obdata=False, material=False, animation=False, obdata_animation=False):
    pass


def material_slot_add():
    pass


def material_slot_assign():
    pass


def material_slot_copy():
    pass


def material_slot_deselect():
    pass


def material_slot_move(direction='UP'):
    pass


def material_slot_remove():
    pass


def material_slot_remove_unused():
    pass


def material_slot_select():
    pass


def meshdeform_bind(modifier=""):
    pass


def metaball_add(type='BALL', radius=2.0, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0)):
    pass


def mode_set(mode='OBJECT', toggle=False):
    pass


def mode_set_with_submode(mode='OBJECT', toggle=False, mesh_select_mode={}):
    pass


def modifier_add(type='SUBSURF'):
    pass


def modifier_add_node_group(asset_library_type='LOCAL', asset_library_identifier="", relative_asset_identifier="", session_uuid=0):
    pass


def modifier_apply(modifier="", report=False, merge_customdata=True, single_user=False):
    pass


def modifier_apply_as_shapekey(keep_modifier=False, modifier="", report=False):
    pass


def modifier_convert(modifier=""):
    pass


def modifier_copy(modifier=""):
    pass


def modifier_copy_to_selected(modifier=""):
    pass


def modifier_move_down(modifier=""):
    pass


def modifier_move_to_index(modifier="", index=0):
    pass


def modifier_move_up(modifier=""):
    pass


def modifier_remove(modifier="", report=False):
    pass


def modifier_set_active(modifier=""):
    pass


def move_to_collection(collection_index=-1, is_new=False, new_collection_name=""):
    pass


def multires_base_apply(modifier=""):
    pass


def multires_external_pack():
    pass


def multires_external_save(filepath="", hide_props_region=True, check_existing=True, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=True, filter_collada=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, display_type='DEFAULT', sort_method='', modifier=""):
    pass


def multires_higher_levels_delete(modifier=""):
    pass


def multires_rebuild_subdiv(modifier=""):
    pass


def multires_reshape(modifier=""):
    pass


def multires_subdivide(modifier="", mode='CATMULL_CLARK'):
    pass


def multires_unsubdivide(modifier=""):
    pass


def ocean_bake(modifier="", free=False):
    pass


def origin_clear():
    pass


def origin_set(type='GEOMETRY_ORIGIN', center='MEDIAN'):
    pass


def parent_clear(type='CLEAR'):
    pass


def parent_inverse_apply():
    pass


def parent_no_inverse_set(confirm=True, keep_transform=False):
    pass


def parent_set(type='OBJECT', xmirror=False, keep_transform=False):
    pass


def particle_system_add():
    pass


def particle_system_remove():
    pass


def paths_calculate(display_type='RANGE', range='SCENE'):
    pass


def paths_clear(only_selected=False):
    pass


def paths_update():
    pass


def paths_update_visible():
    pass


def pointcloud_add(align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0)):
    pass


def posemode_toggle():
    pass


def quadriflow_remesh(use_mesh_symmetry=True, use_preserve_sharp=False, use_preserve_boundary=False, preserve_paint_mask=False, smooth_normals=False, mode='FACES', target_ratio=1.0, target_edge_length=0.1, target_faces=4000, mesh_area=-1.0, seed=0):
    pass


def quick_explode(style='EXPLODE', amount=100, frame_duration=50, frame_start=1, frame_end=10, velocity=1.0, fade=True):
    pass


def quick_fur(density='MEDIUM', length=0.1, radius=0.001, view_percentage=1.0, apply_hair_guides=True, use_noise=True, use_frizz=True):
    pass


def quick_liquid(show_flows=False):
    pass


def quick_smoke(style='SMOKE', show_flows=False):
    pass


def randomize_transform(random_seed=0, use_delta=False, use_loc=True, loc=(0.0, 0.0, 0.0), use_rot=True, rot=(0.0, 0.0, 0.0), use_scale=True, scale_even=False, scale=(1.0, 1.0, 1.0)):
    pass


def reset_override_library():
    pass


def rotation_clear(clear_delta=False):
    pass


def scale_clear(clear_delta=False):
    pass


def select_all(action='TOGGLE'):
    pass


def select_by_type(extend=False, type='MESH'):
    pass


def select_camera(extend=False):
    pass


def select_grouped(extend=False, type='CHILDREN_RECURSIVE'):
    pass


def select_hierarchy(direction='PARENT', extend=False):
    pass


def select_less():
    pass


def select_linked(extend=False, type='OBDATA'):
    pass


def select_mirror(extend=False):
    pass


def select_more():
    pass


def select_pattern(pattern="*", case_sensitive=False, extend=True):
    pass


def select_random(ratio=0.5, seed=0, action='SELECT'):
    pass


def select_same_collection(collection=""):
    pass


def shade_flat():
    pass


def shade_smooth(use_auto_smooth=False, auto_smooth_angle=0.523599):
    pass


def shaderfx_add(type='FX_BLUR'):
    pass


def shaderfx_copy(shaderfx=""):
    pass


def shaderfx_move_down(shaderfx=""):
    pass


def shaderfx_move_to_index(shaderfx="", index=0):
    pass


def shaderfx_move_up(shaderfx=""):
    pass


def shaderfx_remove(shaderfx="", report=False):
    pass


def shape_key_add(from_mix=True):
    pass


def shape_key_clear():
    pass


def shape_key_mirror(use_topology=False):
    pass


def shape_key_move(type='TOP'):
    pass


def shape_key_remove(all=False, apply_mix=False):
    pass


def shape_key_retime():
    pass


def shape_key_transfer(mode='OFFSET', use_clamp=False):
    pass


def simulation_nodes_cache_bake(selected=False):
    pass


def simulation_nodes_cache_bake_single(session_uuid=0, modifier_name="", bake_id=0):
    pass


def simulation_nodes_cache_calculate_to_frame(selected=False):
    pass


def simulation_nodes_cache_delete(selected=False):
    pass


def simulation_nodes_cache_delete_single(session_uuid=0, modifier_name="", bake_id=0):
    pass


def skin_armature_create(modifier=""):
    pass


def skin_loose_mark_clear(action='MARK'):
    pass


def skin_radii_equalize():
    pass


def skin_root_mark():
    pass


def speaker_add(enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0)):
    pass


def subdivision_set(level=1, relative=False):
    pass


def surfacedeform_bind(modifier=""):
    pass


def text_add(radius=1.0, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0)):
    pass


def track_clear(type='CLEAR'):
    pass


def track_set(type='DAMPTRACK'):
    pass


def transfer_mode(use_flash_on_transfer=True):
    pass


def transform_apply(location=True, rotation=True, scale=True, properties=True, isolate_users=False):
    pass


def transform_axis_target():
    pass


def transform_to_mouse(name="", session_uuid=0, matrix=((0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0), (0.0, 0.0, 0.0, 0.0)), drop_x=0, drop_y=0):
    pass


def transforms_to_deltas(mode='ALL', reset_values=True):
    pass


def unlink_data():
    pass


def vertex_group_add():
    pass


def vertex_group_assign():
    pass


def vertex_group_assign_new():
    pass


def vertex_group_clean(group_select_mode='', limit=0.0, keep_single=False):
    pass


def vertex_group_copy():
    pass


def vertex_group_copy_to_selected():
    pass


def vertex_group_deselect():
    pass


def vertex_group_invert(group_select_mode='', auto_assign=True, auto_remove=True):
    pass


def vertex_group_levels(group_select_mode='', offset=0.0, gain=1.0):
    pass


def vertex_group_limit_total(group_select_mode='', limit=4):
    pass


def vertex_group_lock(action='TOGGLE', mask='ALL'):
    pass


def vertex_group_mirror(mirror_weights=True, flip_group_names=True, all_groups=False, use_topology=False):
    pass


def vertex_group_move(direction='UP'):
    pass


def vertex_group_normalize():
    pass


def vertex_group_normalize_all(group_select_mode='', lock_active=True):
    pass


def vertex_group_quantize(group_select_mode='', steps=4):
    pass


def vertex_group_remove(all=False, all_unlocked=False):
    pass


def vertex_group_remove_from(use_all_groups=False, use_all_verts=False):
    pass


def vertex_group_select():
    pass


def vertex_group_set_active(group=''):
    pass


def vertex_group_smooth(group_select_mode='', factor=0.5, repeat=1, expand=0.0):
    pass


def vertex_group_sort(sort_type='NAME'):
    pass


def vertex_parent_set(confirm=True):
    pass


def vertex_weight_copy():
    pass


def vertex_weight_delete(weight_group=-1):
    pass


def vertex_weight_normalize_active_vertex():
    pass


def vertex_weight_paste(weight_group=-1):
    pass


def vertex_weight_set_active(weight_group=-1):
    pass


def visual_transform_apply():
    pass


def volume_add(align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0)):
    pass


def volume_import(filepath="", directory="", files=None, hide_props_region=True, check_existing=False, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=True, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, display_type='DEFAULT', sort_method='', use_sequence_detection=True, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0)):
    pass


def voxel_remesh():
    pass


def voxel_size_edit():
    pass


