from src.functions.generate import generate_public
from src.functions.markdown import extract_title
from src.functions.block import markdown_to_html_node , get_block_parent_html
from pprint import pprint


def main():
    generate_public()

    # test = "### this is a test heading"
    # (get_block_parent_html(test))

    return

main()
