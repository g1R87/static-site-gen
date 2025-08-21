from src.functions.generate import generate_public, generate_page_r, generate_page
from src.functions.markdown import extract_title
from src.functions.block import markdown_to_html_node , get_block_parent_html
from pprint import pprint


def main():
    generate_public()
    # Generating page form ./content/contact/index.html to ./content/contact/index.html using ./template.html
    # generate_page('./content/contact/index.md', './template.html', './content/contact/index.html ')

    generate_page_r('./content', './template.html', './public')

    # test = "### this is a test heading"
    # (get_block_parent_html(test))

    return

main()
