import sys


def add_simple_uvs():
    pass


def add_texture_paint_slot(type='BASE_COLOR', slot_type='IMAGE', name="Untitled", color=(0.0, 0.0, 0.0, 1.0), width=1024, height=1024, alpha=True, generated_type='BLANK', float=False, domain='POINT', data_type='FLOAT_COLOR'):
    pass


def brush_colors_flip():
    pass


def brush_select(sculpt_tool='DRAW', vertex_tool='DRAW', weight_tool='DRAW', image_tool='DRAW', gpencil_tool='DRAW', gpencil_vertex_tool='DRAW', gpencil_sculpt_tool='SMOOTH', gpencil_weight_tool='WEIGHT', curves_sculpt_tool='COMB', toggle=False, create_missing=False):
    pass


def face_select_all(action='TOGGLE'):
    pass


def face_select_hide(unselected=False):
    pass


def face_select_less(face_step=True):
    pass


def face_select_linked():
    pass


def face_select_linked_pick(deselect=False):
    pass


def face_select_loop(select=True, extend=False):
    pass


def face_select_more(face_step=True):
    pass


def face_vert_reveal(select=True):
    pass


def grab_clone(delta=(0.0, 0.0)):
    pass


def hide_show(action='HIDE', area='INSIDE', xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True):
    pass


def image_from_view(filepath=""):
    pass


def image_paint(stroke=None, mode='NORMAL'):
    pass


def mask_box_gesture(xmin=0, xmax=0, ymin=0, ymax=0, wait_for_input=True, use_front_faces_only=False, use_limit_to_segment=False, mode='VALUE', value=1.0):
    pass


def mask_flood_fill(mode='VALUE', value=0.0):
    pass


def mask_lasso_gesture(path=None, use_front_faces_only=False, use_limit_to_segment=False, mode='VALUE', value=1.0):
    pass


def mask_line_gesture(xstart=0, xend=0, ystart=0, yend=0, flip=False, cursor=5, use_front_faces_only=False, use_limit_to_segment=False, mode='VALUE', value=1.0):
    pass


def project_image(image=''):
    pass


def sample_color(location=(0, 0), merged=False, palette=False):
    pass


def texture_paint_toggle():
    pass


def vert_select_all(action='TOGGLE'):
    pass


def vert_select_hide(unselected=False):
    pass


def vert_select_less(face_step=True):
    pass


def vert_select_linked():
    pass


def vert_select_linked_pick(select=True):
    pass


def vert_select_more(face_step=True):
    pass


def vert_select_ungrouped(extend=False):
    pass


def vertex_color_brightness_contrast(brightness=0.0, contrast=0.0):
    pass


def vertex_color_dirt(blur_strength=1.0, blur_iterations=1, clean_angle=3.14159, dirt_angle=0.0, dirt_only=False, normalize=True):
    pass


def vertex_color_from_weight():
    pass


def vertex_color_hsv(h=0.5, s=1.0, v=1.0):
    pass


def vertex_color_invert():
    pass


def vertex_color_levels(offset=0.0, gain=1.0):
    pass


def vertex_color_set(use_alpha=True):
    pass


def vertex_color_smooth():
    pass


def vertex_paint(stroke=None, mode='NORMAL'):
    pass


def vertex_paint_toggle():
    pass


def weight_from_bones(type='AUTOMATIC'):
    pass


def weight_gradient(type='LINEAR', xstart=0, xend=0, ystart=0, yend=0, flip=False, cursor=5):
    pass


def weight_paint(stroke=None, mode='NORMAL'):
    pass


def weight_paint_toggle():
    pass


def weight_sample():
    pass


def weight_sample_group():
    pass


def weight_set():
    pass


