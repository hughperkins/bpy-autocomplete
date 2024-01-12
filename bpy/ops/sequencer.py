import sys


def change_effect_input(swap='A_B'):
    pass


def change_effect_type(type='CROSS'):
    pass


def change_path(filepath="", directory="", files=None, hide_props_region=True, check_existing=False, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, display_type='DEFAULT', sort_method='', use_placeholders=False):
    pass


def change_scene(scene=''):
    pass


def copy():
    pass


def crossfade_sounds():
    pass


def cursor_set(location=(0.0, 0.0)):
    pass


def deinterlace_selected_movies():
    pass


def delete(delete_data=False):
    pass


def duplicate():
    pass


def duplicate_move(SEQUENCER_OT_duplicate=None, TRANSFORM_OT_seq_slide=None):
    pass


def effect_strip_add(type='CROSS', frame_start=0, frame_end=0, channel=1, replace_sel=True, overlap=False, overlap_shuffle_override=False, color=(0.0, 0.0, 0.0)):
    pass


def enable_proxies(proxy_25=False, proxy_50=False, proxy_75=False, proxy_100=False, overwrite=False):
    pass


def export_subtitles(filepath="", hide_props_region=True, check_existing=True, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=8, display_type='DEFAULT', sort_method=''):
    pass


def fades_add(duration_seconds=1.0, type='IN_OUT'):
    pass


def fades_clear():
    pass


def gap_insert(frames=10):
    pass


def gap_remove(all=False):
    pass


def image_strip_add(directory="", files=None, check_existing=False, filter_blender=False, filter_backup=False, filter_image=True, filter_movie=False, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, show_multiview=False, use_multiview=False, display_type='DEFAULT', sort_method='', frame_start=0, frame_end=0, channel=1, replace_sel=True, overlap=False, overlap_shuffle_override=False, fit_method='FIT', set_view_transform=True, use_placeholders=False):
    pass


def images_separate(length=1):
    pass


def lock():
    pass


def mask_strip_add(frame_start=0, channel=1, replace_sel=True, overlap=False, overlap_shuffle_override=False, mask=''):
    pass


def meta_make():
    pass


def meta_separate():
    pass


def meta_toggle():
    pass


def movie_strip_add(filepath="", directory="", files=None, check_existing=False, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=True, filter_python=False, filter_font=False, filter_sound=False, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, show_multiview=False, use_multiview=False, display_type='DEFAULT', sort_method='', frame_start=0, channel=1, replace_sel=True, overlap=False, overlap_shuffle_override=False, fit_method='FIT', set_view_transform=True, adjust_playback_rate=True, sound=True, use_framerate=True):
    pass


def movieclip_strip_add(frame_start=0, channel=1, replace_sel=True, overlap=False, overlap_shuffle_override=False, clip=''):
    pass


def mute(unselected=False):
    pass


def offset_clear():
    pass


def paste(keep_offset=False):
    pass


def reassign_inputs():
    pass


def rebuild_proxy():
    pass


def refresh_all():
    pass


def reload(adjust_length=False):
    pass


def rename_channel():
    pass


def rendersize():
    pass


def retiming_freeze_frame_add(duration=0):
    pass


def retiming_key_add(timeline_frame=0):
    pass


def retiming_reset():
    pass


def retiming_segment_speed_set(speed=100.0):
    pass


def retiming_show():
    pass


def retiming_transition_add(duration=0):
    pass


def sample(size=1):
    pass


def scene_frame_range_update():
    pass


def scene_strip_add(frame_start=0, channel=1, replace_sel=True, overlap=False, overlap_shuffle_override=False, scene=''):
    pass


def scene_strip_add_new(frame_start=0, channel=1, replace_sel=True, overlap=False, overlap_shuffle_override=False, type='NEW'):
    pass


def select(wait_to_deselect_others=False, mouse_x=0, mouse_y=0, extend=False, deselect=False, toggle=False, deselect_all=False, select_passthrough=False, center=False, linked_handle=False, linked_time=False, side_of_frame=False):
    pass


def select_all(action='TOGGLE'):
    pass


def select_box(xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True, mode='SET', tweak=False, include_handles=False):
    pass


def select_grouped(type='TYPE', extend=False, use_active_channel=False):
    pass


def select_handles(side='BOTH'):
    pass


def select_less():
    pass


def select_linked():
    pass


def select_linked_pick(extend=False):
    pass


def select_more():
    pass


def select_side(side='BOTH'):
    pass


def select_side_of_frame(extend=False, side='LEFT'):
    pass


def set_range_to_strips(preview=False):
    pass


def slip(offset=0):
    pass


def snap(frame=0):
    pass


def sound_strip_add(filepath="", directory="", files=None, check_existing=False, filter_blender=False, filter_backup=False, filter_image=False, filter_movie=False, filter_python=False, filter_font=False, filter_sound=True, filter_text=False, filter_archive=False, filter_btx=False, filter_collada=False, filter_alembic=False, filter_usd=False, filter_obj=False, filter_volume=False, filter_folder=True, filter_blenlib=False, filemode=9, relative_path=True, display_type='DEFAULT', sort_method='', frame_start=0, channel=1, replace_sel=True, overlap=False, overlap_shuffle_override=False, cache=False, mono=False):
    pass


def split(frame=0, channel=0, type='SOFT', use_cursor_position=False, side='MOUSE', ignore_selection=False):
    pass


def split_multicam(camera=1):
    pass


def strip_color_tag_set(color='NONE'):
    pass


def strip_jump(next=True, center=True):
    pass


def strip_modifier_add(type=''):
    pass


def strip_modifier_copy(type='REPLACE'):
    pass


def strip_modifier_equalizer_redefine(graphs='SIMPLE', name="Name"):
    pass


def strip_modifier_move(name="Name", direction='UP'):
    pass


def strip_modifier_remove(name="Name"):
    pass


def strip_transform_clear(property='ALL'):
    pass


def strip_transform_fit(fit_method='FIT'):
    pass


def swap(side='RIGHT'):
    pass


def swap_data():
    pass


def swap_inputs():
    pass


def unlock():
    pass


def unmute(unselected=False):
    pass


def view_all():
    pass


def view_all_preview():
    pass


def view_frame():
    pass


def view_ghost_border(xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True):
    pass


def view_selected():
    pass


def view_zoom_ratio(ratio=1.0):
    pass


