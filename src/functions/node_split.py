from src.textnode import TextNode, TextType
from src.functions.regex_funcs import extract_markdown_images, extract_markdown_links

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType ):
    new_nodes = []

    for node in old_nodes:
        text = node.text
        if text.count(delimiter) % 2 != 0:
            raise ValueError("Invalid markdown syntax for: ", node)
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        parts = text.split(delimiter)
        # current_nodes = []
        for i, part in enumerate(parts):
            if(part == ''):
                continue

            if i % 2 == 0:
                new_nodes.append(TextNode(part, TextType.TEXT))
            else:
                new_nodes.append(TextNode(part, text_type))

    return new_nodes

# Usage 
# node = TextNode(
#     "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
#     TextType.TEXT,
# )
# new_nodes = split_nodes_link([node])
# [
#     TextNode("This is text with a link ", TextType.TEXT),
#     TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
#     TextNode(" and ", TextType.TEXT),
#     TextNode(
#         "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
#     ),
# ]
def split_nodes_link(old_nodes: list[TextNode]):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        links = extract_markdown_links(node.text)
        if not links:
            new_nodes.append(node)
            continue

        text = node.text
        for link_tuple in links:
            link_text = link_tuple[0]
            link = link_tuple[1]
            parts = text.split(f"[{link_text}]({link})", 1)
            if parts[0] != '':
                new_nodes.append(TextNode(parts[0], TextType.TEXT))
            new_nodes.append(TextNode(link_text, TextType.LINK, link))
            text = parts[1]

        if text != '':
            new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes

def split_nodes_image(old_nodes: list[TextNode]):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        links = extract_markdown_images(node.text)
        if not links:
            new_nodes.append(node)
            continue

        text = node.text
        for link_tuple in links:
            link_text = link_tuple[0]
            link = link_tuple[1]
            #INFO: might need to check for the parts size but may not be needed as links(tuple) would be empty if the links arent properly closed
            parts = text.split(f"![{link_text}]({link})", 1)

            if parts[0] != '':
                new_nodes.append(TextNode(parts[0], TextType.TEXT))

            new_nodes.append(TextNode(link_text, TextType.IMAGE, link))
            text = parts[1]

        if text != '':
            new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes



def splitNodesDelimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType ):
    new_nodes = []

    for node in old_nodes:
        text = node.text
        if text.count(delimiter) % 2 != 0:
            raise ValueError("Invalid markdown syntax for: ", node)
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        parts = split_partition(text, delimiter)
        found = False
        for part in parts:
            if part != delimiter:
                if found:
                    new_nodes.append(TextNode(part, text_type))
                else:
                    new_nodes.append(TextNode(part, TextType.TEXT))

            elif part == delimiter:
                found = not found
    return new_nodes

def split_partition(text: str, delimiter:str):
    parts = []

    partitions = text.partition(delimiter)
    if partitions[0] != '':
        parts.append(partitions[0])

    if partitions[1] != '':
        parts.append(partitions[1])

    if partitions[2] != '':
        parts.extend(split_partition(partitions[2], delimiter))

    return parts

def split_partition_ref(text: str, delimiter:str, parts: list):
    partitions = text.partition(delimiter)

    if partitions[0] != '':
        parts.append(partitions[0])

    if partitions[1] != '':
        parts.append(partitions[1])

    if partitions[2] != '':
        split_partition(partitions[2], delimiter, parts)




















# def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType ):
#     new_nodes = []
#
#     for node in old_nodes:
#         text = node.text
#         if text.count(delimiter) % 2 != 0:
#             raise ValueError("Invalid markdown syntax for: ", node)
#         if node.text_type != TextType.TEXT:
#             new_nodes.append(node)
#             continue
#
#         filtered = get_filtered_list(text, delimiter)
#
#         parts = text.split(delimiter)
#         for part in parts:
#             if part in filtered:
#                 new_nodes.append(TextNode(part, text_type))
#                 continue
#             new_nodes.append(TextNode(part, TextType.TEXT))
#     return new_nodes

# stupic
def get_filtered_list(text:str, delimiter: str):
    filtered = [] 
    found = False
    word = ''
    for char in text:
        if(char != delimiter and not found):
            continue
        elif char == delimiter:
            found = not found
            if not found:
                filtered.append(word)
                word = ''
            continue

        word += char
    return filtered
















