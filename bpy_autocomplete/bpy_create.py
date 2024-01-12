"""
Given sphinx doc of bpy, generate autocomplete
"""
import argparse
from genericpath import isfile
import os
from os import path
from os.path import join
from typing import Optional
import shutil

# import bpy


def module_to_folder_and_file(module: str) -> tuple[str, str]:
    split_module = module.split('.')
    folder_path = '/'.join(split_module[:-1])
    filename = split_module[-1] + '.py'
    return folder_path, filename


def write_function(folder_path, filename, function) -> None:
    print('folder_path', folder_path, 'filename', filename)
    if not path.isdir(folder_path):
        os.makedirs(folder_path, exist_ok=True)
    file_fullpath = join(folder_path, filename)
    if not path.exists(file_fullpath):
        with open(file_fullpath, 'a') as f:
            f.write("import sys\n\n\n")

    with open(file_fullpath, 'a') as f:
        f.write(f"""def {function}:
    pass


""")


def create_init_files(target_dir: str) -> None:
    child_modules = []
    for child in os.listdir(target_dir):
        child_path = join(target_dir, child)
        if path.isdir(child_path) and not child_path.startswith("."):
            create_init_files(child_path)
        elif path.isfile(child_path):
            child_modules.append(child.split(".")[0])
    with open(join(target_dir, "__init__.py"), 'w') as f:
        for child_module in child_modules:
            f.write(f"import {child_module}\n")
        f.write("\n\n")
        all_l = []
        for m in child_modules:
            all_l.append('"' + m + '"')
        all_str = ", ".join(all_l)
        f.write(f"__all__ = [{all_str}]\n")


def process_file(filepath: str, out_dir: str) -> None:
    module: Optional[str] = None
    with open(filepath) as f:
        contents = f.read()
    for line in contents.split("\n"):
        if line.startswith(".. module:: "):
            module = line.split(".. module:: ")[1]
            print('module', module)
        elif line.startswith(".. function:: "):
            function = line.split(".. function:: ")[1]
            print('function', function)
            assert module is not None
            folder_path, filename = module_to_folder_and_file(module)
            write_function(folder_path, filename, function)


def run(args: argparse.Namespace) -> None:
    if path.isdir(args.out_dir):
        shutil.rmtree(args.out_dir)
    for file in os.listdir(args.in_dir):
        if not file.startswith("bpy."):
            continue
        print(file)
        process_file(path.join(args.in_dir, file), args.out_dir)
    
    create_init_files(args.out_dir)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--in-dir", default=path.expanduser("~/blender-git/blender/doc/python_api/sphinx-in"))
    parser.add_argument("--out-dir", default="bpy")
    args = parser.parse_args()
    run(args)
