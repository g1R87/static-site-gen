import os
import shutil
from pathlib import Path

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page form {from_path} to {dest_path} using {template_path}")
    temp_contents = get_file_contents(template_path)
    md_contents = get_file_contents(from_path)

def get_file_contents(path, max = None):
    with open(path) as f:
        return f.read(max)

def generate_public():
    #INFO: this only works if called from main.sh in the rootdir
    static_dir = "./static"
    public_dir = "./public"

    # prepare public direcotry
    if os.path.exists(public_dir) and os.path.isdir(public_dir):
        for item in os.listdir(public_dir):
            try:
                shutil.rmtree(os.path.join(public_dir, item))
            except OSError:
                os.remove(os.path.join(public_dir, item))
    else:
        os.mkdir(public_dir)

    copy_file_r(static_dir, public_dir)







def copy_file_r(src, dest):
    for item in os.listdir(src):
        file_path = os.path.join(src, item)
        if os.path.isfile(file_path):
            shutil.copy(file_path, dest)
        else:
            dest_folder = os.path.join(dest, item)
            os.mkdir(os.path.join(dest, item))
            copy_file_r(file_path, dest_folder)
