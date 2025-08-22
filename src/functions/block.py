from pprint import pprint
from src.block_type import BlockType
from src.functions.text_to_textnodes import text_to_textnodes
from src.functions.transform import text_node_to_html_node
from src.parentnode import ParentNode
from src.leafnode import LeafNode
import re


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    childrens = []
    for block in blocks:
        block_node = get_block_parent_html(block) 

        childrens.append(block_node)

    if not childrens:
        return LeafNode('div', '')
    return ParentNode('div', childrens)

def get_block_parent_html(block):
    try:
        block_type = block_to_block_type(block)

        if(block_type == BlockType.HEADING):
            match = re.findall(r"^(#{1,6})\s(.*)", block)[0]
            heading_count = match[0].count('#')
            return ParentNode(f'h{heading_count}', children= text_to_children(match[1]))

        if(block_type == BlockType.CODE):
            match = re.findall(r"```(.*)```", block, re.DOTALL)
            return ParentNode('code', children=[LeafNode(None, match[0])])

        if(block_type == BlockType.QUOTE):
            matches = re.findall(r"^>(.*)$", block, re.MULTILINE)
            text = " ".join([match.strip() for match in matches])
            return ParentNode('blockquote', children=text_to_children(text))

        if(block_type == BlockType.UNORDERED_LIST):
            childrens = []
            matches = re.findall(r'^\s*[-*+]\s+(.*?(?=\n\s*[-*+]|\Z))', block, re.DOTALL | re.MULTILINE)
            for list_item in matches:
                childrens.append(ParentNode('li', children=text_to_children(list_item)))
            return ParentNode('ul', childrens)

        if(block_type == BlockType.ORDERED_LIST):
            childrens = []
            matches = re.findall(r'^\s*\d+\.\s+(.*?(?=\n\s*\d+\.|\Z))', block, re.DOTALL | re.MULTILINE)
            for list_item in matches:
                childrens.append(ParentNode('li', children=text_to_children(list_item)))
            return ParentNode('ol', childrens)

        return ParentNode('p', text_to_children(block))
    except Exception:
        print(list_item, 'is the context')
        # raise Exception('test')


def text_to_children(text):
    childrens = []
    text_nodes = text_to_textnodes(text)
    for text_node in text_nodes:
        childrens.append(text_node_to_html_node(text_node))
    return childrens

    
def markdown_to_blocks(markdown: str):
    blocks = markdown.split("\n\n")
    blocks = list(map(lambda x: x.strip(), blocks))
    blocks = [block for block in blocks if block != '']
    return blocks

def block_to_block_type(block: str):
    if is_heading_block(block):
        return BlockType.HEADING
    if is_code_block(block):
        return BlockType.CODE
    if is_quote_block(block):
        return BlockType.QUOTE
    if is_unordered_block(block):
        return BlockType.UNORDERED_LIST
    if is_ordered_block(block):
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH

def is_heading_block(block:str):
    pattern = r"^#{1,6}\s.*"
    matches = re.findall(pattern, block)
    if not matches:
        return False    
    return True

def is_code_block(block:str):
    return block.startswith("```") and block.endswith("```")

def is_quote_block(block:str):
    lines = block.splitlines()
    if not lines:
        return False
    pattern = r"^>"

    for line in lines:
        if not re.match(pattern, line):
            return False
    return True

def is_unordered_block(block:str) -> bool:
    lines = block.strip().splitlines()
    if not lines:
        return False
    
    list_item_pattern = re.compile(r"^\s*[-*+]\s")
    indented_line_pattern = re.compile(r"^\s{2,}")  

    list_item_matched = False
    for i, line in enumerate(lines):
        is_list_item = list_item_pattern.match(line)
        if is_list_item:
            list_item_matched = True
        is_indented = indented_line_pattern.match(line)
        
        if not is_list_item and not is_indented:
            return False
            
    return list_item_matched

def is_ordered_block(block: str):
    matches = re.findall(r"^(\d+)\.\s.*$", block, re.MULTILINE)
    
    if not matches:
        return False
    
    for i, num_str in enumerate(matches):
        current_num = int(num_str)
        expected_num = i + 1
        if current_num != expected_num:
            return False
            
    return True
