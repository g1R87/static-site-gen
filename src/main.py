from src.functions.generate import generate_public, generate_page_r 
import sys

def main():
    generate_public()

    first_arg_index = 1
    base_path = '/' if not first_arg_index < len(sys.argv) else sys.argv[1]

    generate_page_r('./content', './template.html', './docs', base_path)


    return

main()
