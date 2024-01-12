import sys


def alembic_export(filepath="", check_existing=True, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=True, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=8, display_type='DEFAULT', sort_method='', filter_glob="*.abc", start=-2147483648, end=-2147483648, xsamples=1, gsamples=1, sh_open=0.0, sh_close=1.0, selected=False, visible_objects_only=False, flatten=False, uvs=True, packuv=True, normals=True, vcolors=False, orcos=True, face_sets=False, subdiv_schema=False, apply_subdiv=False, curves_as_mesh=False, use_instancing=True, global_scale=1.0, triangulate=False, quad_method='SHORTEST_DIAGONAL', ngon_method='BEAUTY', export_hair=True, export_particles=True, export_custom_properties=True, as_background_job=False, evaluation_mode='RENDER', init_scene_frame_range=True):
    pass


def alembic_import(filepath="", check_existing=False, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=True, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=8, relative_path=True, display_type='DEFAULT', sort_method='', filter_glob="*.abc", scale=1.0, set_frame_range=True, validate_meshes=False, always_add_cache_reader=False, is_sequence=False, as_background_job=False):
    pass


def append(filepath="", directory="", filename="", files=None, check_existing=False, filter_blender=True, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=True, filemode=1, display_type='DEFAULT', sort_method='', link=False, do_reuse_local_id=False, clear_asset_data=False, autoselect=True, active_collection=True, instance_collections=False, instance_object_data=True, set_fake=False, use_recursive=True):
    pass


def batch_rename(data_type='OBJECT', data_source='SELECT', actions=None):
    pass


def blend_strings_utf8_validate():
    pass


def call_menu(name=""):
    pass


def call_menu_pie(name=""):
    pass


def call_panel(name="", keep_open=True):
    pass


def collada_export(filepath="", check_existing=True, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=True, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=8, display_type='DEFAULT', sort_method='', filter_glob="*.dae", prop_bc_export_ui_section='main', apply_modifiers=False, export_mesh_type=0, export_mesh_type_selection='view', export_global_forward_selection='Y', export_global_up_selection='Z', apply_global_orientation=False, selected=False, include_children=False, include_armatures=False, include_shapekeys=False, deform_bones_only=False, include_animations=True, include_all_actions=True, export_animation_type_selection='sample', sampling_rate=1, keep_smooth_curves=False, keep_keyframes=False, keep_flat_curves=False, active_uv_only=False, use_texture_copies=True, triangulate=True, use_object_instantiation=True, use_blender_profile=True, sort_by_name=False, export_object_transformation_type=0, export_object_transformation_type_selection='matrix', export_animation_transformation_type=0, export_animation_transformation_type_selection='matrix', open_sim=False, limit_precision=False, keep_bind_info=False):
    pass


def collada_import(filepath="", check_existing=False, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=True, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=8, display_type='DEFAULT', sort_method='', filter_glob="*.dae", import_units=False, custom_normals=True, fix_orientation=False, find_chains=False, auto_connect=False, min_chain_length=0, keep_bind_info=False):
    pass


def context_collection_boolean_set(data_path_iter="", data_path_item="", type='TOGGLE'):
    pass


def context_cycle_array(data_path="", reverse=False):
    pass


def context_cycle_enum(data_path="", reverse=False, wrap=False):
    pass


def context_cycle_int(data_path="", reverse=False, wrap=False):
    pass


def context_menu_enum(data_path=""):
    pass


def context_modal_mouse(data_path_iter="", data_path_item="", header_text="", input_scale=0.01, invert=False, initial_x=0):
    pass


def context_pie_enum(data_path=""):
    pass


def context_scale_float(data_path="", value=1.0):
    pass


def context_scale_int(data_path="", value=1.0, always_step=True):
    pass


def context_set_boolean(data_path="", value=True):
    pass


def context_set_enum(data_path="", value=""):
    pass


def context_set_float(data_path="", value=0.0, relative=False):
    pass


def context_set_id(data_path="", value=""):
    pass


def context_set_int(data_path="", value=0, relative=False):
    pass


def context_set_string(data_path="", value=""):
    pass


def context_set_value(data_path="", value=""):
    pass


def context_toggle(data_path="", module=""):
    pass


def context_toggle_enum(data_path="", value_1="", value_2=""):
    pass


def debug_menu(debug_value=0):
    pass


def doc_view(doc_id=""):
    pass


def doc_view_manual(doc_id=""):
    pass


def doc_view_manual_ui_context():
    pass


def drop_blend_file(filepath=""):
    pass


def gpencil_export_pdf(filepath="", check_existing=True, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_usd=False, filter_obj=True, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=8, display_type='DEFAULT', sort_method='', use_fill=True, selected_object_type='SELECTED', stroke_sample=0.0, use_normalized_thickness=False, frame_mode='ACTIVE'):
    pass


def gpencil_export_svg(filepath="", check_existing=True, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_usd=False, filter_obj=True, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=8, display_type='DEFAULT', sort_method='', use_fill=True, selected_object_type='SELECTED', stroke_sample=0.0, use_normalized_thickness=False, use_clip_camera=False):
    pass


def gpencil_import_svg(filepath="", directory="", files=None, check_existing=False, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_usd=False, filter_obj=True, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=8, relative_path=True, display_type='DEFAULT', sort_method='', resolution=10, scale=10.0):
    pass


def interface_theme_preset_add(name="", remove_name=False, remove_active=False):
    pass


def keyconfig_preset_add(name="", remove_name=False, remove_active=False):
    pass


def lib_reload(library="", filepath="", directory="", filename="", hide_props_region=True, check_existing=False, filter_blender=True, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=8, relative_path=True, display_type='DEFAULT', sort_method=''):
    pass


def lib_relocate(library="", filepath="", directory="", filename="", files=None, hide_props_region=True, check_existing=False, filter_blender=True, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=8, relative_path=True, display_type='DEFAULT', sort_method=''):
    pass


def link(filepath="", directory="", filename="", files=None, check_existing=False, filter_blender=True, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=True, filemode=1, relative_path=True, display_type='DEFAULT', sort_method='', link=True, do_reuse_local_id=False, clear_asset_data=False, autoselect=True, active_collection=True, instance_collections=True, instance_object_data=True):
    pass


def memory_statistics():
    pass


def obj_export(filepath="", check_existing=True, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=8, display_type='DEFAULT', sort_method='', export_animation=False, start_frame=-2147483648, end_frame=2147483647, forward_axis='NEGATIVE_Z', up_axis='Y', global_scale=1.0, apply_modifiers=True, export_eval_mode='DAG_EVAL_VIEWPORT', export_selected_objects=False, export_uv=True, export_normals=True, export_colors=False, export_materials=True, export_pbr_extensions=False, path_mode='AUTO', export_triangulated_mesh=False, export_curves_as_nurbs=False, export_object_groups=False, export_material_groups=False, export_vertex_groups=False, export_smooth_groups=False, smooth_group_bitflags=False, filter_glob="*.obj;*.mtl"):
    pass


def obj_import(filepath="", directory="", files=None, check_existing=False, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=8, display_type='DEFAULT', sort_method='', global_scale=1.0, clamp_size=0.0, forward_axis='NEGATIVE_Z', up_axis='Y', use_split_objects=True, use_split_groups=False, import_vertex_groups=False, validate_meshes=False, filter_glob="*.obj;*.mtl"):
    pass


def open_mainfile(filepath="", hide_props_region=True, check_existing=False, filter_blender=True, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=8, display_type='DEFAULT', sort_method='', load_ui=True, use_scripts=True, display_file_selector=True, state=0):
    pass


def operator_cheat_sheet():
    pass


def operator_defaults():
    pass


def operator_pie_enum(data_path="", prop_string=""):
    pass


def operator_preset_add(name="", remove_name=False, remove_active=False, operator=""):
    pass


def owner_disable(owner_id=""):
    pass


def owner_enable(owner_id=""):
    pass


def path_open(filepath=""):
    pass


def ply_export(filepath="", check_existing=True, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=8, display_type='DEFAULT', sort_method='', forward_axis='Y', up_axis='Z', global_scale=1.0, apply_modifiers=True, export_selected_objects=False, export_uv=True, export_normals=False, export_colors='SRGB', export_triangulated_mesh=False, ascii_format=False, filter_glob="*.ply"):
    pass


def ply_import(filepath="", directory="", files=None, check_existing=False, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=8, display_type='DEFAULT', sort_method='', global_scale=1.0, use_scene_unit=False, forward_axis='Y', up_axis='Z', merge_verts=False, import_colors='SRGB', filter_glob="*.ply"):
    pass


def previews_batch_clear(files=None, directory="", filter_blender=True, filter_folder=True, use_scenes=True, use_collections=True, use_objects=True, use_intern_data=True, use_trusted=False, use_backups=True):
    pass


def previews_batch_generate(files=None, directory="", filter_blender=True, filter_folder=True, use_scenes=True, use_collections=True, use_objects=True, use_intern_data=True, use_trusted=False, use_backups=True):
    pass


def previews_clear(id_type={}):
    pass


def previews_ensure():
    pass


def properties_add(data_path=""):
    pass


def properties_context_change(context=""):
    pass


def properties_edit(data_path="", property_name="", property_type='FLOAT', is_overridable_library=False, description="", use_soft_limits=False, array_length=3, default_int=(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), min_int=-10000, max_int=10000, soft_min_int=-10000, soft_max_int=10000, step_int=1, default_bool=(False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False), default_float=(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0), min_float=-10000.0, max_float=-10000.0, soft_min_float=-10000.0, soft_max_float=-10000.0, precision=3, step_float=0.1, subtype='', default_string="", id_type='OBJECT', eval_string=""):
    pass


def properties_edit_value(data_path="", property_name="", eval_string=""):
    pass


def properties_remove(data_path="", property_name=""):
    pass


def quit_blender():
    pass


def radial_control(data_path_primary="", data_path_secondary="", use_secondary="", rotation_path="", color_path="", fill_color_path="", fill_color_override_path="", fill_color_override_test_path="", zoom_path="", image_id="", secondary_tex=False, release_confirm=False):
    pass


def read_factory_settings(use_factory_startup_app_template_only=False, app_template="Template", use_empty=False):
    pass


def read_factory_userpref(use_factory_startup_app_template_only=False):
    pass


def read_history():
    pass


def read_homefile(filepath="", load_ui=True, use_splash=False, use_factory_startup=False, use_factory_startup_app_template_only=False, app_template="Template", use_empty=False):
    pass


def read_userpref():
    pass


def recover_auto_save(filepath="", hide_props_region=True, check_existing=False, filter_blender=True, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=False, filter_blenlib=False, filemode=8, display_type='LIST_VERTICAL', sort_method='', use_scripts=True):
    pass


def recover_last_session(use_scripts=True):
    pass


def redraw_timer(type='DRAW', iterations=10, time_limit=0.0):
    pass


def revert_mainfile(use_scripts=True):
    pass


def save_as_mainfile(filepath="", hide_props_region=True, check_existing=True, filter_blender=True, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=8, display_type='DEFAULT', sort_method='', compress=False, relative_remap=True, copy=False):
    pass


def save_homefile():
    pass


def save_mainfile(filepath="", hide_props_region=True, check_existing=True, filter_blender=True, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=8, display_type='DEFAULT', sort_method='', compress=False, relative_remap=False, exit=False, incremental=False):
    pass


def save_userpref():
    pass


def search_menu():
    pass


def search_operator():
    pass


def search_single_menu(menu_idname="", initial_query=""):
    pass


def set_stereo_3d(display_mode='ANAGLYPH', anaglyph_type='RED_CYAN', interlace_type='ROW_INTERLEAVED', use_interlace_swap=False, use_sidebyside_crosseyed=False):
    pass


def splash():
    pass


def splash_about():
    pass


def stl_import(filepath="", directory="", files=None, check_existing=False, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=8, display_type='DEFAULT', sort_method='', global_scale=1.0, use_scene_unit=False, use_facet_normal=False, forward_axis='Y', up_axis='Z', use_mesh_validate=False, filter_glob="*.stl"):
    pass


def sysinfo(filepath=""):
    pass


def tool_set_by_id(name="", cycle=False, as_fallback=False, space_type='EMPTY'):
    pass


def tool_set_by_index(index=0, cycle=False, expand=True, as_fallback=False, space_type='EMPTY'):
    pass


def toolbar():
    pass


def toolbar_fallback_pie():
    pass


def toolbar_prompt():
    pass


def url_open(url=""):
    pass


def url_open_preset(type='', id=""):
    pass


def usd_export(filepath="", check_existing=True, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_usd=True, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=8, display_type='DEFAULT', sort_method='', filter_glob="*.usd", selected_objects_only=False, visible_objects_only=True, export_animation=False, export_hair=False, export_uvmaps=True, export_mesh_colors=True, export_normals=True, export_materials=True, use_instancing=False, evaluation_mode='RENDER', generate_preview_surface=True, export_textures=True, overwrite_textures=False, relative_paths=True, root_prim_path=""):
    pass


def usd_import(filepath="", check_existing=False, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_usd=True, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=8, relative_path=True, display_type='DEFAULT', sort_method='', filter_glob="*.usd", scale=1.0, set_frame_range=True, import_cameras=True, import_curves=True, import_lights=True, import_materials=True, import_meshes=True, import_volumes=True, import_shapes=True, import_skeletons=True, import_blendshapes=True, import_subdiv=False, import_instance_proxies=True, import_visible_only=True, create_collection=False, read_mesh_uvs=True, read_mesh_colors=True, read_mesh_attributes=True, prim_path_mask="", import_guide=False, import_proxy=True, import_render=True, import_all_materials=False, import_usd_preview=True, set_material_blend=True, light_intensity_scale=1.0, mtl_name_collision_mode='MAKE_UNIQUE', import_textures_mode='IMPORT_PACK', import_textures_dir="//textures/", tex_name_collision_mode='USE_EXISTING'):
    pass


def window_close():
    pass


def window_fullscreen_toggle():
    pass


def window_new():
    pass


def window_new_main():
    pass


