# bpy-autocomplete
bpy-autocomplete

# What this is

Auto-completion for Blender bpy!

# To use

- first uninstall `bpy` if it is installed, e.g. `pip uninstall bpy`
- clone this repo
- cd into this repo
- `pip install .`

# How to update

- clone the blender repo
- run a full blender build, e.g. `PYTHON=python && make update && make develop`
- in the blender cloned repo, `cd` into `blender/doc/python_api`
- `pip install sphinx`
- `python sphinx_doc_gen.py`

- clone this repo (`bpy-autocomplete`)
- cd into this cloned repo
- run `python bpy_autocomplete/bpy_create.py`
- rerun `pip install .`
