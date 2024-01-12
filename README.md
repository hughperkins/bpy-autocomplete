# bpy-autocomplete
bpy-autocomplete

# What this is

Auto-completion for Blender bpy!

# To use

- clone this repo
- cd into the repo
- `pip install -e .`

# How to update

- clone the blender repo
- run a full blender build, e.g. `PYTHON=python && make update && make develop`
- in the blender cloned repo, `cd` into `blender/doc/python_api`
- `pip install sphinx`
- `python sphinx_doc_gen.py`

- clone this repo (`bpy-autocomplete`)
- cd into this cloned repo
- run `python bpy_autocomplete/bpy_create.py`
