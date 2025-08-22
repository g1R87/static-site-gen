import os
import shutil
from pathlib import Path
from src.functions.block import markdown_to_html_node
from src.functions.markdown import extract_title

def generate_page_r(dir_path_content, template_path, dest_dir_path, base_path = ''):
    if os.path.isfile(dir_path_content):
        generate_page(dir_path_content, template_path, dest_dir_path.replace('.md', '.html'), base_path)
    else:
        items = os.listdir(dir_path_content)
        for item in items:
            generate_page_r(os.path.join(dir_path_content, item), template_path, os.path.join(dest_dir_path, item), base_path)

def generate_page(from_path, template_path, dest_path, base_path = ''):
    temp_contents = get_file_contents(template_path)
    md_contents = get_file_contents(from_path)
    print(f"Generating page form {from_path} to {dest_path} using {template_path}")

    page_title = extract_title(md_contents)
    html_string = markdown_to_html_node(md_contents).to_html()

    html = temp_contents.replace("{{ Title }}", page_title).replace("{{ Content }}", html_string)

    if base_path != '':
        html = html.replace('href="/', f'href={base_path}').replace('src="/', f'src={base_path}')

    write_file(dest_path, html)

def write_file(file_path, content):
    path_obj = Path(file_path)

    if  not os.path.isfile(file_path):
        path_obj.parent.mkdir(parents=True, exist_ok=True)

        with open(path_obj, 'w') as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

def get_file_contents(path, max = None):
    with open(path) as f:
        return f.read(max)

def generate_public():
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

def generate_docs():
    static_dir = "./static"
    public_dir = "./docs"

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
