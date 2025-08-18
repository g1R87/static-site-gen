from src.textnode import TextNode, TextType
from src.leafnode import LeafNode

def text_node_to_html_node(text_node: TextNode):
    text = text_node.text.replace("\n",' ')
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text)

    if text_node.text_type == TextType.BOLD:
        return LeafNode('b', text)

    if text_node.text_type == TextType.ITALIC:
        return LeafNode('i', text)

    if text_node.text_type == TextType.CODE:
        return LeafNode('code', text)

    if text_node.text_type == TextType.LINK:
        return LeafNode('a', text, {"href" : text_node.url})

    if text_node.text_type == TextType.IMAGE:
        return LeafNode('img', value='', props={"src": text_node.url, "alt": text})

