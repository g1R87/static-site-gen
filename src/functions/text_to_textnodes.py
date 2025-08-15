import src.functions.node_split as sp
from src.textnode import TextNode, TextType

def text_to_textnodes(text):
    old_nodes = [TextNode(text, TextType.TEXT)]
    nodes = sp.split_nodes_delimiter(old_nodes, '**', TextType.BOLD)
    nodes = sp.split_nodes_delimiter(nodes, '_', TextType.ITALIC)
    nodes = sp.split_nodes_delimiter(nodes, '`', TextType.CODE)
    nodes = sp.split_nodes_delimiter(nodes, '`', TextType.CODE)
    nodes = sp.split_nodes_image(nodes)
    nodes = sp.split_nodes_link(nodes)
    return nodes


