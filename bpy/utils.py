import sys


def blend_paths(absolute=False, packed=False, local=False):
    pass


def escape_identifier(string):
    pass


def flip_name(name, strip_digits=False):
    pass


def unescape_identifier(string):
    pass


def register_class(cls):
    pass


def resource_path(type, major=bpy.app.version[0], minor=bpy.app.version[1]):
    pass


def unregister_class(cls):
    pass


def keyconfig_init():
    pass


def keyconfig_set(filepath, *, report=None):
    pass


def load_scripts(*, reload_scripts=False, refresh_scripts=False, extensions=True):
    pass


def modules_from_path(path, loaded_modules):
    pass


def preset_find(name, preset_path, *, display_name=False, ext='.py'):
    pass


def preset_paths(subdir):
    pass


def refresh_script_paths():
    pass


def app_template_paths(*, path=None):
    pass


def register_manual_map(manual_hook):
    pass


def unregister_manual_map(manual_hook):
    pass


def register_classes_factory(classes):
    pass


def register_submodule_factory(module_name, submodule_names):
    pass


def register_tool(tool_cls, *, after=None, separator=False, group=False):
    pass


def make_rna_paths(struct_name, prop_name, enum_name):
    pass


def manual_map():
    pass


def manual_language_code(default='en'):
    pass


def script_path_user():
    pass


def script_paths(*, subdir=None, user_pref=True, check_all=False, use_user=True):
    pass


def smpte_from_frame(frame, *, fps=None, fps_base=None):
    pass


def smpte_from_seconds(time, *, fps=None, fps_base=None):
    pass


def unregister_tool(tool_cls):
    pass


def user_resource(resource_type, *, path='', create=False):
    pass


def execfile(filepath, *, mod=None):
    pass


