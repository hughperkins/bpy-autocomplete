import sys


def BoolProperty(name="", description="", translation_context="*", default=False, options={'ANIMATABLE'}, override=set(), tags=set(), subtype='NONE', update=None, get=None, set=None):
    pass


def BoolVectorProperty(name="", description="", translation_context="*", default=(False, False, False), options={'ANIMATABLE'}, override=set(), tags=set(), subtype='NONE', size=3, update=None, get=None, set=None):
    pass


def CollectionProperty(type=None, name="", description="", translation_context="*", options={'ANIMATABLE'}, override=set(), tags=set()):
    pass


def EnumProperty(items, name="", description="", translation_context="*", default=None, options={'ANIMATABLE'}, override=set(), tags=set(), update=None, get=None, set=None):
    pass


def FloatProperty(name="", description="", translation_context="*", default=0.0, min=-3.402823e+38, max=3.402823e+38, soft_min=-3.402823e+38, soft_max=3.402823e+38, step=3, precision=2, options={'ANIMATABLE'}, override=set(), tags=set(), subtype='NONE', unit='NONE', update=None, get=None, set=None):
    pass


def FloatVectorProperty(name="", description="", translation_context="*", default=(0.0, 0.0, 0.0), min=sys.float_info.min, max=sys.float_info.max, soft_min=sys.float_info.min, soft_max=sys.float_info.max, step=3, precision=2, options={'ANIMATABLE'}, override=set(), tags=set(), subtype='NONE', unit='NONE', size=3, update=None, get=None, set=None):
    pass


def IntProperty(name="", description="", translation_context="*", default=0, min=-2**31, max=2**31-1, soft_min=-2**31, soft_max=2**31-1, step=1, options={'ANIMATABLE'}, override=set(), tags=set(), subtype='NONE', update=None, get=None, set=None):
    pass


def IntVectorProperty(name="", description="", translation_context="*", default=(0, 0, 0), min=-2**31, max=2**31-1, soft_min=-2**31, soft_max=2**31-1, step=1, options={'ANIMATABLE'}, override=set(), tags=set(), subtype='NONE', size=3, update=None, get=None, set=None):
    pass


def PointerProperty(type=None, name="", description="", translation_context="*", options={'ANIMATABLE'}, override=set(), tags=set(), poll=None, update=None):
    pass


def RemoveProperty(cls, attr):
    pass


def StringProperty(name="", description="", translation_context="*", default="", maxlen=0, options={'ANIMATABLE'}, override=set(), tags=set(), subtype='NONE', update=None, get=None, set=None, search=None, search_options={'SUGGESTION'}):
    pass


